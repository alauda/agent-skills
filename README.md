# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities, following the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### doom-doc-assistant

Automatically generate product documentation that complies with the Doom framework specifications. Supports requirement document transformation, architecture analysis, and multi-type document generation.

**Use when:**
- Converting PRDs or requirements into user-facing documentation.
- Generating HowTo, troubleshooting, feature, or concept documents.
- Analyzing and restructuring existing documentation architecture.
- Querying Doom framework terminology or documentation guidelines.

**Document types supported:**
- **intro**: Product/module introduction.
- **quickstart**: Quick start guide.
- **concept**: Core concept explanation.
- **function**: Feature description.
- **howto**: Practical operation guide.
- **troubleshooting**: Troubleshooting guide.
- **installation**: Installation guide.
- **upgrade**: Upgrade guide.
- **arch**: Architecture design.

**Key features:**
- **Terminology Consistency**: Prioritizes Kubernetes and OpenShift official documentation standards.
- **Component Automation**: Automatic retrieval and application of Doom framework MDX component specs.
- **Example-Driven**: Leverages real codebase search for context-aware generation.
- **Multi-Stage Validation**: Checks for format, content, links, and language style.

## Installation

```bash
npx skills add alauda/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
- "Generate a HowTo document for database scaling based on these requirements: [paste requirements]"
- "Review this documentation for Doom framework compliance."
- "Convert this PRD into a product feature document."

## Skill Structure

Each skill follows a modular structure:
- `SKILL.md`: Core instructions for the agent.
- `rules/`: Modular knowledge base (domain-specific guidelines).
- `templates/`: Document templates for standardized scaffolding.
- `scripts/`: (Optional) Helper scripts for automation.

## Development

This project follows the **Agentic Mindset**—writing declarative, modular instructions that empower AI agents to use their native tools.

See [AGENTS.md](AGENTS.md) for the **Supreme Guiding Directive** on developing new skills:
- **Declarative over Imperative**: Trust the AI's reasoning.
- **Modular Knowledge**: Keep instructions lean by using the `rules/` directory.
- **Leverage Native Tools**: Encourage the use of `grep`, `ls`, and `read_file`.
- **Example-Driven (RAG)**: Use real-world code examples as the primary learning source.

## Project Context for AI Assistants

This repository includes pre-configured context files to help AI assistants (like Gemini CLI or Claude Code) quickly understand the project standards:
- [AGENTS.md](AGENTS.md): The core development manual (read this first).
- [GEMINI.md](GEMINI.md) / [CLAUDE.md](CLAUDE.md): Entry points for specific AI agents.
