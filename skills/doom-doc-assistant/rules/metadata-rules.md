# Metadata Specification (Frontmatter)

These are product documentation metadata standards. Explicit target repository rules may override them, but historical samples that omit metadata are legacy evidence only.

## Discovery Order

Determine the frontmatter contract in this order:

1. User task scope and explicit target repository rules
2. Built-in product documentation minimums in this file
3. Sibling pages for local ordering, optional fields, and non-conflicting style
4. Adjacent modules when local evidence is too thin

If an explicit repository rule conflicts with this file, the explicit repository rule wins and the output must say so. If only historical samples conflict, this file wins for new product documentation.

## Field Guidance

| Field | Default status | Use when |
| :--- | :--- | :--- |
| `weight` | Required for new English product docs | Controls local navigation order |
| `queries` | Required for new English product docs | Provides English retrieval hints for RAG and search |
| `title` | Optional | Explicit repository rules or neighboring pages use titles instead of relying on the H1 |
| `author` | Optional | Explicit repository rules require author tracking |
| `category` | Optional | Explicit repository rules require category metadata |

For small edits to existing pages, preserve the existing frontmatter shape. If the page lacks `queries`, list it as a follow-up or add it in the same change only when the approved scope includes metadata completion.

## New Product Documentation Example

Use this minimum contract for new English product documentation:

```yaml
---
weight: 10
queries:
  - "How do I configure <feature>?"
  - "What is <feature> used for?"
  - "<feature> troubleshooting"
---
```

Choose `weight` from the local spacing pattern in sibling pages.

## Optional Extended Example

Only include optional fields when explicit repository rules require them:

```yaml
---
title: "<title-if-required>"
weight: 10
category: "howto"
queries:
  - "How do I configure <feature>?"
  - "What is <feature> used for?"
  - "<feature> troubleshooting"
---
```

Do not include `author` or `category` just because a template mentions a content shape.

## `queries` Rules

- `queries` must be an English string list.
- Default to 3 entries.
- Use 2-4 entries when the page scope is unusually narrow or broad.
- Write queries as user-facing search questions or keywords.
- Cover important synonyms and acronyms when they matter.
- Keep queries specific to the current page.
- Avoid duplicating queries already used by sibling pages when possible.

## Category Rules

Only use `category` when explicit target repository rules require it. When required, use only these values unless the explicit repository rule provides a different closed set:

- `index`
- `introduction`
- `feature`
- `releasenote`
- `architecture`
- `concept`
- `quickstart`
- `howto`
- `troubleshooting`
- `permissions`
- `api`

Never derive a category value from a template file name such as `intro-template`, `function-template`, or `arch-template`.

## Weight Guidance

- Match the local spacing pattern found in sibling pages.
- Do not hardcode a global weight scheme when the directory already has one.
- When creating a new page in a populated directory, choose a value that fits the existing order.
