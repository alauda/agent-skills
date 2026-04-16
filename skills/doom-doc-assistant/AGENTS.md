# doom-doc-assistant — Skill Development Conventions

This file governs development of the `doom-doc-assistant` skill specifically. It extends the root `AGENTS.md` with patterns specific to content-generation skills for Doom documentation repositories.

## Core Principle

Explicit rules and product documentation standards win.

The target repository's explicit rules are authoritative. When a repository is silent, the product documentation standards bundled in this skill are authoritative. Local page samples are useful for placement, ordering, and style, but legacy samples must not override required product documentation standards such as English product content, underscore-only new paths, `weight` plus `queries`, or directory `index.mdx` coverage.

## Current Layout

```text
doom-doc-assistant/
├── SKILL.md
├── AGENTS.md
├── CLAUDE.md
├── rules/
│   ├── best-practices.md
│   ├── common-pitfalls.md
│   ├── content-elements.md
│   ├── core-conventions.md
│   ├── language-style.md
│   ├── markdown-formatting.md
│   ├── mdx-components.md
│   ├── metadata-rules.md
│   ├── terminology-consistency.md
│   ├── terminology-guide.md
│   └── verification-checklist.md
├── templates/
│   ├── arch-template.mdx
│   ├── concept-template.mdx
│   ├── diagnosis-report.md
│   ├── function-template.mdx
│   ├── howto-template.mdx
│   ├── installation-template.mdx
│   ├── intro-template.mdx
│   ├── quickstart-template.mdx
│   ├── release-notes-template.mdx
│   ├── spec-review-report.md
│   ├── troubleshooting-template.mdx
│   └── upgrade-template.mdx
└── references/
    └── regression-cases.md
```

Keep this file aligned with the real directory tree. Do not leave historical placeholder names here.

## Rules And Templates

### `rules/`

- `rules/` files store defaults and reusable checks.
- A rule file must never overrule explicit target repository rules.
- Put stable behaviors here, not repo-specific one-off policies.
- If a rule becomes "discover from the repository first," say that directly in the rule file.

### `templates/`

- Templates are structure references, not truth sources.
- Template file names describe content shapes only. They are not canonical `category` values.
- Templates for new product documentation must include the stable minimum frontmatter contract: `weight` and English `queries`.
- Keep `author` and `category` out of template frontmatter unless a future explicit repository rule requires them.

## Discovery-First Patterns

Prefer runtime discovery over memorized standards for:

- local weight ordering and page placement
- optional frontmatter fields and category values
- MDX component syntax
- link patterns
- page structure and section naming

The preferred sequence is:

1. Read the target repository `AGENTS.md` when it exists
2. Apply the built-in product documentation standards from `rules/`
3. Sample sibling pages in the same directory for local ordering, placement, and non-conflicting style
4. Sample adjacent modules when local evidence is too thin
5. Fall back to templates only for structural scaffolding

## Workflow Design Expectations

- The skill must lock the assistant-facing output language before Phase 0 when the preference is not explicit.
- This language choice is separate from the repository's documentation content language.
- Assistant-facing output may be English or Chinese, but drafted or revised repository documentation content must always stay in English.
- New product documentation paths must use lowercase letters, numbers, and underscores only.
- New product documentation frontmatter must include `weight` and English `queries`.
- For Doom/Yarn repositories, the post-drafting handoff must run `yarn up @alauda/doom` and then `yarn install` before human acceptance.
- Manual acceptance must be handed to a human reviewer who runs `yarn dev` locally only after local preview prep completes successfully.
- `yarn build` and `yarn translate` are never default verification steps. They are separate tasks that require explicit user direction.
- Phase 0 must output a fixed diagnosis contract, not a free-form summary.
- Phase 1 must output a fixed execution-plan contract, not a new-doc-only checklist.
- Phase 1 and the final documentation summary must include a local preview prep and manual acceptance handoff section.
- Review-only or audit-only requests must stay read-only and stop after a findings report unless the user asks for fixes.
- Explicit `yarn build` or `yarn translate` requests must use a separate command branch and must not become default documentation validation.
- Explicit `yarn build` or `yarn translate` requests should use a fixed `Explicit Command Result` contract instead of free-form command reporting.
- Manual acceptance handoff must tell the human to run `yarn dev` only after local preview prep completes successfully.
- Path A must support modifying authoritative existing docs.
- Path B should only be recommended when restructuring is necessary for this round.
- Path C should capture technical debt without silently expanding scope.

## Validation Assets

When changing this skill, use [references/regression-cases.md](./references/regression-cases.md) as the minimum regression suite. Add new cases when the skill learns a new branch or fixes a new class of failure.

## When To Update Which File

| Change needed | Update |
|--------------|--------|
| Workflow order or output contract | `SKILL.md` |
| Default naming, directory, link, or metadata guidance | `rules/core-conventions.md` or `rules/metadata-rules.md` |
| Validation expectations | `rules/verification-checklist.md` or `references/regression-cases.md` |
| Structural page scaffold | `templates/*.mdx` |
| Diagnosis or restructuring report contract | `templates/diagnosis-report.md` or `templates/spec-review-report.md` |

## What Not To Do

- Do not force the agent to ask for a repository path when the current workspace already identifies the target repo.
- Metadata and legacy samples must not become fake rules: require `author` or `category` only when explicit repository rules require them, and do not let legacy naming, missing `queries`, or missing `index.mdx` in existing files dictate new product documentation.
- Command handling must stay narrow: do not automatically run `yarn dev`, `yarn build`, or `yarn translate`, and do not tell the human to run `yarn dev` after a failed `yarn up @alauda/doom` or `yarn install`.
- Read-only review or audit requests must stay read-only; do not run local preview prep commands in those routes.
- Do not treat technical debt as automatic evidence that Path B is required.
- Do not let a user preference for Chinese assistant output turn into Chinese documentation content.
