---
approved_build_baseline_version: 2
baseline_status: draft
project_title: "{{PROJECT_TITLE}}"
created_at: "{{CREATED_AT}}"
---

# Approved Build Baseline — {{PROJECT_TITLE}}

This document is the single pre-build handoff. After approval, Product Build Gate exits and native Codex implements against this contract.

## Locked product

- Primary user and context:
- Problem and observable value:
- Scope:
- Out of scope:
- Main business journey:

## Locked experience

- Experience Map:
- System Map:
- Stable page IDs and responsibilities:
- Whole-product preview:
- Real user entry:
- Visible success:
- Persistence:
- Failure recovery:
- Permissions and protected actions:

## Locked design

- Design Lock: `docs/DESIGN_LOCK.md`
- Approved references/screenshots:
- Non-negotiable visual and interaction constraints:

## Build Blueprint

- Blueprint reference/version/hash:
- Stack and architecture:
- Reuse/adopt/build:
- Data and integrations:
- Privacy/security/Secret/cost boundaries:
- Real versus Mock/Fake boundaries:
- Ordered implementation plan:

## Implementation traceability

| Order/slice | Approved flow IDs | Approved page IDs | Real entry | Visible result | Persistence | Failure recovery |
|---:|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |

## Native implementation contract

- Product Build Gate exits immediately after final approval.
- Native Codex continues the ordered local/isolated implementation without repeating product approvals.
- Every user-facing slice inherits the approved app shell, navigation, page responsibilities, and Design Lock.
- Internal technical tracer bullets remain internal and cannot be presented as the intended product.
- Browser/simulator verification records Local/Mock/Fake/real/not-run/blocked evidence.
- Only a material baseline change reopens the smallest affected checkpoint.

## External-action boundary

- Authorized local/isolated actions:
- Still requires separate explicit approval:
- Production data:
- Paid calls:
- Deployment/publishing:
- Real external writes or customer communication:

## Remaining blocks

-

## Change control

Continue without reapproval for internal code structure, tests, migrations, task ordering, bug fixes, and already-required states that do not change product behavior, safety, cost, or scope.

Reopen the smallest affected checkpoint for material changes to product scope/value, modules/pages/navigation/permissions, core journeys, locked design behavior, sensitive data, external integrations, recurring cost, production writes, deployment, or real customer communication.

<!-- GATE:approved-baseline:START -->
## Final approval

- Approved artifact versions/hashes:
- User approval wording/date:
- Authorized environment:

- [ ] This baseline reflects the latest accepted Product Contract and whole-product preview.
- [ ] It agrees with the Experience Map, System Map, page responsibilities, and Design Lock.
- [ ] Every implementation slice is traceable to approved flow and page IDs.
- [ ] Scope, acceptance criteria, integration boundaries, and remaining blocks are explicit.
- [ ] The user explicitly approved this baseline and authorized local/isolated implementation.
- [ ] Product Build Gate exits; native Codex owns continuous implementation.
<!-- GATE:approved-baseline:END -->
