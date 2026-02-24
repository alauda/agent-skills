# Terminology Consistency Specification

Maintaining terminology consistency is vital for professional technical documentation and for ensuring AI agents provide accurate answers.

## Core Principle: Avoid Inventing Terms

**Strict Directive**: Do not create new technical terms. Always prioritize official community and ecosystem standards.

### Hierarchy of Authority
1. 🥇 **Kubernetes Official Documentation**: For all container-native and orchestration concepts.
2. 🥈 **OpenShift Documentation**: For enterprise Kubernetes and platform-specific features.
3. 🥉 **Upstream Project Documentation**: (e.g., Istio, Velero, Helm) for specific tool-related terms.

## Guidelines for New Terms

If a term is not found in the official sources above:
1. **Research First**: Look for industry-standard terms in CNCF projects.
2. **Flag for Review**: Proactively notify the documentation team and the user before introducing a new term.
3. **Draft with Caution**: Use descriptive language instead of a single new word if no standard exists.

## Common Consistency Pitfalls

| Scenario | Incorrect (Avoid) | Correct (Use) |
| :--- | :--- | :--- |
| **Node Roles** | Master/Slave | Control plane/Worker |
| **Lifecycle** | Kill/Destroy | Delete/Terminate |
| **Status** | Died/Broken | Failed/Unhealthy |
| **Networking** | Blackhole/Pipe | Deny list/Route |

## RAG Optimization

Terminology consistency directly impacts the performance of Retrieval-Augmented Generation (RAG).
- **Keyword Matching**: AI agents rely on specific keywords to retrieve the correct document chunks.
- **Synonym Confusion**: Using "Container Instance" in one place and "Pod" in another confuses the retrieval logic.
- **Acronyms**: Always provide the full name upon first mention: `BGP (Border Gateway Protocol)`.

## Validation Checklist

- [ ] Does the term exist in the `terminology-guide.md`?
- [ ] Is the term consistent with Kubernetes/OpenShift official standards?
- [ ] Is the same term used for the same concept throughout the document?
- [ ] Are "Bad Cases" from the guide avoided?
