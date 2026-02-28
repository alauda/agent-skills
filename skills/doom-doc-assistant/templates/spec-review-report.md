# Specification Review Report Template

Use this template when performing specification review during Phase 2.1 (Restructure Existing Documents) in SKILL.md.

## Template

```markdown
## 🔍 Specification Review Report

### `:::` Directive Check
- **Current Count**: X
- **Standard Limit**: 3-4
- **Status**: ✅ Compliant / ❌ Exceeds Limit

[If exceeded, list details]
| Line | Type | Summary | Priority | Recommendation |
|------|------|---------|----------|----------------|
| ...  | ...  | ...     | ...      | ...            |

### Other Checks
- [ ] Terminology Consistency: ✅ / ❌ [Specific issue]
- [ ] Link Correctness: ✅ / ❌ [Specific issue]
- [ ] Language Style: ✅ / ❌ [Specific issue]
- [ ] Frontmatter: ✅ / ❌ [Specific issue]
- [ ] MDX Component: ✅ / ❌ [Specific issue]

## 💡 Recommendations
[List specific modification suggestions]

---
Should I apply the above changes? Please confirm.
```

## Directive Priority Reference

When streamlining directives that exceed the limit, use this priority order:

1. **DANGER** — Keep (highest priority)
2. **WARNING** — Keep
3. **TIP** — Consider removing
4. **INFO** — Consider removing
5. **NOTE** — Remove first (lowest priority)

## Compliance Check Reference

Load rules explicitly with `cat` before checking:

- [ ] **Common Pitfalls**: Check `rules/common-pitfalls.md` — period spacing, terminology consistency, ambiguous recommendations, table data errors.
- [ ] **Terminology Consistency**: Check against `rules/terminology-guide.md`.
- [ ] **Link Correctness**: Verify internal links, anchor links, and external link components.
- [ ] **Language Style**: Check against `rules/language-style.md`.
- [ ] **Frontmatter Completeness**: Verify weight, author, category, queries, etc.
- [ ] **MDX Component Usage**: Check syntax against `rules/mdx-components.md`.

## Branching Logic

- **User Confirms**: Apply the changes.
- **User Rejects / Partial Adoption**: Respect the decision and proceed accordingly.
- **User Provides New Feedback**: Return to Phase 2.1 for re-analysis.
