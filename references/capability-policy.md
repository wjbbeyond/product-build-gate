# Capability selection policy

Product Build Gate selects assistance only for pre-build confirmation; it does not route implementation tasks or keep specialist Skills permanently active.

## Selection order

1. Native Codex owns the stage by default.
2. Inspect the currently available Skill/plugin catalog.
3. Add a specialist only when it supplies a concrete missing method, tool, or verification surface.
4. Prefer installed, verified, narrow capabilities over broad bundles.
5. If a material capability is missing, research no more than two candidates and ask before installation.

Record:

| Capability | Stage role | Evidence of fit | Cost/risk | Decision |
|---|---|---|---|---|
| Native Codex or Skill name | One concrete responsibility | Source, prior result, or required tool | Context, dependency, privacy, maintenance | use / reject / request install |

## Stage patterns

Verify exact names and availability at runtime; these are patterns, not mandatory bundles.

- Prior Art: browser/web research and GitHub inspection only when a named material evidence gap exists.
- System Map and Preview: native Codex by default for extraction and local prototype implementation; optionally one UI/product specialist; one browser/simulator verifier. External design tools may help with selected screens but cannot replace the system map or page coverage.
- Visual target: one Product Design owner; optionally one visual-generation or Figma specialist; one browser/simulator verifier. If the user already supplied a clear target, validate one faithful direction instead of creating artificial alternatives.
- Design Lock: Product Design audit plus the relevant platform UI specialist if it adds concrete constraints.
- Build Blueprint: one platform specialist for Web, iOS, or game architecture; add database, payments, or AI specialists only when they are in the approved scope.
- Build handoff: record the relevant platform builder/debugger and browser/simulator verifier as advisory implementation capabilities. Native Codex selects and invokes them only after Product Build Gate exits.

## Hard limits

- Maximum per stage: one primary plus two specialists, including transitive dependencies.
- One design owner per visual output. Do not combine several opinionated design systems and average their results.
- Do not preload the initial LeanSkill shortlist or treat it as a whitelist.
- Do not install from popularity, star count, or a social-media claim alone.
- Product Build Gate must exit before ordinary implementation.

## Candidate evaluation

Before proposing an external Skill/plugin, check:

- Task fit and whether native Codex already covers it.
- Evidence from real outputs or maintained documentation.
- Repository activity and issue quality.
- License and redistribution constraints.
- Prompt/code security and data destinations.
- Hidden dependencies, transitive Skills, context cost, and model/tool costs.
- Ease of removal and isolation.
- A small A/B test with the same brief and acceptance rubric.

Adopt only if the candidate materially improves quality, speed, or verification without imposing larger coordination or context costs.

## Avoid negative optimization

Reject or isolate:

- Another persistent router, autonomous loop, or mandatory orchestration layer.
- Broad "do everything" bundles that duplicate native Codex.
- Multiple overlapping frontend/design Skills in the same generation step.
- Skills that replace user approval with a score.
- Skills that claim completion from tests without a real rendered journey.
- Skills that require unapproved accounts, keys, paid calls, external writes, or production data.
