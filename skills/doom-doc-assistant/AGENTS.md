# doom-doc-assistant — Skill Development Conventions

This file governs development of the `doom-doc-assistant` skill specifically. It extends the root `AGENTS.md` with patterns specific to **content generation skills**.

---

## Skill Archetype: Content Generation

This skill produces written documentation for the [Doom](https://github.com/alauda/doom) documentation framework. The AI's job is to author Markdown/MDX that fits seamlessly into an existing codebase — matching tone, component usage, and structural conventions already present.

**Core principle**: Never hardcode style rules as static text. The codebase itself is the source of truth. Teach the AI to *discover* conventions at runtime rather than memorize them at authoring time.

---

## Directory Structure

```text
doom-doc-assistant/
├── SKILL.md
├── AGENTS.md              # ← This file
├── rules/
│   ├── style-guide.md     # Tone, voice, writing principles
│   ├── terminology.md     # Preferred terms and their banned equivalents
│   └── dos-and-donts.md   # Common mistakes to avoid
└── templates/
    ├── concept.mdx        # Template for concept/overview pages
    ├── how-to.mdx         # Template for procedural guides
    └── reference.mdx      # Template for API/config reference pages
```

### rules/ usage

`rules/` files contain **modular knowledge** the AI loads selectively. Do not dump all rules into `SKILL.md` — it causes instruction overload. Instead, use pointers in `SKILL.md`:

> "Before writing, read `rules/style-guide.md` to retrieve tone specifications."

Keep each rules file focused on a single concern. If a file exceeds ~150 lines, split it.

### templates/ usage

Templates provide structural scaffolding. The AI fills in content, but the skeleton (frontmatter fields, section headings, component slots) comes from the template. Update templates when the doc site's page structure changes — don't update `SKILL.md`.

---

## The RAG Pattern: Prefer Discovery Over Memorization

The most important pattern in this skill is **runtime discovery over static rules**.

**❌ Wrong**: Documenting in `rules/` that "the Tabs component should be used like this: `<Tabs items={[...]}>...`"

**✅ Right**: Instructing the AI in `SKILL.md`: "When you need to use a component, search the repository with `grep -r '<ComponentName' docs/ --include='*.mdx' -l | head -5` and read 2–3 real examples before writing."

Why this is better:
- Components evolve. Static rules go stale. Real usage never lies.
- The AI learns the actual pattern in context, not an idealized version.
- No maintenance burden when the codebase changes.

Apply this pattern for: component usage, frontmatter field conventions, link formats, image paths, and any other structural element that appears repeatedly in the codebase.

---

## Workflow Design Principles

### Mandatory self-inspection before body content

The AI must output Frontmatter and section headings for the user to review **before** writing body content. This prevents wasted effort if the structure is wrong.

### Iterative drafting, not one-shot generation

Structure the workflow as: outline → section by section → review. Never instruct "write the complete document." Long one-shot generations are hard to correct and waste context.

### Explicit "done" criteria

Each workflow step should end with a question or check: "Does this structure match what you intended? Confirm before I write the body." The AI should not proceed silently.

---

## When to Update rules/ vs. SKILL.md

| Change needed | Update |
|--------------|--------|
| Tone or voice changed | `rules/style-guide.md` |
| New banned/preferred term | `rules/terminology.md` |
| New page type added to the site | New template in `templates/` + pointer in `SKILL.md` |
| Workflow step added or reordered | `SKILL.md` |
| A component is deprecated | `rules/dos-and-donts.md` (add to "don't" list) |

---

## What NOT to Do

- **Don't use MCP** for this skill's primary workflow. The data the AI needs (existing docs, templates, rules) is all on the filesystem. MCP adds complexity with no benefit here.
- **Don't write parsing scripts for general content**. If content needs to be extracted from existing files, instruct the AI to read and reason over them directly.
- **Don't put domain knowledge in SKILL.md**. Tone guidance, terminology, component syntax — all of that belongs in `rules/`. `SKILL.md` is a workflow orchestrator, not an encyclopedia.
