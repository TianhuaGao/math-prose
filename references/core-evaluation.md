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

## Readiness decision

The core passes the current forward-test gate for definitions, derivations,
proof claims, optimization, and computation. This is a targeted functional
check, not evidence that every mathematical subfield or house style has been
exhausted. Repeat the evaluation when the taxonomy, core patterns, or writing
workflow changes materially.
