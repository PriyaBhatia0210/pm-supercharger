"""
Jira Extractor

Extracts information from Jira tickets using Jira MCP to populate product update Slack messages.
"""

from typing import Dict, List, Optional, Any
import re


class JiraExtractor:
    """Extracts key information from Jira tickets."""
    
    def __init__(self, ticket_key: str, jira_mcp_client=None):
        """
        Initialize Jira extractor.
        
        Args:
            ticket_key: Jira ticket key (e.g., "PD-12345")
            jira_mcp_client: Optional Jira MCP client for fetching ticket data
        """
        self.ticket_key = ticket_key
        self.jira_client = jira_mcp_client
        self.ticket_data = None
        if self.jira_client:
            self._fetch_ticket()
    
    def _fetch_ticket(self):
        """Fetch ticket data from Jira using MCP client."""
        try:
            # Attempt to fetch ticket using Jira MCP
            # This is a placeholder - actual implementation depends on Jira MCP API
            if hasattr(self.jira_client, 'get_issue'):
                self.ticket_data = self.jira_client.get_issue(self.ticket_key)
            elif hasattr(self.jira_client, 'fetch'):
                self.ticket_data = self.jira_client.fetch('issue', {'key': self.ticket_key})
        except Exception as e:
            print(f"Warning: Could not fetch Jira ticket {self.ticket_key}: {e}")
            self.ticket_data = None
    
    def extract_title(self) -> Optional[str]:
        """Extract feature/experiment title from Jira ticket."""
        if self.ticket_data:
            # Extract from ticket data structure
            if isinstance(self.ticket_data, dict):
                return self.ticket_data.get('summary') or self.ticket_data.get('title')
            elif hasattr(self.ticket_data, 'summary'):
                return self.ticket_data.summary
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                return getattr(self.ticket_data.fields, 'summary', None)
        
        # Fallback: use ticket key as title
        return self.ticket_key
    
    def extract_description(self) -> Optional[str]:
        """Extract description from Jira ticket."""
        if self.ticket_data:
            if isinstance(self.ticket_data, dict):
                description = self.ticket_data.get('description') or self.ticket_data.get('body')
                if description:
                    # Remove Jira markup if present
                    return self._clean_jira_markup(description)
            elif hasattr(self.ticket_data, 'description'):
                return self._clean_jira_markup(self.ticket_data.description)
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                desc = getattr(self.ticket_data.fields, 'description', None)
                if desc:
                    return self._clean_jira_markup(desc)
        
        return None
    
    def _clean_jira_markup(self, text: str) -> str:
        """Remove Jira markup from text."""
        if not text:
            return ""
        
        # Remove common Jira markup
        text = re.sub(r'\{code[^\}]*\}', '', text)  # Remove code blocks
        text = re.sub(r'\{panel[^\}]*\}', '', text)  # Remove panels
        text = re.sub(r'\{quote[^\}]*\}', '', text)  # Remove quotes
        text = re.sub(r'\{color[^\}]*\}', '', text)  # Remove color tags
        text = re.sub(r'\{[^\}]+\}', '', text)  # Remove any remaining Jira tags
        text = re.sub(r'\[([^\]]+)\|([^\]]+)\]', r'\1', text)  # Convert links to text
        text = re.sub(r'\[([^\]]+)\]', r'\1', text)  # Remove link brackets
        
        return text.strip()
    
    def extract_why_built(self) -> Optional[str]:
        """Extract 'why we built it' from Jira ticket description."""
        description = self.extract_description()
        if not description:
            return None
        
        # Look for common patterns in description
        patterns = [
            r'(?:Why|Problem|Opportunity)[:\s]+(.+?)(?:\n\n|$)',  # Why/Problem/Opportunity section
            r'##\s+(?:Why|Problem|Opportunity)\s*\n\n(.+?)(?:\n\n##|$)',  # Section header
        ]
        
        for pattern in patterns:
            match = re.search(pattern, description, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        # If no specific section, return first paragraph
        paragraphs = [p.strip() for p in description.split('\n\n') if p.strip()]
        if paragraphs:
            return paragraphs[0]
        
        return None
    
    def extract_how_it_works(self) -> Optional[str]:
        """Extract 'how it works' from Jira ticket."""
        description = self.extract_description()
        if not description:
            return None
        
        patterns = [
            r'(?:How|Approach|Solution)[:\s]+(.+?)(?:\n\n|$)',  # How/Approach/Solution section
            r'##\s+(?:How|Approach|Solution)\s*\n\n(.+?)(?:\n\n##|$)',  # Section header
        ]
        
        for pattern in patterns:
            match = re.search(pattern, description, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_acceptance_criteria(self) -> List[str]:
        """Extract acceptance criteria from Jira ticket."""
        criteria = []
        
        if self.ticket_data:
            if isinstance(self.ticket_data, dict):
                ac = self.ticket_data.get('acceptance_criteria') or self.ticket_data.get('customfield_acceptance_criteria')
                if ac:
                    if isinstance(ac, list):
                        criteria = ac
                    elif isinstance(ac, str):
                        # Split by newlines or bullets
                        criteria = [c.strip() for c in re.split(r'\n|[-*]', ac) if c.strip()]
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                ac = getattr(self.ticket_data.fields, 'acceptance_criteria', None)
                if ac:
                    if isinstance(ac, list):
                        criteria = ac
                    elif isinstance(ac, str):
                        criteria = [c.strip() for c in re.split(r'\n|[-*]', ac) if c.strip()]
        
        # Also try to extract from description
        description = self.extract_description()
        if description and not criteria:
            ac_pattern = r'(?:Acceptance\s+Criteria|AC)[:\s]*(.+?)(?:\n\n##|$)'
            match = re.search(ac_pattern, description, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                ac_text = match.group(1)
                criteria = [c.strip() for c in re.split(r'\n|[-*]', ac_text) if c.strip()]
        
        return criteria
    
    def extract_team_members(self) -> List[str]:
        """Extract team members (assignees, watchers) from Jira ticket."""
        team_members = []
        
        if self.ticket_data:
            if isinstance(self.ticket_data, dict):
                assignee = self.ticket_data.get('assignee')
                if assignee:
                    if isinstance(assignee, dict):
                        team_members.append(assignee.get('displayName') or assignee.get('name'))
                    elif isinstance(assignee, str):
                        team_members.append(assignee)
                
                watchers = self.ticket_data.get('watchers') or self.ticket_data.get('watcher_list')
                if watchers:
                    if isinstance(watchers, list):
                        for watcher in watchers:
                            if isinstance(watcher, dict):
                                team_members.append(watcher.get('displayName') or watcher.get('name'))
                            elif isinstance(watcher, str):
                                team_members.append(watcher)
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                assignee = getattr(self.ticket_data.fields, 'assignee', None)
                if assignee:
                    if hasattr(assignee, 'displayName'):
                        team_members.append(assignee.displayName)
                    elif hasattr(assignee, 'name'):
                        team_members.append(assignee.name)
                    elif isinstance(assignee, str):
                        team_members.append(assignee)
        
        # Clean and deduplicate
        team_members = [m for m in team_members if m]
        return list(set(team_members))
    
    def extract_links(self) -> Dict[str, str]:
        """Extract links from Jira ticket."""
        links = {}
        
        # Jira ticket link
        links['Jira'] = f"https://pandadoc.atlassian.net/browse/{self.ticket_key}"
        
        # Extract links from description
        description = self.extract_description()
        if description:
            link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)|(https?://[^\s\)]+)'
            matches = re.findall(link_pattern, description)
            
            for match in matches:
                text = match[0] if match[0] else match[2]
                url = match[1] if match[1] else match[2]
                
                text_lower = text.lower() if text else ""
                if 'prd' in text_lower or 'product' in text_lower or 'docs.google.com' in url:
                    links['PRD'] = url
                elif 'figma' in text_lower or 'figma.com' in url:
                    links['Figma'] = url
        
        return links
    
    def extract_sprint_info(self) -> Optional[str]:
        """Extract sprint information from Jira ticket."""
        if self.ticket_data:
            if isinstance(self.ticket_data, dict):
                sprint = self.ticket_data.get('sprint') or self.ticket_data.get('customfield_sprint')
                if sprint:
                    if isinstance(sprint, dict):
                        return sprint.get('name')
                    elif isinstance(sprint, str):
                        return sprint
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                sprint = getattr(self.ticket_data.fields, 'sprint', None)
                if sprint:
                    if hasattr(sprint, 'name'):
                        return sprint.name
                    elif isinstance(sprint, str):
                        return sprint
        
        return None
    
    def extract_epic(self) -> Optional[str]:
        """Extract epic information from Jira ticket."""
        if self.ticket_data:
            if isinstance(self.ticket_data, dict):
                epic = self.ticket_data.get('epic') or self.ticket_data.get('customfield_epic')
                if epic:
                    if isinstance(epic, dict):
                        return epic.get('name') or epic.get('key')
                    elif isinstance(epic, str):
                        return epic
            elif hasattr(self.ticket_data, 'fields') and self.ticket_data.fields:
                epic = getattr(self.ticket_data.fields, 'epic', None)
                if epic:
                    if hasattr(epic, 'name'):
                        return epic.name
                    elif hasattr(epic, 'key'):
                        return epic.key
                    elif isinstance(epic, str):
                        return epic
        
        return None
    
    def extract_all(self) -> Dict[str, Any]:
        """Extract all information from Jira ticket."""
        return {
            'title': self.extract_title(),
            'description': self.extract_description(),
            'why_built': self.extract_why_built(),
            'how_it_works': self.extract_how_it_works(),
            'acceptance_criteria': self.extract_acceptance_criteria(),
            'team_members': self.extract_team_members(),
            'links': self.extract_links(),
            'sprint': self.extract_sprint_info(),
            'epic': self.extract_epic(),
        }

