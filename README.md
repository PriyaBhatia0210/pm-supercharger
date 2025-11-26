# PM Supercharger 🚀

A comprehensive toolkit for Product Managers to streamline PRD creation, visual documentation, sprint updates, and product communication.

## Overview

PM Supercharger is a collection of templates, tools, and frameworks designed to help Product Managers work more efficiently. It provides standardized approaches for creating PRDs, generating visual diagrams, crafting sprint updates, and communicating product changes through Slack.

## 📁 Repository Structure

### 🎨 [Flow Diagrams](./Flow%20Diagrams/)
**Visual diagram generation framework for PRDs**

Automatically generate flow charts, mind maps, decision trees, timelines, and architecture diagrams from PRD documents using Mermaid syntax. Perfect for visualizing complex workflows, system architectures, and decision processes.

**Key Features:**
- Multiple diagram types (flow charts, decision trees, mind maps, timelines, state diagrams, architecture)
- Mermaid-based syntax (version-controllable and widely supported)
- Template library for common diagram patterns
- Quick reference guides and prompt templates

📖 [Read the Flow Diagrams Guide](./Flow%20Diagrams/README.md)

---

### 📋 [PRD Templates](./PRD%20templates/)
**Standardized PRD templates for different use cases**

A collection of PRD templates tailored for various product scenarios, ensuring consistency and completeness across all product documentation.

**Available Templates:**
- **PRD-Template-Base.md** - Standard PRD template for general features
- **PRD-Template-New-Feature.md** - Template for new feature development
- **PRD-Template-Growth-Experiment.md** - Template for growth experiments and A/B tests
- **PRD-Template-Multi-Iteration.md** - Template for features with multiple iterations/phases

Each template includes sections for problem statement, success metrics, user stories, technical requirements, and rollout plans.

---

### 📊 [Sprint Review Updates](./Sprint%20review%20updates/)
**Templates and tools for sprint documentation**

Generate professional Product Review Updates and Growth Sprint Presentation slides from sprint planning meeting notes and related documents.

**Key Features:**
- Product Review Update templates
- Growth Sprint Presentation slide templates (2-3 slides per team)
- Extraction guides for pulling information from various sources
- Example outputs for reference

📖 [Read the Sprint Updates Guide](./Sprint%20review%20updates/Templates/README-Sprint-Updates.md)

---

### 💬 [Product Slack Updates](./product%20slack%20updates/)
**Automated Slack message generation for product updates**

Generate formatted product update Slack messages from PRDs, sprint notes, and Jira tickets. Supports multiple update types (experiments, rollouts, features, iterations) with proper formatting, team tags, and stakeholder mentions.

**Key Features:**
- Multiple input sources (PRDs, sprint notes, Jira tickets)
- Type-specific templates (experiments, rollouts, features, iterations)
- Interactive mode for guided prompts
- Automatic formatting with team tags and links
- Jira integration support

📖 [Read the Product Updates Guide](./product%20slack%20updates/README.md)

## 🚀 Quick Start

### For Flow Diagrams
1. Navigate to [Flow Diagrams](./Flow%20Diagrams/)
2. Review the [Quick Reference](./Flow%20Diagrams/QUICK_REFERENCE.md)
3. Use prompt templates to request diagrams from PRDs

### For PRD Creation
1. Navigate to [PRD Templates](./PRD%20templates/)
2. Choose the appropriate template for your use case
3. Copy and customize the template for your feature

### For Sprint Updates
1. Navigate to [Sprint Review Updates](./Sprint%20review%20updates/)
2. Review the [Extraction Guide](./Sprint%20review%20updates/Templates/Sprint-Update-Extraction-Guide.md)
3. Use templates to generate Product Review Updates or Sprint Presentations

### For Product Slack Updates
1. Navigate to [Product Slack Updates](./product%20slack%20updates/)
2. Install dependencies: `pip install jinja2`
3. Run the interactive generator: `python Scripts/interactive_update_generator.py`

## 🛠️ Requirements

### Product Slack Updates
- Python 3.7+
- Jinja2 (`pip install jinja2`)

### Flow Diagrams
- Markdown viewer with Mermaid support (GitHub, VS Code, or online editors)
- No additional installation required

### PRD Templates & Sprint Updates
- No installation required - just copy and customize templates

## 📚 Documentation

Each folder contains comprehensive documentation:
- **Flow Diagrams**: [README.md](./Flow%20Diagrams/README.md) | [Quick Reference](./Flow%20Diagrams/QUICK_REFERENCE.md)
- **PRD Templates**: Templates are self-documenting with inline guidance
- **Sprint Updates**: [README-Sprint-Updates.md](./Sprint%20review%20updates/Templates/README-Sprint-Updates.md)
- **Product Slack Updates**: [README.md](./product%20slack%20updates/README.md)

## 🎯 Use Cases

### Creating a New Feature PRD
1. Use a template from [PRD Templates](./PRD%20templates/)
2. Generate visual diagrams using [Flow Diagrams](./Flow%20Diagrams/)
3. Create Slack announcement using [Product Slack Updates](./product%20slack%20updates/)

### Sprint Planning & Review
1. Document sprint plans in meeting notes
2. Generate Product Review Updates using [Sprint Review Updates](./Sprint%20review%20updates/)
3. Create Growth Sprint Presentation slides

### Communicating Product Changes
1. Extract information from PRDs or sprint notes
2. Use [Product Slack Updates](./product%20slack%20updates/) to generate formatted messages
3. Post to Slack with proper formatting and team tags

## 🤝 Contributing

This is a personal toolkit, but feel free to:
- Suggest improvements
- Add new templates
- Enhance existing tools
- Share feedback

## 📝 License

Personal use - feel free to adapt for your own needs.

## 🔗 Quick Links

- [Flow Diagrams Guide](./Flow%20Diagrams/README.md)
- [PRD Templates](./PRD%20templates/)
- [Sprint Updates Guide](./Sprint%20review%20updates/Templates/README-Sprint-Updates.md)
- [Product Slack Updates Guide](./product%20slack%20updates/README.md)

---

**Built for Product Managers, by a Product Manager** 💼

