---
product_build_gate_version: 1
project_title: "{{PROJECT_TITLE}}"
created_at: "{{CREATED_AT}}"
---

# Product Build Gate — {{PROJECT_TITLE}}

This document is the product decision record. It is not a general task log.

## Gate receipt

- Current gate:
- Produced artifact:
- Verification evidence:
- User decision required:

<!-- GATE:product-contract:START -->
## Gate 0 — Product Contract

### Decision

- Primary user and context:
- Problem:
- Observable value:
- Anchor journey:
- In scope:
- Out of scope:
- Open decisions or blockers:
- Approved version/date:

### Completion

- [ ] One primary user and operating context are explicit.
- [ ] The problem and observable product value are explicit.
- [ ] One anchor journey is defined end to end.
- [ ] In-scope and out-of-scope boundaries are explicit.
- [ ] Contradictions and material open decisions are resolved or blocked.
- [ ] The user explicitly approved this Product Contract.
<!-- GATE:product-contract:END -->

<!-- GATE:prior-art:START -->
## Gate 1 — Prior Art and capability scan

### Search questions

-

### Candidate decisions

| Candidate | Evidence | Fit and gaps | License/security/maintenance/integration | Decision |
|---|---|---|---|---|
|  |  |  |  | adopt / adapt / reference / reject |

### Completion

- [ ] Search questions are tied to material risks.
- [ ] No more than three product/repository references were compared.
- [ ] No more than two external Skill/plugin candidates were compared.
- [ ] Every candidate has direct evidence and a recorded decision.
- [ ] No new Skill/plugin was installed without explicit user approval.
<!-- GATE:prior-art:END -->

<!-- GATE:experience-map:START -->
## Gate 2 — Experience Map

### Anchor journey

`entry → action → visible result → persisted result → failure recovery`

### Screen and state map

| Screen/state | Entry condition | User action | Visible result | Persistence | Recovery |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

### Completion

- [ ] The anchor journey includes entry, action, result, persistence, and recovery.
- [ ] Navigation, prerequisites, and permissions are explicit.
- [ ] Empty, loading, success, and error states are defined where applicable.
- [ ] Each step has a user-observable success criterion.
<!-- GATE:experience-map:END -->

<!-- GATE:visual-prototype:START -->
## Gate 3 — Visual Prototype

### Shared comparison brief

- Content:
- Core actions:
- Target viewport/device:
- Required states:

### Directions

| Direction | Meaningful design difference | Prototype/evidence | User feedback |
|---|---|---|---|
| A |  |  |  |
| B |  |  |  |
| C |  |  |  |

### Completion

- [ ] Exactly three genuinely different directions use the same comparison brief.
- [ ] The anchor journey is clickable in every direction.
- [ ] Required states are rendered.
- [ ] Desktop/mobile or target-device evidence was inspected.
- [ ] The user selected, combined, or rejected directions and feedback is recorded.
<!-- GATE:visual-prototype:END -->

<!-- GATE:design-lock:START -->
## Gate 4 — Design Lock

See `docs/DESIGN_LOCK.md`.

### Completion

- [ ] The selected direction and approved references are recorded.
- [ ] Tokens, component states, responsive behavior, and interaction rules are explicit.
- [ ] Accessibility and do/don't constraints are explicit.
- [ ] The user explicitly approved the Design Lock.
<!-- GATE:design-lock:END -->

<!-- GATE:build-blueprint:START -->
## Gate 5 — Build Blueprint

### Decisions

- Minimum stack and architecture:
- Reuse/adopt/build decisions:
- Data and persistence:
- APIs and external integrations:
- Authentication, privacy, and security:
- Cost and usage limits:
- Real versus Mock/Fake boundaries:
- Test strategy:
- Non-goals:

### Tracer-bullet TODO

| Order | Deliverable | Observable acceptance | Verification |
|---:|---|---|---|
| 1 |  |  |  |

### Completion

- [ ] Architecture follows the accepted journey and Design Lock.
- [ ] Data, integration, privacy, security, and cost boundaries are explicit.
- [ ] Real and Mock/Fake paths are distinguished.
- [ ] TODOs are ordered and have observable acceptance criteria.
- [ ] Speculative infrastructure and unrelated expansion are excluded.
<!-- GATE:build-blueprint:END -->

<!-- GATE:vertical-slice:START -->
## Gate 6 — Vertical Slice

### Evidence

- Real entry:
- User action:
- Visible result:
- Persistence:
- Failure and recovery:
- Browser/simulator evidence:
- Console/runtime result:
- Local/Mock/real/not-run/blocked boundary:
- User acceptance/date:

### Completion

- [ ] The real entry point and anchor action work.
- [ ] The approved visible result appears.
- [ ] Required persistence survives reload/reopen.
- [ ] A realistic failure is understandable and recoverable.
- [ ] The journey was verified in a real browser or simulator.
- [ ] Integration boundaries and blocked items are explicit.
- [ ] The user accepted the slice as representative of the intended product.
<!-- GATE:vertical-slice:END -->
