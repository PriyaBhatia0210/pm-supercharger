"""
PRD Extractor

Extracts information from PRD markdown files to populate product update Slack messages.
"""

import re
from typing import Dict, List, Optional, Any
from pathlib import Path


class PRDExtractor:
    """Extracts key information from PRD markdown files."""
    
    def __init__(self, prd_path: str):
        """
        Initialize PRD extractor.
        
        Args:
            prd_path: Path to PRD markdown file
        """
        self.prd_path = Path(prd_path)
        self.content = self._read_prd()
    
    def _read_prd(self) -> str:
        """Read PRD file content."""
        if not self.prd_path.exists():
            raise FileNotFoundError(f"PRD file not found: {self.prd_path}")
        return self.prd_path.read_text(encoding='utf-8')
    
    def extract_title(self) -> Optional[str]:
        """Extract feature/experiment title from PRD."""
        # Look for title in various formats
        patterns = [
            r'^#\s+(.+?)$',  # Main heading
            r'\*\*([^*]+)\*\*',  # Bold title
            r'##\s+PRD\s+•\s+(.+?)\s+•',  # PRD title format
            r'##\s+(.+?)\s+•\s+Q\d',  # PRD with quarter
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_objective(self) -> Optional[str]:
        """Extract objective from PRD."""
        patterns = [
            r'\*\*Objective\*\*:\s*(.+?)(?:\n|$)',  # Objective: ...
            r'##\s+OBJECTIVE\s*\n\n(.+?)(?:\n\n|$)',  # OBJECTIVE section
            r'Objective[:\s]+(.+?)(?:\n|$)',  # Objective ...
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_hypothesis(self) -> Optional[str]:
        """Extract hypothesis from PRD."""
        patterns = [
            r'\*\*Hypothesis\*\*[:\s]*(.+?)(?:\n\n|$)',  # Hypothesis: ...
            r'##\s+HYPOTHESIS\s*\n\n(.+?)(?:\n\n|$)',  # HYPOTHESIS section
            r'Hypothesis[:\s]+(.+?)(?:\n\n|$)',  # Hypothesis ...
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_why_built(self) -> Optional[str]:
        """Extract 'why we built it' from PRD."""
        # Look for problem statement, opportunity, or why sections
        patterns = [
            r'##\s+OPPORTUNITY\s*\n\n(.+?)(?:\n\n##|$)',  # OPPORTUNITY section
            r'##\s+PROBLEM\s*\n\n(.+?)(?:\n\n##|$)',  # PROBLEM section
            r'###\s+Why\s+We\s+Built\s+It\s*\n\n(.+?)(?:\n\n|$)',  # Why We Built It
            r'Why\s+we\s+built\s+it[:\s]*(.+?)(?:\n\n|$)',  # Why we built it
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_how_it_works(self) -> Optional[str]:
        """Extract 'how it works' from PRD."""
        patterns = [
            r'##\s+APPROACH[,\s]+HYPOTHESIS\s*\n\n(.+?)(?:\n\n##|$)',  # APPROACH section
            r'###\s+How\s+It\s+Works\s*\n\n(.+?)(?:\n\n|$)',  # How It Works
            r'##\s+FUNCTIONAL\s+SPECIFICATION\s*\n\n(.+?)(?:\n\n##|$)',  # Functional spec
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_success_metrics(self) -> List[str]:
        """Extract success metrics from PRD."""
        metrics = []
        
        # Look for success metrics section
        patterns = [
            r'##\s+SUCCESS\s+METRICS\s*\n\n(.+?)(?:\n\n##|$)',  # SUCCESS METRICS section
            r'\*\*Success\s+metrics\*\*\s*\n\n(.+?)(?:\n\n|$)',  # Success metrics
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
                # Extract bullet points
                bullets = re.findall(r'^\s*[-*]\s+(.+?)$', content, re.MULTILINE)
                metrics.extend(bullets)
                break
        
        # Also look for metrics table
        table_pattern = r'\|\s*Metric\s*\|\s*Target\s*\|\s*Owner\s*\|'
        if re.search(table_pattern, self.content, re.IGNORECASE):
            # Extract metric names from table
            metric_rows = re.findall(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', self.content)
            for metric, target in metric_rows:
                if metric.strip() and 'Metric' not in metric:
                    metrics.append(f"{metric.strip()}: {target.strip()}")
        
        return metrics
    
    def extract_timeline(self) -> Optional[str]:
        """Extract timeline/rollout plan from PRD."""
        patterns = [
            r'##\s+TIMELINE\s*\n\n(.+?)(?:\n\n##|$)',  # TIMELINE section
            r'##\s+ROLLOUT\s+PLAN\s*\n\n(.+?)(?:\n\n##|$)',  # ROLLOUT PLAN section
            r'###\s+Timeline\s*\n\n(.+?)(?:\n\n|$)',  # Timeline
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return None
    
    def extract_team_members(self) -> List[str]:
        """Extract team members from PRD."""
        team_members = []
        
        # Look for team section or DRI mentions
        patterns = [
            r'Product\s+DRI\s+\[([^\]]+)\]',  # Product DRI
            r'Engineering\s+DRI\s+\[([^\]]+)\]',  # Engineering DRI
            r'Design\s+DRI\s+\[([^\]]+)\]',  # Design DRI
            r'PMM\s+DRI\s+\[([^\]]+)\]',  # PMM DRI
            r'Core\s+Team[:\s]*(.+?)(?:\n\n|$)',  # Core Team section
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            team_members.extend(matches)
        
        # Also look for email links that might contain names
        email_pattern = r'\[([^\]]+)\]\(mailto:[^\)]+\)'
        email_matches = re.findall(email_pattern, self.content)
        team_members.extend(email_matches)
        
        # Clean and deduplicate
        team_members = [m.strip() for m in team_members if m.strip()]
        return list(set(team_members))
    
    def extract_stakeholders(self) -> List[str]:
        """Extract stakeholders from PRD."""
        stakeholders = []
        
        # Look for stakeholders section
        patterns = [
            r'##\s+Stakeholders\s*\n\n(.+?)(?:\n\n##|$)',  # Stakeholders section
            r'\*\*Stakeholders\*\*\s*\n\n(.+?)(?:\n\n|$)',  # Stakeholders
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
            if match:
                content = match.group(1)
                # Extract bullet points
                bullets = re.findall(r'^\s*[-*]\s+(.+?)$', content, re.MULTILINE)
                stakeholders.extend(bullets)
                break
        
        return stakeholders
    
    def extract_links(self) -> Dict[str, str]:
        """Extract links (PRD, Jira, Figma) from PRD."""
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
            elif 'docs.google.com' in url:
                if 'PRD' not in links:
                    links['PRD'] = url
        
        return links
    
    def extract_feature_flags(self) -> List[str]:
        """Extract feature flags from PRD."""
        flags = []
        
        # Look for feature flag mentions
        patterns = [
            r'Feature\s+Flag[s]?[:\s]+(.+?)(?:\n|$)',  # Feature Flag: ...
            r'Feature\s+flag[s]?[:\s]+(.+?)(?:\n|$)',  # Feature flag: ...
            r'exp_\w+',  # Experiment flags (exp_*)
            r'cpq_\w+',  # CPQ flags (cpq_*)
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, self.content, re.MULTILINE | re.IGNORECASE)
            flags.extend(matches)
        
        return list(set(flags))
    
    def extract_all(self) -> Dict[str, Any]:
        """Extract all information from PRD."""
        return {
            'title': self.extract_title(),
            'objective': self.extract_objective(),
            'hypothesis': self.extract_hypothesis(),
            'why_built': self.extract_why_built(),
            'how_it_works': self.extract_how_it_works(),
            'success_metrics': self.extract_success_metrics(),
            'timeline': self.extract_timeline(),
            'team_members': self.extract_team_members(),
            'stakeholders': self.extract_stakeholders(),
            'links': self.extract_links(),
            'feature_flags': self.extract_feature_flags(),
        }

