---
name: product-build-gate
description: Use only when the user explicitly invokes `$product-build-gate` or asks to start Product Build Gate for a genuinely new user-facing product, app, website, or game, or for a major product/UX redesign. Turn a proposal into an approved build baseline through a product contract, bounded prior-art scan, experience map, exactly three comparable visual prototypes, design lock, build blueprint, and a verified vertical slice. Do not use for headless services or pure CLI tools, routine feature work, bug fixes, status checks, research, provider selection, failed gates, or implementation continuation.
---

# Product Build Gate

## Purpose

Prevent full implementation from starting before the user can see, operate, and approve what will be built.

Produce `docs/APPROVED_BUILD_BASELINE.md`, hand execution back to native Codex, and exit. Do not become a persistent router, loop engine, project manager, or replacement for native implementation judgment.

Use this workflow only when the product has a user interface. Handle headless services, libraries, and pure CLI tools with a smaller architecture-and-contract workflow instead.

## Start safely

1. Read the nearest `AGENTS.md`, project instructions, proposal, relevant code, and current project state.
2. Confirm that the request matches this Skill's explicit trigger. If it does not, stop using this Skill and continue natively.
3. If `docs/APPROVED_BUILD_BASELINE.md` exists, report that a baseline already exists. Do not restart unless the user explicitly requests product re-planning.
4. If `docs/PRODUCT_BUILD_GATE.md` does not exist, initialize it:

   ```bash
   python3 <skill-dir>/scripts/gate.py init --project <project-path> --title "<product title>"
   ```

5. If `docs/LEANSKILL_PLAN.md` exists, consult it only as advisory context. Never invoke, rerun, embed, or simulate LeanSkill from this Skill.
6. Read [gates.md](references/gates.md). At the Prior Art stage, also read [capability-policy.md](references/capability-policy.md).

## Non-negotiable rules

- Do not perform substantial production implementation before Design Lock. Throwaway prototypes are allowed.
- Present exactly three genuinely different, directly comparable visual directions using the same core content, anchor journey, viewport, and required states.
- Verify real rendered prototypes in a browser or simulator; source inspection alone is not acceptance.
- Require explicit user approval at Product Contract, Design Lock, and Vertical Slice/Approved Baseline.
- Allow feedback at any gate. Reopen only the gates affected by a material change.
- Use native Codex as the default owner. Add specialist Skills only when they provide concrete stage-specific value.
- Use at most one primary Skill and two specialist Skills in a stage; count transitive dependencies.
- Do not install, enable, download, or execute a new Skill or plugin without explicit user approval.
- Do not deploy, publish, spend money, use production data, call paid services, or mutate external systems without explicit authority.
- Label every verification result as local, Mock/Fake, real integration, browser/simulator tested, not run, or blocked.
- Treat script validation as structural evidence only. It never substitutes for product judgment, real journey verification, or user approval.

## Run the gates

Maintain decisions and checklist state in `docs/PRODUCT_BUILD_GATE.md`. End every gate update with four short fields: current gate, produced artifact, verification evidence, and user decision required.

### Gate 0 — Product Contract

Define the target user, operating context, problem, measurable value, one anchor journey, scope, and explicit out-of-scope items. Resolve contradictions before any visual or technical work.

Pause for explicit approval. Do not infer approval from silence or from a positive reaction to only part of the contract.

### Gate 1 — Prior Art and capability scan

Research only what can materially reduce risk or improve quality. Compare no more than three product/repository references and no more than two external Skill/plugin candidates.

For each candidate, record evidence, fit, maintenance, license, security/data implications, integration cost, and one decision: adopt, adapt, reference, or reject. Prefer installed and verified capabilities. If a material capability is missing, propose candidates and wait for installation approval.

### Gate 2 — Experience Map

Map the anchor journey as:

`entry → user action → visible result → persisted result → failure recovery`

Define the screen/state map, navigation, permissions, empty/loading/success/error states, and what the user can observe after each action. Do not choose the production stack yet.

### Gate 3 — Visual Prototype

Create exactly three comparable directions. Each direction must include the same product content and core actions while differing meaningfully in hierarchy, layout, visual language, density, and interaction treatment.

Make the prototypes clickable enough to run the anchor journey. Render and inspect desktop/mobile or the relevant target device, including loading, empty, success, and error states. Ask the user to select, combine, or reject directions. Iterate here until the visual target is credible.

### Gate 4 — Design Lock

After Gate 3 is complete, create the design lock:

```bash
python3 <skill-dir>/scripts/gate.py create-design-lock --project <project-path>
```

Record approved references, screenshots, design tokens, typography, spacing, component and interaction states, responsive rules, motion, accessibility, and explicit do/don't constraints in `docs/DESIGN_LOCK.md`.

Pause for explicit approval. No production UI implementation may start before approval is recorded.

### Gate 5 — Build Blueprint

Choose the minimum production architecture only after Design Lock. Record reuse decisions, stack, data model, API/integration boundaries, privacy/security/cost limits, test strategy, and an ordered tracer-bullet TODO.

Every TODO must connect to observable acceptance criteria. Avoid infrastructure or abstraction that the accepted vertical slice does not require.

### Gate 6 — Vertical Slice

Implement only the first real end-to-end journey:

`entry → action → visible result → persistence → failure recovery`

Use real browser or simulator evidence. Verify the actual entry, interactive action, visible outcome, persistence across reload/reopen where applicable, and a recoverable failure. Clearly distinguish Mock/Fake behavior from real integration.

Pause for user acceptance. If the slice is wrong, stop expansion and reopen the affected Product Contract, Experience, Visual, Design, or Blueprint gate.

### Gate 7 — Approved Build Baseline

After Gate 6 is accepted, create the handoff document:

```bash
python3 <skill-dir>/scripts/gate.py create-baseline --project <project-path>
```

Consolidate the latest accepted product contract, experience, design lock, architecture, vertical-slice evidence, scope, acceptance criteria, unresolved blocks, and change-control rules in `docs/APPROVED_BUILD_BASELINE.md`.

Ask for explicit final approval, mark the final checklist, then run:

```bash
python3 <skill-dir>/scripts/gate.py validate --project <project-path> --through approved-baseline
```

When validation passes, state that Product Build Gate has exited. Native Codex now owns implementation and may choose installed specialist Skills directly as concrete needs arise.

## Handle changes without restarting blindly

- Small copy, spacing, or implementation-detail changes: update the relevant artifact and keep the current gate.
- Journey, information architecture, visual direction, or component behavior changes: reopen Experience Map, Visual Prototype, and/or Design Lock.
- Scope, target user, value, or anchor-journey changes: reopen Product Contract and every affected downstream gate.
- Architecture changes that do not alter the accepted experience: reopen Build Blueprint and reverify the Vertical Slice.

Never silently alter an approved baseline. Record the reason, affected gates, evidence, and new approval.
