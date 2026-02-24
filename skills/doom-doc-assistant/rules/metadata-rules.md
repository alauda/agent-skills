# Metadata Specification (Frontmatter)

Every `.mdx` document must contain standardized Frontmatter metadata to ensure proper navigation sorting, authorship tracking, and RAG search optimization.

## Metadata Fields

| Field | Requirement | Description |
| :--- | :--- | :--- |
| **title** | Recommended | Document title. If omitted, the first H1 heading will be used. |
| **weight** | **Mandatory** | Navigation sorting weight (integer). Lower values appear first. |
| **author** | **Mandatory** | The author's email or identifier. |
| **category** | **Mandatory** | Document type (howto, concept, function, intro, etc.). |
| **queries** | **Mandatory** | RAG search optimization keywords/phrases. |

## Configuration Example

```yaml
---
title: "Installing the Cluster"
weight: 10
author: "dev@alauda.io"
category: "installation"
queries:
  - install kubernetes cluster
  - setup control plane
---
```

## RAG Optimization with `queries`

The `queries` field helps different users find the most relevant documentation by anticipating their questions and vocabulary.

### Guidelines for `queries`:
1. **User Perspective**: Think of the specific questions a user might ask (e.g., "How to install ACP").
2. **Handle Synonyms**: Include different terms for the same concept.
   - **Example**: If "Middleware" is commonly used by users but the documentation uses "Application Service," include "Middleware" in the queries.
3. **Contextual Diversity**: Use phrases that answer "How do I...?" or "What is...?".
4. **Acronyms**: Include both acronyms and full names (e.g., "pvc" and "persistent volume claim").
5. **Quantity**: Provide approximately **3 relevant queries** per document.
6. **Unique Themes**: Ensure queries specifically cover the content of the current `.mdx` file to avoid cross-referencing confusion.

### Example:
For a document about **PVC Backup**:
```yaml
queries:
  - back up persistent volume claim
  - pvc snapshot guide
  - persistent storage data protection
```

## Weight Rules

- **Intro/Overview**: Typically `weight: 1`.
- **Quickstart**: Typically `weight: 2`.
- **General Guides**: Increments of 10 (10, 20, 30...) to allow for future insertions.
- **Troubleshooting**: Placed at the end with higher weight values.
