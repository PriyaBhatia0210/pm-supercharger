#!/usr/bin/env python3
"""
Product Update Generator

Generates product update Slack messages from PRDs, sprint notes, or Jira tickets.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List
from jinja2 import Environment, FileSystemLoader, Template

# Add extractors to path
sys.path.insert(0, str(Path(__file__).parent))

from extractors.prd_extractor import PRDExtractor
from extractors.sprint_notes_extractor import SprintNotesExtractor
from extractors.jira_extractor import JiraExtractor


class ProductUpdateGenerator:
    """Generates product update Slack messages from various sources."""
    
    def __init__(self, templates_dir: Optional[Path] = None):
        """
        Initialize generator.
        
        Args:
            templates_dir: Directory containing templates (defaults to Templates/ relative to script)
        """
        if templates_dir is None:
            templates_dir = Path(__file__).parent.parent / "Templates"
        self.templates_dir = Path(templates_dir)
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def format_team_members(self, members: List[str]) -> str:
        """Format team members as Slack tags."""
        if not members:
            return ""
        
        formatted = []
        for member in members:
            # Convert name to Slack format
            # If it's already a tag, keep it; otherwise format as @username
            if member.startswith('@'):
                formatted.append(member)
            elif ' ' in member:
                # Full name - convert to username format (first.last)
                name_parts = member.lower().split()
                username = '.'.join(name_parts)
                formatted.append(f"@{username}")
            else:
                formatted.append(f"@{member}")
        
        return " ".join(formatted)
    
    def format_stakeholders(self, stakeholders: List[str]) -> str:
        """Format stakeholders as Slack tags."""
        if not stakeholders:
            return ""
        
        formatted = []
        for stakeholder in stakeholders:
            if stakeholder.startswith('@'):
                formatted.append(stakeholder)
            else:
                # Common stakeholder groups
                stakeholder_lower = stakeholder.lower()
                if 'support' in stakeholder_lower:
                    formatted.append("@supportteam")
                elif 'ams' in stakeholder_lower or 'account manager' in stakeholder_lower:
                    formatted.append("@ams")
                elif 'csm' in stakeholder_lower or 'customer success' in stakeholder_lower:
                    formatted.append("@csms")
                else:
                    formatted.append(f"@{stakeholder}")
        
        return " ".join(formatted)
    
    def format_links(self, links: Dict[str, str]) -> str:
        """Format links as markdown list."""
        if not links:
            return ""
        
        formatted = []
        for label, url in links.items():
            formatted.append(f"* [{label}]({url})")
        
        return "\n".join(formatted)
    
    def format_bullet_list(self, items: List[str]) -> str:
        """Format list of items as bullet points."""
        if not items:
            return ""
        
        return "\n".join([f"* {item}" for item in items])
    
    def determine_update_type(self, data: Dict[str, Any], explicit_type: Optional[str] = None) -> str:
        """Determine update type from data."""
        if explicit_type:
            return explicit_type.lower()
        
        # Check for experiment indicators
        if data.get('hypothesis') or 'experiment' in str(data.get('title', '')).lower():
            return 'experiment'
        
        # Check for rollout indicators
        if 'rollout' in str(data.get('title', '')).lower() or data.get('rollout_plan'):
            return 'rollout'
        
        # Check for iteration indicators
        if 'iteration' in str(data.get('title', '')).lower():
            return 'iteration'
        
        # Default to feature
        return 'feature'
    
    def get_template_name(self, update_type: str) -> str:
        """Get template filename for update type."""
        template_map = {
            'experiment': 'Product-Update-Template-Experiment.md',
            'rollout': 'Product-Update-Template-Rollout.md',
            'feature': 'Product-Update-Template-Feature.md',
            'iteration': 'Product-Update-Template-Iteration.md',
        }
        return template_map.get(update_type, 'Product-Update-Template-Feature.md')
    
    def prepare_template_data(self, extracted_data: Dict[str, Any], update_type: str) -> Dict[str, Any]:
        """Prepare data for template rendering."""
        data = extracted_data.copy()
        
        # Format team members
        if 'team_members' in data:
            data['team_members'] = self.format_team_members(data['team_members'])
        
        # Format stakeholders
        if 'stakeholders' in data:
            data['stakeholders'] = self.format_stakeholders(data['stakeholders'])
        
        # Format links
        if 'links' in data:
            data['links'] = self.format_links(data['links'])
        
        # Format lists as bullet points
        for key in ['objectives', 'success_metrics', 'decisions', 'action_items', 
                   'acceptance_criteria', 'feature_flags']:
            if key in data and isinstance(data[key], list):
                data[key] = self.format_bullet_list(data[key])
        
        # Set update type
        data['update_type'] = update_type
        data['type'] = update_type.capitalize()
        
        # Ensure title has type tag if not present
        title = data.get('title', '')
        if title and not title.startswith('['):
            type_tag = update_type.capitalize()
            if update_type == 'rollout':
                type_tag = 'Gradual Rollout'
            data['title'] = f"[{type_tag}] {title}"
        
        return data
    
    def generate_from_prd(self, prd_path: str, update_type: Optional[str] = None) -> str:
        """Generate message from PRD file."""
        extractor = PRDExtractor(prd_path)
        extracted = extractor.extract_all()
        
        update_type = self.determine_update_type(extracted, update_type)
        template_data = self.prepare_template_data(extracted, update_type)
        
        template_name = self.get_template_name(update_type)
        template = self.env.get_template(template_name)
        
        return template.render(**template_data)
    
    def generate_from_sprint_notes(self, notes_path: str, update_type: Optional[str] = None) -> str:
        """Generate message from sprint notes."""
        extractor = SprintNotesExtractor(notes_path)
        extracted = extractor.extract_all()
        
        update_type = self.determine_update_type(extracted, update_type)
        template_data = self.prepare_template_data(extracted, update_type)
        
        template_name = self.get_template_name(update_type)
        template = self.env.get_template(template_name)
        
        return template.render(**template_data)
    
    def generate_from_jira(self, ticket_key: str, jira_client=None, update_type: Optional[str] = None) -> str:
        """Generate message from Jira ticket."""
        extractor = JiraExtractor(ticket_key, jira_client)
        extracted = extractor.extract_all()
        
        update_type = self.determine_update_type(extracted, update_type)
        template_data = self.prepare_template_data(extracted, update_type)
        
        template_name = self.get_template_name(update_type)
        template = self.env.get_template(template_name)
        
        return template.render(**template_data)
    
    def generate_from_dict(self, data: Dict[str, Any], update_type: Optional[str] = None) -> str:
        """Generate message from dictionary data."""
        update_type = self.determine_update_type(data, update_type)
        template_data = self.prepare_template_data(data, update_type)
        
        template_name = self.get_template_name(update_type)
        template = self.env.get_template(template_name)
        
        return template.render(**template_data)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate product update Slack messages from various sources'
    )
    parser.add_argument(
        '--prd',
        type=str,
        help='Path to PRD markdown file'
    )
    parser.add_argument(
        '--sprint-notes',
        type=str,
        help='Path to sprint notes markdown file'
    )
    parser.add_argument(
        '--jira',
        type=str,
        help='Jira ticket key (e.g., PD-12345)'
    )
    parser.add_argument(
        '--type',
        type=str,
        choices=['experiment', 'rollout', 'feature', 'iteration'],
        help='Explicit update type (overrides auto-detection)'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (default: stdout)'
    )
    
    args = parser.parse_args()
    
    generator = ProductUpdateGenerator()
    
    try:
        if args.prd:
            message = generator.generate_from_prd(args.prd, args.type)
        elif args.sprint_notes:
            message = generator.generate_from_sprint_notes(args.sprint_notes, args.type)
        elif args.jira:
            message = generator.generate_from_jira(args.jira, update_type=args.type)
        else:
            parser.error("Must specify one of --prd, --sprint-notes, or --jira")
        
        if args.output:
            Path(args.output).write_text(message, encoding='utf-8')
            print(f"Message written to {args.output}")
        else:
            print(message)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

