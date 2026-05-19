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

### Pitfall 9a: Internal Bookkeeping Strings Copied Into Customer-Facing Docs

**Issue**: When the source material handed to this skill is an internal ticket description, test report, or PR body, that material contains internal-bookkeeping strings that must not appear in customer-facing product docs. The skill must extract the **user-facing outcome** and discard the bookkeeping before drafting.

**Concrete strings to detect and strip** before any text reaches a customer-facing page (`docs/en/...` in product doc repositories such as `immutable-infra-docs`, `acp-docs`, and equivalents):

| Category | Examples | What goes in the customer doc instead |
|---|---|---|
| Issue tracker IDs | `AIT-70656`, `DBS-142`, `DEVOPS-12345`, `MIDDLEWARE-30911` | Describe the user-observable behavior; if a fix version matters, name the released version. |
| Internal test dates | `Verified 2026-05-19 in the release test`, `Validated 2026-05-12 against a live test environment`, any `YYYY-MM-DD` paired with `verified`/`validated`/`on hcslab`/`in the AIT-XXXXX release test` | Describe the steady-state behavior. Customers should not see when QA last ran a check. |
| Internal decision rationale (Path A/B/C, alternative analysis) | "Pick one of three paths: A — rolling replacement … B — node-level manual fix … C — DaemonSet that mutates the host." | Document only the supported path. Move the rejected paths into engineering decision records, not the customer page. |
| Internal validation markers | `Verified in release test`, `RUS-T3b 2026-05-19`, `KI-HCS-002`, `TC-HCS-007`, baseline names like `hcslab`, internal commit shas | If a behavior is supported, state it. If it is not supported, state the unsupported behavior without citing the test ID. |
| Internal repo / branch / build artifact references | `gitlab-ce.alauda.cn`, `build-harbor.alauda.cn`, `package-minio.alauda.cn`, `BuildRun cluster-api-provider-hcs-lbdhc`, `MR !14`, `MR !311` | Reference customer-visible installable units (released plugin version, image tags published in the release notes). |

**Bad** (excerpt from a customer-facing upgrade page):

```
B — Node-level manual fix … Does not persist on MicroOS / SLE Micro. Verified 2026-05-19 in the AIT-70656 release test on hcslab: the controller's fix sets cloud-init manage_etc_hosts: true …
```

**Good** (same intent, customer-facing prose):

```
Manual edits to /etc/hostname and /etc/hosts on an existing MicroOS / SLE Micro node do not persist. Cloud-init re-renders these files on every boot, including reboots triggered by transactional-update, OS patching, or systemctl reboot.
```

**Bad** (excerpt from a customer-facing troubleshooting page):

```
This pattern is the failure mode of the AIT-70656 hostname/FQDN bug that is fixed in cluster-api-provider-hcs v1.0.1+.
```

**Good**:

```
In cluster-api-provider-hcs releases earlier than v1.0.1, a dotted HCSMachineConfigPool.spec.configs[].hostname is rendered into cloud-init as the full FQDN string in the hostname field …
```

**Prevention**:
1. Before drafting, scan the source material (Jira description, internal test report, design doc, PR body) for the categories in the table above and produce a translation list. Each internal token must map to either a customer-facing replacement or "drop".
2. When the source presents multiple internal options (Path A / B / C, alternative analyses, "Why we did not pick X"), keep only the one the product supports. The customer page documents the supported path, not the decision history.
3. When the source cites a version, prefer the released customer-visible version label (for example `v1.0.1`) over internal build tags or commit shas.
4. After drafting, grep the new or modified pages for the pattern set: `(AIT-|DBS-|DEVOPS-|MIDDLEWARE-)[0-9]+`, `[0-9]{4}-[0-9]{2}-[0-9]{2}`, the literal strings `Path A`, `Path B`, `Path C`, `Verified`, `Validated`, `release test`, `hcslab`, `RUS-`, `KI-`, `TC-`, `BuildRun`, `gitlab-ce`, `build-harbor`, `package-minio`, `MR !`. Each match needs an explicit justification or removal.
5. If the user authored an internal test report or Jira description and asks for "the same content as a product doc", reply with a draft that **strips** these tokens. Do not echo the internal material verbatim. The internal version stays in its engineering home; the product doc is a translation, not a copy.

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
- [ ] **No Internal Bookkeeping In Customer Docs** (Pitfall 9a): Customer-facing pages contain no issue-tracker IDs (`AIT-`, `DBS-`, `DEVOPS-`, `MIDDLEWARE-`, `TC-`, `KI-`, `RUS-`), no internal test dates (`Verified YYYY-MM-DD`, `Validated YYYY-MM-DD on hcslab`), no internal decision rationale (`Path A / B / C`, alternative analyses, "Why we did not pick X"), and no internal repo / build / artifact references (`gitlab-ce`, `build-harbor`, `package-minio`, `MR !N`, `BuildRun <name>`).

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
