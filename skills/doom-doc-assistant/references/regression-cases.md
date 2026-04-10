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

`请用中文和我沟通，但帮我起草这个仓库里的文档改动。`

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

## Case 3: Repository Does Not Use `author/category/queries`

Prompt:

`Create or update a page in a repo where neighboring pages only use weight, with optional title.`

Expected assertions:

- The plan does not require `author`, `category`, or `queries`.
- The generated frontmatter follows the local minimum contract.

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

`Create a new overview page in a repo whose sibling pages use the long-form introduction category value.`

Expected assertions:

- The skill does not output the legacy short intro category value just because `intro-template.mdx` exists.
- The skill reuses the category value found in the repository, or omits `category` if the repo does not use it.

## ACP Validation Case: Operator Targeted Deployment

Repository:

`/Users/changjia/acp-docs`

Expected assertions:

- The diagnosis identifies `docs/en/extend/operator.mdx` as the authoritative entry point.
- Path A is recommended.
- The diagnosis does not confuse ingress-related examples with the operator's own core capability.

## Static Consistency Checks

After any refactor, run repository-local searches to confirm:

- no rule claims a single legacy naming style is the only allowed style everywhere
- no rule still marks `author`, `category`, and `queries` as unconditionally mandatory
- no template frontmatter still outputs legacy template-name-derived category values
- no file references the old nonexistent architecture template filename
