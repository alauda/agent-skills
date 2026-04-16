---
name: doom-doc-assistant
description: Use when working in a Doom documentation repository to turn requirements into repository-aligned documentation diagnosis, plans, and drafts. Supports modifying authoritative existing pages, adding focused scenario documents, planning doc-tree restructures, read-only convention reviews, and explicitly requested `yarn build` or `yarn translate` tasks. Explicit target repository rules override skill defaults; when the repository is silent, built-in product documentation standards govern new product docs.
---

# Doom Documentation Assistant

## Core Operating Rules

- Never modify files directly without the user's approval. Always produce the diagnosis or plan first, then wait for confirmation.
- Treat explicit target repository rules as authoritative, but do not let legacy samples override the built-in product documentation standards in this skill.
- When explicit repository rules override a built-in product documentation rule, say so explicitly in the output. Use wording like: `Repository rules override the skill defaults here: ...`
- Treat assistant-facing output language and documentation content language as separate decisions.
- Product documentation content must be English. Do not produce Chinese product documentation content with this skill.
- For Doom/Yarn documentation repositories, the default manual-acceptance preparation flow is `yarn up @alauda/doom` and then `yarn install` before handing the task back to a human reviewer.
- Do not automatically run `yarn dev`. Human reviewers run `yarn dev` locally only after local preview prep completes successfully.
- Do not automatically or by default run `yarn build` or `yarn translate`. Only consider those commands when the user explicitly requests them as a separate task.

## Rule Priority

Apply guidance in this order:

1. User task scope and explicit target repository rules
2. Built-in product documentation standards from this skill
3. Real documentation in the target directory and adjacent modules, only for local placement, ordering, and style that does not violate product documentation standards
4. `templates/*`

Never let a lower-priority source overrule a higher-priority source.
Product documentation content language is a non-overridable skill rule: write English content only.

## When To Use

Activate this skill when the user asks for any of the following in a Doom or `@alauda/doom` documentation repository:

- Transform requirements, PRDs, or feature notes into documentation updates
- Modify an existing authoritative page
- Add a new scenario-focused document under an existing section
- Evaluate whether documentation should be restructured, split, or merged
- Check Doom documentation conventions, MDX component usage, or terminology
- Handle an explicit `yarn build` or `yarn translate` request for the same documentation repository without treating those commands as default validation steps

## Workflow

Follow this sequence. Do not skip steps.

### 1. Lock The Assistant-Facing Output Language

1. Determine which language the assistant should use for diagnosis reports, execution plans, questions, and other printed output.
2. If the user already stated a preference, use it.
3. If the current conversation makes the preference obvious, follow that language.
4. If the preference is not explicit, ask the user whether assistant-facing output should be in English or Chinese.
5. Clarify that this choice applies only to the assistant's printed output. Documentation content produced by this skill remains English-only.

Success criterion: the assistant knows whether to print its reports and questions in English or Chinese before starting repository analysis, while keeping documentation content English-only.

### 2. Ground On The Repository

1. Determine the target repository.
   - If the current workspace already looks like the documentation repository, use it.
   - Treat the current workspace as the target repository only when it shows clear documentation-repo signals such as a docs tree with real `.mdx` pages, Doom config files, or existing Doom MDX component usage.
   - Do not treat a generic `AGENTS.md` file by itself as sufficient evidence that the current workspace is the target docs repository.
   - If the current workspace is not clearly the target repo and the user provided a path, use that path.
   - Ask for a path only when there is no clear repository context.
2. Read the target repository `AGENTS.md` before applying any built-in rule when it exists.
3. Explore the relevant directory with `rg`, `ls`, and file reads.
4. Search with multiple keywords from the requirement to avoid keyword traps.
5. Before suggesting placement, `weight` values, optional metadata, or category values, sample 3-5 neighboring pages in the same directory or adjacent module.
6. Before recommending MDX components, search for real examples in the repository.
7. If the user requests Chinese product documentation content or asks to write under `docs/zh`, stop and explain that this skill only drafts English product documentation. Ask for the English target path or English content target.
8. Before assuming standard local preview preparation, check for Doom/Yarn repository signals such as a root `package.json`, Yarn usage, a `dev` script, `doom dev`, or `@alauda/doom`.

Success criterion: you can name the target repository root, the likely authoritative page or section, the local conventions you found, and whether standard Doom/Yarn preview preparation applies.

### 3. Route The Request

Classify the request before planning edits:

- `review/audit only`: The user only asks to inspect, review, audit, lint, or check documentation conventions and does not ask for changes.
- `documentation collaboration`: The user asks to create, modify, restructure, or draft documentation.
- `explicit command task`: The user explicitly asks to run `yarn build` or `yarn translate`.

If the request is `review/audit only`:

1. Keep the workflow read-only.
2. Load only the rules needed for the requested check.
3. Inspect repository examples and the target document.
4. Output a Review Findings Report using the contract in Output Contracts.
5. Do not output an execution plan, modify files, run `yarn up @alauda/doom`, run `yarn install`, or hand off `yarn dev`.
6. Ask whether the user wants a fix plan for the findings.
7. Stop unless the user asks for edits.

If the request includes an `explicit command task`:

1. Treat `yarn build` or `yarn translate` as a separate explicitly requested task.
2. Do not add either command to the default documentation collaboration verification flow.
3. Do not use either command as a substitute when local preview prep fails or is not applicable.
4. If documentation changes are also requested, keep the normal documentation collaboration plan separate from the explicit command task.
5. Before running the explicit command, state the exact command, scope, and expected output or failure handling.

If the request is `documentation collaboration`, continue to Phase 0.

Success criterion: review-only work stops with findings only, explicit command work is separated from default validation, and documentation collaboration continues through the phased workflow.

### 4. Phase 0: Intake And Diagnosis

1. Restate the requirement in repository context.
2. Identify the most relevant existing documents.
3. Assess source material coverage.
4. Decide between these paths:
   - Path A: the current structure is healthy enough to directly modify the authoritative page and/or add a focused new document within the existing structure.
   - Path B: the current structure is wrong enough that restructuring must happen before the new or revised content can be correct.
   - Path C: structural issues exist, but they are not required to solve the current task; record the debt and continue with the narrowest safe scope.
5. Load `templates/diagnosis-report.md` and output the diagnosis with all required sections.
6. Explain all three paths. Do not output only the recommended path.
7. If the recommended path is not the only plausible option, explain why the other paths are not chosen for this round.
8. Ask for confirmation before moving on.

Success criterion: the user can see the requirement, relevant documents, coverage, Path A/B/C definitions, the recommended path, and why other paths were not selected.

### 5. Phase 1: Planning

1. Load `rules/core-conventions.md`.
2. Verify directory integrity, especially the `index.mdx` rule for any directory you will create or touch.
3. Classify the task as one of:
   - `modify existing authoritative doc`
   - `add new scenario doc`
   - `restructure doc tree`
4. Determine whether the repository supports standard Doom/Yarn local preview preparation.
   - Confirm repository signals such as a root `package.json`, Yarn usage, a `dev` script, `doom dev`, or `@alauda/doom`.
   - If the standard preview flow applies, plan `yarn up @alauda/doom` and then `yarn install`.
   - If those commands may change dependency files, include `package.json`, `yarn.lock`, or equivalent dependency files under `Files to Modify`.
   - If the standard preview flow does not apply, say that clearly instead of inventing a substitute validation command.
5. Build the metadata contract from explicit repository rules plus built-in product documentation minimums.
   - Use neighboring pages to determine local `weight` spacing and optional fields only when they do not conflict with explicit repository rules or built-in product documentation standards.
   - Never invent `category` values from template file names.
   - For new English product documentation, require `weight` and English `queries`.
   - Do not require `author` or `category` unless explicit repository rules require them.
   - If modifying an existing page that lacks `queries`, list a follow-up or planned completion item depending on the edit scope.
6. Output the execution plan with the exact sections required by the template below.
7. Use `None` when a section is empty. Do not omit required sections.
8. Ask: `Should I proceed with generating or modifying the documentation based on this plan?`
9. Stop until the user confirms.

Use this contract for the execution plan:

```markdown
## Execution Plan

**Action Type**: [modify existing authoritative doc / add new scenario doc / restructure doc tree]

### Files to Create
| File | Weight | Queries | Purpose |
|------|--------|---------|---------|
| [new lowercase_underscore path or `None`] | [weight] | [2-4 English queries] | [purpose] |

### Files to Modify
| File | Changes | Metadata Handling |
|------|---------|-------------------|
| [existing file, dependency file, or `None`] | [changes] | [preserve / add queries / follow-up / dependency update] |

### Directory Integrity Check Result
[List missing or verified `index.mdx` coverage]

### Local Preview Prep
**Applicability**: [Standard Doom/Yarn prep applies / Not applicable]
**AI Commands Before Manual Acceptance**:
- `yarn up @alauda/doom` / `None`
- `yarn install` / `None`
**Files That May Change**: [package.json / yarn.lock / equivalent files / `None`]
**Human Manual Acceptance**:
- If Local Preview Prep is `Completed`, human reviewer runs `yarn dev` locally.
- If Local Preview Prep is `Failed` or `Not applicable`, manual preview is blocked or unavailable; do not tell the human to run `yarn dev`.
**Default Prohibited Commands**:
- `yarn build`
- `yarn translate`

### Outline per Target Document
[One outline per document that will be created or materially reworked]

### Assumptions
[List assumptions or `None`]

### Acceptance Criteria
[Flat checklist or bullets]
```

Success criterion: the plan makes clear what will be created, what will be modified, whether directory structure is sound, whether manual preview handoff is available, and what a successful outcome looks like.

### 6. Phase 2: Execution

1. If the user chose Path B, perform a specification review on the affected existing documents before restructuring them.
2. Load these rules before drafting:
   - `rules/metadata-rules.md`
   - `rules/language-style.md`
   - `rules/content-elements.md`
   - `rules/markdown-formatting.md`
   - `rules/core-conventions.md`
   - `rules/common-pitfalls.md`
3. Load these only when needed:
   - `rules/mdx-components.md`
   - `rules/terminology-guide.md`
   - `rules/terminology-consistency.md`
   - `rules/best-practices.md`
4. Treat explicit repository rules as authoritative. Treat historical repository samples as evidence only when they do not violate built-in product documentation standards.
5. Use templates only as structural references after sampling real repository pages. Historical samples cannot justify new hyphenated paths, missing required `queries`, missing required `index.mdx`, or Chinese product documentation content.
6. Available structural templates are:
   - `templates/howto-template.mdx`
   - `templates/function-template.mdx`
   - `templates/concept-template.mdx`
   - `templates/arch-template.mdx`
   - `templates/quickstart-template.mdx`
   - `templates/installation-template.mdx`
   - `templates/release-notes-template.mdx`
   - `templates/troubleshooting-template.mdx`
   - `templates/upgrade-template.mdx`
   - `templates/intro-template.mdx`
7. Template file names describe content shapes, not mandatory `category` values.
8. Before using a Doom MDX component, search for a real example in the target repository.
9. If no trusted example exists, prefer plain Markdown or explicitly note the uncertainty.
10. For frontmatter, include `weight` and English `queries` for new product documentation. Include other fields only when confirmed by explicit repository rules.
11. Write all document titles, headings, prose, and examples in English only, even when the assistant-facing output is Chinese.
12. Do not automatically or by default run `yarn build` or `yarn translate` as part of documentation collaboration. Those commands require an explicit separate user request.

Success criterion: the generated or revised documentation follows the approved plan, matches repository conventions, and does not introduce template-driven fake standards.

### 7. Specification Review For Path B

When restructuring existing documents:

1. Load `rules/mdx-components.md`.
2. Count all `:::` directives except `:::details`.
3. Compare the directive density against neighboring pages in the same area of the repository.
4. If the draft materially exceeds the local pattern, or uses directives for routine notes when no clear local pattern exists, streamline them with this priority:
   - DANGER
   - WARNING
   - TIP
   - INFO
   - NOTE
5. Check terminology, links, language, MDX components, and frontmatter against repository-discovered requirements.
6. Load `templates/spec-review-report.md`.
7. Output the review report before making the restructuring change.
8. Wait for confirmation.

Success criterion: the user sees the current directive count, the observed local directive baseline, any compliance issues, the repository-specific frontmatter contract, and the proposed restructuring changes before execution.

### 8. Self-Verification

1. Load `rules/verification-checklist.md`.
2. Run the checks in order.
3. Verify plan consistency before any style or content checks.
4. Confirm that metadata matches the approved contract, including explicit repository overrides and built-in minimum product documentation fields.
5. Confirm that any MDX component usage is backed by real repository examples.
6. If any discrepancy exists, stop and report it instead of silently continuing.

Success criterion: you can explicitly state that the output matches the approved plan, local metadata contract, and repository conventions.

### 9. Local Preview Prep And Manual Acceptance

1. Decide whether standard Doom/Yarn preview preparation applies by checking for a root `package.json`, Yarn usage, a `dev` script, `doom dev`, or `@alauda/doom`.
2. When it applies, run `yarn up @alauda/doom` and then `yarn install`.
3. If either command fails, stop and report the blocking error. Do not tell the human to run `yarn dev`.
4. Do not automatically run `yarn dev`. Manual acceptance belongs to the human reviewer.
5. Do not automatically or by default run `yarn build` or `yarn translate`. Only do so when the user explicitly requested that exact command as a separate task.
6. If standard preview preparation does not apply, report that clearly instead of substituting `yarn build`, `yarn translate`, or another validation command.

Success criterion: the assistant either finishes standard preview preparation and hands `yarn dev` to the human reviewer, or clearly reports why that handoff is blocked or unavailable.

### 10. Explicit Build Or Translate Tasks

Use this section only when the user explicitly requested `yarn build` or `yarn translate`.

1. Confirm the command is an explicit user request, not a default validation step.
2. State the exact command and scope before running it.
3. Run only the requested command.
4. Report the command result with the Explicit Command Result contract in Output Contracts.
5. If the command fails, report the failure and do not claim documentation collaboration passed by default.
6. Do not run `yarn build` or `yarn translate` after a failed or unavailable local preview prep unless the user explicitly requested that exact command anyway and understands it is separate.

Success criterion: explicit build or translate output is clearly separate from the default manual-acceptance flow.

## Output Contracts

### Diagnosis Report

Always include:

- `Requirement`
- `Related Documents Found`
- `Source Material Coverage`
- `All Branching Paths`
- `Recommended Path`
- `Reasoning`
- An explicit confirmation request
- Use the assistant-facing output language selected in Step 1.
- Keep any generated or revised documentation content in English.

### Review Findings Report

For `review/audit only` requests, use this structure and stop after the report unless the user asks for fixes:

```markdown
## Review Findings Report

**Scope**: [documents, directories, or conventions reviewed]
**Repository Evidence Used**: [target AGENTS.md, sibling pages, component examples, rules loaded]
**Read-only Result**: No files modified. No local preview prep commands run.

## Findings

| Severity | Location | Finding | Recommendation |
|----------|----------|---------|----------------|
| P1/P2/P3 | [file or section] | [issue] | [actionable recommendation] |

## Non-Issues Or Confirmed Good Patterns

[List relevant passing checks or `None`]

## Suggested Next Step

[Ask whether the user wants a fix plan or implementation.]
```

### Explicit Command Result

For explicitly requested `yarn build` or `yarn translate` tasks, use this structure:

```markdown
## Explicit Command Result

**Requested Command**: [`yarn build` / `yarn translate ...`]
**Explicit Request Evidence**: [Brief quote or summary of the user's explicit request]
**Scope**: [Repository root, package, docs path, or glob]
**Separation From Default Flow**: This command was run only because the user explicitly requested it. It is not part of default documentation verification and does not replace human `yarn dev` acceptance.

## Command Outcome

**Status**: [Succeeded / Failed / Not run]
**Output Summary**: [Short summary of relevant command output]
**Failure Handling**: [Blocking error and next step, or `None`]
```

### Documentation Summary

After generating or revising documentation, use this structure:

```markdown
## Documentation Summary

**Action Type**: [modify existing authoritative doc / add new scenario doc / restructure doc tree]
**Execution Path**: [A / B / C]
**Evidence Used**: [Short summary]
**Repository Overrides**: [Any skill defaults that were overridden, or `None`]

## Generated Or Revised Content

[Draft, diff summary, or content]

## Local Preview Prep

**Status**: [Completed / Failed / Not applicable]
**AI Commands Run**:
- `yarn up @alauda/doom` / `None`
- `yarn install` / `None`
**Files Changed Or Potentially Changed**: [package.json / yarn.lock / equivalent files / `None`]
**Default Prohibited Commands Not Run**:
- `yarn build`
- `yarn translate`

## Manual Acceptance Handoff

- If Local Preview Prep status is `Completed`, human reviewer must run `yarn dev` locally.
- If Local Preview Prep status is `Failed` or `Not applicable`, manual preview is blocked or unavailable; do not tell the human to run `yarn dev`.
- The assistant does not run `yarn dev` automatically.
- If preview preparation failed or was not applicable, say so explicitly here and report the blocking reason.

## Verification Results

- [x] Plan consistency check
- [x] Repository metadata contract check
- [x] Structure and link check
- [x] Language and formatting check

## Technical Debt Or Follow-ups

[Optional]
```

## Default Principles

- Ask for the assistant-facing output language when it is not explicit
- Product documentation content is English-only for repository collaboration with this skill
- CLI-first procedures unless the repository or requirement clearly favors UI-first guidance
- For Doom/Yarn repos, prepare local preview with `yarn up @alauda/doom` and then `yarn install` before manual acceptance
- Human reviewers run `yarn dev` locally only after local preview prep completes successfully
- `yarn build` and `yarn translate` are never default validation commands
- No invented terminology
- No invented frontmatter fields
- No invented component syntax
