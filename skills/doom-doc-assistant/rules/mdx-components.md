# Doom Framework MDX Components

This document describes the standard MDX components used in the Doom framework.

## `<Overview />`

### Usage
Used in the `index.mdx` of a directory to automatically generate a summary and child navigation list.

## `<Term />`

### Usage
Used for replaceable terms (e.g., product names, company names) defined in `terminology-guide.md`.

### Parameters
- `name`: The key of the term.
- `textCase`: Formatting (e.g., `capitalize`, `upper`, `lower`).

## `<Directive />`

### Usage
Used for highlighting important information (Tips, Warnings, etc.).

### Parameters
- `type`: `tip`, `info`, `warning`, or `danger`.
- `title`: The header text.

### Constraints
- **Do not** use `:::` syntax (Option 1 from `content-elements.md`) inside JSX components like `<TabItem>`, `<Tabs>`, `<Overview>`, `<Steps>`, or deep list indentations. The markdown parser will fail.
- You **must** use the `<Directive />` component in these scenarios instead.
## `<Steps />`

### Usage
**Mandatory** for HowTo guides and procedural instructions. It visualizes standard Markdown headings (`###`) as numbered steps.

```mdx
<Steps>
### Step 1
Content for step 1

### Step 2
Content for step 2
</Steps>
```
## `<ExternalSiteLink />`

### Usage
Used for linking to documents in other sub-sites or external websites.

### Parameters
- `name`: The site identifier (from `sites.yaml`).
- `href`: The target path.
- `children`: The link text.

## `<ExternalSite />`

### Usage
Used in entry documents for independent documentation sub-sites to generate jump instructions and links.

### Parameters
- `name`: The unique identifier of the sub-site (as registered in `sites.yaml`).

## `<Tabs />` and `<Tab />`

### Usage
Used to display content in tabs (e.g., switching between CLI and Web UI instructions).

```mdx
<Tabs>
  <Tab label="Tab 1">
  Tab 1 content
  </Tab>

  <Tab label="Tab 2">
  Tab 2 content
  </Tab>
</Tabs>
```

### Constraint
Tabs must include descriptive text alongside code blocks to ensure RAG accessibility.

## Core Constraint: Directive Abuse Prevention

- **Limit**: Do not exceed **3-4** `:::` or `<Directive />` elements in a single document.
- **Priority**: DANGER > WARNING > TIP > INFO.
