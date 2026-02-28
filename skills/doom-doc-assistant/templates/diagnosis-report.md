# Diagnosis Report Template

Use this template when outputting Phase 0 (Intake & Diagnosis) results in SKILL.md.

## Template

```markdown
## 🔍 Diagnosis Report

**Requirement**: [User's description]

**Related Documents Found**:
| Document | Relevance | Quality Assessment |
|----------|-----------|--------------------|
| ...      | High/Med/Low | Structurally sound / Needs restructuring / Poor quality |

**Source Material Coverage**:
Analyze what content is available vs missing in the provided source material.
| Content Area | Available | Missing | Notes |
|--------------|-----------|---------|-------|
| [e.g., Installation] | ✅ / ❌ | | If missing, note how it will be handled |
| [e.g., Cluster Creation] | ✅ / ❌ | | |

**Recommended Path**:
- Path A / Path B / Path C (see below)

**Reasoning**: [Why this path is recommended based on the findings]

---

Please confirm the above findings, or let me know of any related documents I may have missed.
After your confirmation, tell me which path you'd like to take.
```

## Branching Paths Reference

**Path A: Existing docs are in good shape → Create new document directly**
- Proceed to Phase 1 to plan the new document's location, type, and outline.

**Path B: Existing docs need restructuring → Restructure first, then write**
- Proceed to Phase 1 to plan the restructuring, then Phase 2 to plan the new document.

**Path C: Existing docs need restructuring, but skip it this time → Create new document only**
- Proceed to Phase 1 to plan the new document only.
- Output the following reminder before continuing:

```markdown
⚠️ Technical Debt Notice:
[Brief description of the structural issues identified, without file paths.]
Recommend tracking this in Jira for a future iteration.
```

## Important Notes

- **⚠️ CRITICAL**: When source material is incomplete, explicitly identify gaps and propose how to handle them (e.g., reference existing patterns, mark as placeholder, ask user for additional information). This sets clear expectations before proceeding.

- **Feedback Loop**:
  - User confirms findings → Proceed to the user's chosen path
  - User provides feedback/corrections → Re-process Phase 0 with the feedback and re-output the diagnosis report. Do NOT proceed to Phase 1 until the user confirms.
