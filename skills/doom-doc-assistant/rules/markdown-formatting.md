# Markdown Formatting Rules

This document defines Markdown syntax formatting standards to ensure consistent rendering across different Markdown parsers.

## Line Breaks and Spacing

### Hard Break vs Paragraph Break

| Scenario | Syntax | Example |
|----------|--------|---------|
| Line break within table cell | `<br />` | `First line<br />Second line` |
| Paragraph separation | Empty line | `Para 1\n\nPara 2` |
| Line break within list item | `<br />` | `- Item text<br />Continued` |
| Section separation | Empty line | `## Section 1\n\n## Section 2` |

### Priority: Empty Lines First

**Rule**: Always prioritize using empty lines to separate paragraphs. Only use `<br />` when empty lines are impossible (e.g., inside table cells).

**Good**:
```markdown
If a hardware LoadBalancer is available, use it.

If not, you can enable Self-built VIP.
```

**Bad**:
```markdown
If a hardware LoadBalancer is available, use it.<br /><br />
If not, you can enable Self-built VIP.
```

### Spacing Rules

| Break Type | Usage | Rendering |
|-----------|-------|-----------|
| Single `<br />` | Same paragraph, new line | Text continues |
| `<br /><br />` | Separate info blocks (like empty line) | Visual separation |
| Empty line | New paragraph | New paragraph |

## Bold Syntax

### Priority: Markdown over HTML

| Syntax | Priority | When to Use |
|--------|----------|-------------|
| `**bold**` | 🥇 Highest | All normal text bolding |
| `__bold__` | 🥈 Medium | Avoid (use asterisks) |
| `<b>bold</b>` | 🥉 Lowest | Only in MDX JSX props/attributes |

**Good**:
```markdown
**Recommendation**: Using a domain name is recommended.
```

**Bad**:
```markdown
<b>Recommendation</b>: Using a domain name is recommended.
```

**Exception**: In MDX table cells with JSX style props, `<b>` may be used for consistency with existing code:
```markdown
<td style={{ whiteSpace: 'nowrap' }}><b>Cluster Endpoint</b></td>
```

## Table Cell Formatting

### Multi-Line Content

Use `<br />` to separate lines within table cells:

```markdown
| Column 1 | Column 2 |
|----------|----------|
| Header | First paragraph.<br /><br />Second paragraph.<br />- List item 1<br />- List item 2 |
```

### Table Cell Structure

| Content Type | Pattern |
|-------------|---------|
| Single paragraph | `Text here.` |
| Multiple paragraphs | `Para 1.<br /><br />Para 2.` |
| Paragraph + list | `Para.<br /><br />List:<br />- Item 1<br />- Item 2` |
| List only | `- Item 1<br />- Item 2` |

## Inline Code and Backticks

### Usage Guidelines

| Scenario | Syntax | Example |
|----------|--------|---------|
| Parameters/fields | `` `parameter_name` `` | `` `Cluster Endpoint` `` |
| Features/functions | `` `Self-Built VIP` `` | `` `Self-Built VIP` `` |
| Commands | `` `kubectl` `` | `` `kubectl get pods` `` |
| File paths | `` `path/to/file` `` | `` `/etc/hosts` `` |
| Menu paths | **Bold** not code | **File > Save** |

**Good**:
```markdown
Enter the `Cluster Endpoint` parameter.
```

**Bad**:
```markdown
Enter the Cluster Endpoint parameter.
```

## Emphasis vs Code

| Purpose | Syntax | Example |
|---------|--------|---------|
| Emphasize a term | `**bold**` | **Recommendation**: |
| Technical term/code | `` `code` `` | The `global` cluster |
| UI button/menu | **Bold** | Click **Save** |

## Lists and Breaks

### Code Blocks in Lists

When a code block appears inside a list item, it must be indented to align with the list content. The linter `remark-lint-code-block-split-list` enforces this rule.

**Good** (properly indented):
```markdown
1. First item
   1.1. Sub-item with code block:
       ```
       code here
       ```
```

**Bad** (missing indentation):
```markdown
1. First item
   1.1. Sub-item with code block:
   ```
   code here (wrong indentation)
   ```
```

**Rule**: Add 2 spaces for each nesting level to align the code block with the list text. Most linters support `--fix` to auto-correct this.

### List Item Continuation

To add multiple paragraphs within a single list item, use `<br />`:

```markdown
- First point with continued text.<br />
  Continued text on new line.<br /><br />
  New paragraph within same item.
```

### List Item Ending

End list items with `<br />` when:
- The item contains structured sub-information
- The item is followed by another item with different structure

## Common Patterns

### Pattern: Recommendation with Note

```markdown
**Recommendation**: [Recommendation content]. [Reason].

**Note**: [Note content].
```

### Pattern: Two-Option Choice

```markdown
If [condition A], it is **recommended** to [option A].
If not, you can [option B].
```

### Pattern: Table Cell with Structured Content

```markdown
[Primary instruction].<br />
[Alternative instruction].<br />
[Special case note].<br /><br />
[Requirements header]:<br />
- [Requirement 1]<br />
- [Requirement 2]
```

## What to Avoid

| ❌ Avoid | ✅ Use Instead | Reason |
|---------|----------------|--------|
| `<b>text</b>` in body | `**text**` | Markdown native syntax |
| `<br />` for paragraphs | Empty line | Semantic correctness |
| Excessive `<br />` | Better structure | Readability |
| Mixed bold styles | Consistent `**` | Maintain consistency |
| `__bold__` | `**bold**` | Doom standard |
