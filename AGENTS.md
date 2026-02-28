# Agent Skills Development Manual

This repository contains **Agent Skills** — modular behavioral instruction sets for AI agents. Each skill teaches an AI how to complete a specific, repeatable task.

> **Mindset shift**: You are not writing traditional program code. You are authoring a **behavioral manual for another AI**. The agent reading your skill will use its own reasoning and tools to execute the workflow — your job is to guide it clearly, not control every line.

---

## Repository Structure

```text
agent-skills/
├── AGENTS.md                   # ← This file. Universal conventions for all skills.
└── skills/
    ├── doom-doc-assistant/
    │   ├── AGENTS.md           # Skill-local conventions (content generation patterns)
    │   └── SKILL.md
    └── k8s-yaml-validator/
        ├── AGENTS.md           # Skill-local conventions (tool-invocation patterns)
        └── SKILL.md
```

**Rule**: Root `AGENTS.md` defines what is true for **every** skill. Skill-local `AGENTS.md` defines what is true for **that skill type only**. When they conflict, skill-local wins.

---

## Universal Directory Layout

Every skill must follow this structure:

```text
skills/<skill-name>/
├── SKILL.md          # Required. Frontmatter + workflow instructions.
├── AGENTS.md         # Required. Skill-local development conventions.
├── scripts/          # Optional. Helper scripts the AI can execute.
├── references/       # Optional. Reference docs loaded into context on demand.
├── rules/            # Optional. Modular knowledge (style guides, terminology, etc.)
└── templates/        # Optional. Output templates.
```

Not every directory is needed — only create what the skill actually uses.

---

## SKILL.md Requirements (All Skills)

Every `SKILL.md` must have:

```yaml
---
name: skill-name          # Lowercase, hyphenated. Matches the directory name.
description: |            # One paragraph. Covers: what it does AND when to trigger.
  ...
---
```

The `description` field is the primary trigger mechanism — the AI decides whether to use this skill based on it alone. Write it to be specific enough to trigger correctly and broad enough not to miss valid use cases.

**Body guidelines:**
- Keep under 500 lines. If longer, split content into `references/` and use pointers.
- Define the workflow as a numbered linear sequence.
- Include explicit stop/validate conditions between steps where failures can cascade.
- End each major step with a clear success criterion the AI can self-check.

---

## Two Skill Archetypes

Skills in this repo fall into two patterns. Each has its own best practices — see the skill-local `AGENTS.md` for details.

### Content Generation Skills
*Example: `doom-doc-assistant`*

The AI produces written artifacts (docs, reports, copy). Quality depends on style consistency, context understanding, and iterative refinement. Key patterns: RAG over existing content, modular `rules/` files, iterative drafting.

### Tool Invocation Skills
*Example: `k8s-yaml-validator`*

The AI orchestrates external tools (CLI utilities, scripts, APIs) and interprets their output. Quality depends on correct tool usage, version handling, and structured reporting. Key patterns: setup scripts, staged validation, deterministic output parsing.

---

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Skill directory | lowercase, hyphenated | `k8s-yaml-validator` |
| `name` frontmatter | same as directory | `k8s-yaml-validator` |
| Script files | lowercase, underscored | `yaml_check.py` |
| Reference files | lowercase, hyphenated | `crd-schemas.md` |
| All files | English only | — |

---

## Adding a New Skill

1. Create `skills/<skill-name>/` directory.
2. Identify which archetype it is (content generation or tool invocation).
3. Copy the `AGENTS.md` from the closest existing skill as a starting point.
4. Write `SKILL.md` following the requirements above.
5. Test by simulating 3–5 representative user requests and verifying the AI activates the skill and produces correct output.

---

## What Belongs Here vs. in Skill-Local AGENTS.md

| Topic | Root AGENTS.md | Skill-local AGENTS.md |
|-------|---------------|----------------------|
| Directory structure | ✅ | — |
| Naming conventions | ✅ | — |
| SKILL.md frontmatter format | ✅ | — |
| Skill archetype philosophy | ✅ (overview) | ✅ (detailed patterns) |
| RAG / grep strategies | — | ✅ |
| Tool installation & versioning | — | ✅ |
| Output format specifications | — | ✅ |
| Domain-specific rules | — | ✅ |
