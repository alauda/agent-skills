# Verification Checklist

This document provides a checklist for verifying generated documentation against Doom framework expectations without inventing repository rules.

## Plan Consistency Check (Critical)

Before any other checks, verify that all generated or modified files match the approved plan.

- [ ] Planned create, modify, and restructure actions match the approved action type
- [ ] File paths match exactly and no silent renames were introduced
- [ ] Directory integrity matches the plan, including any required `index.mdx`
- [ ] Frontmatter fields and values match the approved plan, explicit repository rules, and built-in product documentation minimums
- [ ] Local preview prep applicability matches the repository signals that were discovered
- [ ] Any dependency files that may change during `yarn up @alauda/doom` or `yarn install` are included in planned modifications
- [ ] Review-only or audit-only requests did not produce write plans, file edits, or local preview prep commands
- [ ] Explicit `yarn build` or `yarn translate` tasks appear only when the user requested that exact command
- [ ] Explicit command tasks use the `Explicit Command Result` section instead of free-form reporting
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
- [ ] New product documentation frontmatter includes `weight` and English `queries`
- [ ] Optional fields such as `author` and `category` appear only when explicit repository rules require them

## Content Check

Refer to `rules/content-elements.md` for detailed rules.

- [ ] No redundant phrasing or repeated facts
- [ ] Recommendations specify their scope or conditions
- [ ] Exception notes appear close to the related recommendation
- [ ] Terminology is consistent
- [ ] `:::` directive density matches neighboring pages, or stays minimal when the repository shows no clear baseline; `details` is excluded from ordinary directive density
- [ ] Any explicit repository-rule override of a skill default is explicitly stated when relevant
- [ ] For documentation collaboration flows, the documentation summary includes a Local Preview Prep section and a Manual Acceptance Handoff section
- [ ] The default flow does not claim `yarn build` or `yarn translate` were run automatically
- [ ] If preview prep completed, the summary tells the human reviewer to run `yarn dev`
- [ ] If preview prep failed or was not applicable, the summary says manual preview is blocked or unavailable and does not tell the human to run `yarn dev`
- [ ] For review-only or audit-only flows, the Review Findings Report states that the run stayed read-only and did not execute preview prep commands
- [ ] Branding guidance does not conflict with explicit repository terminology, `<Term />` usage, or controlled terminology rules

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

- [ ] The target repository `AGENTS.md` was checked when it exists before applying built-in defaults
- [ ] Neighboring pages were sampled for local ordering, optional metadata, placement, and structure
- [ ] Any nontrivial MDX component usage is backed by repository examples
- [ ] Root `package.json` and Doom/Yarn signals were checked before using the standard preview prep flow
- [ ] Hardcoded brand names were avoided unless explicit repository rules or repository-approved `<Term />` usage require them

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
