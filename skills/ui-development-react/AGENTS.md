# ui-development-react — Skill Development Conventions

This file governs development of the `ui-development-react` skill specifically. It extends the root `AGENTS.md` with patterns specific to **design system skills**.

---

## Skill Archetype: Design System / Tool Invocation

This skill provides design tokens and validation tools for the Alauda Container Platform (ACP) UI. The AI's job is to provide consistent design guidance, generate token files, and validate design implementations.

**Core principle**: Design tokens are the source of truth. Teach the AI to reference token files rather than memorizing color values or spacing scales.

---

## Directory Structure

```text
ui-development-react/
├── SKILL.md          # Main instruction file
├── AGENTS.md         # ← This file
├── references/       # Detailed design documentation
│   ├── accessibility.md
│   ├── dark-mode.md
│   ├── design-patterns.md
│   ├── design-tokens.md
│   └── guidelines.md
├── docs/             # Quick-start guides and FAQs
│   ├── best-practices.md
│   ├── faq.md
│   ├── quick-start.md
│   ├── token-usage.md
│   └── visual-identity.md
├── scripts/          # Python tools for token conversion and validation
│   ├── design-tokens-converter.py
│   └── design-validator.py
└── tokens/           # Actual token files in various formats
    ├── colors.module.css
    ├── design-tokens.css
    ├── design-tokens.json
    ├── design-tokens.ts
    └── tailwind.config.js
```

### tokens/ usage

The `tokens/` directory contains the **actual design token values** that AI should reference when generating UI code. These are source-truth files that should be read directly, not copied into SKILL.md.

**When AI needs color values**: Read from `tokens/design-tokens.json` or `tokens/design-tokens.ts`

**When AI needs spacing values**: Read from the spacing scale in token files

**When AI needs typography**: Read from the typography definitions

### scripts/ usage

The `scripts/` directory contains Python tools for:
- Converting tokens between formats
- Validating UI implementations against the design system

**Rules for script usage**:
- Always use Python 3
- Scripts are optional helper tools, not required for basic token usage
- Document script dependencies in each script's docstring

---

## The Reference-First Pattern

For design system skills, **reference documentation is primary**.

**❌ Wrong**: Embedding all color values in SKILL.md as static text

**✅ Right**: Instructing the AI: "When you need color values, read `tokens/design-tokens.json` and extract the relevant semantic color"

Why this is better:
- Token files are single source of truth
- Updates to tokens automatically propagate
- SKILL.md stays concise and focused on workflow

---

## Workflow Design Principles

### Token lookup before hardcoding

The AI must always reference token files before using design values in generated code.

### Format-specific guidance

Different projects use different token formats. The AI should:
1. Ask which framework/format the user is using
2. Recommend the appropriate token file from `tokens/`
3. Provide implementation examples for that format

### Validation as optional enhancement

Design validation is helpful but not required. The AI should offer validation but not block progress if the user declines.

---

## When to Update tokens/ vs. SKILL.md

| Change needed | Update |
|--------------|--------|
| New color added | `tokens/design-tokens.*` files (all formats) |
| Spacing scale changed | `tokens/design-tokens.*` files |
| New framework support | New file in `tokens/` + mention in SKILL.md |
| Workflow step changed | `SKILL.md` |
| New reference doc | New file in `references/` + pointer in SKILL.md |

---

## What NOT to Do

- **Don't embed token values in SKILL.md**. Token files are the source of truth.
- **Don't hardcode color hex values** in generated code. Always reference tokens.
- **Don't ignore dark mode**. Always provide both light and dark mode variants.
- **Don't skip accessibility**. All color combinations must meet WCAG AA.
- **Don't override tokens without discussion**. If a user wants a custom value, discuss design system implications first.
