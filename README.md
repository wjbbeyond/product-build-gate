# Product Build Gate

Product Build Gate is an explicit-only Codex Skill for genuinely new user-facing products and major product/UX redesigns.

> Confirm the whole product, lock the design, approve one build baseline—then build continuously.

## Why

A strong written proposal can still become the wrong interface or workflow. Product Build Gate makes the whole product visible before production implementation, but exits as soon as the approved build baseline is ready. It is not a persistent router, sprint process, or implementation manager.

## Workflow

Internal preparation:

1. Product Contract
2. Conditional Prior Art/capability scan
3. Experience Map
4. System-wide page/function map and browsable Mock/Fake preview
5. Conditional visual-target comparison
6. Design Lock
7. Build Blueprint and Approved Build Baseline

Only three user approvals are required:

1. Product + whole-product preview
2. Design Lock
3. Approved Build Baseline + authorization to begin local/isolated development

After the third approval, Product Build Gate exits. Native Codex implements continuously from the locked baseline. The first Vertical Slice is an implementation milestone, not another Product Build Gate.

## Efficiency rules

- Existing complete source documents are extracted and reconciled; the user does not restate them.
- Prior Art runs only for a named decision-changing evidence gap.
- A clear existing visual target needs one faithful direction, not three artificial alternatives.
- Internal architecture, tests, migrations, TODO ordering, and bug fixes do not require user reapproval.
- Only material changes to product scope, modules/pages/navigation, core journeys, locked design, sensitive data, integrations, cost, production writes, deployment, or real customer communication reopen the smallest affected checkpoint.
- Technical tracer bullets remain internal and cannot replace the approved app shell or real user entry.

## Install

Keep the repository checkout as the editable source of truth, validate it there, then install a derived runtime copy:

```bash
PBG_SOURCE_DIR="/Users/your-name/Documents/CODING/Skills/product-build-gate"

python3 /path/to/skill-creator/scripts/quick_validate.py "$PBG_SOURCE_DIR"

PBG_RUNTIME_DIR="${CODEX_HOME:-$HOME/.codex}/skills/product-build-gate"
mkdir -p "$(dirname "$PBG_RUNTIME_DIR")"
rsync -a --delete --exclude=.git --exclude=__pycache__ \
  "$PBG_SOURCE_DIR/" "$PBG_RUNTIME_DIR/"
```

Do not edit only the runtime copy. Start a new Codex task after installation so the Skill catalog is refreshed.

## Invoke

```text
$product-build-gate

这是我的新项目方案：
[粘贴完整方案]

请在开发前让我确认整个产品、页面和流程；确认开发基线后直接开始开发。
```

Do not invoke this Skill for implementation continuation, routine feature work, bug fixes, status checks, provider selection, headless services, libraries, or pure CLI tools.

## Project artifacts

- `docs/PRODUCT_BUILD_GATE.md` — preparation, evidence, checkpoint approval, and reopen record
- `docs/SYSTEM_PREVIEW.md` — whole-product module/page/permission/flow coverage and rendered evidence
- `docs/DESIGN_LOCK.md` — approved visual and interaction contract
- `docs/APPROVED_BUILD_BASELINE.md` — single pre-build handoff to native Codex

The helper creates and structurally validates these artifacts:

```bash
python3 scripts/gate.py --help
```

Structural validation does not replace rendered verification or product judgment.

## Safety

- No substantial production implementation before Design Lock and build authorization
- No automatic Skill/plugin installation or LeanSkill rerouting
- No deployment, paid calls, production data, real external writes, or real customer communication without explicit authority
- Local, Mock/Fake, real integration, not-run, and blocked evidence remain distinct

## Requirements

- Codex Desktop or Codex CLI with Skill support
- Python 3.10+
- A user-facing product proposal

## License

Apache-2.0. See [LICENSE](LICENSE).
