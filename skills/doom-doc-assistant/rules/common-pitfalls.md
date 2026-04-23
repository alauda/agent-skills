# Common Pitfalls to Avoid

This document catalogs common documentation issues observed in real-world reviews (e.g., CodeRabbit AI, manual audits). **When generating content, actively avoid these pitfalls.**

## Priority 1: Must Avoid (High-Impact Issues)

### Pitfall 1: Missing Space After Period
**Issue**: Period followed immediately by capital letter.

**Bad**: `supported.If the OS...`
**Good**: `supported. If the OS...`

**Root Cause**: Careless typing or copy-paste errors.

**Prevention**: After writing any sentence ending with a period followed by a capital letter, verify there's a space.

---

### Pitfall 2: Inconsistent Feature Name Capitalization
**Issue**: Same feature name written with different capitalization within/across documents.

**Examples**:
- `Self-Built VIP` vs `Self-built VIP` vs `self-built vip`
- `Cluster Endpoint` vs `cluster endpoint`

**ACP Standard Terminology**:
| Term | Standard Form |
|------|--------------|
| Self-Built VIP feature | `Self-built VIP` (b lowercase in built) |
| Cluster Endpoint | `Cluster Endpoint` (both capitalized) |
| global cluster | `` `global` cluster `` (backticked, lowercase) |
| Platform Access Address | `Platform Access Address` (both capitalized) |
| keepalived component | `` `keepalived` `` (backticked, lowercase) |

**Prevention**:
1. When first introducing a feature name, decide the standard form
2. Use `grep` to find all occurrences and ensure consistency
3. If uncertain, check existing docs for the established pattern

---

### Pitfall 3: Ambiguous Recommendations
**Issue**: Making recommendations without specifying applicable scope, leading users to apply them incorrectly.

**Bad**: "**Recommendation**: Using a domain name is recommended."
- Problem: Users might try to apply it to Self-Built VIP (which doesn't support domains)

**Good**: "**Recommendation**: When using a hardware LoadBalancer, configuring the Cluster Endpoint with a domain name is recommended."
- Clear: The recommendation applies specifically to LoadBalancer scenarios

**Prevention**:
1. Always ask: "Does this recommendation apply universally or only in specific scenarios?"
2. If scenario-specific, lead with the condition: "When using X, ..."
3. If there are exceptions, follow immediately with a **Note**

---

### Pitfall 4: Copy-Paste Errors in Data Tables
**Issue**: Repeating values across table rows when they should differ.

**Example**:
| ACP Version | Firefox |
|-------------|---------|
| 4.2         | 141     |
| 4.1         | 138     |
| 4.0         | **144** | ← Copy-paste error; should be 134 |

**Prevention**:
1. After creating any table, review each column for logical consistency
2. Version numbers should generally follow expected progressions
3. If values look identical across non-adjacent rows, verify they're correct

---

## Priority 2: Should Avoid (Medium-Impact Issues)

### Pitfall 5: Unnecessary Hardcoded Version Numbers
**Issue**: Embedding specific version numbers in prose that will become stale.

**Bad**: "Built with `@alauda/doom` (v1.18.3)"
**Good**: "Built with `@alauda/doom`"

**Reason**: Version numbers in docs require constant updates. If the version is not essential for understanding, omit it.

**Prevention**:
1. Ask: "Is this version number essential for the user to know right now?"
2. If yes (e.g., compatibility requirements), keep it
3. If no (e.g., decorative metadata), remove it

---

### Pitfall 6: Exception Notes Separated from Recommendation
**Issue**: The limitation note appears far from the recommendation, causing users to miss it.

**Bad**:
```markdown
**Recommendation**: Using a domain name is recommended.

[... several paragraphs later ...]

**Note**: Self-Built VIP doesn't support domains.
```

**Good**:
```markdown
**Recommendation**: When using a hardware LoadBalancer, using a domain name is recommended.

**Note**: `Self-built VIP` does not support domain name configuration.
```

**Prevention**: Immediately follow any recommendation with its exception note, if applicable.

---

### Pitfall 7: Field Tells Users What, But Not Where To Get It
**Issue**: A parameter table explains what a field means but not where the real value comes from, whether it is a display name, or whether an administrator must provide it.

**Bad**: "`availabilityZone`: Availability zone"

**Good**: "`availabilityZone`: Provider-recognized API value matched against `ZoneName`. Do not use the tenant UI display name. Get the exact value from the platform administrator."

**Prevention**:
1. For every critical input field, ask: "Can a user discover the right value from this page alone?"
2. If not, add the authoritative source or link to the prerequisite checklist
3. Call out display-name versus API-value differences explicitly

---

### Pitfall 8: Cross-Workflow Constraint Updated In Only One Page
**Issue**: A prerequisite or limitation is updated on the create page but not propagated to manage, upgrade, or overview pages that rely on the same constraint.

**Bad**: `subnetName` inventory rules are documented only in cluster creation, while node-management pages still imply looser behavior.

**Good**: The authoritative page is updated and sibling workflow pages either receive synchronized updates or an explicit tracked follow-up is recorded.

**Prevention**:
1. When adding a prerequisite, field constraint, lifecycle boundary, or limitation, scan sibling workflows
2. Update all in-scope affected pages in the same change when feasible
3. If not feasible, record explicit debt instead of silently localizing the rule

---

### Pitfall 9: Engineering Truth Presented As Generic Product Guidance
**Issue**: Baseline-specific validation results, evidence IDs, or issue-tracker conclusions leak into public product docs without being translated into user-facing guidance.

**Bad**: "TC-HCS-007 is Partial due to KI-HCS-002."

**Good**: "Worker replacement can stall after instance creation because the provider may fail to parse a specific API response. Track the known issue in the provider repository."

**Prevention**:
1. Classify the document layer before drafting
2. Keep evidence bookkeeping in engineering docs
3. Translate only the stable operational conclusion into user-facing docs unless the repo explicitly wants internal traceability

---

### Pitfall 10: Code Path Exists Is Misreported As Supported
**Issue**: The doc states a path is supported simply because code or schema exists, even though it has not been formally validated or is outside the documented workflow.

**Bad**: "The provider supports automatic network creation" with no baseline or validation scope.

**Good**: "The code path exists, but it is not part of the current documented and formally validated workflow."

**Prevention**:
1. Distinguish `implemented`, `documented workflow`, `formally validated`, and `known issue`
2. For version-sensitive claims, anchor them to a baseline when writing engineering docs
3. For public docs, document only the workflow users should actually rely on

---

## Integration: Add to Self-Verification Checklist

During the `Self-Verification` workflow step, add these checks:

### Format Check (Additions)
- [ ] **Period Spacing**: No `word.Word` patterns (missing space after period)

### Content Check (Additions)
- [ ] **Terminology Consistency**: Feature names use consistent capitalization throughout
- [ ] **Recommendation Scope**: All recommendations specify applicable conditions
- [ ] **Exception Proximity**: Exception notes immediately follow related recommendations
- [ ] **Value Sources**: Critical inputs say where the real values come from
- [ ] **Cross-Workflow Propagation**: Shared constraints are updated beyond a single page when needed
- [ ] **Support Boundary**: Implemented paths are not overstated as supported or validated

### Data Check (New Category)
- [ ] **Table Data Logical**: Version numbers and values in tables follow expected patterns
- [ ] **No Stale Versions**: Unnecessary version numbers omitted from prose

---

## Mental Checklist During Writing

Before finishing any document generation, ask yourself:

1. ✅ Are all my sentences properly spaced? (Check for `Period.Capital` patterns)
2. ✅ Did I use consistent capitalization for feature names?
3. ✅ Do my recommendations clearly state when they apply?
4. ✅ Are my table data values logically consistent?
5. ✅ Did I avoid unnecessary version numbers?
6. ✅ Are exception notes right next to their recommendations?

If any answer is "no", fix it before outputting the document.
