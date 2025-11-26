# Timeline Diagram Template

This template shows the structure for timelines and Gantt charts.

## Example: Simple Timeline

```mermaid
gantt
    title Project Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Task 1           :a1, 2025-01-01, 30d
    Task 2           :a2, after a1, 20d
    section Phase 2
    Task 3           :a3, 2025-02-20, 25d
    Task 4           :a4, after a3, 15d
```

## Example: Milestone Timeline

```mermaid
gantt
    title Project Milestones
    dateFormat  YYYY-MM-DD
    section Wave 1
    Planning          :milestone, m1, 2025-01-01, 0d
    Execution         :active, 2025-01-02, 30d
    Review            :milestone, m2, 2025-02-01, 0d
    section Wave 2
    Planning          :2025-02-15, 15d
    Execution         :2025-03-01, 45d
    Review            :milestone, m3, 2025-04-15, 0d
```

## Alternative: Flowchart Timeline

For more visual control:

```mermaid
flowchart LR
    Start([Q1 2025]) -->|Phase 1| P1[Phase 1<br/>Jan - Feb]
    P1 -->|Phase 2| P2[Phase 2<br/>Mar - Apr]
    P2 -->|Phase 3| P3[Phase 3<br/>May - Jun]
    P3 --> End([Q2 2025])
```

