"""
Sprint Notes Extractor

Extracts information from sprint meeting notes to populate product update Slack messages.
"""

import re
from typing import Dict, List, Optional, Any
from pathlib import Path


class SprintNotesExtractor:
    """Extracts key information from sprint meeting notes."""
    
    def __init__(self, notes_path: str):
        """
        Initialize sprint notes extractor.
        
        Args:
            notes_path: Path to sprint notes markdown file
        """
        self.notes_path = Path(notes_path)
        self.content = self._read_notes()
    
    def _read_notes(self) -> str:
        """Read sprint notes file content."""
        if not self.notes_path.exists():
            raise FileNotFoundError(f"Sprint notes file not found: {self.notes_path}")
        return self.notes_path.read_text(encoding='utf-8')
    
    def extract_title(self) -> Optional[str]:
        """Extract project/feature title from sprint notes."""
        patterns = [
            r'##\s+\*\*Project\s+Overview[:\s]+(.+?)\*\*',  # Project Overview: Title
            r'##\s+Project\s+Overview[:\s]+(.+?)(?:\n|$)',  # Project Overview: ...
            r'#\s+\[Sprint[^\]]+\]\s+(.+?)(?:\n|$)',  # [Sprint ...] Title
            r'##\s+Project\s+Overview\s*\n\n\*\*(.+?)\*\*',  # Project Overview with bold title
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_sprint_goal(self) -> Optional[str]:
        """Extract sprint goal from notes."""
        patterns = [
            r'\*\*Sprint\s+goal[:\s]+\*\*(.+?)(?:\n|$)',  # Sprint goal: ...
            r'Sprint\s+goal[:\s]+(.+?)(?:\n|$)',  # Sprint goal ...
            r'##\s+Sprint\s+Planning\s+Decisions\s*\n\n\*\*Sprint\s+goal[:\s]+\*\*(.+?)(?:\n|$)',  # In sprint planning section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_why_built(self) -> Optional[str]:
        """Extract 'why we built it' from sprint notes."""
        # Look for goal, approach, or problem sections
        patterns = [
            r'##\s+Project\s+Overview[:\s]*\*\*(.+?)\*\*\s*\n\n(.+?)(?:\n\n##|$)',  # Project Overview content
            r'\*\*Goal[:\s]+\*\*(.+?)(?:\n|$)',  # Goal: ...
            r'##\s+Project\s+Overview\s*\n\n(.+?)(?:\n\n##|$)',  # Project Overview section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1) if len(match.groups()) == 1 else match.group(2)
                if content:
                    return content.strip()
        
        return None
    
    def extract_how_it_works(self) -> Optional[str]:
        """Extract 'how it works' from sprint notes."""
        patterns = [
            r'##\s+Technical\s+Architecture\s+Discussion\s*\n\n(.+?)(?:\n\n##|$)',  # Technical Architecture
            r'\*\*Approach[:\s]+\*\*(.+?)(?:\n\n|$)',  # Approach: ...
            r'##\s+Approach\s*\n\n(.+?)(?:\n\n##|$)',  # Approach section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_decisions(self) -> List[str]:
        """Extract key decisions from sprint notes."""
        decisions = []
        
        patterns = [
            r'##\s+Sprint\s+Planning\s+Decisions\s*\n\n(.+?)(?:\n\n##|$)',  # Sprint Planning Decisions
            r'##\s+Decisions\s*\n\n(.+?)(?:\n\n##|$)',  # Decisions section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
                # Extract bullet points
                bullets = re.findall(r'^\s*[-*]\s+(.+?)$', content, re.MULTILINE)
                decisions.extend(bullets)
                break
        
        return decisions
    
    def extract_action_items(self) -> List[str]:
        """Extract action items from sprint notes."""
        action_items = []
        
        patterns = [
            r'##\s+Next\s+Steps\s*/\s*Action\s+Items\s*\n\n(.+?)(?:\n\n##|$)',  # Next Steps / Action Items
            r'##\s+Action\s+Items\s*\n\n(.+?)(?:\n\n##|$)',  # Action Items section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
                # Extract bullet points with assignees
                bullets = re.findall(r'^\s*[-*]\s+(.+?)$', content, re.MULTILINE)
                action_items.extend(bullets)
                break
        
        return action_items
    
    def extract_team_members(self) -> List[str]:
        """Extract team members from sprint notes."""
        team_members = []
        
        # Look for participants section
        patterns = [
            r'Participants[:\s]+(.+?)(?:\n|$)',  # Participants: ...
            r'Owner[:\s]+(.+?)(?:\n|$)',  # Owner: ...
            r'##\s+Participants\s*\n\n(.+?)(?:\n\n##|$)',  # Participants section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                content = match.group(1)
                # Split by comma or newline
                members = re.split(r'[,;\n]', content)
                team_members.extend([m.strip() for m in members if m.strip()])
                break
        
        # Also look for action item assignees
        action_items = self.extract_action_items()
        for item in action_items:
            # Look for patterns like "Name:" or "* Name:"
            assignee_match = re.search(r'^\s*[-*]?\s*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)[:\s]', item)
            if assignee_match:
                team_members.append(assignee_match.group(1))
        
        # Clean and deduplicate
        team_members = [m.strip() for m in team_members if m.strip()]
        return list(set(team_members))
    
    def extract_timeline(self) -> Optional[str]:
        """Extract timeline information from sprint notes."""
        # Look for dates, sprints, or timeline mentions
        patterns = [
            r'Date[:\s]+(.+?)(?:\n|$)',  # Date: ...
            r'Sprint\s+#?\d+',  # Sprint number
            r'##\s+Timeline\s*\n\n(.+?)(?:\n\n##|$)',  # Timeline section
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                if match.groups():
                    return match.group(1).strip()
                else:
                    return match.group(0).strip()
        
        return None
    
    def extract_links(self) -> Dict[str, str]:
        """Extract links from sprint notes."""
        links = {}
        
        # Extract markdown links
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        matches = re.findall(link_pattern, self.content)
        
        for text, url in matches:
            text_lower = text.lower()
            if 'prd' in text_lower or 'product' in text_lower:
                links['PRD'] = url
            elif 'jira' in text_lower or 'atlassian' in text_lower:
                links['Jira'] = url
            elif 'figma' in text_lower:
                links['Figma'] = url
            elif 'notes' in text_lower:
                links['Notes'] = url
        
        return links
    
    def extract_all(self) -> Dict[str, Any]:
        """Extract all information from sprint notes."""
        return {
            'title': self.extract_title(),
            'sprint_goal': self.extract_sprint_goal(),
            'why_built': self.extract_why_built(),
            'how_it_works': self.extract_how_it_works(),
            'decisions': self.extract_decisions(),
            'action_items': self.extract_action_items(),
            'team_members': self.extract_team_members(),
            'timeline': self.extract_timeline(),
            'links': self.extract_links(),
        }

