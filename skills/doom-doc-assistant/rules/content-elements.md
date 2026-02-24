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

### Four Types

| Type | Purpose | Typical Scenario |
| :--- | :--- | :--- |
| **Tip** | Supplementary info; can be ignored. | Optimization or shortcut suggestions. |
| **Info/Note** | Additional explanation. | Version compatibility, parameter basis. |
| **Warning** | Matters requiring attention. | Potential latency or performance impact. |
| **Danger** | Major risks. | Potential data loss or cluster crash. |

### Syntax Options

**Option 1: ::: Syntax (Preferred for simplicity)**
```markdown
:::tip
Tip: Use resource limits to avoid contention.
:::
```

**Option 2: Directive Component (For structured content)**
```mdx
<Directive type="tip" title="Optimization">
Use resource limits to avoid contention.
</Directive>
```

### Constraints
- Keep directive content concise (usually within one paragraph).
- **Exclusions**: Do not include tables or complex images inside a directive (icons are acceptable).
- Place Warnings and Dangers *before* the relevant text or step.
- **Strict Limit**: Do not exceed 3-4 directives per document (excluding details).

## Links

### Guidelines
- Use descriptive link text (avoid "Click here" or "Read more").
- Limit link descriptions to 15 characters.
- Use relative paths for internal documents: `[Guide](./deployment.mdx)`.
- Use the `ExternalSiteLink` component for cross-site or external links.
- **Language**: English documents must point to English pages; do not link to Chinese pages from English documentation.

## Code Blocks

### Formatting
- Specify the language (e.g., ` ```yaml `).
- Use `title` for file names: ` ```yaml title="deployment.yaml" `.
- **Context**: Provide context before the code block (e.g., "On the **Control Plane**, use **kubectl** to run:").
- **Variables**: Use `<>` to mark placeholders/variables: `kubectl apply -f <filename.yaml>`.
- **Expected Output**: Provide sample output after important commands.
- **Comments**: Add comments to complex code snippets.
- **Omission**: Use `#...` to indicate omitted lines in YAML or long config files.

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
