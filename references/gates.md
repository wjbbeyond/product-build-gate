# Gate acceptance criteria

Use these criteria to decide whether a gate is genuinely complete. A checked box is a claim that must be backed by the named artifact, rendered evidence, or explicit user approval.

## Gate 0 — Product Contract

Required:

- One named primary user and a concrete use context.
- A problem stated in user language, not as a feature list.
- A measurable or directly observable product outcome.
- One anchor journey that can later become a vertical slice.
- In-scope and out-of-scope boundaries.
- Contradictions and open decisions resolved or explicitly blocked.
- Explicit user approval recorded with date and the approved version.

Reject the gate when the proposal contains several unrelated products, relies on undefined terms such as "AI-powered" as the value, or has no observable user outcome.

## Gate 1 — Prior Art

Required:

- Search questions tied to an identified product or delivery risk.
- At most three product/repository references.
- At most two external Skill/plugin candidates.
- Direct evidence from official documentation, maintained repositories, or rendered products.
- Fit, license, maintenance, security/data, and integration-cost notes.
- Adopt, adapt, reference, or reject decision for every candidate.

Stop searching when the evidence can support a decision. Popularity alone is not evidence of fit.

## Gate 2 — Experience Map

Required:

- One complete anchor journey from entry through recovery.
- Screen/state map with navigation and prerequisites.
- Visible result and persistence behavior.
- Empty, loading, success, validation-error, system-error, and permission states where applicable.
- Plain-language success criteria that a user can verify.

Reject the gate if it describes only backend states, API calls, or page names without user-visible outcomes.

## Gate 3 — Visual Prototype

Required:

- Exactly three comparable directions.
- Same product content, anchor journey, core actions, target viewport, and required states in all three.
- Meaningful differences in composition, hierarchy, density, typography, visual language, and interaction—not merely colors.
- Clickable anchor journey.
- Real rendered desktop/mobile or target-device evidence.
- Loading, empty, success, and error states.
- User decision and requested changes recorded.

The prototype may use disposable data and code. It must not be mistaken for production architecture.

## Gate 4 — Design Lock

Required in `docs/DESIGN_LOCK.md`:

- Approved direction and reference captures.
- Color, typography, spacing, radius, elevation, icon, and motion tokens.
- Component states and interaction behavior.
- Responsive or device-layout rules.
- Accessibility constraints.
- Explicit do/don't rules.
- User approval recorded.

Reject the gate if terms such as "modern", "premium", or "beautiful" are used without visual evidence and tokens.

## Gate 5 — Build Blueprint

Required:

- Minimum stack and architecture justified by the accepted journey.
- Reuse/adopt/build decisions.
- Data, persistence, API, authentication, privacy, security, and cost boundaries.
- Real versus Mock/Fake integration plan.
- Ordered tracer-bullet TODO.
- Observable acceptance criteria and proportional tests for each slice.
- Explicit non-goals that prevent expansion.

Reject speculative infrastructure, generalized frameworks, or abstractions not required by the accepted vertical slice.

## Gate 6 — Vertical Slice

Required:

- Real entry point works.
- User action produces the approved visible result.
- Persistence survives reload/reopen where the product requires it.
- At least one realistic failure is understandable and recoverable.
- Real browser or simulator evidence exists.
- Console/runtime errors are checked.
- Local, Mock/Fake, real integration, not run, and blocked boundaries are explicit.
- User accepts the slice as representative of the intended product.

Test success alone is insufficient. The slice must be usable without understanding internal state machines.

## Gate 7 — Approved Build Baseline

Required:

- Latest accepted decisions are consolidated, not copied from stale drafts.
- Product contract, experience map, design lock, build blueprint, and vertical-slice evidence agree.
- Scope, acceptance criteria, unresolved blocks, and change-control rules are explicit.
- User gives final approval.
- Product Build Gate exits and native Codex assumes implementation ownership.

