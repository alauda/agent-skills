# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities.

Skills follow the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### doom-doc-assistant

Automatically generate product documentation that complies with Doom framework specifications. Supports requirement document transformation, architecture analysis, and multiple document types.

**Use when:**
- Converting PRD or requirements to user-facing documentation
- Generating HowTo, troubleshooting, feature, or concept documents
- Analyzing and restructuring existing documentation architecture
- Querying Doom framework terminology or documentation guidelines

**Document types supported:**
- intro - Product/module introduction
- quickstart - Quick start guide
- concept - Core concept explanation
- function - Feature description
- howto - Practical operation guide
- troubleshooting - Troubleshooting
- installation - Installation guide
- upgrade - Upgrade guide
- arch - Architecture design

**Key features:**
- Terminology consistency enforcement (prioritizing Kubernetes and OpenShift official documentation)
- Automatic retrieval and application of Doom framework MDX component specifications
- Example-driven learning via real codebase search
- Multi-stage validation (format, content, links, language)

**Categories covered:**
- Metadata rules (Frontmatter, weight, author, queries)
- Language style (objective tone, avoid slang, consistency)
- Content elements (lists, tables, directives, links, code blocks)
- Core conventions (file naming, static resources, RAG optimization)
- MDX components (Overview, Term, Directive, ExternalSiteLink)
- Terminology guide (common, AIT, ACP, ecosystem, AI terms)

## Installation

```bash
npx skills add alauda/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
```
Generate a HowTo document for database scaling based on these requirements:
[paste requirements]
```
```
Review this documentation for Doom framework compliance
```
```
Convert this PRD into a product feature document
```

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `rules/` - Modular knowledge base (domain-specific guidelines)
- `templates/` - Document templates (optional)
- `scripts/` - Helper scripts for automation (optional)

## Development

See [AGENTS.md](AGENTS.md) for best practices on developing new skills:

- Declarative over imperative
- Modular knowledge base
- Leverage native tools
- Outsource complex logic to MCP
- Linear workflows
- Example-driven learning
