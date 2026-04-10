# Verification Checklist

This document provides a checklist for verifying generated documentation against Doom framework expectations without inventing repository rules.

## Plan Consistency Check (Critical)

Before any other checks, verify that all generated or modified files match the approved plan.

- [ ] Planned create, modify, and restructure actions match the approved action type
- [ ] File paths match exactly and no silent renames were introduced
- [ ] Directory integrity matches the plan, including any required `index.mdx`
- [ ] Frontmatter fields and values match the repository-discovered contract and the approved plan
- [ ] No unplanned files were created

If any inconsistency is found:

1. Stop and report the discrepancy
2. Ask whether to correct it or revise the plan

## Format Check

Refer to `rules/markdown-formatting.md` for detailed rules.

- [ ] Bold syntax uses `**bold**` instead of unnecessary HTML
- [ ] Line breaks use `<br />` only where empty lines are impossible
- [ ] Paragraph spacing is handled with empty lines
- [ ] Period spacing is correct
- [ ] Code formatting uses backticks consistently
- [ ] Frontmatter includes only repository-supported fields for that location

## Content Check

Refer to `rules/content-elements.md` for detailed rules.

- [ ] No redundant phrasing or repeated facts
- [ ] Recommendations specify their scope or conditions
- [ ] Exception notes appear close to the related recommendation
- [ ] Terminology is consistent
- [ ] `:::` directives do not exceed 3-4 per document
- [ ] Any repository override of a skill default is explicitly stated when relevant

## Structure Check

- [ ] Related information is grouped together
- [ ] Important notes stand out appropriately
- [ ] Lists and tables have enough framing context
- [ ] Directory integrity is preserved
- [ ] The chosen path fits the current scope and does not expand a modify-only task into an unnecessary new-doc task

## Data Check

- [ ] Table data and version references are internally consistent
- [ ] No stale versions or copied values remain in prose

## Repository-Fact Check

- [ ] The target repository `AGENTS.md` was checked before applying built-in defaults
- [ ] Neighboring pages were sampled for local naming, frontmatter, and structure
- [ ] Any nontrivial MDX component usage is backed by repository examples

## Language Check

Refer to `rules/language-style.md` for detailed rules.

- [ ] Tone is objective
- [ ] Voice is active and direct
- [ ] Instructions are clear and specific
- [ ] Double negatives and filler words are avoided

## Using This Checklist

When executing self-verification in `SKILL.md`:

1. Load this file with `cat rules/verification-checklist.md`
2. Execute all checks in order:
   - Plan Consistency Check
   - Format Check
   - Content Check
   - Structure Check
   - Data Check
   - Repository-Fact Check
   - Language Check
3. Report the results in the execution summary
