#!/usr/bin/env python3
"""
Test script to simulate the interactive update generator flow
"""

import sys
from pathlib import Path

# Add Scripts to path
sys.path.insert(0, str(Path(__file__).parent / "Scripts"))

from interactive_update_generator import InteractiveGenerator

def simulate_interactive_flow():
    """Simulate the interactive flow with test data."""
    generator = InteractiveGenerator()
    
    print("=" * 60)
    print("SIMULATED Interactive Product Update Generator")
    print("=" * 60)
    print()
    
    # Simulate: Start from scratch
    print("=== Simulating: Start from scratch ===")
    print()
    
    # Set test data
    generator.data = {
        'title': 'Smart Document Recommendations',
        'update_type': 'feature',
        'type': 'Feature',
        'why_built': 'Users struggle to find relevant templates and documents. We want to help them discover content faster using AI-powered recommendations based on their usage patterns.',
        'how_it_works': 'The system analyzes user behavior, document types, and industry patterns to suggest relevant templates and documents. Recommendations appear in the document lister and template gallery.',
        'objectives': [
            'Increase template usage by 25%',
            'Reduce time to create first document by 30%',
            'Improve user satisfaction score to 4.5+'
        ],
        'timeline': 'Rollout starting Q1 2025: 10% → 25% → 50% → 100% over 8 weeks',
        'team_members': ['priya.bhatia', 'alona.zaleska', 'teamspirit'],
        'stakeholders': ['supportteam', 'csms'],
        'links': {
            'PRD': 'https://docs.google.com/document/d/example-prd',
            'Jira': 'https://pandadoc.atlassian.net/browse/PD-12345',
            'Figma': 'https://figma.com/design/example'
        },
        'feature_flags': ['exp_smart_recommendations', 'feature_smart_docs']
    }
    
    print("✓ Test data loaded")
    print()
    
    # Generate preview
    print("=" * 60)
    print("Preview:")
    print("=" * 60)
    preview = generator.generate_preview()
    print(preview)
    print("=" * 60)
    print()
    
    # Save to file
    output_path = "test-interactive-output.md"
    Path(output_path).write_text(preview, encoding='utf-8')
    print(f"✓ Message saved to {output_path}")
    print()
    
    return output_path

if __name__ == '__main__':
    try:
        output_file = simulate_interactive_flow()
        print(f"\n✅ Test completed successfully! Check {output_file}")
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

