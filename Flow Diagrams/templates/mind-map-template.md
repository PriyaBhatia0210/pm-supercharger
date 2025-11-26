# Mind Map Template

This template shows the structure for mind maps and concept relationships.

## Example: Central Concept Mind Map

```mermaid
mindmap
  root((Central Concept))
    Branch 1
      Sub-branch 1.1
      Sub-branch 1.2
        Detail 1.2.1
        Detail 1.2.2
    Branch 2
      Sub-branch 2.1
      Sub-branch 2.2
    Branch 3
      Sub-branch 3.1
```

## Example: Feature Breakdown

```mermaid
mindmap
  root((Feature Name))
    Core Features
      Feature A
        Sub-feature A1
        Sub-feature A2
      Feature B
    Technical
      Component 1
      Component 2
    User Impact
      Benefit 1
      Benefit 2
```

## Alternative: Flowchart-style Mind Map

For more control, use flowchart syntax:

```mermaid
flowchart TD
    Center[Central Concept] --> A[Branch A]
    Center --> B[Branch B]
    Center --> C[Branch C]
    A --> A1[Sub-branch A1]
    A --> A2[Sub-branch A2]
    B --> B1[Sub-branch B1]
    C --> C1[Sub-branch C1]
    C --> C2[Sub-branch C2]
```

