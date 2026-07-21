# Equation and Paragraph Discourse

Use equation placement to control emphasis and reduce mechanical definition
sequences. Each display should have a reason to appear and a clear connection to
the surrounding argument.

## Before a display

Use the lead sentence to do one of four jobs:

- state the object being introduced;
- state the operation being performed;
- state the result being claimed;
- state the question the equation answers.

Avoid an empty lead such as `The equation is as follows.` Prefer a semantic
lead:

> Projecting the unconstrained vector onto the feasible set gives

> The closed-loop error evolves according to

> Define the energy functional by

## After a display

Do not merely translate every symbol back into words. Use the next sentence to:

- define nonstandard symbols or spaces;
- interpret the mathematical role;
- identify a condition or singular case;
- connect the result to the next operation;
- explain why the equation matters to the argument.

## Common architectures

### Local definition

> Let $x\in\mathcal X$ denote the state. Define the functional
> \[
> V(x):=\cdots .
> \]
> Here, ... .

Use `denote` for the name and `define` for the functional. Do not merge the two
actions if that obscures the type or scope.

### Explicit formula for an existing object

> The coefficient is given by
> \[
> c=\cdots,
> \]
> where ... .

Use this pattern when the coefficient has already been introduced by role.

### Grouped definitions

Group objects when they share scope and their correspondence is unambiguous:

> Define the position and velocity errors, respectively, by
> \[
> e_x=\cdots,\qquad e_v=\cdots .
> \]

Do not use `respectively` across a long sentence, mixed types, or a nonparallel
list.

### Derivation chain

Use connective phrases to identify the actual operation:

> Substituting (3) into (5) and collecting like terms yields
> \[
> \cdots .
> \]
> Applying the bound in Lemma 1 then gives ... .

Avoid repeating `we have` between every aligned equation. An aligned display may
carry algebraic continuity, while prose marks only the non-obvious operation or
logical transition.

### Mapping or transformation

State direction before consequences:

> Let $T:\mathcal X\to\mathcal Y$ map the original coordinates to the reduced
> state. Applying $T$ to the dynamics gives ... .

For frames and coordinate transforms, state what the map acts on and in which
direction. A matrix label alone is insufficient when conventions differ.

### Dynamical system

Separate the governing law, initial condition, and interpretation:

> The state evolves according to
> \[
> \dot x=f(x,u),\qquad x(0)=x_0.
> \]
> The first relation specifies the vector field, while the second fixes the
> initial state.

Do not write `is initialized as` when the code or model actually initializes
from a measured state, a distribution, or a previous iterate.

### Optimization problem

Identify all mathematical roles:

> Given the data $D$, estimate $\theta$ by solving
> \[
> \min_{\theta\in\Theta} J(\theta;D)
> \quad\text{subject to}\quad g(\theta)\le 0.
> \]

Distinguish the decision variable, admissible set, objective, data, and
constraints. `The optimal parameter is given by` is too strong unless a
solution exists and the displayed expression actually characterizes it.

### Piecewise or case definition

State whether the cases define an object or report a consequence. Verify that
the cases cover the intended domain and clarify boundary overlap.

### Equation followed by interpretation

Use a strength-matched interpretation:

- an identity `shows` an exact relation;
- an inequality `bounds` a quantity;
- an approximation `suggests` behavior only in its regime;
- a simulation `indicates` an observed trend;
- a theorem `establishes` its stated conclusion under its hypotheses.

## Paragraph rhythm

A mathematical paragraph often follows this sequence:

1. purpose or available data;
2. formal object or operation;
3. displayed relation;
4. symbol and condition clarification;
5. consequence or interpretation;
6. connection to the next step.

Not every paragraph needs all six moves. Preserve the logical order even when
compressing for a venue limit.

## Anti-patterns

- orphaned displays with no stated role;
- a `where` sentence that defines only physical meaning but omits type or space;
- repeated `is` sentences that actually mix naming, construction, inference,
  and interpretation;
- `equivalently` between one-way implications;
- an after-equation sentence that overclaims what the equation proves;
- several single-sentence paragraphs created only to vary sentence openings;
- decorative `thus`, `therefore`, or `hence` without a logical dependency.
