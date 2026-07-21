# Math Prose

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Precise, natural mathematical writing for AI agents—without changing the
mathematics.**

Math Prose is an open Agent Skill for drafting, revising, and auditing English
mathematical prose. It helps an AI agent choose language from the mathematical
action being performed, instead of rotating through a list of synonyms.

Use it for research papers, theses, technical reports, theorem statements,
proofs, derivations, notation blocks, optimization problems, dynamical systems,
and prose around displayed equations.

Math Prose follows the open
[Agent Skills specification](https://agentskills.io/specification). Any
skills-compatible agent can load its `SKILL.md`; agents without native skill
support can use the same workflow by reading that file directly.

## Why Math Prose?

Many mathematical sentences contain *is*, but they do not all perform the same
action. A sentence may assign notation, introduce a definition, provide an
explicit formula, report a calculation, state an assumption, or draw a logical
consequence. Those distinctions determine the appropriate wording.

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

The goal is not to eliminate *is*. Plain forms such as *is* and *are* remain
the clearest choice for identity, membership, status, and many mathematical
properties.

### It also avoids mechanical variation

A synonym-only edit can replace one repeated frame with another:

```text
The measured state collects these quantities in the ordered tuple X=(...).
The desired state collects these quantities in the ordered tuple X_d=(...).
```

When the surrounding mathematics supports distinct roles, Math Prose can vary
the information structure instead:

```text
The measured variables form the state tuple X=(...).
Define the desired reference by X_d=(...).
```

If the two objects are genuinely parallel, the skill retains the parallel
wording. It never trades mathematical precision for surface-level variety.

## Quick Start

### 1. Install the skill

For a project-level installation using the cross-client `.agents/skills`
convention:

```bash
mkdir -p .agents/skills
git clone https://github.com/TianhuaGao/math-prose.git \
  .agents/skills/math-prose
```

For a user-level installation:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/TianhuaGao/math-prose.git \
  ~/.agents/skills/math-prose
```

Skill discovery paths and invocation syntax vary by agent client. If your
client uses a different skill directory or provides its own installer, use the
client's documented installation method.

If your agent has no native skill support, clone the repository anywhere the
agent can read it, then ask the agent to open `math-prose/SKILL.md` and resolve
its linked resources relative to the repository root.

### 2. Ask the agent to use Math Prose

```text
Use the math-prose skill to revise this paragraph while preserving every
equation, symbol, assumption, number, and citation.
```

A skills-compatible agent may also select Math Prose automatically when the
request matches the skill description.

### 3. Provide the mathematical contract

For the most reliable result, include:

- the formulas and current prose;
- notation, numbers, and citations that must remain unchanged;
- known assumptions and the intended claim strength;
- the desired mode: draft, revise, or audit only;
- venue, terminology, or style constraints.

## What Can I Ask It to Do?

### Draft from mathematics

```text
Write the prose around these equations. Introduce the given data, define the
decision variables, state the optimization problem, and interpret the solution
without adding convexity, feasibility, or uniqueness claims.
```

### Revise existing prose

```text
Revise this notation block. Reduce repeated sentence frames, but preserve all
formulas and keep deliberate parallelism where the objects play parallel roles.
```

### Audit without rewriting

```text
Audit this theorem statement and proof for undefined notation, false
equivalence, unclear antecedents, and unsupported inference language. Report
the issues without rewriting the text.
```

### Check logical force

```text
Check whether “deduce,” “therefore,” “equivalently,” and “guarantees” are
justified by the visible derivation. Do not strengthen any claim.
```

## What It Protects

By default, Math Prose preserves:

- formulas, symbols, operators, indices, signs, and quantifiers;
- assumptions, domains, codomains, admissible sets, and edge conditions;
- approximation order, implication direction, and equivalence;
- numbers, units, citations, and stated claim strength;
- stable technical terminology required by the field.

It does not silently repair ambiguous mathematics, invent missing hypotheses,
fabricate a derivation or proof, or claim that numerical evidence establishes a
theorem. When the source relation is ambiguous, the skill keeps that ambiguity
visible and reports the possible interpretations.

## How It Works

For each equation-adjacent sentence, the skill:

1. records the mathematical content that must remain unchanged;
2. classifies the sentence's mathematical behavior;
3. identifies its position before, within, or after the displayed equation;
4. selects a construction licensed by that behavior;
5. checks the logical strength of inference and result language;
6. revises sentence structure before considering vocabulary changes;
7. compares nearby sentence frames and runs a preservation audit.

The behavior taxonomy contains 31 cases in six groups:

| Group | Coverage |
|---|---|
| A. Declaration and scope | variables, notation, definitions, types, assumptions, indexing |
| B. Representation and construction | mappings, formulas, decompositions, parameterizations, aggregation |
| C. Transformation and equivalence | substitution, rewriting, simplification, approximation, normalization |
| D. Inference and results | implication, derivation, bounds, existence, uniqueness, optimality, convergence |
| E. Dynamics and computation | differential equations, recurrences, algorithms, initialization, updates |
| F. Interpretation and comparison | meaning, measurement, encoding, contrast, limiting behavior |

See the full
[behavior taxonomy](references/behavior-taxonomy.md),
[equation-discourse guide](references/equation-discourse.md), and
[proof and claim-language guide](references/proof-and-claim-language.md).

## Evidence Base

The core corpus currently contains:

- **32 influential anchors**: 24 research articles and 8 classic or
  established textbooks;
- **112 localized, paraphrased prose observations**;
- coverage of **all 31 mathematical behavior codes**;
- **31 synthesized patterns**, each supported by at least three independent
  anchors and at least two core disciplines;
- 8 anchors in each of pure mathematics, applied mathematics, probability and
  statistics, and optimization and numerical analysis.

Research articles provide evidence for publication-state compression, while
textbooks provide fuller evidence for definitions, constructions, derivations,
and proofs. Sources act as evidence anchors, not as authors to imitate.

The public corpus stores bibliographic metadata, precise locators, behavior
annotations, cue phrases, and paraphrased observations. It contains no paper or
textbook full text and currently stores no verbatim source quotations.

Explore the
[core corpus](references/corpora/math-core.jsonl) and the
[corpus construction method](references/corpus-method.md).

## Repository Structure

```text
math-prose/
├── SKILL.md                         # Agent workflow and trigger description
├── agents/openai.yaml               # Optional client UI metadata
├── references/
│   ├── behavior-taxonomy.md         # The 31 mathematical behaviors
│   ├── equation-discourse.md        # Equation and paragraph structures
│   ├── proof-and-claim-language.md  # Logical-force safeguards
│   ├── corpus-method.md             # Evidence and annotation protocol
│   ├── core-evaluation.md           # Forward-test record
│   └── corpora/math-core.jsonl      # Core evidence registry
├── scripts/validate_corpus.py       # Corpus and readiness validator
└── tests/test_validate_corpus.py    # Validator tests
```

The runtime entry point stays concise. Detailed guidance and corpus data are
loaded only when a task needs them.

## Validation

The validator uses only the Python standard library.

Validate the corpus and its readiness gate:

```bash
python3 scripts/validate_corpus.py --require-core-ready \
  references/corpora/math-core.jsonl
```

Run the test suite:

```bash
python3 -m unittest discover -s tests -v
```

If the Agent Skills reference validator is installed, validate the skill
package with:

```bash
skills-ref validate .
```

The current forward tests cover definitions, mapping direction, proof-claim
strength, asymptotic derivation, optimization roles, state-dependent
initialization, ordered updates, and local repetition. See the
[core evaluation record](references/core-evaluation.md).

## Contributing

Issues and pull requests are welcome. Corpus contributions should keep three
evidence levels separate:

1. a source record with stable bibliographic, access, genre, and influence
   evidence;
2. a localized observation with an auditable locator and paraphrased summary;
3. a synthesized pattern with explicit boundaries and supporting source IDs.

Please do not add full papers, textbook chapters, or long quotations. A pattern
may be marked `validated` only when matching observations support it in at
least three independent anchor sources from the same corpus layer. For a
domain-general core pattern, evidence should span at least two disciplines.

Before submitting a pull request, run the corpus validator and unit tests.

## License

Math Prose is released under the [MIT License](LICENSE).
