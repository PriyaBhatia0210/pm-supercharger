# Product Update Slack Message Generator

A comprehensive system to generate product update Slack messages from PRDs, sprint notes, and Jira tickets following established patterns.

## Overview

This tool automatically generates formatted product update Slack messages by extracting information from various sources and applying consistent templates. It supports multiple update types (experiments, rollouts, features, iterations) and ensures proper formatting with team tags, stakeholder mentions, and links.

## Features

- **Multiple Input Sources**: Generate messages from PRDs, sprint notes, or Jira tickets
- **Type-Specific Templates**: Automatically selects appropriate template based on update type
- **Interactive Mode**: Guided prompts for missing information
- **Automatic Formatting**: Properly formats team tags, links, and bullet lists
- **Jira Integration**: Supports Jira MCP for fetching ticket data

## Installation

### Requirements

- Python 3.7+
- Jinja2

### Setup

```bash
# Install dependencies
pip install jinja2

# Make scripts executable (optional)
chmod +x Scripts/generate_product_update.py
chmod +x Scripts/interactive_update_generator.py
```

## Usage

### Command Line Interface

#### Generate from PRD

```bash
python Scripts/generate_product_update.py --prd path/to/prd.md --output update.md
```

#### Generate from Sprint Notes

```bash
python Scripts/generate_product_update.py --sprint-notes path/to/sprint-notes.md --output update.md
```

#### Generate from Jira Ticket

```bash
python Scripts/generate_product_update.py --jira PD-12345 --output update.md
```

#### Specify Update Type

```bash
python Scripts/generate_product_update.py --prd prd.md --type experiment --output update.md
```

### Interactive Mode

For a guided experience that prompts for missing information:

```bash
python Scripts/interactive_update_generator.py
```

The interactive mode will:
1. Optionally load data from a source file (PRD, sprint notes, or Jira)
2. Prompt for any missing required information
3. Allow you to add optional sections
4. Generate a preview
5. Save the final message

## Update Types

The generator supports four update types:

1. **Experiment**: For A/B tests and experiments
   - Includes hypothesis, objectives, experiment details
   - Template: `Product-Update-Template-Experiment.md`

2. **Rollout**: For gradual feature rollouts
   - Includes rollout plan, monitoring, guardrails
   - Template: `Product-Update-Template-Rollout.md`

3. **Feature**: For new feature releases
   - Includes TL;DR, what's changing, rollout details
   - Template: `Product-Update-Template-Feature.md`

4. **Iteration**: For iteration updates
   - Includes previous signals, what's new, next steps
   - Template: `Product-Update-Template-Iteration.md`

## Information Extraction

### From PRDs

The PRD extractor looks for:
- **Title**: Main heading or PRD title
- **Objective**: Objective section
- **Hypothesis**: Hypothesis section (for experiments)
- **Why We Built It**: Problem/Opportunity section
- **How It Works**: Approach/Functional Specification section
- **Success Metrics**: Success metrics section or table
- **Timeline**: Timeline or Rollout Plan section
- **Team Members**: DRI mentions and email links
- **Stakeholders**: Stakeholders section
- **Links**: PRD, Jira, Figma links
- **Feature Flags**: Feature flag mentions

### From Sprint Notes

The sprint notes extractor looks for:
- **Title**: Project Overview title
- **Sprint Goal**: Sprint goal section
- **Why We Built It**: Project Overview or Goal section
- **How It Works**: Technical Architecture or Approach section
- **Decisions**: Sprint Planning Decisions section
- **Action Items**: Next Steps / Action Items section
- **Team Members**: Participants, Owner, or action item assignees
- **Timeline**: Date or Sprint mentions
- **Links**: Any markdown links

### From Jira Tickets

The Jira extractor fetches:
- **Title**: Ticket summary
- **Description**: Ticket description (cleaned of Jira markup)
- **Why We Built It**: Extracted from description
- **How It Works**: Extracted from description
- **Acceptance Criteria**: From ticket fields or description
- **Team Members**: Assignees and watchers
- **Links**: Jira ticket link and links from description
- **Sprint/Epic**: Sprint and epic information

## Template Variables

Templates support the following variables:

- `{title}` - Feature/experiment name with type tag
- `{type}` - Update type (Experiment, Rollout, etc.)
- `{why_built}` - Why we built it section
- `{hypothesis}` - Hypothesis (for experiments)
- `{how_it_works}` - How it works section
- `{objectives}` - Objectives/success metrics (formatted as bullets)
- `{timeline}` - Timeline/rollout plan (formatted as bullets)
- `{team_members}` - Formatted team member tags
- `{stakeholders}` - Formatted stakeholder CCs
- `{links}` - Formatted learn more links
- `{feature_flags}` - Feature flags (formatted as bullets)
- `{monitoring}` - What we're monitoring (formatted as bullets)
- `{guardrails}` - Guardrails (formatted as bullets)
- `{how_to_help}` - How you can help (formatted as bullets)

## Team Member Formatting

Team members are automatically formatted as Slack tags:
- Full names are converted to username format (e.g., "John Doe" → "@john.doe")
- Already formatted tags are preserved (e.g., "@teammooncake")
- Team groups are recognized (e.g., "support team" → "@supportteam")

## Common Stakeholder Groups

The generator recognizes common stakeholder groups:
- Support team → `@supportteam`
- Account Managers → `@ams`
- Customer Success Managers → `@csms`

## Examples

See the `Examples/` directory for example outputs:
- `example-from-prd.md` - Generated from a PRD
- `example-from-sprint.md` - Generated from sprint notes
- `example-from-jira.md` - Generated from a Jira ticket

## Customization

### Custom Templates

Templates are located in `Templates/`. You can modify them to match your team's style. Templates use Jinja2 syntax.

### Custom Extractors

Extractors are in `Scripts/extractors/`. You can extend them to extract additional information or support different formats.

## Troubleshooting

### Missing Information

If the generator is missing information:
1. Use interactive mode to fill in gaps
2. Check that your source file follows expected formats
3. Manually edit the generated message

### Template Errors

If you see template errors:
1. Check that all required variables are provided
2. Verify template syntax (Jinja2)
3. Check for special characters that need escaping

### Jira Integration

If Jira extraction isn't working:
1. Ensure Jira MCP is properly configured
2. Check that you have access to the ticket
3. The extractor will fall back to basic information if MCP is unavailable

## File Structure

```
Product updates slack message/
├── Product Updates examples.md (existing examples)
├── Templates/
│   ├── Product-Update-Template-Base.md
│   ├── Product-Update-Template-Experiment.md
│   ├── Product-Update-Template-Rollout.md
│   ├── Product-Update-Template-Feature.md
│   ├── Product-Update-Template-Iteration.md
│   └── README-Templates.md
├── Scripts/
│   ├── generate_product_update.py
│   ├── interactive_update_generator.py
│   └── extractors/
│       ├── __init__.py
│       ├── prd_extractor.py
│       ├── sprint_notes_extractor.py
│       └── jira_extractor.py
├── Examples/
│   ├── example-from-prd.md
│   ├── example-from-sprint.md
│   └── example-from-jira.md
└── README.md
```

## Contributing

To add support for new input sources or update types:
1. Create a new extractor in `Scripts/extractors/`
2. Create a new template in `Templates/`
3. Update the generator to support the new source/type

## License

Internal tool for PandaDoc product team.

