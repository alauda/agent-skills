# Specification Review Report Template

Use this template when performing specification review during Path B restructuring work.

## Template

```markdown
## Specification Review Report

### `:::` Directive Check
- **Current Count**: X
- **Standard Limit**: 3-4
- **Status**: Compliant / Exceeds Limit

| Line | Type | Summary | Priority | Recommendation |
|------|------|---------|----------|----------------|
| ...  | ...  | ...     | ...      | ...            |

### Other Checks
- [ ] Terminology Consistency: Pass / Fail [Specific issue]
- [ ] Link Correctness: Pass / Fail [Specific issue]
- [ ] Language Style: Pass / Fail [Specific issue]
- [ ] Repository Frontmatter Contract: Pass / Fail [Only check fields required by the target repo]
- [ ] MDX Components: Pass / Fail [Specific issue]

## Recommendations
[List specific modification suggestions]

## Repository Overrides
[List any repository facts that override the skill defaults, or `None`]

Should I apply the above changes? Please confirm.
```

## Directive Priority Reference

When streamlining directives that exceed the limit, use this priority order:

1. DANGER
2. WARNING
3. TIP
4. INFO
5. NOTE

## Compliance Check Reference

Load rules explicitly with `cat` before checking:

- `rules/common-pitfalls.md`
- `rules/terminology-guide.md`
- `rules/language-style.md`
- `rules/mdx-components.md`

Verify only the frontmatter fields required by the target repository and neighboring pages.
