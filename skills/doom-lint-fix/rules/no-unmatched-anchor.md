# Fixing Unmatched Anchor Errors

## Overview

The `doom-lint:no-unmatched-anchor` rule ensures anchor links (`#hash`) only reference **explicitly defined custom IDs** — never auto-generated heading slugs. This guarantees anchor stability across translations where heading text differs but anchor targets must be identical.

**Core principle:** Every heading targeted by an anchor link MUST have a custom ID. Use `{#custom-id}` in `.md` files, `\{#custom-id}` in `.mdx` files (braces are JSX expression delimiters in MDX and must be escaped). Auto-slugs don't count.

## When to Use

- `doom lint` outputs: `Unmatched anchor ...`
- Headings are referenced by `[text](#id)` links but lack `{#id}`
- Cross-language docs need stable anchor references
- Error message matches: ``Unmatched anchor `X` in link `Y`, make sure the target has the correct id with `{#X}` in heading or `<a id="X"></a>` element.``

## Error Message Anatomy

```
Unmatched anchor `{hash}` in link `{url}`, make sure the target has the correct id with `{#{hash}}` in heading or `<a id="{hash}"></a>` element.
```

| Field  | Meaning                                                               |
| ------ | --------------------------------------------------------------------- |
| `hash` | The anchor fragment being referenced                                  |
| `url`  | Full link containing `#{hash}` — may include path for cross-file refs |

The message includes inline fix hints: add `{#hash}` to a heading, or add an `<a id="hash"></a>` element.

## Fix Decision Flow

```dot
digraph fix {
  rankdir=TB;
  "Parse error" [shape=box];
  "Heading slugs to hash?" [shape=diamond];
  "Add {#hash} to heading" [shape=box, style=bold];
  "Hash close to existing anchor?" [shape=diamond];
  "Fix the link URL" [shape=box];
  "Add <a id> element" [shape=box];

  "Parse error" -> "Heading slugs to hash?";
  "Heading slugs to hash?" -> "Add {#hash} to heading" [label="yes (90% of cases)"];
  "Heading slugs to hash?" -> "Hash close to existing anchor?" [label="no"];
  "Hash close to existing anchor?" -> "Fix the link URL" [label="typo"];
  "Hash close to existing anchor?" -> "Add <a id> element" [label="no match"];
}
```

## Fix Patterns

### 1. Add Custom ID to Heading (Most Common)

A heading exists whose slug matches the hash, but it lacks an explicit custom ID.

```markdown
<!-- BEFORE — heading has no custom ID, link triggers error -->

## Sidebar Configuration

[See sidebar](#sidebar-configuration)

<!-- AFTER (.md file) — custom ID added -->

## Sidebar Configuration {#sidebar-configuration}

[See sidebar](#sidebar-configuration)
```

**In `.mdx` files**, escape the brace to avoid JSX parse errors:

```mdx
## Sidebar Configuration \{#sidebar-configuration}
```

**Cross-language — same `{#id}` on every translation:**

```markdown
<!-- en/usage/config.md -->

## Sidebar Configuration {#sidebar-configuration}

<!-- zh/usage/config.md -->

## 侧边栏配置 {#sidebar-configuration}

<!-- For .mdx files, use \{#sidebar-configuration} in both -->
```

### 2. Fix Typo in Link

The hash is close to but doesn't match an existing custom ID. Open the target file, search for headings with custom IDs, and pick the closest match.

```markdown
<!-- BEFORE — typo: "configration" -->

[See config](#sidebar-configration)

<!-- AFTER — corrected to match existing {#sidebar-configuration} -->

[See config](#sidebar-configuration)
```

### 3. Add Anchor Element (No Matching Heading)

When the anchor target isn't a heading (e.g., a specific paragraph or section marker), add an element with an `id` attribute. The error message suggests `<a id="..."></a>`:

```markdown
<!-- Use an anchor element with id attribute -->

<a id="custom-anchor"></a>

Content that needs an anchor target...
```

**In MDX files**, JSX syntax works:

```mdx
<a id="custom-anchor"></a>
```

Other elements with `id` also work (e.g., `<span id="...">`, `<div id="...">`), but `<a id>` is the recommended form.

## Recognized Anchor Sources

The rule collects anchors from exactly three sources:

| Source              | `.md` syntax      | `.mdx` syntax     | Example ID extracted |
| ------------------- | ----------------- | ----------------- | -------------------- |
| Custom heading ID   | `## Title {#id}`  | `## Title \{#id}` | `id`                 |
| JSX `id` attribute  | N/A               | `<a id="id"></a>` | `id`                 |
| HTML `id` attribute | `<a id="id"></a>` | `<a id="id"></a>` | `id`                 |

Any HTML element with an `id` attribute is recognized (`<a>`, `<span>`, `<div>`, etc.).

**NOT recognized:** auto-generated slugs from heading text, `<a name="...">`, double-escaped `\\{#id}`.

## Batch Fix Strategy

When many errors exist:

1. Run `doom lint`, capture all `no-unmatched-anchor` errors
2. Group by **target file** (resolve the path from the link URL in the error)
3. For each target file:
   - Read the file
   - For each missing anchor, find the heading and add `{#hash}` (or `\{#hash}` for `.mdx`)
   - Write back once (not per-anchor)
4. For cross-file refs: fix the **target file**, not the linking file
5. Re-run `doom lint` to verify

## Common Mistakes

| Mistake                                    | Why It Fails                                           | Fix                                             |
| ------------------------------------------ | ------------------------------------------------------ | ----------------------------------------------- |
| Relying on auto-slug `## Title` → `#title` | Rule ignores auto-slugs by design                      | Add `{#title}` (`.md`) or `\{#title}` (`.mdx`)  |
| Adding `{#id}` only in primary language    | Other language files still lack the anchor             | Add same `{#id}` / `\{#id}` to ALL translations |
| Using `<a name="id">`                      | Rule only recognizes `id` attribute, not `name`        | Use `<a id="id"></a>`                           |
| Using `{#id}` in `.mdx` without escaping   | MDX parser treats `{}` as JSX expression → parse error | Escape: `\{#id}`                                |
| Fixing the link instead of the heading     | Link is correct; heading is missing the anchor         | Add custom ID to the heading                    |

## Excluded From This Rule

- External URLs (`https://...`)
- API docs paths (`{lang}/apis/...`) — anchors are dynamically generated
- Non-existent target files — handled by `doom-lint:check-dead-links` instead
- Files outside the configured docs root
