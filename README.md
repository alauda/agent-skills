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

## Installation

Install one skill:

```bash
npx skills add alauda/agent-skills --skill <skill-name>
```

Install the full skill bundle only if you want every skill in this repository:

```bash
npx skills add alauda/agent-skills
```

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected.

**Examples:**
- "Fix the `doom lint` errors in this branch."
- "Create child stories from the description of epic `<EPIC-KEY>`."

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

This repository includes pre-configured context files to help AI assistants quickly understand the project standards:
- [AGENTS.md](AGENTS.md): The core development manual (read this first).
- [GEMINI.md](GEMINI.md) / [CLAUDE.md](CLAUDE.md): Entry points for specific AI agents.
