# Core Corpus Evaluation

## Purpose

This document records the manual part of the mathematical-core readiness gate.
The JSONL validator checks corpus structure and coverage; these forward tests
check whether the skill preserves mathematical meaning when it actually writes.

## Protocol

On 2026-07-21, three independent forward-test runs received short mathematical
writing tasks without a model answer. Each run had to revise the prose and then
audit its own output for formula preservation, notation, scope, conditions, and
claim strength. A case passes only if the revision:

1. preserves every supplied formula and symbol;
2. selects language matching the mathematical behavior;
3. retains assumptions, direction, frame, and approximation status; and
4. introduces no unsupported existence, uniqueness, convexity, stability, or
   equivalence claim.

## Cases and results

| Area | Blind input behavior | Required distinction | Result |
|---|---|---|---|
| Definition | Define a residual from `r(x):=Ax-b` with stated dimensions | stipulative definition versus denotation or ordinary equality | PASS |
| Type and mapping | Describe `R∈SO(3)`, `v_I=Rv_B`, and `v_B=R^Tv_I` | mapping direction, domain convention, and inverse relation | PASS |
| Proof claim | Revise a local Lyapunov derivative bound followed by a global-stability overclaim | local consequence versus unsupported global theorem | PASS |
| Derivation | Explain `exp(hA)=I+hA+O(h^2)` and a discrete update | asymptotic expansion versus exact equality | PASS |
| Optimization | State `arg min` with data, decision variable, objective, and constraint | mathematical roles without invented convexity or existence | PASS |
| Computation | Initialize `R_c(0)=R(0)` and propagate a matrix recurrence | measured-state initialization versus fixed default; ordered update | PASS |

The runs correctly used definition, denotation, property, consequence,
approximation, optimization, initialization, and update language. In particular,
they rejected the unsupported global-stability claim and retained the
second-order remainder before presenting the first-order approximation.

## Local repetition regression cases

The following cases were added after a real revision exposed the same repair
template in adjacent equation introductions. They were manually reviewed in the
same editing session, so they are regression checks rather than new independent-
agent evidence.

| Case | Input condition | Required behavior | Review |
|---|---|---|---|
| Unintended duplicate frame | Two nearby tuple introductions both use `collects ... in the ordered tuple` | Distinguish assembly of known measurements from stipulative definition by changing information structure, not by rotating synonyms | PASS (manual) |
| Intentional parallelism | Two inverse maps or symmetric assumptions use matched sentence frames | Retain the parallel form when it makes the mathematical correspondence easier to see | PASS (manual) |
| Precision fallback | Repeated wording carries a stable property or technical term and no equally precise alternative is available | Keep the wording or group the statements; do not introduce a vague substitute solely for variety | PASS (manual) |

Repeat these checks whenever the revision workflow or equation-discourse rules
change. A successful revision must detect the local frame repetition, explain
whether it is functional, and preserve the mathematical behavior and claim
strength of every changed sentence.

## Readiness decision

The core passes the current forward-test gate for definitions, derivations,
proof claims, optimization, and computation. This is a targeted functional
check, not evidence that every mathematical subfield or house style has been
exhausted. Repeat the evaluation when the taxonomy, core patterns, or writing
workflow changes materially.

On 2026-07-21, 16 further observations were checked against five existing
anchors and added without changing any recommended construction, boundary, or
workflow rule. The added evidence completed independent, cross-disciplinary
support for the nine previously provisional patterns and introduced explicit
coverage of piecewise displays, an additional `where`-clause role, and a proof
calculation step. Structural validation and the existing validator unit tests
were rerun; this evidence update is not counted as a new independent-agent
forward test.
