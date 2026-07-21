# Math Prose

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Evidence-informed mathematical writing for AI agents.**

Math Prose is an open Agent Skill for drafting, revising, and auditing English
mathematical prose without silently changing the mathematics. It helps an AI
agent choose language from the mathematical action being performed, rather
than from a list of interchangeable synonyms.

Use it for research papers, theses, technical reports, proofs, derivations,
optimization problems, dynamical systems, notation blocks, and prose around
displayed equations.

The repository follows the open
[Agent Skills specification](https://agentskills.io/specification): a portable
`SKILL.md` entry point with supporting references and scripts. Any
skills-compatible agent can load it. An agent without native skill discovery
can still use the same instructions by reading `SKILL.md` and resolving its
linked resources relative to the repository root.

## Why Math Prose?

Mathematical writing often becomes repetitive because many different actions
are expressed with the same verb:

> The matrix is the attitude. The vector is the error. The control moment is
> the output.

Replacing every *is* mechanically does not solve the problem. The writer first
has to determine what each sentence does:

| Mathematical action | Typical construction |
|---|---|
| Assign a symbol | `Let x denote ...` |
| Introduce a definition | `Define r by r(x):=Ax-b.` |
| Supply an existing object's formula | `The coefficient is given by ...` |
| Rewrite an equivalent relation | `Equivalently, ...` or `can be rewritten as ...` |
| Report a calculation | `Substituting ... into ... gives ...` |
| Draw a logical consequence | `It follows from ... that ...` |
| State an assumption | `Given ...`, `Suppose ...`, or `Assume ...` |
| Interpret a quantity | `represents`, `measures`, or `encodes` |

Math Prose makes these distinctions explicit. It also retains plain forms such
as *is* and *are* when they are the clearest way to state identity, membership,
status, or a mathematical property.

## What It Does

- drafts equation-adjacent prose from formulas and author notes;
- revises repetitive or mechanical prose while preserving supplied formulas;
- audits notation, definitions, domains, assumptions, and first use;
- distinguishes `define`, `denote`, `given by`, `express`, `derive`, and
  `deduce` by mathematical function;
- protects implication direction, equivalence, approximation order, and claim
  strength;
- flags unsupported existence, uniqueness, optimality, convergence, or
  stability claims instead of inventing a proof;
- supports definition blocks, derivations, theorem statements, proofs,
  optimization, recurrences, and continuous-time dynamics.

## Quick Example

Input:

```text
x∈X is the decision variable and y is the data. J is the objective and g is the
constraint. The solution is

x* ∈ arg min_{x∈X} J(x;y),  g(x;y) ≤ 0.
```

Possible revision:

```text
Given the data y, estimate the decision variable x∈X by solving

x* ∈ arg min_{x∈X} J(x;y)  subject to  g(x;y)≤0,

where J denotes the objective and g specifies the inequality constraint.
```

The revision clarifies the mathematical roles but does not add convexity,
feasibility, existence, or uniqueness assumptions.

Math Prose also catches overclaims. For example, a Lyapunov inequality stated
only on a neighborhood does not by itself establish global exponential
stability. The skill preserves the local scope and reports the missing
hypotheses.

## Install

### Skills-compatible agents

Install this repository with the skill installer or registry provided by your
agent client. Installation commands and user-level skill directories vary by
client, so consult that client's documentation for the exact location.

If your client scans the common project-level `.agents/skills` directory, add
Math Prose to a project with:

```bash
mkdir -p .agents/skills
git clone https://github.com/TianhuaGao/math-prose.git \
  .agents/skills/math-prose
```

Automatic discovery and invocation depend on the client implementation. The
[Agent Skills integration guide](https://agentskills.io/client-implementation/adding-skills-support)
describes the standard discovery and progressive-loading model.

### Agents without native skill support

Clone the repository anywhere accessible to the agent:

```bash
git clone https://github.com/TianhuaGao/math-prose.git
```

Then instruct the agent to read `math-prose/SKILL.md`, follow its workflow, and
load the referenced files only when the task requires them. This manual route
provides the same writing guidance, although automatic selection and interface
features depend on the host agent.

## Usage

Select or invoke `math-prose` through your agent's skill interface. If the
client has no explicit skill syntax, ask the agent to use the Math Prose skill
or to read its `SKILL.md` before completing the task.

```text
Use the math-prose skill to revise this paragraph while preserving every
equation, symbol, assumption, and citation.
```

```text
Use the math-prose skill to audit the following theorem statement and proof for
unclear definitions, false equivalence, and unsupported inference language.
Do not rewrite it yet.
```

```text
Use the math-prose skill to write the prose around these equations. Introduce
the given data, define the decision variables, state the optimization problem,
and interpret the solution without adding convexity or uniqueness claims.
```

A skills-compatible agent may select the skill automatically when a request
matches its description. Explicit selection is useful when mathematical
preservation is a hard requirement.

For best results, provide:

- the formulas and existing prose;
- notation or equations that must remain unchanged;
- known assumptions and the intended claim strength;
- the desired mode: draft, revise, or audit only;
- any venue, terminology, or style constraints.

## How It Works

Math Prose uses a 31-behavior taxonomy organized into six groups:

1. declaration and scope;
2. representation and construction;
3. transformation and equivalence;
4. inference and results;
5. dynamics and computation;
6. interpretation and comparison.

For each sentence, the skill identifies the mathematical behavior, its
position relative to the equation, and the strength of the claim. It then
selects a construction whose meaning matches that behavior and audits the
result against the supplied mathematics.

The complete taxonomy is available in
[references/behavior-taxonomy.md](references/behavior-taxonomy.md).

## Evidence Base

The core corpus currently contains:

- **24 influential anchor papers**;
- **70 localized prose observations**;
- **all 31 mathematical behavior codes**;
- **31 synthesized patterns**, including 12 validated across at least three
  independent anchors and 19 provisional patterns awaiting broader evidence;
- equal source coverage across pure mathematics, applied mathematics,
  probability and statistics, and optimization and numerical analysis.

The corpus includes source metadata, precise locators, behavior annotations,
cue phrases, and paraphrased observations. It does **not** redistribute paper
full text. Famous papers are used as evidence anchors, not as authors to
imitate.

Explore the evidence in
[references/corpora/math-core.jsonl](references/corpora/math-core.jsonl) and
the construction method in
[references/corpus-method.md](references/corpus-method.md).

## Boundaries

By default, Math Prose:

- preserves supplied formulas, notation, numbers, assumptions, citations, and
  claim strength;
- does not silently repair ambiguous or incorrect mathematics;
- does not treat stylistic variation as permission to change meaning;
- does not claim that a numerical experiment proves a theorem;
- does not imitate one paper or author.

When the source relation is ambiguous, the skill keeps the ambiguity visible
and asks for clarification or reports the possible interpretations.

## Repository Structure

```text
math-prose/
├── SKILL.md                         # Agent workflow and trigger description
├── agents/openai.yaml               # Optional client-specific UI metadata
├── references/
│   ├── behavior-taxonomy.md         # The 31 mathematical behaviors
│   ├── equation-discourse.md        # Equation and paragraph structures
│   ├── proof-and-claim-language.md  # Logical-force safeguards
│   ├── corpus-method.md             # Evidence and annotation protocol
│   ├── core-evaluation.md           # Blind forward-test record
│   └── corpora/math-core.jsonl      # Core evidence registry
├── scripts/validate_corpus.py       # Corpus and readiness validator
└── tests/test_validate_corpus.py    # Validator tests
```

## Validation

Validate the corpus and its readiness gate:

```bash
python3 scripts/validate_corpus.py --require-core-ready \
  references/corpora/math-core.jsonl
```

Run the validator tests:

```bash
python3 -m unittest discover -s tests -v
```

The current forward tests cover definitions, mapping direction, proof-claim
strength, asymptotic derivation, optimization roles, state-dependent
initialization, and ordered updates. See
[references/core-evaluation.md](references/core-evaluation.md).

## Contributing

Issues and pull requests are welcome. Corpus contributions should preserve the
three evidence levels:

1. a source record with stable bibliographic and influence evidence;
2. a localized observation with an auditable locator and paraphrased summary;
3. a synthesized pattern with explicit boundaries and supporting source IDs.

Do not add long quotations or full paper text. A pattern may be marked
`validated` only when matching observations support it in at least three
independent anchor sources from the same corpus layer. Run the corpus validator
and unit tests before submitting a pull request.

## License

Math Prose is released under the [MIT License](LICENSE).
