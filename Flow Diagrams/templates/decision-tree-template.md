# Decision Tree Template

This template shows the structure for decision trees and branching logic.

## Example: Simple Decision Tree

```mermaid
flowchart TD
    Start{Initial Decision} -->|Condition A| PathA[Action A]
    Start -->|Condition B| PathB{Sub-decision}
    PathB -->|Sub-condition 1| PathB1[Action B1]
    PathB -->|Sub-condition 2| PathB2[Action B2]
    PathA --> End
    PathB1 --> End
    PathB2 --> End
```

## Example: Multi-level Decision Tree

```mermaid
flowchart TD
    Root{Primary Decision} -->|Option 1| L1A{Level 1 Decision A}
    Root -->|Option 2| L1B{Level 1 Decision B}
    Root -->|Option 3| L1C[Direct Action]
    
    L1A -->|A1| L2A1[Action A1]
    L1A -->|A2| L2A2[Action A2]
    
    L1B -->|B1| L2B1{Level 2 Decision}
    L1B -->|B2| L2B2[Action B2]
    
    L2B1 -->|B1a| L3B1a[Action B1a]
    L2B1 -->|B1b| L3B1b[Action B1b]
    
    L2A1 --> End
    L2A2 --> End
    L2B2 --> End
    L3B1a --> End
    L3B1b --> End
    L1C --> End
```

## Styling Tips

- Use diamond shapes `{}` for decision points
- Use rectangles `[]` for actions/outcomes
- Use rounded rectangles `([ ])` for start/end points
- Label all edges clearly

