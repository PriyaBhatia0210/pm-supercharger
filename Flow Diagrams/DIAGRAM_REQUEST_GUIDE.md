# How to Request Diagrams from PRDs

This guide shows you how to request visual diagrams (flowcharts, mind maps, decision trees, etc.) from any PRD using simple prompts.

## Quick Start

Use this simple prompt format:

```
Create a [DIAGRAM_TYPE] for [CONCEPT/FLOW] from [PRD_NAME]
```

## Prompt Template Structure

### Basic Template

```
Create a [diagram type] for [specific concept/flow/process] from [PRD name]
```

### With Additional Context (Optional)

```
Create a [diagram type] for [specific concept/flow/process] from [PRD name]
Focus on: [specific aspect to highlight]
Include: [additional details to show]
```

## Diagram Types Available

1. **flowchart** / **flow chart** - Process flows, user journeys, workflows
2. **decision tree** - Decision points, branching logic, conditional paths
3. **mind map** - Concept relationships, feature breakdowns
4. **timeline** / **gantt** - Project phases, rollout schedules, milestones
5. **architecture** / **schema** - System components, technical architecture, data flows
6. **state diagram** - Status transitions, lifecycle flows

## Examples

### Example 1: Simple Flowchart Request
```
Create a flowchart for the 3-wave price alignment process from the Price Uplifts PRD
```

### Example 2: Decision Tree Request
```
Create a decision tree for selecting the AI email assistant approach from the AI Email Assistant PRD
```

### Example 3: User Flow Request
```
Create a flowchart for the starter plan personalized churn deflection flow from the Reducing In-Product Churn PRD
```

### Example 4: Timeline Request
```
Create a timeline diagram for the rollout plan from the Price Uplifts PRD
```

### Example 5: Architecture Request
```
Create an architecture diagram for the technical components from the Price Uplifts PRD
```

### Example 6: Mind Map Request
```
Create a mind map of the price uplift PRD concepts
```

### Example 7: With Focus
```
Create a flowchart for the cancellation flow from the Reducing In-Product Churn PRD
Focus on: the personalized offer logic based on contract type and tenure
```

## What Happens When You Request

1. **I analyze the PRD** to find the relevant section
2. **I extract the key information** (processes, decisions, relationships, etc.)
3. **I generate Mermaid code** in the appropriate diagram format
4. **I create a markdown file** in `Flow Diagrams/[PRD-name]/[diagram-name].md`
5. **You can view it** in GitHub, VS Code, or mermaid.live

## Tips for Better Results

### Be Specific
✅ Good: "Create a flowchart for the starter plan personalized churn deflection flow"
❌ Vague: "Create a diagram for the churn PRD"

### Name the PRD Clearly
✅ Good: "from the Reducing In-Product Churn PRD"
✅ Good: "from the Price Uplifts PRD"
❌ Unclear: "from that PRD about pricing"

### Specify What to Visualize
✅ Good: "the 3-wave process"
✅ Good: "the personalized offer logic"
❌ Too broad: "everything in the PRD"

### Request Multiple Views
You can ask for different diagram types for the same concept:
- "Create a flowchart for the process"
- "Create a decision tree for the same process"
- "Create a timeline for the rollout"

## Common Patterns

### Process/Workflow Visualization
```
Create a flowchart for [process name] from [PRD name]
```

### Decision Logic Visualization
```
Create a decision tree for [decision point] from [PRD name]
```

### Concept Overview
```
Create a mind map of [PRD name] concepts
```

### Project Planning
```
Create a timeline diagram for [project/initiative] from [PRD name]
```

### Technical Documentation
```
Create an architecture diagram for [system/component] from [PRD name]
```

## Advanced: Requesting Multiple Diagrams

You can request multiple diagrams in one go:

```
Create the following diagrams from the Price Uplifts PRD:
1. A flowchart for the 3-wave process
2. A timeline for the rollout plan
3. A mind map of the key concepts
```

## Output Location

All diagrams are saved to:
```
Flow Diagrams/
└── [PRD-name]/
    └── [diagram-name].md
```

## Viewing Diagrams

- **GitHub/GitLab**: Native Mermaid support
- **VS Code**: Install "Markdown Preview Mermaid Support"
- **Online**: Copy code to [mermaid.live](https://mermaid.live)
- **Embed in PRD**: Copy Mermaid code block into your PRD document

## Need Help?

If a diagram doesn't capture what you need:
1. Ask for refinements: "Can you add [detail] to the flowchart?"
2. Request a different view: "Can you create a simpler version?"
3. Ask for multiple perspectives: "Can you also create a decision tree version?"

