# doom-doc-assistant — Skill Development Conventions

This file governs development of the `doom-doc-assistant` skill specifically. It extends the root `AGENTS.md` with patterns specific to content-generation skills for Doom documentation repositories.

## Core Principle

Repository facts win.

The target repository's `AGENTS.md`, local page samples, and neighboring documentation patterns are more trustworthy than anything bundled in this skill. `rules/` and `templates/` are defaults that help when the repository does not say more.

## Current Layout

```text
doom-doc-assistant/
├── SKILL.md
├── AGENTS.md
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
- A rule file must never claim authority over the target repository.
- Put stable behaviors here, not repo-specific one-off policies.
- If a rule becomes "discover from the repository first," say that directly in the rule file.

### `templates/`

- Templates are structure references, not truth sources.
- Template file names describe content shapes only. They are not canonical `category` values.
- Do not hardcode unstable frontmatter into templates.
- If a field is conditional across repos, keep it out of template frontmatter and mention it in comments instead.

## Discovery-First Patterns

Prefer runtime discovery over memorized standards for:

- frontmatter fields and category values
- filename and directory naming
- MDX component syntax
- link patterns
- page structure and section naming

The preferred sequence is:

1. Read the target repository `AGENTS.md`
2. Sample sibling pages in the same directory
3. Sample adjacent modules when local evidence is too thin
4. Fall back to bundled rules and templates only when the repository is silent

## Workflow Design Expectations

- The skill must lock the assistant-facing output language before Phase 0 when the preference is not explicit.
- This language choice is separate from the repository's documentation content language.
- Phase 0 must output a fixed diagnosis contract, not a free-form summary.
- Phase 1 must output a fixed execution-plan contract, not a new-doc-only checklist.
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
- Do not require `author`, `category`, or `queries` unless repository facts support them.
- Do not let one directory's legacy naming pattern turn into a fake global naming rule for the whole repository.
- Do not treat technical debt as automatic evidence that Path B is required.
