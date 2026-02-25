# Content Element Specification

This document defines the standards for using various Markdown and MDX elements in product documentation.

## Lists

### Usage Principles
1. **Sequential Relationship**: Use ordered lists (1, 2, 3...).
2. **Non-Sequential Relationship**: Use unordered lists (-).
3. **Single Item**: Integrate it into the main paragraph.

### Guidelines
- Use standard Markdown markers (no custom characters).
- **Consistent Punctuation**: Ensure all list items in a single list use the same punctuation at the end (either none, or all use periods).
- **Quantity**: Limit lists to 2-9 items.
- **Introduction**: Provide an introductory sentence before the list to provide context.
- **Nesting**: Do not exceed three levels of nesting.

## Tables

### Guidelines
- Must have at least two columns and one row. If you have only two rows and one column, consider transposing it.
- Left-align by default.
- **Consistency**: Maintain consistent data types and formats (and punctuation) within the same column.
- Use concise headers.
- **No Blanks**: Use "-" for empty cells; avoid leaving them blank.
- **No Duplicates**: Avoid using "Same as above" (同上). Merge cells if necessary, or repeat the info if required for readability.
- **Readability**: Split overly complex tables into multiple smaller ones.

## Information Indicators (Directives)

### Six Types

| Type | Color | Purpose | Typical Scenario |
| :--- | :--- | :--- | :--- |
| **NOTE** | Gray | Supplementary or non-critical info. | Background context. |
| **TIP** | Green | Practical advice or optimization. | Shortcuts or efficiency tips. |
| **INFO** | Blue | Neutral, important info. | Version compatibility, parameter basis. |
| **WARNING**| Yellow| Potential risks, proceed with caution. | Potential latency or performance impact. |
| **DANGER** | Red | Severe risks, irreversible consequences. | Potential data loss or cluster crash. |
| **DETAILS**| N/A | Collapsible detailed information. | Long logs or secondary deep-dive content. |

### Syntax Options

**Option 1: ::: Syntax (Preferred for standard Markdown)**
```markdown
:::tip
Tip: Use resource limits to avoid contention.
:::
```

**Option 2: Directive Component (Mandatory inside JSX/MDX components)**
```mdx
<Directive type="tip" title="Optimization">
Use resource limits to avoid contention.
</Directive>
```

### Constraints
- Keep directive content concise (usually within one paragraph).
- **Exclusions**: Do not include tables or complex images inside a directive (icons are acceptable).
- Place Warnings and Dangers *before* the relevant text or step.
- **Strict Limit**: Do not exceed 3-4 directives per document (excluding details). If you exceed this limit, fallback to inline bolding (e.g., `**Note:**`).
- **Syntax Boundaries**: `:::` and `<Directive />` render identical styles. However, **`:::` syntax fails inside JSX components** (like `<Tabs>`, `<TabItem>`, or other custom components) and deep list indentations. **You MUST use `<Directive />`** whenever you are placing a directive inside any JSX tag or complex nested list.

### Fallback Notes (e.g., `**Note:**`)
When falling back from a Directive to inline text (`**Note:**`) due to limits:
1. **Paragraph Spacing**: You **must** insert a completely blank line before `**Note:**` if it follows a list item. Without the blank line, it will render inline with the list instead of starting a new block.
2. **Indentation and Wrapping**: If the note spans multiple sentences, either keep them on the same line immediately following `**Note:** `, or ensure the subsequent lines are structurally separated (e.g., as another list item) so they don't break the document's hierarchy.


## Links

### Guidelines
- Use descriptive link text (avoid "Click here" or "Read more").
- Limit link descriptions to 15 characters.
- Use relative paths for internal documents: `[Guide](./deployment.mdx)`.
- Use the `ExternalSiteLink` component for cross-site or external links.
- **Language**: English documents must point to English pages; do not link to Chinese pages from English documentation.
## Custom Anchors

You can assign a custom anchor ID to headings using `\{#custom_id}` syntax. This ensures cross-links remain reliable even if the heading text changes.

```mdx
## Hello World \{#custom_id}

[Link to Hello World](./page.mdx#custom_id)
```

## Code Blocks

### Formatting
- Specify the language (e.g., ` ```yaml `).
- Use `title` for file names: ` ```yaml title="deployment.yaml" `.
- **Context**: Provide context before the code block (e.g., "On the **Control Plane**, use **kubectl** to run:").
- **Variables**: Use `<>` to mark placeholders/variables: `kubectl apply -f <filename.yaml>`.
- **Expected Output**: Provide sample output after important commands.
- **Comments**: Add comments to complex code snippets.
- **Omission**: Use `#...` to indicate omitted lines in YAML or long config files.

### Highlighting Lines
You can highlight specific lines in a code block by appending `{line_ranges}` to the code fence:
````mdx
```js {1,3-5}
console.log('Hello World');
```
````

### Code Callouts
Use the `<Callouts>` component to annotate specific code lines visually. Append `[!code callout]` (or `[\!code callout]` if inside MDX examples to escape it) in the code comments, and provide a `<Callouts>` component immediately after the block.
````mdx
```sh
Memory overhead ≈ (requested memory) \
    + 218 MiB \  # [\!code callout]
    + (additional)  # [\!code callout]
```

<Callouts>
1. Required for the `virt-launcher` pod.
2. Additional memory overhead.
</Callouts>
````
## Units and Symbols

- Keep a space between the value and the unit (e.g., `100 m`, `24 Gi`, `38 Mi`).
- Follow international standards for capitalization.

## Sensitive Information (Prohibited)

The following information is strictly prohibited:
1. **Internal Branding**: ACP, Alauda, or company-specific internal terms.
2. **Discriminatory Terms**: Avoid biased or offensive language.
3. **Third-Party Info**: Do not include non-essential company names, logos, or products.
4. **PII**: Avoid ID numbers, phone numbers, home addresses, or bank accounts.
5. **Intellectual Property**: No unauthorized code, fonts, or images.
6. **Confidentiality**: No internal project codes, testing environment URLs, or commercial secrets (financials, contracts).
7. **Political/Religious**: No sensitive political, religious, or racial content.

| Prohibited | Replacement |
| :--- | :--- |
| master nodes | control plane nodes |
| slave nodes | worker nodes |
| blacklist | deny list |
| whitelist | allow list |

## Content Conciseness

### Redundancy Elimination

**Principle**: Remove information that provides no value to users. Keep only core operational steps and essential context.

| Redundancy Type | Example | Why Remove |
|---------------|---------|------------|
| Redundant premise | "If you need to access through a domain name..." | Table row already states this is for domain access |
| Implementation details | "The installer will automatically deploy keepalived" | Users only need to know enable/disable |
| Repeated recommendations | Same tip mentioned multiple times | Say it once in the most appropriate location |
| Obvious context | "Please ensure that..." when step already implies it | Trust user intelligence |

### Information Layering

**Principle**: Organize information in clear layers: Recommendation → Reason → Note. Don't mix them together.

**Structure**:
```
[Recommendation: What to do]
    ↓
[Reason: Why it's recommended]
    ↓
[Note: Important limitations or exceptions]
```

**Good Example**:
```markdown
**Recommendation**: Using a domain name for the Cluster Endpoint is recommended.
If the VIP needs to be changed after cluster installation, using a domain name allows for easy DNS record updates without impacting cluster operations.

**Note**: `Self-Built VIP` does not support domain name configuration.
```

**Bad Example** (everything mixed):
```markdown
You should use a domain name for the Cluster Endpoint because if the VIP needs to be changed... also note that Self-Built VIP doesn't support domains so consider that when...
```

### Conciseness Guidelines

| Guideline | Example |
|-----------|---------|
| One idea per sentence | "Enter the domain name. If unavailable, enter the VIP." |
| Remove filler words | "Basically" → (remove), "In order to" → "To" |
| Use active voice | "The system creates" instead of "A creation is made by the system" |
| Be direct | "Enter the value" instead of "You should enter the value" |
| Trust context | Don't repeat what's already in the table heading |
