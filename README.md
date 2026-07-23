# Product Build Gate

Product Build Gate is an explicit-only Codex Skill for new user-facing products, apps, websites, and games. It prevents full implementation from starting before the product contract, experience, visual direction, production blueprint, and first real end-to-end journey have been reviewed.

> See it, operate it, approve it—then build it.

## Why

An apparently strong written plan can still become the wrong interface or the wrong product. Product Build Gate reduces that gap by requiring observable product decisions and rendered evidence before implementation expands.

It is not a persistent router, autonomous loop, or project manager. It exits after producing an Approved Build Baseline, and native Codex then owns implementation.

## Workflow

1. Product Contract
2. Bounded Prior Art and capability scan
3. Experience Map
4. Exactly three comparable visual prototypes
5. Design Lock
6. Build Blueprint
7. Verified Vertical Slice
8. Approved Build Baseline

The user explicitly approves the Product Contract, Design Lock, and final Vertical Slice/Baseline.

## Install

```bash
PBG_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$PBG_SKILLS_DIR"
git clone https://github.com/wjbbeyond/product-build-gate.git \
  "$PBG_SKILLS_DIR/product-build-gate"
```

Start a new Codex conversation after installation so the Skill list is refreshed.

## Invoke

Product Build Gate is explicit-only. You only need to remember the first invocation. After that, Codex guides every transition with a short menu.

Call it by exact name for a genuinely new user-facing product or a major product/UX redesign:

```text
$product-build-gate

Here is my product proposal:
[paste the proposal]

Start Product Build Gate. Complete the Product Contract first and wait for my approval before continuing.
```

Chinese example:

```text
$product-build-gate

这是我的新项目方案：
[粘贴完整方案]

请启动 Product Build Gate，先完成 Product Contract，等待我确认后再继续。
```

At the end of every Gate, Codex asks:

```text
请选择：
1. 修改当前内容
2. 确认当前 Gate，并进入下一步
3. 暂停并保存进度

可直接回复数字，也可以直接写修改意见。
```

Reply `1` with feedback, `2` to approve the named Gate and continue, or `3` to pause. At the visual-prototype Gate, reply with the selected direction as well, for example `2，选择 B`.

Do not invoke this Skill for routine feature work, bug fixes, status checks, provider selection, implementation continuation, headless services, libraries, or pure CLI tools.

## Project artifacts

The workflow maintains three durable project documents:

- `docs/PRODUCT_BUILD_GATE.md` — gate decisions, evidence, and approval state
- `docs/DESIGN_LOCK.md` — approved visual and interaction contract
- `docs/APPROVED_BUILD_BASELINE.md` — final handoff to native Codex

The included helper creates and structurally validates these artifacts:

```bash
python3 scripts/gate.py --help
```

Structural validation verifies required files and checklists. It does not replace real rendered evidence, product judgment, or user approval.

## Safety and scope

- No automatic Skill or plugin installation
- No automatic LeanSkill rerouting
- No deployment, publishing, paid calls, production data, or external mutation without authority
- At most one primary and two specialist Skills per stage
- Real browser or simulator verification before product approval
- Explicit separation of local, Mock/Fake, real integration, not-run, and blocked results

## Requirements

- Codex Desktop or Codex CLI with Skill support
- Python 3.10+
- A user-facing product proposal

## License

Apache-2.0. See [LICENSE](LICENSE).
