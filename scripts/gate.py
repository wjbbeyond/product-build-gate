#!/usr/bin/env python3
"""Create and structurally validate Product Build Gate project artifacts."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
ASSET_DIR = SKILL_DIR / "assets"
MAIN_FILE = Path("docs/PRODUCT_BUILD_GATE.md")
DESIGN_FILE = Path("docs/DESIGN_LOCK.md")
BASELINE_FILE = Path("docs/APPROVED_BUILD_BASELINE.md")

GATES = (
    "product-contract",
    "prior-art",
    "experience-map",
    "visual-prototype",
    "design-lock",
    "build-blueprint",
    "vertical-slice",
    "approved-baseline",
)


class GateError(RuntimeError):
    pass


def project_path(raw: str) -> Path:
    project = Path(raw).expanduser().resolve()
    if not project.exists() or not project.is_dir():
        raise GateError(f"Project directory does not exist: {project}")
    if project in {Path("/").resolve(), Path.home().resolve()}:
        raise GateError(f"Refusing broad project target: {project}")
    return project


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def render_asset(name: str, title: str) -> str:
    template_path = ASSET_DIR / name
    if not template_path.is_file():
        raise GateError(f"Missing Skill asset: {template_path}")
    return (
        template_path.read_text(encoding="utf-8")
        .replace("{{PROJECT_TITLE}}", title)
        .replace("{{CREATED_AT}}", now_iso())
    )


def write_new(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(content)
    except FileExistsError as exc:
        raise GateError(f"Refusing to overwrite existing file: {path}") from exc


def read_required(path: Path) -> str:
    if not path.is_file():
        raise GateError(f"Required artifact is missing: {path}")
    return path.read_text(encoding="utf-8")


def project_title(main_text: str) -> str:
    match = re.search(r'^project_title:\s*"([^"]+)"\s*$', main_text, re.MULTILINE)
    if not match:
        raise GateError("Cannot read project_title from PRODUCT_BUILD_GATE.md")
    return match.group(1)


def marked_section(text: str, gate: str) -> str:
    start = f"<!-- GATE:{gate}:START -->"
    end = f"<!-- GATE:{gate}:END -->"
    if start not in text or end not in text:
        raise GateError(f"Missing structural markers for gate: {gate}")
    return text.split(start, 1)[1].split(end, 1)[0]


def checklist_counts(text: str) -> tuple[int, int]:
    items = re.findall(r"^\s*-\s*\[([ xX])\]\s+.+$", text, re.MULTILINE)
    total = len(items)
    unchecked = sum(1 for item in items if item == " ")
    return total, unchecked


def check_section(text: str, gate: str, label: str, failures: list[str]) -> None:
    try:
        section = marked_section(text, gate)
    except GateError as exc:
        failures.append(str(exc))
        return
    total, unchecked = checklist_counts(section)
    if total == 0:
        failures.append(f"{label}: checklist is missing")
    elif unchecked:
        failures.append(f"{label}: {unchecked}/{total} checklist items remain unchecked")


def check_full_checklist(text: str, label: str, failures: list[str]) -> None:
    total, unchecked = checklist_counts(text)
    if total == 0:
        failures.append(f"{label}: checklist is missing")
    elif unchecked:
        failures.append(f"{label}: {unchecked}/{total} checklist items remain unchecked")


def validate_project(project: Path, through: str) -> list[str]:
    failures: list[str] = []
    main_path = project / MAIN_FILE
    try:
        main_text = read_required(main_path)
    except GateError as exc:
        return [str(exc)]

    through_index = GATES.index(through)
    main_last = min(through_index, GATES.index("vertical-slice"))
    for gate in GATES[: main_last + 1]:
        check_section(main_text, gate, f"Gate {gate}", failures)

    if through_index >= GATES.index("design-lock"):
        design_path = project / DESIGN_FILE
        try:
            design_text = read_required(design_path)
            check_full_checklist(design_text, "Design Lock", failures)
        except GateError as exc:
            failures.append(str(exc))

    if through == "approved-baseline":
        baseline_path = project / BASELINE_FILE
        try:
            baseline_text = read_required(baseline_path)
            check_section(
                baseline_text,
                "approved-baseline",
                "Approved Build Baseline",
                failures,
            )
        except GateError as exc:
            failures.append(str(exc))

    return failures


def command_init(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    target = project / MAIN_FILE
    write_new(target, render_asset("PRODUCT_BUILD_GATE.template.md", args.title))
    print(f"CREATED {target}")
    return 0


def command_create_design_lock(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    failures = validate_project(project, "visual-prototype")
    if failures:
        raise GateError(
            "Cannot create Design Lock before prior gates pass:\n- "
            + "\n- ".join(failures)
        )
    main_text = read_required(project / MAIN_FILE)
    target = project / DESIGN_FILE
    write_new(
        target,
        render_asset("DESIGN_LOCK.template.md", project_title(main_text)),
    )
    print(f"CREATED {target}")
    return 0


def command_create_baseline(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    failures = validate_project(project, "vertical-slice")
    if failures:
        raise GateError(
            "Cannot create Approved Build Baseline before prior gates pass:\n- "
            + "\n- ".join(failures)
        )
    main_text = read_required(project / MAIN_FILE)
    target = project / BASELINE_FILE
    write_new(
        target,
        render_asset("APPROVED_BUILD_BASELINE.template.md", project_title(main_text)),
    )
    print(f"CREATED {target}")
    return 0


def command_status(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    main_path = project / MAIN_FILE
    main_text = read_required(main_path)
    print(f"PROJECT {project}")
    for gate in GATES[:-1]:
        try:
            section = marked_section(main_text, gate)
            total, unchecked = checklist_counts(section)
            state = "CHECKED" if total and unchecked == 0 else "PENDING"
            print(f"{state:7} {gate:18} checked={total - unchecked}/{total}")
        except GateError:
            print(f"MISSING {gate}")

    for label, relative in (
        ("design-lock-file", DESIGN_FILE),
        ("approved-baseline-file", BASELINE_FILE),
    ):
        target = project / relative
        print(f"{'PRESENT' if target.is_file() else 'MISSING':7} {label:18} {target}")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    project = project_path(args.project)
    failures = validate_project(project, args.through)
    if failures:
        print(f"FAIL through={args.through}")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        f"STRUCTURAL PASS through={args.through}; "
        "user approval and rendered evidence remain required"
    )
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Create and structurally validate Product Build Gate artifacts."
    )
    subparsers = result.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create PRODUCT_BUILD_GATE.md")
    init_parser.add_argument("--project", required=True)
    init_parser.add_argument("--title", required=True)
    init_parser.set_defaults(func=command_init)

    design_parser = subparsers.add_parser(
        "create-design-lock",
        help="Create DESIGN_LOCK.md after Gates 0-3 pass",
    )
    design_parser.add_argument("--project", required=True)
    design_parser.set_defaults(func=command_create_design_lock)

    baseline_parser = subparsers.add_parser(
        "create-baseline",
        help="Create APPROVED_BUILD_BASELINE.md after Gates 0-6 pass",
    )
    baseline_parser.add_argument("--project", required=True)
    baseline_parser.set_defaults(func=command_create_baseline)

    status_parser = subparsers.add_parser("status", help="Show structural gate status")
    status_parser.add_argument("--project", required=True)
    status_parser.set_defaults(func=command_status)

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate structural completion through a selected gate",
    )
    validate_parser.add_argument("--project", required=True)
    validate_parser.add_argument("--through", choices=GATES, required=True)
    validate_parser.set_defaults(func=command_validate)

    return result


def main() -> int:
    args = parser().parse_args()
    try:
        return args.func(args)
    except GateError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
