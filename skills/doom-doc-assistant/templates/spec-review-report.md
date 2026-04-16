# Specification Review Report Template

Use this template when performing specification review during Path B restructuring work.

## Template

```markdown
## Specification Review Report

### `:::` Directive Check
- **Current Count**: X, excluding `details`
- **Observed Local Pattern**: [What neighboring pages do, or `No clear baseline`]
- **Status**: Matches local pattern / Needs streamlining

| Line | Type | Summary | Priority | Recommendation |
|------|------|---------|----------|----------------|
| ...  | ...  | ...     | ...      | ...            |

### Other Checks
- [ ] Terminology Consistency: Pass / Fail [Specific issue]
- [ ] Link Correctness: Pass / Fail [Specific issue]
- [ ] Language Style: Pass / Fail [Specific issue]
- [ ] Metadata Contract: Pass / Fail [Check explicit repository rules and built-in product documentation minimums]
- [ ] MDX Components: Pass / Fail [Specific issue]

## Recommendations
[List specific modification suggestions]

## Repository Overrides
[List any explicit repository rules that override the skill defaults, or `None`]

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
- `rules/metadata-rules.md`
- `rules/mdx-components.md`

Verify the frontmatter fields required by explicit repository rules and built-in product documentation minimums.
For directive density, compare with neighboring pages first. If no local baseline is clear, prefer minimal directives and fold routine notes back into prose.
Exclude `details` from ordinary note/tip/info/warning/danger density counts.
