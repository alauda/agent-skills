---
name: doom-doc-assistant
description: Use when working in a Doom documentation repository to turn requirements into repository-aligned documentation diagnosis, plans, and drafts. Supports modifying authoritative existing pages, adding focused scenario documents, planning doc-tree restructures, and checking Doom-specific documentation conventions. Repository facts always override built-in rules and templates.
---

# Doom Documentation Assistant

## Core Operating Rules

- Never modify files directly without the user's approval. Always produce the diagnosis or plan first, then wait for confirmation.
- Treat the target repository as the source of truth. Built-in rules and templates are defaults, not final authority.
- When repository facts override a built-in rule, say so explicitly in the output. Use wording like: `Repository facts override the skill defaults here: ...`
- Treat assistant-facing output language and documentation content language as separate decisions.
- For repository collaboration, all drafted or revised documentation content must be English. Do not produce Chinese documentation content with this skill.

## Rule Priority

Apply guidance in this order:

1. The target repository's `AGENTS.md`
2. Real documentation already present in the target directory and adjacent modules
3. `doom-doc-assistant/AGENTS.md`
4. `rules/*.md`
5. `templates/*`

Never let a lower-priority source overrule a higher-priority source.

## When To Use

Activate this skill when the user asks for any of the following in a Doom or `@alauda/doom` documentation repository:

- Transform requirements, PRDs, or feature notes into documentation updates
- Modify an existing authoritative page
- Add a new scenario-focused document under an existing section
- Evaluate whether documentation should be restructured, split, or merged
- Check Doom documentation conventions, MDX component usage, or terminology

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
   - Use the current workspace when it clearly contains documentation signals such as `AGENTS.md`, `docs/en/`, Doom config files, or an existing docs tree.
   - If the current workspace is not clearly the target repo and the user provided a path, use that path.
   - Ask for a path only when there is no clear repository context.
2. Read the target repository `AGENTS.md` before applying any built-in rule.
3. Explore the relevant directory with `rg`, `ls`, and file reads.
4. Search with multiple keywords from the requirement to avoid keyword traps.
5. Before suggesting frontmatter, path names, or category values, sample 3-5 neighboring pages in the same directory or adjacent module.
6. Before recommending MDX components, search for real examples in the repository.

Success criterion: you can name the target repository root, the likely authoritative page or section, and the local conventions you found.

### 3. Phase 0: Intake And Diagnosis

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

### 4. Phase 1: Planning

1. Load `rules/core-conventions.md`.
2. Verify directory integrity, especially the `index.mdx` rule for any directory you will create or touch.
3. Classify the task as one of:
   - `modify existing authoritative doc`
   - `add new scenario doc`
   - `restructure doc tree`
4. Infer the metadata contract from the target repo.
   - Reuse exact neighboring field names and values.
   - Never invent `category` values from template file names.
   - Never force `author`, `category`, or `queries` unless the repository actually uses them.
5. Output the execution plan with the exact sections required by the template below.
6. Use `None` when a section is empty. Do not omit required sections.
7. Ask: `Should I proceed with generating or modifying the documentation based on this plan?`
8. Stop until the user confirms.

Use this contract for the execution plan:

```markdown
## Execution Plan

**Action Type**: [modify existing authoritative doc / add new scenario doc / restructure doc tree]

### Files to Create
[Table or `None`]

### Files to Modify
[Table or `None`]

### Directory Integrity Check Result
[List missing or verified `index.mdx` coverage]

### Outline per Target Document
[One outline per document that will be created or materially reworked]

### Assumptions
[List assumptions or `None`]

### Acceptance Criteria
[Flat checklist or bullets]
```

Success criterion: the plan makes clear what will be created, what will be modified, whether directory structure is sound, and what a successful outcome looks like.

### 5. Phase 2: Execution

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
4. Treat all built-in rules as defaults. Repository facts still win.
5. Use templates only as structural references after sampling real repository pages.
6. Available structural templates are:
   - `templates/howto-template.mdx`
   - `templates/function-template.mdx`
   - `templates/concept-template.mdx`
   - `templates/arch-template.mdx`
   - `templates/quickstart-template.mdx`
   - `templates/installation-template.mdx`
   - `templates/troubleshooting-template.mdx`
   - `templates/upgrade-template.mdx`
   - `templates/intro-template.mdx`
7. Template file names describe content shapes, not mandatory `category` values.
8. Before using a Doom MDX component, search for a real example in the target repository.
9. If no trusted example exists, prefer plain Markdown or explicitly note the uncertainty.
10. For frontmatter, include only fields confirmed by the repository contract for that location.
11. Write all document titles, headings, prose, and examples in English only, even when the assistant-facing output is Chinese.

Success criterion: the generated or revised documentation follows the approved plan, matches repository conventions, and does not introduce template-driven fake standards.

### 6. Phase 2.1: Specification Review For Path B

When restructuring existing documents:

1. Load `rules/mdx-components.md`.
2. Count all `:::` directives except `:::details`.
3. If there are more than 3-4 directives, streamline them with this priority:
   - DANGER
   - WARNING
   - TIP
   - INFO
   - NOTE
4. Check terminology, links, language, MDX components, and frontmatter against repository-discovered requirements.
5. Load `templates/spec-review-report.md`.
6. Output the review report before making the restructuring change.
7. Wait for confirmation.

Success criterion: the user sees the current directive count, any compliance issues, the repository-specific frontmatter contract, and the proposed restructuring changes before execution.

### 7. Phase 2.7: Self-Verification

1. Load `rules/verification-checklist.md`.
2. Run the checks in order.
3. Verify plan consistency before any style or content checks.
4. Confirm that metadata matches the repository-discovered contract, not a hardcoded skill default.
5. Confirm that any MDX component usage is backed by real repository examples.
6. If any discrepancy exists, stop and report it instead of silently continuing.

Success criterion: you can explicitly state that the output matches the approved plan, local metadata contract, and repository conventions.

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

### Documentation Summary

After generating or revising documentation, use this structure:

```markdown
## Documentation Summary

**Action Type**: [modify existing authoritative doc / add new scenario doc / restructure doc tree]
**Execution Path**: [A / B / C]
**Repository Facts Used**: [Short summary]
**Repository Overrides**: [Any skill defaults that were overridden, or `None`]

## Generated Or Revised Content

[Draft, diff summary, or content]

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
- Documentation content is English-only for repository collaboration with this skill
- CLI-first procedures unless the repository or requirement clearly favors UI-first guidance
- No invented terminology
- No invented frontmatter fields
- No invented component syntax
