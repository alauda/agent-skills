# Doom Framework Core Conventions

These are default conventions for Doom documentation work. Apply them only after checking the target repository `AGENTS.md` and neighboring pages.

## Repository-First Discovery

Before proposing paths, frontmatter, or structure:

1. Read the target repository `AGENTS.md`
2. Sample neighboring pages in the same directory
3. Sample adjacent modules when the local pattern is unclear
4. Fall back to these defaults only if the repository is silent

If a repository fact conflicts with this file, the repository fact wins.

## Directory And File Organization

### Naming Conventions

- New files and directories should follow the naming style required by the target repository.
- If the target repo explicitly says `kebab-case`, use `kebab-case` for new paths.
- Do not infer a global naming rule from historical legacy files.
- Do not rename existing files just to normalize style unless the user asks for it or the approved restructuring plan requires it.
- Keep names lowercase and ASCII unless the target repo clearly does otherwise.

### Sorting Control

Use the `weight` field only when the target repository uses it for navigation order. Preserve the local spacing pattern found in sibling pages.

### Directory `index.mdx`

Critical default rule:

> Every directory that contains `.mdx` files or subdirectories should have an `index.mdx` unless the target repository clearly uses a different navigation mechanism.

Purpose: `index.mdx` is usually the navigation entry for that directory and often hosts `<Overview />`.

Verification steps:

1. Traverse the target documentation tree with `ls`, `find`, or `rg --files`.
2. For every directory you will create or modify, check whether it contains `.mdx` files or subdirectories.
3. Verify whether an `index.mdx` already exists or must be added.
4. Report the result in the execution plan.

Common mistake:

Wrong:

```text
docs/en/apis/providers/huawei-dcs/
docs/en/apis/providers/huawei-cloud-stack/
docs/en/apis/providers/
```

The parent directory is missing its navigation entry.

Correct:

```text
docs/en/apis/providers/index.mdx
docs/en/apis/providers/huawei-dcs/index.mdx
docs/en/apis/providers/huawei-cloud-stack/index.mdx
```

## Titles

- Keep titles concise and descriptive.
- Match the title pattern used by sibling pages.
- Avoid punctuation that is known to break anchors or search.
- When abbreviations appear in titles, explain them on first mention in the body if the local repository does so.

## Static Assets

Verify asset conventions in the target repository before creating images or diagrams.

Default expectations:

- Prefer text explanations over screenshots.
- Keep document-specific assets in a nearby `assets/` directory when the repo does so.
- Avoid cross-module asset references unless the repository explicitly allows them.

## Links

Verify link style from neighboring pages before writing links.

Default expectations:

- Use relative links for internal documentation.
- Reuse the anchor style already present in the repository.
- Reuse Doom link components only after checking real repository examples.

## Default Content Shapes

These are content-shape defaults, not category enums:

- how-to
- feature or overview
- concept
- quick start
- troubleshooting
- installation
- upgrade
- architecture

If the repository uses a `category` field, infer the exact allowed values from sibling pages or repo docs. Never derive a category directly from a template file name.

## Search And Chunking

Doom repositories often rely on headings and components for chunking and retrieval.

- Use descriptive headings.
- Avoid sections that contain only code without framing text.
- When using `<Tabs>`, ensure each tab has enough text to be retrievable on its own.

## `shared` Directory Convention

The `shared` directory is usually for reusable fragments, CRDs, or non-page content. Do not assume content under `shared` should become a generated documentation page unless the repository explicitly treats it that way.
