# Flow Chart Template

This template shows the structure for process/workflow flow charts.

## Example: Simple Process Flow

```mermaid
flowchart TD
    Start([Start]) --> Step1[Step 1: Action]
    Step1 --> Decision{Decision Point?}
    Decision -->|Yes| Step2[Step 2: Path A]
    Decision -->|No| Step3[Step 3: Path B]
    Step2 --> End([End])
    Step3 --> End
```

## Example: User Flow

```mermaid
flowchart LR
    A[User Action] --> B{System Check}
    B -->|Valid| C[Process]
    B -->|Invalid| D[Show Error]
    C --> E[Success]
    D --> A
```

## Common Patterns

### Sequential Steps
```mermaid
flowchart LR
    A[Step 1] --> B[Step 2] --> C[Step 3] --> D[Step 4]
```

### Parallel Processes
```mermaid
flowchart TD
    Start --> A[Process A]
    Start --> B[Process B]
    Start --> C[Process C]
    A --> Merge
    B --> Merge
    C --> Merge
    Merge --> End
```

### Loops
```mermaid
flowchart TD
    Start --> Process[Process Item]
    Process --> Check{More Items?}
    Check -->|Yes| Process
    Check -->|No| End
```

