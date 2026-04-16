# Doom Framework Core Conventions

These are product documentation standards for Doom documentation work. Explicit target repository rules may override them, but historical samples must not override them for new product documentation.

## Repository-First Discovery

Before proposing paths, frontmatter, or structure:

1. Read the target repository `AGENTS.md` when it exists
2. Apply these built-in product documentation standards
3. Sample neighboring pages in the same directory for local ordering and placement
4. Sample adjacent modules when the local placement pattern is unclear
5. Fall back to templates only for structural scaffolding when repository rules and local samples are silent

If an explicit repository rule conflicts with this file, the explicit repository rule wins. If only legacy examples conflict with this file, this file wins for new content.

## Directory And File Organization

### Naming Conventions

- New product documentation files and directories must use lowercase English letters, numbers, and underscores only.
- Do not create new paths that use hyphens, spaces, uppercase letters, or non-ASCII characters.
- Do not infer a global naming rule from historical legacy files.
- Do not rename existing files just to normalize style unless the user asks for it or the approved restructuring plan requires it.
- Existing noncompliant paths are legacy evidence, not valid examples for new paths.

### Sorting Control

Use the `weight` field for new product documentation. Preserve the local spacing pattern found in sibling pages.

### Directory `index.mdx`

Critical rule:

> Every product documentation directory that contains `.mdx` files or subdirectories must have an `index.mdx` unless an explicit target repository rule says otherwise.

Purpose: `index.mdx` is the navigation entry for that directory and should contain an H1 plus `<Overview />` by default.

Verification steps:

1. Traverse the target documentation tree with `ls`, `find`, or `rg --files`.
2. For every directory you will create or modify, check whether it contains `.mdx` files or subdirectories.
3. Verify whether an `index.mdx` already exists or must be added.
4. Report the result in the execution plan.

Common mistake:

Wrong:

```text
docs/en/apis/providers/provider-alpha/
docs/en/apis/providers/provider-beta/
docs/en/apis/providers/
```

The parent directory is missing its navigation entry.

Correct:

```text
docs/en/apis/providers/index.mdx
docs/en/apis/providers/provider_alpha/index.mdx
docs/en/apis/providers/provider_beta/index.mdx
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
- release notes

If explicit repository rules require a `category` field, follow `rules/metadata-rules.md`. Never derive a category directly from a template file name or historical sample alone.

## Search And Chunking

Doom repositories often rely on headings and components for chunking and retrieval.

- Use descriptive headings.
- Avoid sections that contain only code without framing text.
- When using `<Tabs>`, ensure each tab has enough text to be retrievable on its own.

## `shared` Directory Convention

The `shared` directory is usually for reusable fragments, CRDs, or non-page content. Do not assume content under `shared` should become a generated documentation page unless the repository explicitly treats it that way.
