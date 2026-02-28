# Language Style Specification

To ensure documentation is professional, objective, and easy to translate, all contributors must follow these language style guidelines.

## Core Principles

### 1. Objective and Professional
- Use a neutral tone. Avoid emotional language, marketing fluff, or slang.
- **Good**: "Ensure the cluster configuration is correct; otherwise, service deployment may fail."
- **Bad**: "You must make sure your cluster is right, or else you're on your own."

### 2. User-Centric Perspective
- **Target Audience**: Explicitly identify if the document is for DevOps Engineers, Developers, or Namespace Admins. Provide support information tailored to their skill levels (e.g., K8s beginners vs. senior DevOps).
- **Scenario-Oriented**: Write for real-world tasks, not just product features.
- **Flowcharts**: For complex task flows (e.g., multi-cluster deployment), provide a flowchart or overview table before the steps.

### 3. Conciseness and Clarity
- Use simple, direct sentences (Subject-Verb-Object). Avoid long, nested clauses (no more than 5 commas per sentence).
- **No Double Negatives**: Always use positive assertions for clarity.
- **Active Voice**: "The system creates a backup" is better than "A backup is created."

### 4. Precision
- Use specific descriptions instead of abstract ones.
- **Good**: "The container failed to start and returned a `CrashLoopBackOff` error."
- **Bad**: "The deployment failed."
- **Quantifiable Data**: Use exact numbers instead of "many," "large," or "a while."
- **Good**: "Image size exceeds 2 GB" or "Wait approximately 3 minutes."
- **Bad**: "The image is too large" or "Wait a while."

### 5. Consistency
- Maintain consistent terminology and sentence structures (e.g., use imperative sentences for all steps).

## Wording Standards

### Actionable Steps
- Start instructions with an imperative verb.
- **Good**: "Expand the Deployment replica count to 3."
- **Bad**: "Increase the number of services."

### UI Elements
- Bold UI elements such as button names, menu items, and field labels.
- **Format**: **[Button Name]** or **[Menu Item]**.

### Technical Terms
- Use professional terms and industry-standard language.
- **Good**: "Expose the service using an Ingress Controller."
- **Bad**: "Use a gateway to open the service to the outside."

### Preserving Technical Concepts
- When referring to a specific technical concept or method, preserve its original form rather than converting it to a generic verb phrase.
- **Good**: "The platform uses an **in-place upgrade approach**." (preserves the technical concept)
- **Bad**: "The platform performs **in-place upgrades**." (loses precision, becomes a generic action)
- **Principle**: If a term represents a distinct technical strategy, use `[term] + [noun]` structure (e.g., `approach`, `method`, `strategy`) to maintain its status as a technical concept.

## Maintainability and Compatibility

- **Best Practices**: Include long-term maintenance tips.
- **Good**: "Store configurations in a **ConfigMap** for easy modification rather than hardcoding them in the Pod definition."
- **Compatibility**: Clearly state version requirements and dependencies.
- **Good**: "This feature requires Kubernetes v1.20 or higher."

## Prohibited Expressions (Bad Cases)

| Category | Avoid Using | Use Instead |
| :--- | :--- | :--- |
| **Colloquialism** | "Basically," "Essentially," "Just," "Done" | (Remove or be specific) |
| **Slang/Jargon** | "Maxed out," "Under the hood" | "Resource exhausted," "Technical implementation" |
| **Ambiguity** | "Etc.," "And so on," "Things like that" | (Be exhaustive or provide categories) |
| **Outdated Terms** | "Master," "Slave" | "Control plane," "Worker" |
| **Subjectivity** | "Obviously," "Of course," "Clearly" | (Present the evidence/facts) |

## Accessibility and Inclusivity

- Avoid gendered pronouns (he/she); use "they" or "you."
- Ensure descriptions are non-discriminatory and neutral.
