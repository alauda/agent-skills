# AI-Usable Documentation Rules

Use this rule file when the task involves documentation quality for AI writing, AI review, retrieval, or assistant answering. The goal is not to optimize for generic prose quality alone. The goal is to make the documentation self-contained enough that an assistant can answer correctly without guessing.

## 1. Classify The Documentation Layer First

Before planning or drafting, classify the target into one of these layers:

- `user-facing product doc`
- `engineering fact doc`
- `versioned validation report`
- `known issue tracker`
- `evidence index`

Do not silently mix layers.

### Layer Guidance

| Layer | Primary audience | What belongs here | What does not belong here |
| :--- | :--- | :--- | :--- |
| `user-facing product doc` | Operators and product users | Stable workflows, prerequisites, field meanings, source of values, supported boundaries | Raw test bookkeeping, evidence IDs, long log excerpts |
| `engineering fact doc` | Engineers and maintainers | Delivered capability, ownership boundaries, current gaps, implementation caveats | End-user tutorial prose that implies product support without evidence |
| `versioned validation report` | Reviewers and release stakeholders | Baseline-bound conclusions, pass or partial status, scope, follow-up order | Unbounded statements detached from a version or commit |
| `known issue tracker` | Engineers and support | Symptom, impact, scope, current guidance, fix direction | Marketing language or "already solved" phrasing when not solved |
| `evidence index` | Reviewers and auditors | Evidence identifiers, external locations, mapping to test cases or issues | Raw long logs copied into the main repository without need |

## 2. AI-Usable User-Facing Docs

When drafting or reviewing `user-facing product doc` content, ensure the page can answer the following questions without guessing:

1. What must be prepared before the user starts?
2. Where does each critical value come from?
3. Which values are display names and which are provider-recognized API values?
4. Which fields are controller-managed and should not be written manually?
5. Which combinations are allowed, disallowed, deprecated, or create-only?
6. Which workflows are supported, unsupported, or out of scope for the current page?

### Preferred Content Shapes

Use these shapes when they improve task success:

- prerequisite checklist
- value-to-field mapping
- source tables for credentials, IDs, and platform values
- boundary notes such as create-only, upgrade-not-supported, or admin-required values
- sibling-page links when one page cannot safely carry the whole workflow

## 3. Source-Of-Value Rule

For critical fields, explain the source of truth, not only the field meaning.

Examples of useful distinctions:

- UI display name vs provider API value
- tenant-accessible value vs admin-only value
- user-supplied field vs controller-populated field
- optional display convenience vs required operational prerequisite

If the page cannot hold all sourcing detail safely, link to the authoritative prerequisite or infrastructure page.

## 4. Support-Boundary Rule

Do not collapse these states into one vague statement:

- `implemented`
- `documented workflow`
- `formally validated`
- `known issue`
- `out of current scope`

For `engineering fact doc` and `versioned validation report`, be explicit about which state applies.
For `user-facing product doc`, document only the workflow the user should actually rely on, plus the boundaries that materially affect success.

## 5. Constraint Propagation Rule

If a change introduces or revises any of the following:

- prerequisite input
- field constraint
- lifecycle boundary
- known limitation
- troubleshooting interpretation

then inspect sibling workflows and overview pages for propagation needs.

Typical propagation targets:

- create
- manage nodes
- upgrade
- infrastructure preparation
- troubleshooting
- index or overview pages

If the current scope cannot update all affected pages, record explicit debt. Do not silently localize a cross-workflow rule to one page.

## 6. Versioned Engineering Truth

For `engineering fact doc` and `versioned validation report`, version-sensitive conclusions must be bound to a baseline.

Minimum baseline fields:

- `Baseline ref`
- `Baseline commit SHA`
- `Validation date`
- `Promotion status`

Use baseline-bound wording such as:

- "validated on `v1.0.0@04125bb`"
- "not part of the formally validated workflow"
- "known issue for the current baseline"

Avoid timeless claims when the evidence is version-specific.

## 7. Review Lens For AI Usability

When doing an AI-usability review, check these questions explicitly:

1. Can an assistant identify the authoritative page for this question?
2. Can it find prerequisite inputs without stitching together multiple scattered hints?
3. Can it answer where to obtain each critical value?
4. Can it tell which workflow boundaries apply?
5. Can it distinguish stable guidance from issue-specific or baseline-specific engineering truth?
6. If one page was updated, were sibling pages updated where needed?

If the answer is no, report it as an AI-usability finding even when the Markdown and Doom syntax are otherwise correct.
