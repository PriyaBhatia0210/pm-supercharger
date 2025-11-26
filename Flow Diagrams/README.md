# PRD Visual Diagram Framework

This framework enables automatic generation of visual diagrams (flow charts, mind maps, decision trees, timelines, etc.) from PRD documents.

## Overview

When working with PRDs, complex concepts, workflows, and relationships can be better understood through visual representations. This framework provides a standardized approach to generate these diagrams using Mermaid syntax.

## Supported Diagram Types

### 1. Flow Charts
**Use for:** User flows, process workflows, system interactions, step-by-step procedures

**Example requests:**
- "Create a flow chart for the 3-wave price alignment process"
- "Generate a user flow for the AI email assistant feature"

### 2. Decision Trees
**Use for:** Decision points, branching logic, conditional paths, if/then scenarios

**Example requests:**
- "Create a decision tree for selecting the AI email approach"
- "Generate a decision tree for handling price uplift exceptions"

### 3. Mind Maps
**Use for:** Concept relationships, feature breakdowns, problem-solution mapping, hierarchical structures

**Example requests:**
- "Create a mind map of the price uplift PRD concepts"
- "Generate a mind map showing all features and their relationships"

### 4. Timeline Diagrams
**Use for:** Project phases, rollout schedules, milestone sequences, Gantt-style views

**Example requests:**
- "Create a timeline diagram for the rollout plan"
- "Generate a Gantt chart for the 3-wave execution"

### 5. Schema/Architecture Diagrams
**Use for:** System components, data flows, technical architecture, component relationships

**Example requests:**
- "Create an architecture diagram for the technical components"
- "Generate a system diagram showing data flow"

### 6. State Diagrams
**Use for:** Status transitions, lifecycle flows, state machines

**Example requests:**
- "Create a state diagram for customer pricing status"
- "Generate a lifecycle diagram for document processing"

## How to Use

1. **Request a diagram** by asking:
   - "Create a [diagram type] for [PRD name or concept]"
   - "Generate a [diagram type] showing [specific aspect]"

2. **Diagrams are generated** in Mermaid format and saved to:
   - `Flow Diagrams/[PRD-name]/[diagram-name].md`

3. **View diagrams** in:
   - GitHub/GitLab (native Mermaid support)
   - VS Code with Mermaid extensions
   - Online Mermaid editors (mermaid.live)
   - Any markdown viewer with Mermaid support

## Diagram Naming Convention

- `[prd-name]-[diagram-type].md`
- Examples:
  - `price-uplifts-workflow-flowchart.md`
  - `ai-email-assistant-decision-tree.md`
  - `platform-hardening-mind-map.md`

## Mermaid Syntax Reference

All diagrams use [Mermaid](https://mermaid.js.org/) syntax, which is:
- Text-based and version-controllable
- Widely supported in markdown viewers
- Easy to edit and maintain

## Quick Start

### Simple Request Format

```
Create a [diagram type] for [concept/flow] from [PRD name]
```

### Examples

- `Create a flowchart for the 3-wave price alignment process from the Price Uplifts PRD`
- `Create a decision tree for the AI email approach selection from the AI Email Assistant PRD`
- `Create a timeline diagram for the rollout plan from the Price Uplifts PRD`
- `Create a flowchart for the starter plan personalized churn deflection flow from the Reducing In-Product Churn PRD`

### What Happens Automatically

When you request a diagram, I will:

1. ✅ Find and read the relevant PRD
2. ✅ Extract the specific information needed
3. ✅ Generate appropriate Mermaid diagram code
4. ✅ Create a markdown file in the correct location
5. ✅ Provide the diagram ready to view

## Best Practices

1. **Be specific** in your requests - mention which PRD and what aspect to visualize
2. **Request multiple views** - different diagram types can show different perspectives
3. **Iterate** - ask for refinements if the diagram doesn't capture what you need
4. **Embed in PRDs** - copy Mermaid code blocks into your PRD documents for inline viewing

## Documentation

- **[DIAGRAM_REQUEST_GUIDE.md](./DIAGRAM_REQUEST_GUIDE.md)** - Complete user guide with examples
- **[PROMPT_TEMPLATES.md](./PROMPT_TEMPLATES.md)** - Copy-paste prompt templates
- **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)** - Quick cheat sheet
- **[templates/](./templates/)** - Example diagram templates

## Examples

See the `[PRD-name]/` directories for generated diagrams from your PRDs.

