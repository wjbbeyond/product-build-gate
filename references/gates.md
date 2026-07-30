# Gate acceptance criteria

These criteria determine whether the pre-build confirmation is complete. Product Build Gate exits before production implementation.

## Gate 0 — Product Contract

Required:

- One named primary user and concrete operating context.
- A problem stated in user language.
- A measurable or directly observable product outcome.
- One complete main business journey.
- In-scope and out-of-scope boundaries.
- Contradictions resolved or explicitly visible in the whole-product preview.

Existing complete source documents may satisfy this Gate. Do not make the user restate approved information.

## Gate 1 — Prior Art and capability scan

This Gate is conditional.

When run, require:

- Search questions tied to a material decision or risk.
- At most three product/repository references.
- At most two external Skill/plugin candidates.
- Direct evidence and one adopt/adapt/reference/reject decision per candidate.

When no decision-changing gap exists, record `SKIPPED — no decision-changing evidence gap`. Do not search or request approval for ceremony.

## Gate 2 — Experience Map

Required:

- One complete journey from the real user entry through recovery.
- Screen/state map with navigation and prerequisites.
- Visible result and persistence behavior.
- Empty, loading, success, validation-error, system-error, and permission states where applicable.
- Plain-language success criteria.

Reject a journey that starts from a convenient seeded technical object when the approved user must first complete another business step.

## Gate 3 — System Map and whole-product preview

Required in `docs/SYSTEM_PREVIEW.md`:

- Every key module has a named responsibility and at least one representative page/surface.
- Every page has a stable ID, user goal, actions, permission, required states, dependencies, source coverage, and preview reference.
- Core flows map to ordered page IDs and include failure/recovery routes.
- Cross-page navigation and shared-data dependencies are explicit.
- Unsupported, deferred, and ambiguous requirements are visible.
- A system overview makes module → page → flow relationships understandable.
- A visual target and initial tokens exist.
- The preview is browsable with Mock/Fake data and labeled non-production.
- Every page entry and required state was inspected in a real browser or simulator.
- Product Contract, Experience Map, System Map, and preview agree.
- The user explicitly approved the combined product and whole-product preview checkpoint.

Reject one-journey previews, page-name-only sitemaps, hidden key modules, or a technical console presented as the product.

## Gate 4 — Visual target resolution

This Gate is conditional:

- If the user already supplied a clear visual target or approved reference, one faithful rendered direction is sufficient.
- If unresolved, compare the smallest useful set—normally two, never more than three.
- Every compared direction uses the same content, actions, viewport, and required states.
- Differences are meaningful, not color swaps.
- Rendered browser/simulator evidence exists.

Do not create alternatives solely to satisfy a numeric quota.

## Gate 5 — Design Lock

Required in `docs/DESIGN_LOCK.md`:

- Approved target and reference captures.
- Color, typography, spacing, radius, elevation, icon, and motion tokens.
- Component states and interaction behavior.
- Responsive or device-layout rules.
- Accessibility constraints.
- Explicit do/don't rules.
- User approval recorded.

## Gate 6 — Build Blueprint and Approved Build Baseline

Required:

- Minimum stack and architecture follow the accepted journey.
- Reuse/adopt/build decisions are explicit.
- Data, persistence, API, authentication, privacy, security, cost, Secret, and external-action boundaries are explicit.
- Ordered implementation slices exist.
- Every user-facing slice maps to approved flow IDs and page IDs.
- Every representative slice identifies the real user entry, visible result, persistence, and recoverable failure.
- Approved app shell, navigation, page responsibilities, and Design Lock are inherited.
- Internal technical tracer bullets are labeled internal and cannot replace the product UI.
- Speculative infrastructure and unrelated expansion are excluded.
- `docs/APPROVED_BUILD_BASELINE.md` consolidates the latest accepted decisions.
- The user explicitly approved the baseline and authorized local/isolated implementation.
- Structural validation passes through `approved-baseline`.

After this Gate, Product Build Gate exits. Vertical Slice is the first native implementation milestone, not another Product Build Gate.

## Native implementation milestone — first Vertical Slice

Verify during implementation:

- The approved real entry works.
- The user action produces the approved visible result.
- Required persistence survives reload/reopen.
- At least one realistic failure is understandable and recoverable.
- Real browser or simulator evidence exists.
- Local, Mock/Fake, real integration, not-run, and blocked boundaries are explicit.
- The product can be used without understanding internal state machines.

Failure here normally means fixing implementation against the baseline. Reopen a pre-build checkpoint only when the baseline itself must materially change.
