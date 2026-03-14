# Issue Templates Reference

Load this file when drafting a GitHub issue to use the appropriate structural template.

## Bug Report

```markdown
## Description

[1-2 sentence summary of the bug]

## Steps to Reproduce

1. [First step]
2. [Second step]
3. [Observe the error]

## Expected Behavior

[What should happen]

## Actual Behavior

[What actually happens. Include error messages, screenshots, or logs if available.]

## Environment

- OS: [e.g., macOS 14.2, Ubuntu 22.04]
- Runtime: [e.g., Node 20.11, Python 3.12]
- Version/Commit: [e.g., v2.3.1, abc1234]
- Browser (if applicable): [e.g., Chrome 121]

## Additional Context

[Stack traces, screenshots, related issues, or anything else that helps diagnose.]

## Acceptance Criteria

- [ ] Bug no longer reproduces following the steps above
- [ ] Regression test added
- [ ] No unrelated behavior changes introduced
```

**Suggested labels:** `bug`, `severity:*` (critical/high/medium/low)

---

## Feature Request

```markdown
## Problem Statement

[What problem does this solve? Who has this problem? Link to user feedback or data if available.]

## Proposed Solution

[Describe the desired feature. Be specific about behavior, not implementation.]

## Alternatives Considered

- **[Alternative A]:** [Why it was rejected or is less preferred]
- **[Alternative B]:** [Why it was rejected or is less preferred]

## Design Considerations

[API surface, backward compatibility, performance implications, security considerations, or UX notes.]

## Acceptance Criteria

- [ ] [Specific, testable criterion]
- [ ] [Another criterion]
- [ ] Documentation updated
```

**Suggested labels:** `enhancement`, `priority:*`

---

## Task

```markdown
## Objective

[What needs to be done and why. Link to parent epic or feature if applicable.]

## Scope

### In Scope
- [Concrete deliverable]
- [Another deliverable]

### Out of Scope
- [Explicitly excluded work]

## Implementation Notes

[Technical guidance, relevant files/modules, architectural constraints, or dependencies.]

## Acceptance Criteria

- [ ] [Specific, verifiable criterion]
- [ ] [Another criterion]
- [ ] Tests passing
```

**Suggested labels:** `task`, `area:*`

---

## RFC / Proposal

```markdown
## Summary

[1-2 sentence overview of the proposal]

## Motivation

[Why is this change needed? What problem does it solve? Include data, user feedback, or incident references.]

## Detailed Design

### Current State
[How things work today and why that is insufficient]

### Proposed Change
[Detailed description of the proposed approach]

### Migration / Rollout Plan
[How to get from current state to proposed state. Phased rollout, feature flags, backward compatibility.]

## Tradeoffs

| Approach | Pros | Cons |
|----------|------|------|
| This proposal | [pros] | [cons] |
| Alternative A | [pros] | [cons] |
| Alternative B | [pros] | [cons] |

## Open Questions

- [ ] [Unresolved question that needs input]
- [ ] [Another open question]

## Acceptance Criteria

- [ ] Team consensus reached
- [ ] Design doc approved
- [ ] Implementation plan agreed upon
```

**Suggested labels:** `rfc`, `discussion`, `area:*`

---

## Label Taxonomy (Common Conventions)

### Type
`bug`, `enhancement`, `task`, `rfc`, `documentation`, `chore`, `refactor`

### Priority / Severity
`priority:critical`, `priority:high`, `priority:medium`, `priority:low`

### Area
`area:frontend`, `area:backend`, `area:infra`, `area:api`, `area:docs`

### Status
`needs-triage`, `needs-reproduction`, `blocked`, `help-wanted`, `good-first-issue`
