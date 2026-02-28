# Kubernetes YAML Validation Workflow

This document describes the automated validation workflow for Kubernetes YAML code blocks in generated documentation.

---

## When to Run

Run this validation **after** document generation but **before** self-verification (Phase 2.6a).

**Trigger**: The generated document contains Kubernetes YAML code blocks.

---

## Detection

Scan the generated document for YAML code blocks containing Kubernetes indicators:
- `apiVersion:`
- `kind: Deployment|Service|ConfigMap|StatefulSet|DaemonSet|Ingress|...`

If no K8s YAML is detected, skip to Phase 2.7.

---

## Validation Workflow

### Step 1: Ask for K8s Version

If the target K8s version is not already known, prompt the user:

```
The document contains Kubernetes YAML. What is the target K8s version?
(Common versions: 1.34, 1.33, 1.32, 1.31. Default: 1.34 if unspecified)
```

### Step 2: Setup Validation Tools

Run the setup script (idempotent, safe to re-run):

```bash
bash scripts/setup.sh
```

This ensures `ruamel.yaml` and `kubeconform` are installed.

### Step 3: Extract YAML Blocks

Extract YAML code blocks from the generated document and save to a temporary file (e.g., `/tmp/manifest.yaml`).

### Step 4: Stage 1 — YAML 1.2 Syntax Check

```bash
python3 scripts/yaml_check.py /tmp/manifest.yaml
```

**If this fails with parse errors:**
- **STOP** and report the errors to the user
- Ask whether to:
  - Fix automatically and retry
  - Wait for manual correction

### Step 5: Stage 2 — K8s Schema Validation

```bash
kubeconform \
  -kubernetes-version <VERSION> \
  -summary \
  -output json \
  /tmp/manifest.yaml
```

### Step 6: Report Results

**If all validations pass:**

```
✅ All Kubernetes YAML validated successfully (K8s <VERSION>)
```

**If errors are found:**

```
❌ YAML Validation Failed

### Errors found (N)
- **Deployment/xxx** (apps/v1)
  - Line 12: `spec.replicas` value must be integer, not string

Would you like me to:
1. Fix automatically and regenerate
2. Keep as-is and proceed (not recommended)
```

### Step 7: Handle Automatic Fix (If Chosen)

If user chooses automatic fix:
1. Apply corrections
2. Regenerate the affected section
3. Re-validate

---

## Completion Criteria

**Only proceed to Phase 2.7 after**:
- All YAML validations pass, OR
- User explicitly chooses to proceed despite errors

---

## Platform Requirements

- **Supported**: Linux, macOS (Apple Silicon and Intel)
- **Not supported**: Windows (use WSL2 or install tools manually)
- **Python**: 3.6+ required for `yaml_check.py`
- **Network**: Required to download kubeconform binary (unless pre-installed)
