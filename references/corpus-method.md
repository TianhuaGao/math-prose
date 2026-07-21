# Corpus Construction and Synthesis

## Contents

- [Purpose](#purpose)
- [Three record levels](#three-record-levels)
- [Annotation axes](#annotation-axes)
- [Influence gate](#influence-gate)
- [Sampling strategy](#sampling-strategy)
- [Extraction unit](#extraction-unit)
- [Pattern synthesis](#pattern-synthesis)
- [Copyright and provenance](#copyright-and-provenance)
- [Quality states](#quality-states)
- [JSONL fields](#jsonl-fields)

## Purpose

Build a corpus that teaches agents to choose language from mathematical meaning.
Do not optimize for rare vocabulary or imitate a single author. Famous papers
are useful anchors, but fame does not guarantee clear, modern, or transferable
prose.

## Influence gate

Use influential, field-recognized works as the anchor corpus. An anchor source
must satisfy at least one stable criterion:

- it establishes a landmark theorem, model, or method that shaped later work;
- it received an official test-of-time or comparable scholarly award;
- it is a canonical survey, guide, or reference published by a leading venue;
- its method became standard practice in an authoritative research software or
  technical community.

For every anchor, record a concise `influence_basis` and an authoritative
`influence_source`. Prefer official award pages, publisher pages, author or
institutional publication records, and authoritative technical documentation.
Do not use a volatile citation count as the sole admission criterion. Citation
counts may support an audit when dated and sourced, but they do not replace a
stable account of the paper's field-level role.

Influence is an admission gate, not a style endorsement. Annotate only local
equation-prose events that are mathematically sound, intelligible in context,
and transferable without copying an author's idiosyncrasies. Use
`source_role: comparison` for a non-anchor source retained only to analyze a
boundary, counterexample, or historical contrast.

## Three record levels

Keep three types of record in one JSONL file or in three validated JSONL files.

### Source

Record one paper or book with stable bibliographic metadata, field, venue,
access route, and reuse status. A source record answers *where the evidence came
from*.

### Observation

Record one local equation-prose event. Annotate the mathematical behavior,
formula form, discourse position, section role, cue phrase, conditions, and a
paraphrased summary. An observation answers *what the author did in this local
context*.

### Pattern

Synthesize a reusable recommendation across observations. Record recommended
constructions, boundaries, counterexamples, a synthetic example, contributing
sources, and validation state. A pattern answers *what another writer may safely
reuse*.

Never promote a memorable sentence from one paper directly into a universal
rule.

## Annotation axes

Annotate each observation on independent axes.

### Primary mathematical behavior

Use one code from `behavior-taxonomy.md`, such as `A1` for naming, `B2` for
construction, `C2` for equivalent rewriting, `D2` for logical inference, or
`E3` for an update law.

### Discourse position

Use one of:

- `before-display`
- `display-lead`
- `where-clause`
- `after-display`
- `derivation-step`
- `result-statement`
- `proof-step`
- `paragraph-transition`

### Formula form

Use one of:

- `symbol-or-notation`
- `definition`
- `equality-or-identity`
- `membership-or-signature`
- `mapping-or-transform`
- `differential-equation`
- `recurrence-or-update`
- `optimization`
- `inequality-or-bound`
- `limit-or-asymptotic`
- `integral-or-sum`
- `piecewise-or-cases`
- `probability-or-expectation`
- `theorem-or-proposition`
- `algorithmic-relation`

### Claim strength

Use one of:

- `descriptive`
- `definitional`
- `exact-algebraic`
- `approximate`
- `one-way-consequence`
- `equivalence`
- `proved-result`
- `empirical-observation`

### Section role

Use one of:

- `notation-or-preliminaries`
- `problem-formulation`
- `method-or-model`
- `derivation-or-analysis`
- `theorem-or-proof`
- `algorithm`
- `experiment-or-results`
- `discussion-or-limitations`
- `appendix`

### Discipline

Use a broad top-level label and an optional subfield:

- `pure-mathematics`
- `applied-mathematics`
- `probability-statistics`
- `optimization-machine-learning`
- `control-robotics`
- `physics-engineering`

## Sampling strategy

Build a stratified corpus of influential anchors rather than a popularity list.

1. Run a 6--8 source pilot across the six top-level disciplines to test the
   schema, annotation boundaries, and validator before scaling collection.
2. Expand to 24--36 anchor sources across at least four disciplines only after
   the pilot records can be annotated consistently.
3. Include multiple author groups, venues, decades, and section roles.
4. Admit anchor papers through the influence gate, then sample local passages
   for expository quality and behavioral coverage.
5. Prefer author-owned manuscripts, open-access versions, preprints, and sources
   with clear reuse terms for any stored text.
6. Oversample underrepresented behaviors rather than collecting more instances
   of easy notation definitions.
7. Keep theorem/proof prose separate from applied equation exposition during
   analysis, then identify patterns that genuinely transfer.

For a stable public pattern, target at least three independent sources and two
author groups. For a domain-general recommendation, seek evidence from at least
two disciplines. Treat these as review thresholds, not statistical proof.

## Extraction unit

Use an equation-centered event rather than an isolated sentence:

- one relevant formula or theorem statement;
- up to two preceding sentences;
- the local `where` or definition sentence;
- up to two following interpretation or inference sentences;
- section role and exact locator;
- the annotator's paraphrase of the mathematical action.

Keep full extraction units private unless their license permits redistribution.
The public corpus should normally retain metadata, brief conventional cue
phrases, structural annotations, and synthesized examples.

## Pattern synthesis

Summarize observations into a behavior card with:

1. behavior code and mathematical intent;
2. canonical grammatical frames;
3. typical equation position;
4. required preconditions;
5. claim-strength ceiling;
6. common misuses and near-synonym distinctions;
7. domain-specific variants;
8. a synthetic example whose mathematics is self-contained;
9. contributing source identifiers;
10. status: `seed`, `provisional`, or `validated`.

Report coverage counts by behavior, discipline, and section role. Do not rank a
construction only by frequency. A frequent phrase may be vague, field-specific,
or tied to one journal's style.

## Copyright and provenance

- Store full papers outside the public Skill repository unless redistribution
  is explicitly permitted.
- Prefer paraphrased observations and synthetic examples.
- Keep any verbatim quotation short, attributed, and necessary. Record its word
  count and reuse basis.
- Record DOI, stable URL, version, section, page or equation locator, access
  route, and license when known.
- Do not infer an open license merely because a PDF is freely accessible.
- Separate source-attested wording from the Skill's recommended wording.

## Quality states

- `seed`: expert-proposed behavior or construction not yet corpus-supported.
- `provisional`: supported by one or two independent anchor sources or still
  narrow in discipline and context.
- `validated`: supported by at least three independent anchor sources,
  reviewed for mathematical meaning, and checked against counterexamples.
  Domain-general patterns should also span at least two disciplines.

Validation means the annotation and synthesis passed review. It does not mean
the phrase is mandatory or universally optimal.

## JSONL fields

Use `scripts/validate_corpus.py` to check the following records.

### Source record

Required fields:

```json
{"id":"src-example","record_type":"source","source_role":"anchor","title":"...","year":2026,"discipline":"applied-mathematics","citation":"...","access":"open-access","influence_basis":"Canonical field reference for ...","influence_source":"https://..."}
```

Recommended optional fields include `authors`, `venue`, `doi`, `url`,
`version`, `license`, and `notes`.

`source_role` is either `anchor` or `comparison`. Anchor records must include
non-empty `influence_basis` and `influence_source` fields. Comparison records
may include them, but they are not treated as evidence that a pattern has been
tested against influential literature.

### Observation record

Required fields:

```json
{"id":"obs-example","record_type":"observation","source_id":"src-example","behavior":"C1","discourse_position":"derivation-step","formula_form":"equality-or-identity","claim_strength":"exact-algebraic","section_role":"derivation-or-analysis","locator":"Sec. 3, Eq. (7)","cue":"substituting ... gives","summary":"A paraphrase of the mathematical action.","quote_words":0}
```

Use optional `quote` only when redistribution is justified. The validator limits
it to 25 words but cannot decide whether reuse is legally permitted.

### Pattern record

Required fields:

```json
{"id":"pat-example","record_type":"pattern","behavior":"C1","intent":"Introduce the result of a valid substitution.","constructions":["substituting ... into ... gives"],"boundaries":["Name the substituted relation and preserve its conditions."],"synthetic_example":"Substituting the feedback law into the dynamics gives the closed-loop system.","source_ids":["src-example"],"status":"provisional"}
```
