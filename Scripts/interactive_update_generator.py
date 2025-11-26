#!/usr/bin/env python3
"""
Interactive Product Update Generator

Interactive CLI that prompts for missing information and generates product update Slack messages.
"""

import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_product_update import ProductUpdateGenerator
from extractors.prd_extractor import PRDExtractor
from extractors.sprint_notes_extractor import SprintNotesExtractor
from extractors.jira_extractor import JiraExtractor


class InteractiveGenerator:
    """Interactive generator that prompts for missing information."""
    
    def __init__(self):
        """Initialize interactive generator."""
        self.generator = ProductUpdateGenerator()
        self.data: Dict[str, Any] = {}
    
    def prompt(self, question: str, default: Optional[str] = None, required: bool = False) -> str:
        """Prompt user for input."""
        prompt_text = question
        if default:
            prompt_text += f" [{default}]"
        if required:
            prompt_text += " *"
        prompt_text += ": "
        
        while True:
            response = input(prompt_text).strip()
            if response:
                return response
            elif default:
                return default
            elif not required:
                return ""
            else:
                print("This field is required. Please provide a value.")
    
    def prompt_list(self, question: str, default: Optional[List[str]] = None) -> List[str]:
        """Prompt user for a list of items."""
        print(question)
        if default:
            print(f"Default: {', '.join(default)}")
        print("Enter items (one per line, empty line to finish):")
        
        items = []
        while True:
            item = input().strip()
            if not item:
                break
            items.append(item)
        
        return items if items else (default or [])
    
    def prompt_yes_no(self, question: str, default: bool = False) -> bool:
        """Prompt user for yes/no answer."""
        default_text = "Y/n" if default else "y/N"
        response = input(f"{question} [{default_text}]: ").strip().lower()
        
        if not response:
            return default
        
        return response in ['y', 'yes', 'true', '1']
    
    def select_option(self, question: str, options: List[str]) -> str:
        """Prompt user to select from options."""
        print(question)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                choice = int(input("Select option: ").strip())
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(options)}")
            except ValueError:
                print("Please enter a valid number")
    
    def collect_basic_info(self):
        """Collect basic information."""
        print("\n=== Basic Information ===")
        
        self.data['title'] = self.prompt("Feature/Experiment name", required=True)
        
        update_types = ['experiment', 'rollout', 'feature', 'iteration']
        update_type = self.select_option("Update type", update_types)
        self.data['update_type'] = update_type
        self.data['type'] = update_type.capitalize()
        
        if update_type == 'iteration':
            self.data['iteration_number'] = self.prompt("Iteration number (e.g., 3)", required=True)
    
    def collect_why_built(self):
        """Collect 'why we built it' information."""
        print("\n=== Why We Built It ===")
        self.data['why_built'] = self.prompt(
            "Why we built this feature/experiment",
            required=True
        )
    
    def collect_hypothesis(self):
        """Collect hypothesis (for experiments)."""
        if self.data.get('update_type') == 'experiment':
            print("\n=== Hypothesis ===")
            self.data['hypothesis'] = self.prompt("Hypothesis", required=True)
    
    def collect_how_it_works(self):
        """Collect 'how it works' information."""
        print("\n=== How It Works ===")
        self.data['how_it_works'] = self.prompt("How it works", required=True)
    
    def collect_objectives(self):
        """Collect objectives/success metrics."""
        print("\n=== Objectives / Success Metrics ===")
        objectives = self.prompt_list("Enter objectives/success metrics")
        self.data['objectives'] = objectives
        self.data['success_metrics'] = objectives
    
    def collect_timeline(self):
        """Collect timeline/rollout plan."""
        print("\n=== Timeline / Rollout Plan ===")
        if self.data.get('update_type') == 'rollout':
            self.data['rollout_plan'] = self.prompt("Rollout plan", required=True)
        else:
            self.data['timeline'] = self.prompt("Timeline")
    
    def collect_team_info(self):
        """Collect team member and stakeholder information."""
        print("\n=== Team Information ===")
        team_members = self.prompt_list("Enter team members (usernames or names)")
        self.data['team_members'] = team_members
        
        channel = self.prompt("Team channel (e.g., #team-mooncake)")
        if channel:
            self.data['channel_mention'] = channel
        
        stakeholders = self.prompt_list("Enter stakeholders (e.g., @supportteam, @ams)")
        self.data['stakeholders'] = stakeholders
    
    def collect_links(self):
        """Collect links."""
        print("\n=== Links ===")
        links = {}
        
        if self.prompt_yes_no("Do you have a PRD link?"):
            links['PRD'] = self.prompt("PRD URL", required=True)
        
        if self.prompt_yes_no("Do you have a Jira ticket link?"):
            links['Jira'] = self.prompt("Jira URL", required=True)
        
        if self.prompt_yes_no("Do you have a Figma link?"):
            links['Figma'] = self.prompt("Figma URL", required=True)
        
        self.data['links'] = links
    
    def collect_feature_flags(self):
        """Collect feature flags."""
        if self.prompt_yes_no("Do you have feature flags?"):
            flags = self.prompt_list("Enter feature flags (one per line)")
            self.data['feature_flags'] = flags
    
    def collect_optional_sections(self):
        """Collect optional sections."""
        print("\n=== Optional Sections ===")
        
        if self.prompt_yes_no("Do you want to add monitoring section?"):
            monitoring = self.prompt_list("What are you monitoring?")
            self.data['monitoring'] = monitoring
        
        if self.prompt_yes_no("Do you want to add guardrails section?"):
            guardrails = self.prompt_list("What are the guardrails?")
            self.data['guardrails'] = guardrails
        
        if self.prompt_yes_no("Do you want to add 'how you can help' section?"):
            how_to_help = self.prompt_list("How can people help?")
            self.data['how_to_help'] = how_to_help
    
    def load_from_source(self):
        """Load initial data from source file."""
        print("\n=== Load from Source ===")
        source_types = ['PRD', 'Sprint Notes', 'Jira', 'Start from scratch']
        source_type = self.select_option("Load data from source?", source_types)
        
        if source_type == 'Start from scratch':
            return
        
        if source_type == 'PRD':
            prd_path = self.prompt("PRD file path", required=True)
            try:
                extractor = PRDExtractor(prd_path)
                self.data = extractor.extract_all()
                print("✓ Loaded data from PRD")
            except Exception as e:
                print(f"Error loading PRD: {e}")
                return
        
        elif source_type == 'Sprint Notes':
            notes_path = self.prompt("Sprint notes file path", required=True)
            try:
                extractor = SprintNotesExtractor(notes_path)
                self.data = extractor.extract_all()
                print("✓ Loaded data from sprint notes")
            except Exception as e:
                print(f"Error loading sprint notes: {e}")
                return
        
        elif source_type == 'Jira':
            ticket_key = self.prompt("Jira ticket key (e.g., PD-12345)", required=True)
            try:
                extractor = JiraExtractor(ticket_key)
                self.data = extractor.extract_all()
                print("✓ Loaded data from Jira ticket")
            except Exception as e:
                print(f"Error loading Jira ticket: {e}")
                return
    
    def generate_preview(self) -> str:
        """Generate preview of message."""
        update_type = self.data.get('update_type', 'feature')
        return self.generator.generate_from_dict(self.data, update_type)
    
    def run(self):
        """Run interactive generator."""
        print("=" * 60)
        print("Product Update Slack Message Generator")
        print("=" * 60)
        
        # Load from source if desired
        self.load_from_source()
        
        # Collect information
        if not self.data.get('title'):
            self.collect_basic_info()
        else:
            # Confirm or update basic info
            print(f"\nCurrent title: {self.data.get('title')}")
            if not self.prompt_yes_no("Use this title?", default=True):
                self.data['title'] = self.prompt("Feature/Experiment name", required=True)
        
        if not self.data.get('why_built'):
            self.collect_why_built()
        
        if self.data.get('update_type') == 'experiment' and not self.data.get('hypothesis'):
            self.collect_hypothesis()
        
        if not self.data.get('how_it_works'):
            self.collect_how_it_works()
        
        if not self.data.get('objectives') and not self.data.get('success_metrics'):
            self.collect_objectives()
        
        if not self.data.get('timeline') and not self.data.get('rollout_plan'):
            self.collect_timeline()
        
        if not self.data.get('team_members'):
            self.collect_team_info()
        else:
            # Confirm or update team info
            print(f"\nCurrent team members: {', '.join(self.data.get('team_members', []))}")
            if not self.prompt_yes_no("Use these team members?", default=True):
                self.collect_team_info()
        
        if not self.data.get('links'):
            self.collect_links()
        
        self.collect_feature_flags()
        self.collect_optional_sections()
        
        # Generate preview
        print("\n" + "=" * 60)
        print("Preview:")
        print("=" * 60)
        preview = self.generate_preview()
        print(preview)
        print("=" * 60)
        
        # Confirm and save
        if self.prompt_yes_no("\nSave this message?", default=True):
            output_path = self.prompt("Output file path", default="product_update.md")
            Path(output_path).write_text(preview, encoding='utf-8')
            print(f"✓ Message saved to {output_path}")
        else:
            print("Message not saved.")


def main():
    """Main entry point."""
    try:
        generator = InteractiveGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

