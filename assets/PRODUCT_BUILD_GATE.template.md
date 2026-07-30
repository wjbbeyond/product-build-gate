---
product_build_gate_version: 3
project_title: "{{PROJECT_TITLE}}"
created_at: "{{CREATED_AT}}"
---

# Product Build Gate — {{PROJECT_TITLE}}

This is a pre-build product decision record, not a sprint log or implementation task tracker.

## Current receipt

- Current stage:
- Produced artifact:
- Verification evidence:
- User decision required:

## Approval checkpoints

Only three user approvals are required:

1. Product Contract + Experience Map + System Map + whole-product preview.
2. Design Lock.
3. Approved Build Baseline and authorization to begin local/isolated implementation.

Internal stages advance without an approval menu when their evidence is complete.

## Reopen and change log

| Date/version | Material reason | Checkpoint reopened | Preserved evidence | New approval |
|---|---|---|---|---|
|  |  |  |  |  |

<!-- GATE:product-contract:START -->
## Gate 0 — Product Contract

### Decision

- Primary user and context:
- Problem:
- Observable value:
- Main business journey:
- In scope:
- Out of scope:
- Material contradictions or blockers:

### Completion

- [ ] One primary user and operating context are explicit.
- [ ] The problem and observable product value are explicit.
- [ ] The main business journey is defined end to end.
- [ ] In-scope and out-of-scope boundaries are explicit.
- [ ] Material contradictions are resolved or made visible for the combined product checkpoint.
<!-- GATE:product-contract:END -->

<!-- GATE:prior-art:START -->
## Gate 1 — Prior Art and capability scan

### Decision

- Status: `RUN` / `SKIPPED — no decision-changing evidence gap`
- Material question or risk:

| Candidate | Direct evidence | Fit/gap | Cost/security/maintenance | Decision |
|---|---|---|---|---|
|  |  |  |  | adopt / adapt / reference / reject |

### Completion

- [ ] A material evidence gap is named, or the scan is explicitly skipped.
- [ ] If run, limits and evidence requirements were respected.
- [ ] No Skill/plugin was installed without explicit user approval.
<!-- GATE:prior-art:END -->

<!-- GATE:experience-map:START -->
## Gate 2 — Experience Map

### Main journey

`real entry → user action → visible result → persisted result → failure recovery`

| Screen/state | Entry condition | User action | Visible result | Persistence | Recovery |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Completion

- [ ] The journey begins at the approved real user entry.
- [ ] Navigation, prerequisites, and permissions are explicit.
- [ ] Required empty, loading, success, and error states are defined.
- [ ] Each step has a user-observable success criterion.
<!-- GATE:experience-map:END -->

<!-- GATE:system-preview:START -->
## Gate 3 — System Map and whole-product preview

See `docs/SYSTEM_PREVIEW.md`.

### Coverage receipt

- Source documents:
- Functional modules:
- Representative pages:
- Roles/permissions:
- Core flows:
- Cross-page dependencies:
- Browsable preview:
- Browser/simulator evidence:
- Local/Mock/real/not-run/blocked boundary:
- Approved artifact versions/hashes:
- Product checkpoint approval/date:

### Completion

- [ ] Every key module has at least one representative page preview.
- [ ] Stable page IDs map modules, pages, permissions, flows, states, and dependencies.
- [ ] The real entry and whole planned product are understandable.
- [ ] Gaps, assumptions, deferred scope, and prohibited actions are explicit.
- [ ] The browsable Mock/Fake preview was inspected in a real browser or simulator.
- [ ] Product Contract, Experience Map, System Map, and preview agree.
- [ ] The user explicitly approved the combined product and whole-product preview checkpoint.
<!-- GATE:system-preview:END -->

<!-- GATE:visual-prototype:START -->
## Gate 4 — Visual target resolution

### Decision

- Status: `EXISTING TARGET` / `COMPARISON REQUIRED`
- Existing target/reference:
- Comparison count and reason:
- Rendered evidence:
- Direction carried into Design Lock:

### Completion

- [ ] A clear existing target was faithfully rendered, or the smallest useful comparison set was inspected.
- [ ] Compared directions use the same content, actions, viewport, and states.
- [ ] No alternatives were created solely to satisfy a quota.
<!-- GATE:visual-prototype:END -->

<!-- GATE:design-lock:START -->
## Gate 5 — Design Lock

See `docs/DESIGN_LOCK.md`.

### Receipt

- Approved artifact version/hash:
- Browser/simulator evidence:
- Approval/date:

### Completion

- [ ] Approved references and rendered evidence are recorded.
- [ ] Tokens, component states, responsive behavior, and interaction rules are explicit.
- [ ] Accessibility and do/don't constraints are explicit.
- [ ] The user explicitly approved the Design Lock.
<!-- GATE:design-lock:END -->

<!-- GATE:build-blueprint:START -->
## Gate 6 — Build Blueprint and Approved Build Baseline

### Decisions

- Minimum stack and architecture:
- Reuse/adopt/build:
- Data and persistence:
- APIs and integrations:
- Authentication, privacy, security, and Secrets:
- Cost and external-action limits:
- Real versus Mock/Fake boundaries:
- Test strategy:
- Non-goals:

### Implementation traceability

| Order/slice | Approved flow IDs | Approved page IDs | Real entry | Visible result | Persistence | Failure recovery |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |

### Build authorization receipt

- Approved Build Baseline: `docs/APPROVED_BUILD_BASELINE.md`
- Approved version/hash:
- User authorization/date:
- Authorized environment:
- External actions still blocked:

### Completion

- [ ] Architecture and slices implement the accepted journey and Design Lock.
- [ ] Data, integration, privacy, security, Secret, cost, and external-action boundaries are explicit.
- [ ] Every user-facing slice maps to approved flow/page IDs and a real entry.
- [ ] Technical tracer bullets are internal and cannot replace approved product UI.
- [ ] TODOs are ordered with observable acceptance and proportional verification.
- [ ] The Approved Build Baseline consolidates the latest accepted decisions.
- [ ] The user explicitly approved the baseline and authorized local/isolated implementation.
<!-- GATE:build-blueprint:END -->
