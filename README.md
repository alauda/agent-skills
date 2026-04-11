# Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities, following the [Agent Skills](https://agentskills.io/) format.

## Available Skills

### doom-lint-fix

Use when `doom lint` reports any `doom-lint:*` rule errors in markdown or MDX documentation files using @alauda/doom — routes to rule-specific fix guides in the rules/ subdirectory

**Use when:**

- `doom lint` reports any `doom-lint:*` error
- You're fixing lint errors in markdown (`.md`) or MDX (`.mdx`) documentation files
- You need to understand what a doom-lint rule expects

### jira-epic-to-stories

Automatically parse JIRA epic descriptions and create child stories or jobs. Use this skill when you need to generate Jira issues from a standardized epic description.

> **Prerequisite:** This skill requires the [Jira CLI (ankitpokhrel/jira-cli)](https://github.com/ankitpokhrel/jira-cli) to be installed and authenticated on the host machine.

**Use when:**
- Generating stories from an epic key based on the epic's description.
- Parsing "Stories" or "Steps"/"Progression" from an epic to create "Story" or "Job" issues.

**Key features:**
- **Automated Issue Creation**: Interfaces with the JIRA CLI to create child issues.
- **Robust Parsing**: Handles complex formatting like ANSI escape codes and indentation.
- **Dry-run Mode**: Supports a `--dry-run` flag to preview issues before creation.

**Jira Commands (`/jira`):**
This repository also includes standalone scripts and commands in the `jira/` directory:
- `epic-to-stories.py`: A comprehensive Python script to parse an epic and automatically create stories via the Jira CLI.
- `epic-to-stories-skill.sh`: A shell script demonstrating the automation pattern for creating stories from an epic.
- `load.sh`: Helper script to load Jira-related functions or environment configurations.

### doom-doc-assistant

Repository-first assistant for Doom documentation work. It turns requirements into repository-aligned diagnosis reports, execution plans, and drafts for existing or new documentation.

**Use when:**
- Converting PRDs or requirements into user-facing documentation.
- Modifying authoritative existing pages or adding focused new scenario documents.
- Analyzing when documentation architecture should stay in place versus be restructured.
- Querying Doom framework terminology or documentation guidelines.

**Content shapes supported:**
- Overview or introduction
- Quick start
- Concept
- Feature guide
- How-to
- Troubleshooting
- Installation
- Upgrade
- Architecture

**Key features:**
- **Repository Facts First**: Target repo `AGENTS.md` and neighboring pages override skill defaults.
- **English-Only Documentation Content**: The skill may discuss plans in English or Chinese, but drafted or revised repository documentation content stays in English.
- **Fixed Output Contracts**: Diagnosis Report and Execution Plan include required sections instead of free-form summaries.
- **Example-Driven**: Leverages real codebase search for context-aware component and frontmatter choices.
- **Scope Control**: Distinguishes direct modification, focused addition, and true restructure work.

**Agent Compatibility (Empirical)**

Based on hands-on usage with various AI coding agents:

| Agent | Experience | Notes |
|-------|-----------|-------|
| **Claude Code** | ⭐⭐⭐⭐ | Optimal integration and output quality |
| **OpenCode** | ⭐⭐⭐ | Works well, but 2-3x slower than Claude Code for similar tasks |
| **Gemini CLI** | ⭐⭐ | Not recommended for this skill |

> **Note**: These observations are based on current usage as of 2026-02-25. Other agents have not been tested. If you have experience with different agents, please feel free to update this README via PR.

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
