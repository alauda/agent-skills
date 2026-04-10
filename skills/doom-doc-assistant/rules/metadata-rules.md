# Metadata Specification (Frontmatter)

Frontmatter must be discovered from the target repository, not assumed from this skill.

## Discovery Order

Determine the frontmatter contract in this order:

1. The target repository `AGENTS.md`
2. Pages in the same directory
3. Pages in adjacent modules that clearly share the same documentation pattern
4. This file, only as a fallback

If repository facts conflict with this file, the repository facts win.

## Field Guidance

| Field | Default status | Use when |
| :--- | :--- | :--- |
| `weight` | Usually required in Doom repos | The repository uses it for navigation order |
| `title` | Optional | The repository or neighboring pages use explicit titles instead of relying on the H1 |
| `author` | Conditional | The repository actually tracks authors in the same directory |
| `category` | Conditional | The repository uses a category field and the allowed values can be inferred from real pages or repo docs |
| `queries` | Conditional | The repository uses retrieval hints in that area of the docs |

Do not force `author`, `category`, or `queries` unless you have direct repository evidence for them.

## Minimal Example

Use the smallest frontmatter contract the repository supports.

```yaml
---
weight: 10
---
```

## Extended Example

Only use a larger contract when the repository already uses it.

```yaml
---
title: "Access a Cluster With kubeconfig"
weight: 10
author: "dev@alauda.io"
category: "howto"
queries:
  - access cluster with kubeconfig
  - download kubeconfig
---
```

## Category Rules

- Never derive a category value from a template file name such as `intro-template` or `arch-template`.
- Reuse exact category values already present in sibling pages.
- If the repository does not use `category` in that area, omit it.

## `queries` Guidance

When the repository uses `queries`:

- Prefer user-facing search phrases
- Cover synonyms and acronyms when they matter
- Keep them specific to the current page
- Match the style and density used by neighboring pages

If the repository does not use `queries`, do not introduce them.

## Weight Guidance

- Match the local spacing pattern found in sibling pages.
- Do not hardcode a global weight scheme when the directory already has one.
- When creating a new page in a populated directory, choose a value that fits the existing order.
