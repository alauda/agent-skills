# Best Practices - Common Patterns

This document provides reusable patterns for common documentation scenarios in the Doom framework.

## Pattern 1: Recommendation with Note

**Scenario**: Recommend using a feature, with important notes or limitations.

**Template**:
```markdown
**Recommendation**: [What to recommend]. [Why it's recommended - benefits or reasons].

**Note**: [Important limitation, exception, or requirement].
```

**Example**:
```markdown
**Recommendation**: Using a domain name for the Cluster Endpoint is recommended.
If the VIP needs to be changed after cluster installation, using a domain name allows for easy DNS record updates without impacting cluster operations.

**Note**: `Self-Built VIP` does not support domain name configuration.
```

**When to use**:
- Recommending a configuration option
- Suggesting a best practice
- Advising on architecture decisions

---

## Pattern 2: Two-Option Choice

**Scenario**: Present users with two clear options, with a recommended choice.

**Template**:
```markdown
If [condition for option A], it is **recommended** to [option A].
If not, you can [option B].
```

**Example**:
```markdown
If a hardware LoadBalancer is available in your environment, it is **recommended** to use it.
If not, you can enable `Self-built VIP`, which provides software load balancing using keepalived.
```

**When to use**:
- Presenting alternative approaches
- Hardware vs software options
- Configurable features with defaults

---

## Pattern 3: Table Cell with Multiple Info Blocks

**Scenario**: Table description column contains multiple types of information.

**Template**:
```markdown
[Primary instruction].<br />
[Alternative/fallback option].<br />
[Special case note].<br /><br />
[Requirements header]:<br />
- [Requirement 1]<br />
- [Requirement 2]<br />
- [Requirement 3]
```

**Example**:
```markdown
Enter the pre-prepared domain name.<br />
If no domain name is available, enter the pre-prepared `global` VIP.<br />
`Self-Built VIP` is disabled by default.<br /><br />
The following conditions must be met when using `Self-Built VIP`:<br />
- A usable VRID is available<br />
- The host network supports the VRRP protocol<br />
- All control plane nodes and the VIP must be on the same subnet
```

**When to use**:
- Parameter description tables
- Configuration option tables
- Feature comparison tables

---

## Pattern 4: Conditional Requirements

**Scenario**: Something is required only under specific conditions.

**Template**:
```markdown
[General statement].<br /><br />
A [thing] is **required** in the following cases:<br />
- [Condition 1]<br />
- [Condition 2]<br />
- [Condition 3]
```

**Example**:
```markdown
Using a domain name is recommended for most deployments.<br /><br />
A domain name is **required** in the following cases:<br />
- The `global` cluster needs to support IPv6 access<br />
- A disaster recovery plan for the `global` cluster is planned
```

**When to use**:
- Explaining when something is mandatory vs optional
- Documenting conditional requirements
- Clarifying edge cases

---

## Pattern 5: Step with Tip

**Scenario**: A procedural step with additional helpful information.

**Template**:
```markdown
### [Step Title]

[Main instruction content].<br /><br />
<b>Tip:</b> [Helpful shortcut, optimization, or reminder].
```

**Example**:
```markdown
### Configure Network Settings

Enter the Cluster Endpoint and select the network protocol.<br /><br />
<b>Tip:</b> For single-node deployments in test scenarios, you can directly enter the node IP.
```

**When to use**:
- How-to guides with optional optimizations
- Procedures with shortcuts
- Steps with common pitfalls

---

## Pattern 6: Parameter Table Entry

**Scenario**: Standard parameter description in a configuration table.

**Template**:
```markdown
<b>[Parameter Name]</b>

[Primary purpose].<br />
[Default behavior or value].<br />
[Important note or constraint].<br /><br />
<b>Note:</b> [Critical requirement or limitation].<br /><br />
<b>Tip:</b> [Helpful usage advice].
```

**Example**:
```markdown
<b>Cluster Endpoint</b>

Used to access the cluster API server.<br />
Defaults to the first node's IP if not specified.<br />
Must be accessible from all worker nodes.<br /><br />
<b>Note:</b> Once set, this value cannot be changed after cluster creation.<br /><br />
<b>Tip:</b> Using a domain name is recommended for production environments.
```

**When to use**:
- Installation parameter tables
- Configuration reference tables
- Feature settings documentation

---

## Pattern 7: Prerequisite List

**Scenario**: Listing requirements before a procedure.

**Template**:
```markdown
### Prerequisites

Before you begin, ensure you have:

- [Requirement 1]
- [Requirement 2] with [specific detail]
- [Requirement 3]

**Note**: [Additional requirement or warning].
```

**Example**:
```markdown
### Prerequisites

Before you begin, ensure you have:

- A `global` cluster with at least 3 control plane nodes
- Network connectivity between clusters
- Sufficient resources as described in [Resource Planning](./planning.md)

**Note**: If using IPv6, all nodes must have correctly configured IPv6 addresses.
```

**When to use**:
- How-to guides
- Installation procedures
- Setup instructions

---

## Pattern 8: Result Verification

**Scenario**: Verifying that a procedure completed successfully.

**Template**:
```markdown
### Verify [What was done]

[Method 1 to verify].<br />
[Method 2 to verify].

<b>Expected Result:</b> [What success looks like].
```

**Example**:
```markdown
### Verify Installation

Run the following command to check cluster status:

```bash
kubectl get nodes
```

<b>Expected Result:</b> All nodes show `Ready` status.
```

**When to use**:
- End of procedures
- Installation guides
- Configuration instructions

---

## Pattern 9: Troubleshooting Note

**Scenario**: Quick troubleshooting hint within a procedure.

**Template**:
```markdown
<b>Troubleshooting:</b> [Common issue] - [Solution].

Or use inline: [Instruction] (<b>Note:</b> [If X fails, try Y>)
```

**Example**:
```markdown
<b>Troubleshooting:</b> Connection timeout - Check firewall rules and ensure port 6443 is open.

Or:

Run the installer script (<b>Note:</b> If the script fails, check that all prerequisites are met).
```

**When to use**:
- Common failure points
- Known issues
- Error-prone steps

---

## Pattern 10: Resource Table Entry

**Scenario**: Hardware or resource requirements in a table.

**Template**:
```markdown
| Resource | Minimum Requirement |
| -------- | ------------------- |
| [Name]   | [Value with unit]   |
```

**Example**:
```markdown
| Resource | Minimum Requirement |
| -------- | ------------------- |
| CPU      | 8 cores             |
| Memory   | 16 GB               |
| Storage  | [Storage Capacity](./storage.md#capacity) |
```

**When to use**:
- System requirements tables
- Resource planning tables
- Hardware specification tables

---

## Usage Guidelines

1. **Copy and Adapt**: These patterns are templates. Adapt them to your specific context.
2. **Maintain Consistency**: When similar content appears across documents, use the same pattern.
3. **Layer Information**: Start simple, add complexity only when needed.
4. **Cross-Reference**: Link to related patterns or detailed information when appropriate.

## Anti-Patterns to Avoid

| ❌ Anti-Pattern | ✅ Correct Approach |
|---------------|-------------------|
| Mixing recommendation and reason in one sentence | Separate sentences for clarity |
| Using `<b>` everywhere | Use `**bold**` for emphasis in body text |
| Long paragraphs in tables | Use `<br />` to break up content |
| Repeating the same info in multiple places | State it once in the most relevant location |
| Complex nested lists | Flatten to 2 levels maximum |
