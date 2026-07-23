# Control-Systems Overlay Evaluation

Date: 2026-07-23

Two fresh writing tasks tested the new domain patterns without model answers.
A different reviewer audited the exact outputs against the supplied control
contracts. Both cases passed. These are scoped behavioral tests, not a general
verification of control theory or every control subfield.

## CF5-CTRL-1 — Qualified control implications — PASS

Prompt:

```text
For a stated control-affine system, a safe set C is defined by a control
barrier function h, and a locally Lipschitz feedback k satisfies the supplied
pointwise CBF inequality. Conclude only forward invariance; do not infer
convergence, optimality, or performance.

An MPC theorem assumes Assumptions 2.2, 2.3, 2.17, and 2.23 together with IOSS,
and concludes asymptotic stability of the origin only on the feasible set X_N.
Preserve every hypothesis and do not say global stability.

A hybrid Lyapunov theorem supplies sufficient flow-and-jump decrease conditions
for pre-asymptotic stability, but solution completeness is not supplied. Do
not upgrade the conclusion to asymptotic stability.
```

Observed output:

> For the stated control-affine system, let \(C\) denote the safe set defined
> by the control barrier function \(h\). If the locally Lipschitz feedback
> \(k\) satisfies the supplied pointwise CBF inequality, then \(C\) is forward
> invariant. Under Assumptions 2.2, 2.3, 2.17, and 2.23 together with IOSS, the
> MPC theorem establishes asymptotic stability of the origin on the feasible
> set \(X_N\). Finally, the stated flow and jump decrease conditions are
> sufficient for pre-asymptotic stability of the hybrid system. Since
> completeness of solutions is not supplied, no asymptotic-stability
> conclusion follows from this hybrid result.

Self-audit:

> The CBF statement retains the stated system, \(C\), \(h\), local Lipschitz
> continuity of \(k\), and the pointwise inequality, and concludes only forward
> invariance. The MPC statement retains all four numbered assumptions and IOSS
> and restricts asymptotic stability to \(X_N\). The hybrid statement retains
> both flow and jump conditions and their sufficiency, but only for
> pre-asymptotic stability. No convergence, optimality, performance, global
> stability, or stronger hybrid-stability claim was introduced.

Independent audit: **PASS**. No defect was found.

## CF5-CTRL-2 — Guarantee qualification — PASS

Prompt:

```text
Under Assumptions A, a finite-horizon MPC minimizer exists for each feasible
initial state, but it may be nonunique, so the optimizer and feedback law may
be set-valued. Finite-horizon optimality alone does not ensure closed-loop
stability. A nominal terminal-set shift argument gives recursive feasibility
under the nominal model, but additive disturbances, model mismatch, or
state-estimation error can destroy it. A higher-relative-degree barrier
construction is stated only for unconstrained input. Keep these scopes separate
and make no robustness or uniqueness claim.
```

Observed output:

> Under Assumptions A, a finite-horizon MPC minimizer exists for every feasible
> initial state. The minimizer need not be unique, so both the optimizer and
> the induced feedback law may be set-valued. Finite-horizon optimality alone
> does not establish closed-loop stability. Separately, the nominal
> terminal-set shift argument establishes recursive feasibility only under the
> nominal model, and additive disturbances, model mismatch, or
> state-estimation error may invalidate this conclusion. The stated
> higher-relative-degree barrier construction applies only when the input is
> unconstrained.

Self-audit:

> Existence is conditional on Assumptions A and initial-state feasibility.
> Nonuniqueness and possible set-valuedness are preserved. No closed-loop
> stability is inferred from finite-horizon optimality. Recursive feasibility
> remains nominal-only, with all three listed failure sources retained and no
> robustness claim. The barrier construction is not extended to constrained
> inputs.

Independent audit: **PASS**. No defect was found.
