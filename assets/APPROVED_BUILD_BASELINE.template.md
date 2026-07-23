---
approved_build_baseline_version: 1
project_title: "{{PROJECT_TITLE}}"
created_at: "{{CREATED_AT}}"
---

# Approved Build Baseline — {{PROJECT_TITLE}}

## Product contract

- Primary user and context:
- Problem and observable value:
- Anchor journey:
- Scope:
- Out of scope:

## Approved experience

- Journey and state-map reference:
- User-visible success:
- Persistence:
- Failure recovery:

## Approved design

- Design Lock: `docs/DESIGN_LOCK.md`
- Approved prototype/screenshots:
- Non-negotiable visual and interaction constraints:

## Build blueprint

- Stack and architecture:
- Reuse/adopt/build decisions:
- Data and integrations:
- Privacy/security/cost boundaries:
- Ordered implementation plan:

## Vertical-slice evidence

- Browser/simulator evidence:
- Entry/action/result:
- Persistence:
- Failure recovery:
- Local/Mock/real/not-run/blocked boundary:
- User acceptance:

## Remaining scope and blocks

-

## Change control

- Small implementation-detail changes update this baseline without restarting unaffected gates.
- Product contract, journey, design, or architecture changes reopen only the affected gates and downstream verification.
- Native Codex must not silently change this approved baseline.

<!-- GATE:approved-baseline:START -->
## Final approval

- [ ] This baseline reflects the latest accepted Product Contract.
- [ ] This baseline agrees with the approved Experience Map and Design Lock.
- [ ] This baseline agrees with the verified Vertical Slice.
- [ ] Scope, acceptance criteria, integration boundaries, and blocks are explicit.
- [ ] The user explicitly approved this baseline.
- [ ] Product Build Gate will exit and native Codex will own implementation.
<!-- GATE:approved-baseline:END -->
