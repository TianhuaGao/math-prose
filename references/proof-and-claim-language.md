# Proof and Claim Language

Match linguistic strength to the mathematical support. A polished sentence
cannot repair a missing hypothesis or invalid implication.

## Strength ladder

From weaker description to stronger mathematical commitment:

1. `is consistent with`, `suggests`, `indicates`;
2. `can be obtained`, `calculation gives`, `we derive`;
3. `satisfies`, `implies`, `it follows that`;
4. `establishes`, `shows`, `proves`;
5. `is equivalent to`, `if and only if`, `guarantees`.

These are not interchangeable style variants. Select a level from the actual
evidence and argument.

## Assumptions and scope

- Put assumptions before the result that depends on them.
- Preserve `for all`, `there exists`, `almost surely`, `with probability`,
  `locally`, `uniformly`, and other scope markers.
- Read nested quantifiers from left to right. In
  \(\forall\alpha\,\exists C(\alpha)\,\forall u\,\forall n\), the constant may
  depend on \(\alpha\), but it is uniform in \(u\) and \(n\).
- Distinguish an adopted modeling assumption from a proved property.
- State regularity, nonzero, rank, compactness, convexity, and boundary
  conditions when they license a later operation.

## Common proof moves

| Move | Useful constructions | Requirement |
|---|---|---|
| Fix an arbitrary object | `fix`, `let ... be arbitrary` | Keep its space and scope visible. |
| Invoke a result | `by Lemma 2`, `applying Theorem 1` | Check that every hypothesis is satisfied. |
| Construct a witness | `choose`, `construct`, `set` | Explain why the witness is admissible. |
| Transform an expression | `substituting`, `rearranging`, `integrating`, `taking norms` | Preserve equality or inequality direction and side conditions. |
| Establish a bound | `using ... gives`, `is bounded by`, `applying ... yields` | State the norm, constants, and dependence. |
| Split cases | `consider`, `distinguish`, `if ... whereas ...` | Cover the whole domain without overlap ambiguity. |
| Contradiction | `suppose for contradiction`, `contradicting ...` | Identify the contradicted statement. |
| Conclude | `therefore`, `hence`, `which proves` | The conclusion must match the stated claim exactly. |

Expose the full architecture when it carries mathematical information:

- induction states the base case, fixes an arbitrary index, invokes the
  induction hypothesis, and proves the successor case;
- an `if and only if` proof gives both implications;
- a case proof covers the full domain without ambiguous overlap;
- contradiction names the assumed negation and the incompatible conclusions.

## Deduce, derive, obtain, and show

- Use `derive` when a sequence of mathematical operations produces a formula.
- Use `obtain` for a neutral result of calculation or construction.
- Use `deduce` when premises entail a conclusion. It is stronger than a local
  algebraic transition.
- Use `show` when the surrounding argument establishes a stated property or
  result. Do not use it for a plot that merely illustrates a trend.

## Equivalence and implication

- `A implies B` is directional.
- `A is equivalent to B` requires both directions on the stated domain.
- `A reduces to B` describes a restriction, limit, or parameter choice and is
  not automatically equivalence.
- `A can be written as B` normally asserts equality of representations. State
  approximation explicitly when equality does not hold.

## Existence and uniqueness

Separate these claims unless one theorem establishes both. A constructed
solution establishes existence only after admissibility is checked. A numerical
solver returning one output does not establish mathematical uniqueness.
Likewise, an infimum need not be attained, a stationary point need not be a
minimizer, and a displayed `argmin` may be empty or set-valued. State the
convexity and constraint qualifications that turn KKT conditions into necessary
or sufficient optimality claims.

## Bounds, convergence, and stability

Always preserve:

- the norm or metric;
- local versus global scope;
- deterministic, probabilistic, or almost-sure meaning;
- asymptotic, exponential, finite-time, or practical convergence;
- dependence of constants on parameters or initial data;
- invariant set, residual set, or limiting value;
- strict versus non-strict inequalities.

Use `converges` only when the limiting statement is supported. Use `remains
bounded` for boundedness and `approaches a neighborhood` for practical or
residual convergence.

Keep probability modes explicit:

- convergence in distribution does not generally imply convergence in
  probability;
- convergence in probability does not by itself imply almost-sure convergence,
  although every subsequence has a further almost-surely convergent
  subsequence;
- a tail bound whose failure probability tends to zero supports a
  high-probability or convergence-in-probability conclusion, not automatically
  an almost-sure one; an argument such as summability plus Borel--Cantelli is
  needed for the latter.

## Mathematical and empirical evidence

Keep evidence modes distinct:

- a proof establishes a formal claim under assumptions;
- a symbolic or numerical check verifies selected cases;
- a simulation demonstrates behavior in the tested setup;
- an experiment provides observations with measurement and sampling limits;
- a citation transfers only the claim actually supported by the cited source.

Do not use `prove`, `guarantee`, or `establish` for empirical evidence alone.
If an official erratum invalidates a proof step, retain the old step only as
historical or superseded evidence and cite the corrected argument as current.
