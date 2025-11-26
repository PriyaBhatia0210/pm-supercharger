# Product Update Templates

This directory contains templates for generating product update Slack messages.

## Template Files

- **Product-Update-Template-Base.md** - Base template with all common sections and emoji mapping guide
- **Product-Update-Template-Experiment.md** - Template for experiment updates
- **Product-Update-Template-Rollout.md** - Template for gradual rollout updates
- **Product-Update-Template-Feature.md** - Template for feature release updates
- **Product-Update-Template-Iteration.md** - Template for iteration updates

## Usage

Templates use Jinja2 syntax for variable substitution and conditional sections.

### Common Variables

- `{title}` - Feature/experiment name
- `{type}` - Update type tag (e.g., "Experiment", "Gradual Rollout")
- `{why_built}` - Why we built it section
- `{hypothesis}` - Hypothesis (for experiments)
- `{how_it_works}` - How it works section
- `{objectives}` - Objectives/success metrics
- `{timeline}` - Timeline/rollout plan
- `{team_members}` - Formatted team member tags
- `{stakeholders}` - Formatted stakeholder CCs
- `{links}` - Learn more links
- `{feature_flags}` - Feature flags if applicable

### Conditional Sections

Templates support conditional sections using Jinja2 syntax:
- `{% if variable %}...{% endif %}` - Include section only if variable exists
- `{% if variable|length > 1 %}...{% endif %}` - Conditional based on list length

### Formatting Guidelines

1. **Team Member Tags**: Format as `[@teammooncake](link) [@username](link)`
2. **Stakeholder CCs**: Format as `[@supportteam](link) [@ams](link)`
3. **Links**: Format as `* [PRD](url)`, `* [Jira](url)`, `* [Figma](url)`
4. **Bullet Lists**: Use `*` for bullet points
5. **Emojis**: Use Slack emoji syntax `:emoji_name:`

## Template Selection

Select the appropriate template based on update type:
- **Experiment**: Use Experiment template
- **Gradual Rollout**: Use Rollout template
- **Feature Release**: Use Feature template
- **Iteration**: Use Iteration template

