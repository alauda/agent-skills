# Diagnosis Report Template

Use this template when outputting Phase 0 (Intake & Diagnosis) results in `SKILL.md`.

## Template

```markdown
## Diagnosis Report

**Requirement**: [User's description]

**Related Documents Found**:
| Document | Role | Relevance | Quality Assessment |
|----------|------|-----------|--------------------|
| ...      | Authoritative / Supporting / Adjacent | High / Medium / Low | Structurally sound / Needs restructuring / Poor quality |

**Source Material Coverage**:
| Content Area | Evidence Found | Coverage | Gaps And Handling |
|--------------|----------------|----------|-------------------|
| ...          | [Page names or examples] | Full / Partial / Missing | [How gaps will be handled] |

**All Branching Paths**:
- **Path A**: [Explain the direct-modify or focused-add option in this repository]
- **Path B**: [Explain the restructure-first option in this repository]
- **Path C**: [Explain the narrow-scope-with-technical-debt option in this repository]

**Recommended Path**: Path A / Path B / Path C

**Reasoning**:
- [Why the recommended path fits the repository evidence]
- [Why the non-selected paths are not the best choice for this round]

Please confirm the findings above.
If I missed a related document, tell me which one.
After that, tell me whether you want Path A, Path B, or Path C.
```

## Branching Paths Reference

**Path A: Structure is healthy enough to proceed directly**

- Use this when the task can be solved by modifying the authoritative existing page and/or adding a focused new document within the current structure.

**Path B: Restructure first, then write**

- Use this when the current information architecture would make the result wrong, misleading, or unmaintainable unless it is restructured first.

**Path C: Structural issues exist, but do not expand scope this round**

- Use this when restructuring is desirable but not required to complete the current task safely.
- Record the debt and continue with the narrowest viable scope.

If Path C is chosen, output this reminder before continuing:

```markdown
Technical Debt Notice:
[Brief description of the structural issues identified.]
Recommend tracking this for a future iteration.
```

## Important Notes

- When source material is incomplete, explicitly identify gaps and propose how to handle them.
- The report is incomplete if it only outputs the recommended path. Path A, Path B, and Path C must all be explained.
- Path A must be allowed for both "modify authoritative existing doc" and "add focused new doc" scenarios.
- If explicit repository rules override the skill defaults, say so explicitly in the reasoning.
