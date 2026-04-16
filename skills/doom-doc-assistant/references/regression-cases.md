# doom-doc-assistant Regression Cases

Use these cases whenever you change the workflow, templates, or rules for `doom-doc-assistant`.

## Case 1: Modify A Healthy Authoritative Page

Prompt:

`Update the operator targeted deployment documentation in acp-docs based on this new requirement ...`

Expected assertions:

- Diagnosis Report identifies the authoritative page instead of defaulting to a new document.
- Path A is recommended.
- The report explains Path B and Path C, not just Path A.
- The plan centers on `Files to Modify`, not `Files to Create`.

## Case 1A: Assistant-Facing Output Language

Prompt:

`Help me document this Doom repo feature.`

Expected assertions:

- If the preferred assistant-facing output language is not explicit, the skill first asks whether the assistant should print in English or Chinese.
- The question makes clear this is about the assistant's reports and questions, not automatically the documentation content language.

## Case 1B: Chinese Assistant Output, English Documentation

Prompt:

`The user asks the assistant to communicate in Chinese while drafting documentation changes for the repository.`

Expected assertions:

- The assistant may print diagnosis and planning output in Chinese.
- Any generated or revised repository documentation content remains in English.
- The skill does not switch document headings or prose into Chinese.

## Case 2: Related How-To Docs Are Scattered, But Scope Stays Narrow

Prompt:

`Improve the general overview page and note any gaps in the scattered how-to guides, but do not restructure them in this round.`

Expected assertions:

- The diagnosis can mention structural debt.
- Path C remains valid when restructuring is not required to complete the current task.
- The plan does not silently expand scope to Path B.

## Case 3: New Product Doc Requires Metadata Even When Samples Are Thin

Prompt:

`Create a new HowTo page in a repo where neighboring pages only use weight and the repository has no explicit AGENTS.md.`

Expected assertions:

- The plan still requires `weight` and 2-4 English `queries`.
- The plan does not require `author` or `category`.
- The generated frontmatter uses the built-in product documentation minimum rather than copying missing metadata from legacy samples.

## Case 4: No Path Given, But Current Workspace Is The Repository

Prompt:

`Please update this documentation based on the requirement below ...`

Expected assertions:

- The skill uses the current repository when the workspace clearly contains the docs tree and `AGENTS.md`.
- It does not ask for a path before exploring.

## Case 5: Diagnosis Report Contract

Prompt:

`Analyze this requirement and tell me the best documentation path.`

Expected assertions:

- The Diagnosis Report includes `Requirement`.
- The Diagnosis Report includes `Related Documents Found`.
- The Diagnosis Report includes `Source Material Coverage`.
- The Diagnosis Report includes `All Branching Paths`.
- The Diagnosis Report includes `Recommended Path`.
- The Diagnosis Report includes `Reasoning`.
- The Diagnosis Report ends with an explicit request for confirmation.

## Case 6: Template And Category Drift

Prompt:

`Create a new overview page in a repo whose explicit metadata rules use the long-form introduction category value.`

Expected assertions:

- The skill does not output the legacy short intro category value just because `intro-template.mdx` exists.
- The skill uses the explicit category rule when present.
- The skill omits `category` when the value appears only in historical samples without an explicit repository rule.

## Case 7: New Path Uses Lowercase Underscores

Prompt:

`Create a new provider API page for Huawei DCS under docs/en/apis/providers.`

Expected assertions:

- The proposed path uses lowercase letters, numbers, and underscores only.
- The plan rejects hyphenated, uppercase, spaced, or non-ASCII new paths.
- Existing noncompliant sibling files, if any, are treated as legacy evidence rather than new naming rules.

## Case 8: New Directory Requires Index Coverage

Prompt:

`Create a new how-to under docs/en/networking/load_balancing/session_affinity.`

Expected assertions:

- The execution plan checks both the parent directory and the target directory for `index.mdx`.
- Missing `index.mdx` files are listed in the Directory Integrity Check Result.
- New `index.mdx` content is planned as H1 plus `<Overview />` unless explicit repository rules say otherwise.

## Case 9: Chinese Product Documentation Is Rejected

Prompt:

`The user asks, in Chinese, to create a Chinese product documentation page under docs/zh.`

Expected assertions:

- The assistant may explain the issue in Chinese if that is the selected assistant-facing language.
- The skill does not draft Chinese product documentation content.
- The skill asks for an English target path or English documentation goal.

## Case 10: Legacy Samples Do Not Override Product Standards

Prompt:

`Add a new page next to old pages that lack queries and use mixed naming styles.`

Expected assertions:

- The plan keeps existing files unchanged unless restructuring is approved.
- The new page still uses lowercase underscore naming.
- The new page still includes `weight` and English `queries`.

## Case 11: Directive Details Support

Prompt:

`Review this draft that uses details blocks for long optional logs and several warnings.`

Expected assertions:

- `details` is recognized as a supported directive type.
- `details` does not count toward ordinary note/tip/info/warning/danger density.
- Warnings and dangers are still reviewed against local density and relevance.

## Case 12: Modify Existing Page With Missing Queries

Prompt:

`Update this existing authoritative page with a small paragraph-level clarification.`

Expected assertions:

- The plan recommends Path A when the structure is healthy.
- The plan does not force a file rename for legacy naming.
- If the existing page lacks `queries`, the plan marks it as a follow-up or includes it only when the approved edit scope includes metadata completion.

## Case 12A: Read-Only Convention Review

Prompt:

`Review this document for Doom documentation convention compliance only. Do not modify files.`

Expected assertions:

- The skill chooses the `review/audit only` route.
- The skill outputs a Review Findings Report instead of an execution plan.
- The skill does not modify files.
- The skill does not run `yarn up @alauda/doom`, `yarn install`, `yarn dev`, `yarn build`, or `yarn translate`.
- The report asks whether the user wants a fix plan or implementation.

## Case 13: Standard Local Preview Prep And Human Handoff

Prompt:

`Update this English documentation page in a Doom/Yarn repository and prepare it for local manual acceptance.`

Expected assertions:

- After the documentation change is ready, the skill runs `yarn up @alauda/doom` and then `yarn install`.
- The skill does not automatically run `yarn dev`.
- The final summary tells the human reviewer to run `yarn dev` locally only after local preview prep completes.
- The summary does not claim `yarn build` or `yarn translate` were run by default.

## Case 14: Preview Prep Failure Blocks Manual Handoff

Prompt:

`Update the documentation, but assume the dependency update or install step fails.`

Expected assertions:

- The skill stops after the failed `yarn up @alauda/doom` or `yarn install` command.
- The skill reports the blocking error.
- The skill says manual preview is blocked or unavailable.
- The skill does not tell the human reviewer to run `yarn dev`.
- The skill does not substitute `yarn build` or `yarn translate` as fallback validation.

## Case 15: Explicit `yarn build` Request

Prompt:

`After planning the documentation update, also run yarn build for this repo.`

Expected assertions:

- The skill treats `yarn build` as an explicit separate request, not as default documentation verification.
- The command appears in an `Explicit Command Result` section.
- The result includes `Requested Command`, `Explicit Request Evidence`, `Scope`, and `Separation From Default Flow`.
- The default manual-acceptance flow still keeps `yarn dev` with the human reviewer.
- The skill does not rewrite the default summary to imply `yarn build` always belongs to documentation collaboration.

## Case 15A: Command-Only `yarn build` Request

Prompt:

`Run yarn build for this documentation repository.`

Expected assertions:

- The skill chooses the `explicit command task` route.
- The skill skips Phases 0-9 and does not output a Diagnosis Report or Execution Plan.
- The skill outputs an `Explicit Command Result` section.
- The skill stops after the explicit command result unless the user separately asks for documentation changes.

## Case 16: Explicit `yarn translate` Request

Prompt:

`After updating the English documentation, also run yarn translate for the specified glob.`

Expected assertions:

- The skill treats `yarn translate` as an explicit separate request, not as default documentation verification.
- The command appears in an `Explicit Command Result` section.
- The result includes `Requested Command`, `Explicit Request Evidence`, `Scope`, and `Separation From Default Flow`.
- The default manual-acceptance flow still avoids automatic `yarn translate` unless the user asked for it.
- The skill does not rewrite the default summary to imply `yarn translate` always belongs to documentation collaboration.

## Case 17: Standard Preview Prep Not Applicable

Prompt:

`Update the documentation in a repository that does not have the normal Doom/Yarn package signals.`

Expected assertions:

- The plan states that standard Doom/Yarn preview prep is not applicable.
- The skill does not invent substitute validation commands.
- The summary says manual preview is blocked or unavailable.
- The summary does not tell the human reviewer to run `yarn dev`.

## Case 18: Branded Terms And `<Term />`

Prompt:

`Review a draft that uses Alauda, ACP, and <Term /> in a repository that has explicit terminology examples.`

Expected assertions:

- The skill does not apply a blanket ban to all branded terms.
- The skill rejects unsafe hardcoded brand names when the repository expects replaceable `<Term />` usage.
- The skill follows explicit repository terminology rules or real `<Term />` examples.
- The skill does not invent new brand names or strip required product terminology blindly.

## ACP Validation Case: Operator Targeted Deployment

Repository:

`<workspace>/acp-docs`

Expected assertions:

- The diagnosis identifies `docs/en/extend/operator.mdx` as the authoritative entry point.
- Path A is recommended.
- The diagnosis does not confuse ingress-related examples with the operator's own core capability.
- If the current workspace is already this repository, the skill does not pause to ask for the path again.

## Static Consistency Checks

After any refactor, run repository-local searches to confirm:

- no rule claims a single legacy naming style is the only allowed style everywhere
- no rule turns optional `author` or `category` fields into required fields
- no template frontmatter still outputs legacy template-name-derived category values
- no file references the old nonexistent architecture template filename
- no product documentation rule recommends hyphenated, uppercase, spaced, or non-ASCII new paths
- all new document templates include `weight` and English `queries`
- directive rules include `details` and exclude it from ordinary density counts
- the skill rules mention `yarn up @alauda/doom`, `yarn install`, and `yarn dev` for the default manual-acceptance flow
- the default skill flow does not describe `yarn build` or `yarn translate` as automatic steps
- review-only or audit-only routes do not include file edits or local preview prep commands
- explicit `yarn build` and `yarn translate` requests are represented as separate command tasks
- explicit command tasks use the `Explicit Command Result` section
- branding rules allow repository-approved `<Term />` or explicit terminology patterns while preventing unsafe hardcoded brand defaults
