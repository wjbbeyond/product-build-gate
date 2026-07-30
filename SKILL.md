---
name: product-build-gate
description: Use only when the user explicitly invokes `$product-build-gate` or asks to start Product Build Gate for a genuinely new user-facing product, app, website, or game, or for a major product/UX redesign. Turn a proposal into one approved pre-build baseline through a product contract, bounded evidence gathering, experience and system maps, a browsable Mock/Fake whole-product preview, a resolved visual target, Design Lock, and a traceable Build Blueprint. Exit before production implementation so native Codex can build continuously from the approved baseline. Do not use for implementation continuation, routine feature work, bug fixes, status checks, research, provider selection, failed gates, headless services, or pure CLI tools.
---

# Product Build Gate

## Purpose

Prevent implementation from starting against an invisible or misunderstood product, while avoiding repeated confirmation after the product is already clear.

Produce `docs/APPROVED_BUILD_BASELINE.md`, obtain one explicit build authorization, hand execution back to native Codex, and exit **before production implementation**. Do not become a persistent router, loop engine, project manager, sprint process, or replacement for native implementation judgment.

Use this workflow only for a genuinely new user-facing product or a major product/UX redesign. Once the baseline is approved, implementation continuation must run natively and must not re-invoke this Skill unless the user explicitly requests product re-planning.

## Core contract

- Confirm product meaning, whole-product coverage, and design before production implementation.
- Treat every approved page ID, journey, responsibility, permission, state, and design rule as an implementation contract.
- After the build baseline is approved, develop continuously. Do not ask the user to reconfirm internal task ordering, code structure, tests, or already-approved behavior.
- Reopen only the smallest affected checkpoint when implementation would materially change the approved product.
- A technical tracer bullet may precede a user-facing milestone, but it is internal evidence. It must not replace the approved app shell, navigation, real user entry, or page responsibilities.

## Start safely

1. Read the nearest `AGENTS.md`, project instructions, proposal, relevant code, and current project state.
2. Confirm that the request matches this Skill's explicit trigger. If it does not, stop using this Skill and continue natively.
3. If `docs/APPROVED_BUILD_BASELINE.md` already records user build approval, report that the pre-build gate has exited and continue implementation natively. Do not restart unless the user explicitly requests product re-planning.
4. If `docs/PRODUCT_BUILD_GATE.md` does not exist, initialize it:

   ```bash
   python3 <skill-dir>/scripts/gate.py init --project <project-path> --title "<product title>"
   ```

5. If `docs/LEANSKILL_PLAN.md` exists, consult it only as advisory context. Never invoke, rerun, embed, or simulate LeanSkill from this Skill.
6. Read [gates.md](references/gates.md). Only when a material evidence gap exists, read [capability-policy.md](references/capability-policy.md) and run a bounded prior-art/capability scan.

## Three approval checkpoints

Internal stages may advance automatically when their evidence is complete. Ask the user only at these three decision points:

1. **Product and whole-product preview approval** — product contract, experience map, system map, pages, flows, states, permissions, and Mock/Fake preview agree.
2. **Design Lock approval** — the visual target, tokens, components, interactions, responsive behavior, and accessibility are resolved.
3. **Approved Build Baseline and build authorization** — the Build Blueprint is traceable to the approved experience and design; the user authorizes local/isolated implementation.

Do not show an approval menu after Prior Art, Experience Map, internal architecture notes, TODO decomposition, or implementation subtasks.

At a checkpoint, show only:

```text
请选择：
1. 修改当前确认内容
2. 批准当前确认内容并继续
3. 暂停并保存
```

For the final checkpoint, option 2 must say:

```text
2. 批准开发基线并立即开始本地/隔离环境开发
```

The approval does not authorize deployment, production data, paid calls, real external writes, or real customer communication. Those still require their own explicit authority.

## Workflow

Maintain decisions and evidence in `docs/PRODUCT_BUILD_GATE.md`. Every approval record must identify the artifact versions or hashes that were approved.

### Gate 0 — Product Contract

Define the primary user, operating context, problem, measurable or directly observable value, scope, out-of-scope items, and the main end-to-end business journey.

If a complete source document already supplies these decisions, extract and reconcile them instead of asking the user to repeat them. Carry unresolved material contradictions into the whole-product preview; do not interrupt for minor implementation details.

### Gate 1 — Bounded Prior Art and capability scan (conditional)

Run only when a named product, UX, technical, security, cost, or capability risk cannot be resolved from current evidence.

Compare no more than three product/repository references and no more than two external Skill/plugin candidates. Stop as soon as the evidence supports a decision. If no material gap exists, record `SKIPPED — no decision-changing evidence gap` and continue without user approval.

### Gate 2 — Experience Map

Map the main business journey as:

`real entry → user action → visible result → persisted result → failure recovery`

Define navigation, prerequisites, permissions, empty/loading/success/error states, and observable outcomes. The journey must begin where the approved user actually begins, not at a convenient mid-flow technical object.

### Gate 3 — System Map and whole-product preview

After Gate 2, create the system-preview record:

```bash
python3 <skill-dir>/scripts/gate.py create-system-preview --project <project-path>
```

Extract the complete planned product into:

- functional modules and responsibilities;
- page/surface inventory with stable page IDs, user goals, and primary actions;
- roles, permissions, and protected actions;
- core flows and their ordered page sequence;
- empty, loading, success, validation, permission, offline, and system-error states;
- cross-page navigation and data dependencies;
- source-document coverage, assumptions, gaps, and deferred scope.

Define the initial visual target and tokens, then create a disposable browsable Mock/Fake preview. Every key module needs at least one representative page. Verify the real rendered preview in a browser or simulator.

Now request **Checkpoint 1: Product and whole-product preview approval**. One approval covers the reconciled Product Contract, Experience Map, System Map, page responsibilities, and preview. Do not ask for separate approvals for Gates 0–2 unless a material contradiction blocked the combined result.

### Gate 4 — Visual target resolution (conditional)

If the user already supplied a clear visual target or approved reference, implement one faithful comparable direction and validate it. Do not generate alternatives merely to satisfy a quota.

If the visual target is unresolved, create the smallest useful comparison set—normally two, never more than three—using the same representative content, viewport, and required states. Differences must be meaningful, not color swaps.

Gate 4 is evidence gathering for Design Lock, not another mandatory approval checkpoint.

### Gate 5 — Design Lock

Create the design lock:

```bash
python3 <skill-dir>/scripts/gate.py create-design-lock --project <project-path>
```

Record approved references, screenshots, design tokens, typography, spacing, components, interaction states, responsive rules, motion, accessibility, and explicit do/don't constraints in `docs/DESIGN_LOCK.md`.

Request **Checkpoint 2: Design Lock approval**.

### Gate 6 — Build Blueprint and Approved Build Baseline

Choose the minimum production architecture that implements the already-approved product. Record:

- reuse/adopt/build decisions;
- stack and module boundaries;
- data, persistence, commands, events, API, and integration contracts;
- privacy, security, cost, Secret, and external-action boundaries;
- ordered implementation slices;
- proportional tests and observable acceptance criteria.

Add a traceability matrix:

| Implementation slice | Approved journey/flow IDs | Approved page IDs | Real user entry | Visible result | Persistence | Failure recovery |
|---|---|---|---|---|---|---|

Rules:

- Every user-facing slice inherits the approved app shell, navigation, page responsibility, and Design Lock.
- The first representative user-facing slice must start from an approved real entry. A pre-seeded mid-flow route may be used only as an internal technical test.
- Internal infrastructure order may change without user approval when behavior, cost, security, and scope remain inside the baseline.
- Do not put an approved page or prerequisite business step “after” a representative slice that depends on it.

Create the baseline before implementation:

```bash
python3 <skill-dir>/scripts/gate.py create-baseline --project <project-path>
```

Consolidate the latest accepted product, experience, page map, design, architecture, scope, acceptance criteria, implementation traceability, unresolved blocks, and change-control rules in `docs/APPROVED_BUILD_BASELINE.md`.

Request **Checkpoint 3: Approved Build Baseline and build authorization**. When approved, run:

```bash
python3 <skill-dir>/scripts/gate.py validate --project <project-path> --through approved-baseline
```

When validation passes, state that Product Build Gate has exited. Native Codex must immediately continue with the ordered local/isolated implementation unless a separate external-action approval is required.

## After exit: native implementation contract

Product Build Gate does not run during implementation.

Native Codex must:

1. Read the approved baseline and current implementation slice.
2. Check the slice against its approved flow IDs, page IDs, real entry, visible result, persistence, and recovery.
3. Implement the smallest complete slice without redefining product navigation or page responsibilities.
4. Verify the rendered journey in a browser or simulator and record Local/Mock/Fake/real/not-run/blocked evidence.
5. Continue to the next ordered slice automatically when the implementation matches the baseline.

Do not ask for another product approval merely because:

- a new internal module, migration, test, adapter interface, or task breakdown is needed;
- implementation order changes without user-visible or material operational impact;
- a bug is found and fixed inside approved behavior;
- a partial technical tracer bullet is built and clearly kept internal.

## Drift control

Continue without reopening a checkpoint for:

- internal code structure, libraries, tests, migrations, and implementation ordering;
- copy or spacing corrections inside the Design Lock;
- bug fixes and missing states already required by the baseline;
- additional diagnostics that remain outside the primary user experience.

Stop and reopen only the smallest affected checkpoint when a proposed change alters:

- target user, product value, scope, or out-of-scope boundary;
- modules, page responsibilities, navigation, permissions, or a core business journey;
- user-visible state behavior or persistence/recovery expectations;
- visual direction or locked component behavior;
- data sensitivity, external integration, recurring cost, paid usage, production writes, deployment, or real customer communication;
- an architecture contract in a way that changes the accepted experience, safety, or cost.

Never silently alter an approved baseline. Record the reason, affected checkpoint, preserved evidence, and new approval.

## Safety and evidence

- No substantial production implementation before Design Lock and final build authorization. Throwaway previews are allowed.
- No automatic Skill/plugin installation or LeanSkill rerouting.
- No deployment, publishing, paid calls, production data, real external writes, or real customer communication without explicit authority.
- Use native Codex by default and at most one primary plus two specialist Skills in a stage.
- Label evidence as local, Mock/Fake, real integration, browser/simulator tested, not run, or blocked.
- Script validation is structural evidence only; it never substitutes for product judgment or rendered verification.
