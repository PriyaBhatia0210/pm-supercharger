# State Diagram Template

This template shows the structure for state machines and lifecycle diagrams.

## Example: Simple State Machine

```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2: Event1
    State2 --> State3: Event2
    State3 --> State1: Event3
    State3 --> [*]: Complete
```

## Example: Complex State Machine

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review: Submit
    Review --> Approved: Approve
    Review --> Rejected: Reject
    Rejected --> Draft: Revise
    Approved --> Published: Publish
    Published --> Archived: Archive
    Archived --> [*]
```

## Example: Parallel States

```mermaid
stateDiagram-v2
    [*] --> Active
    state Active {
        [*] --> Processing
        Processing --> Validating
        Validating --> Complete
        Complete --> [*]
    }
    Active --> Inactive: Deactivate
    Inactive --> Active: Reactivate
    Inactive --> [*]
```

