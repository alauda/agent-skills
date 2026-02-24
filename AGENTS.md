# Agent Skill Development Manual (AGENTS.md)

This document serves as the **Supreme Guiding Directive** for developing skills within this repository. When undertaking a development task, you must undergo a **"Mindset Shift"**: You are not writing traditional program code; you are authoring a **highly modular behavioral manual** for another AI.

---

## 1. Core Philosophy: The Agentic Mindset

### Declarative over Imperative
* **❌ The Wrong Way (Traditional Thinking)**: Writing complex Python or Node scripts to hardcode logic for parsing YAML, reading Markdown, and concatenating strings into a prompt.
* **✅ The Right Way (Agentic Thinking)**: In `SKILL.md`, use clear natural language to instruct the execution-phase AI: "Use your file-reading tool to examine `config.yaml` and extract the template configuration." **Trust the AI's innate reasoning and tool-use capabilities.**

### Embrace Modular Knowledge
* Avoid stuffing thousands of words of specifications into a single `SKILL.md`. This causes instruction confusion and consumes excessive tokens.
* Split independent knowledge points (e.g., tone guides, component syntax, terminology tables) into separate Markdown files within the `rules/` directory. Use pointers in your workflow: "Before writing, **you must first read** `rules/style-guide.md` to retrieve tone specifications."

### Leverage Native Tools & RAG (Example-Driven Learning)
* The AI executing the skill possesses powerful terminal execution, file reading, and global search tools.
* **Don't hardcode rules**: Instruct the future AI: "When you want to use the Tabs component, use your search tool to run `grep -r "<Tabs" .` in the repository to find the 3 most recent real-world examples and mimic them." This RAG-based approach is far more robust than static rules.

---

## 2. Standard Directory Structure

Every Skill must strictly adhere to the following layout to ensure predictability and tool compatibility:

```text
skills/<skill-name>/
├── SKILL.md          # Core Instruction File: Defines "When to use", "Workflow", and "Core Principles"
├── rules/            # Modular Knowledge Base: Specific guidelines, terminology, and "Dos/Don'ts"
├── templates/        # Content Templates: Markdown/MDX templates for generation
└── scripts/          # (Optional) Helper Scripts: Automated tasks for the AI to execute
```

---

## 3. Golden Rules for Writing `SKILL.md`

### Linear Workflows
* Define procedures using ordered lists (1, 2, 3...) to establish clear precedence.
* **Mandatory Validation Steps**: Require the AI to confirm the success of the previous step before proceeding. For example: "Before generating the body content, you must output the Frontmatter metadata for self-inspection."

### Outsource Complex Logic to MCP (Model Context Protocol)
* If a task is too complex for an LLM (e.g., querying an internal database or precise scoring across millions of rows).
* **Never write intermediate parsing scripts.** Instead, develop a lightweight server compliant with the **Model Context Protocol (MCP)** and expose that capability as a Tool for the AI.

---

## 4. Key Commands & Operations

* **Add a New Skill**: `npx skills add <source>`
* **Development Reference**: Use the `skills/doom-doc-assistant` directory as the gold standard for implementation.
* **Verification**: Simulate user requirements and observe if the AI activates based on the `SKILL.md` triggers and accurately references the rules in `rules/`.

---

## 5. Contribution Guidelines

1. **Naming Conventions**: Use English for all file and directory names.
2. **Metadata**: Ensure `SKILL.md` includes clear `name` and `description` Frontmatter.
3. **AI Guiding AI**: Always maintain the perspective of "AI guiding AI." You are writing a "Strategy Guide," not a "Device Driver."
