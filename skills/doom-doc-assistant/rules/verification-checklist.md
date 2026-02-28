# Verification Checklist

This document provides a comprehensive checklist for verifying generated documentation against Doom framework specifications.

## Plan Consistency Check (⚠️ CRITICAL)

**Before any other checks, verify that all generated/modified files match the approved plan.**

- [ ] **All planned files were created** — Compare actual files created vs. "Files to Create" table
- [ ] **Weight values match exactly** — Each file's weight must match the approved plan
- [ ] **File paths match exactly** — No deviation from planned directory structure
- [ ] **Metadata fields match** — author, category match the approved plan
- [ ] **No unplanned files** — No extra files created beyond the plan

**If any inconsistency is found:**
1. Stop and report the discrepancy
2. Ask user whether to:
   - Proceed with correction (fix the inconsistency)
   - Revise the plan (if the change was intentional)

---

## Format Check

Refer to `rules/markdown-formatting.md` for detailed rules.

- [ ] **Bold Syntax**: Used `**bold**` instead of `<b>` tags (except in MDX JSX props)
- [ ] **Line Breaks**: Used `<br />` only in table cells or where empty lines are impossible
- [ ] **Paragraph Spacing**: Used empty lines to separate paragraphs in normal text
- [ ] **Period Spacing**: No `word.Word` patterns (missing space after period)
- [ ] **No Redundant HTML**: No HTML tags where Markdown syntax works
- [ ] **Code Formatting**: Proper use of backticks for parameters, features, and technical terms
- [ ] **Frontmatter**: Complete metadata (weight, author, category, queries)

---

## Content Check

Refer to `rules/content-elements.md` for detailed rules.

- [ ] **No Redundancy**: Removed "if you need to..." when context is clear
- [ ] **No Implementation Details**: Removed unnecessary internal details users don't need
- [ ] **Information Layering**: Content follows Recommendation → Reason → Note structure
- [ ] **Single Source**: Each piece of information appears only once in the most appropriate location
- [ ] **Consistent Terminology**: Feature names use consistent capitalization throughout (e.g., `Self-built VIP` not `Self-Built VIP`)
- [ ] **Recommendation Scope**: All recommendations specify applicable conditions (e.g., "When using X, ...")
- [ ] **Exception Proximity**: Exception notes immediately follow related recommendations
- [ ] **Directive Count**: `:::` directives do not exceed 3-4 per document

---

## Structure Check

- [ ] **Related Information Grouped**: Related content is grouped together
- [ ] **Important Notes Stand Out**: Critical information has proper spacing and emphasis
- [ ] **Lists Have Context**: Lists are introduced with explanatory text
- [ ] **Tables Are Readable**: Complex tables are split or well-structured
- [ ] **Directory Integrity**: Every directory with `.mdx` files or subdirectories has `index.mdx` (see `rules/core-conventions.md`)

---

## Data Check

- [ ] **Table Data Logical**: Version numbers and values in tables follow expected patterns (no copy-paste errors)
- [ ] **No Stale Versions**: Unnecessary version numbers omitted from prose

---

## Language Check

Refer to `rules/language-style.md` for detailed rules.

- [ ] **Objective Tone**: No marketing fluff or emotional language
- [ ] **Active Voice**: "The system creates" not "A creation is made by..."
- [ ] **Direct Instructions**: "Enter the value" not "You should enter the value"
- [ ] **No Double Negatives**: Positive assertions for clarity
- [ ] **No Filler Words**: Removed "basically", "essentially", etc.

---

## Using This Checklist

When executing Phase 2.7 (Self-Verification) in SKILL.md:

1. Load this file: `cat rules/verification-checklist.md`
2. Execute all checks in order:
   - Plan Consistency Check (first, mandatory)
   - Format Check
   - Content Check
   - Structure Check
   - Data Check
   - Language Check
3. Report results in the specified output format
