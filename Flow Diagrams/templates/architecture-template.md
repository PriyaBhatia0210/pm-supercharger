# Architecture/Schema Diagram Template

This template shows the structure for system architecture and component diagrams.

## Example: Component Architecture

```mermaid
graph TB
    subgraph "Frontend"
        A[User Interface]
        B[Client App]
    end
    
    subgraph "Backend"
        C[API Gateway]
        D[Service Layer]
        E[Data Layer]
    end
    
    subgraph "External"
        F[Third-party API]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    D --> F
```

## Example: Data Flow

```mermaid
flowchart LR
    Source[Data Source] -->|Extract| Process[Processing Engine]
    Process -->|Transform| Validate[Validation]
    Validate -->|Load| Target[Target System]
    Validate -->|Error| Log[Error Log]
```

## Example: System Relationships

```mermaid
erDiagram
    USER ||--o{ DOCUMENT : creates
    DOCUMENT ||--o{ RECIPIENT : has
    DOCUMENT ||--|| PRICING : uses
    PRICING ||--o{ ITEM : contains
```

