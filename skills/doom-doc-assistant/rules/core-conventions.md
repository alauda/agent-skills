# Doom Framework Core Conventions

## Directory and File Organization

### Naming Conventions
- **Format**: `xxx/xxx.mdx`
- **Characters**: Only lowercase letters, numbers, and underscores are allowed.
- **Examples**:
  - `deployment_guide.mdx` ✓
  - `Deployment-Guide.mdx` ✗
  - `deployment-guide.mdx` ✗ (No hyphens)
  - `部署指南.mdx` ✗

### Sorting Control
Use the `weight` metadata field to control the sorting in the left navigation menu.

### Directory `index.mdx`
Each directory must contain an `index.mdx` file:
```mdx
# Navigation Name

<Overview />
```

## Title Writing Rules

Titles must be concise and descriptive to help users quickly locate information.

- **Structure Consistency**: Maintain the same structure for titles of the same type.
- **Good**: "Deploying Operator" and "Deploying Deployment".
- **Bad**: "Deploying Operator" and "Deployment of Deployment".
- **No Special Characters**: Do not use `+`, `*`, `|`, `^`, `~`, `'`, `\`, or `/` in titles, as they may interfere with search and rendering.
- **Abbreviations**: You may use abbreviations in titles without providing the full name (provide the full name on first mention in the body).

## Static Asset Management

### Resource Directories
1. **Global Assets**: `docs/public/`
2. **Document-Specific Assets**: `docs/en/<module>/guides/assets/`

### Image Guidelines
- **Text-First**: Prefer text descriptions over UI screenshots.
- **Registration**: If a screenshot is absolutely necessary, it must be registered with the documentation team first.
- **English-Only**: Assets (diagrams, screenshots) should only be provided in English.

## Link Conventions

### Internal Links
Use relative paths: `[Link Name](./module/guides/xxx.mdx)`.

### Anchor Links
1. **Add Anchor**: `## Hello World {#custom_id}`
2. **Reference Anchor**: `[Section Name](./path.mdx#custom_id)`
- Use only lowercase letters, numbers, and underscores for anchor IDs.

### Component-Based Links
- **Cross-site**: Use `<ExternalSiteLink name="devops" href="/arch.html" children="Arch" />`.
- **Sub-site**: Use `<ExternalSite name="connectors" />`.

## Core Principles

### English-First
- Ensure the correctness and readability of the English version above all else.
- If multi-language support is unavailable, prioritize the English version.

### CLI-First
- Prioritize command-line operation instructions.
- Provide Web UI instructions as a supplement when applicable.

## RAG Search Optimization

AI agents use specific segmentation logic to retrieve information:
1. **Header Segmentation**: Markdown headers (`#`, `##`, `###`) are used to split documents into short chunks.
2. **Tab Segmentation**: The `<Tabs>` component is also used to create semantic blocks.
3. **Requirement**: Ensure every segment (under a header or inside a tab) has independent, searchable semantic meaning. Do not include only code blocks; always provide descriptive text.
4. **Descriptive Headers**: Titles must directly describe the paragraph content to improve recall accuracy.

## Document Types & Strategic Objectives

Every document must align with a specific type and objective. These document types map to the `category` field in frontmatter metadata.

### HowTo Documents (category: `howto`)
- **Objective**: Solve specific problems in real-world scenarios.
- **Structure**: Title (Verb-first) -> Introduction -> Scenarios -> Prerequisites -> Steps (using `<Steps />`) -> Verification.

### Function Guides (category: `feature` or `introduction`)
- **Objective**: Explain what a feature is and how it works.
- **CLI-First**: Prioritize CLI instructions.

### Concept Documents (category: `concept`)
- **Objective**: Introduce core concepts and background theories.

### Troubleshooting Documents (category: `troubleshooting`)
- **Objective**: Diagnose and resolve common issues.

## `shared` Directory Convention
The `shared` directory is for reusable components, fragments, and CRDs. Content here is **not automatically generated** as documentation pages.
