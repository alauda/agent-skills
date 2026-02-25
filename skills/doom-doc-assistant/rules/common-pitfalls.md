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

## Integration: Add to Self-Verification Checklist

In **Phase 2, Step 9 (Self-Verification)**, add these checks:

### Format Check (Additions)
- [ ] **Period Spacing**: No `word.Word` patterns (missing space after period)

### Content Check (Additions)
- [ ] **Terminology Consistency**: Feature names use consistent capitalization throughout
- [ ] **Recommendation Scope**: All recommendations specify applicable conditions
- [ ] **Exception Proximity**: Exception notes immediately follow related recommendations

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
