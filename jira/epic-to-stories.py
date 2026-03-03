#!/usr/bin/env python3
"""
JIRA Epic to Stories Automation Tool
Parses epic descriptions and creates stories automatically
"""

import subprocess
import re
import sys
import json
from typing import List, Dict, Tuple

class JiraEpicToStories:
    def __init__(self, epic_key: str):
        self.epic_key = epic_key
        self.epic_data = None
        
    def fetch_epic(self) -> str:
        """Fetch epic content using jira CLI"""
        print(f"Fetching epic {self.epic_key}...")
        try:
            # Use Popen to handle interactive output
            process = subprocess.Popen(
                ["jira", "issue", "view", self.epic_key],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a bit for output then send 'q' to quit pager
            import time
            time.sleep(3)
            
            try:
                stdout, stderr = process.communicate(input='q', timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
            
            return stdout
        except Exception as e:
            print(f"Error fetching epic: {e}")
            sys.exit(1)
    
    def parse_stories(self, epic_content: str) -> List[Dict[str, str]]:
        """
        Parse stories from epic description
        Expected format:
        Stories: or **Stories**:
        • Story title
          • (optional) Additional context
        • Another story title
        """
        stories = []
        # Remove all ANSI escape codes first
        clean_content = re.sub(r'\x1b\[[0-9;]+m', '', epic_content)
        lines = clean_content.split('\n')
        
        # Find Stories section (handle both "Stories:" and "**Stories**:")
        in_stories_section = False
        current_story = None
        
        for line in lines:
            # Check if we're in the Stories section
            if re.search(r'\*?\*?Stories\*?\*?:', line):
                in_stories_section = True
                continue
            
            # Exit stories section if we hit another section or separator
            if in_stories_section:
                if '————' in line or 'Linked Issues' in line or line.strip().startswith('View this issue'):
                    break
            
            if in_stories_section:
                # Look for bullets - handle different spacing
                # Main story bullet: "  • Story text" or "    • Story text"
                match = re.match(r'^(\s{2,4})•\s+(.+)', line)
                if match:
                    indent = len(match.group(1))
                    text = match.group(2).strip()
                    
                    # If this looks like a top-level story (less indent, 2 spaces)
                    if indent == 2 and text:
                        # Save previous story if exists
                        if current_story:
                            stories.append(current_story)
                        
                        current_story = {
                            'summary': text,
                            'description': text
                        }
                    # Sub-bullet (more indent, 6 spaces) - additional context
                    elif current_story and indent > 2 and text:
                        if text != current_story['summary']:
                            current_story['description'] += f"\n\n{text}"
        
        # Add last story
        if current_story:
            stories.append(current_story)
        
        return stories
    
    def create_story(self, summary: str, description: str, dry_run: bool = False) -> Tuple[bool, str]:
        """Create a JIRA story using jira CLI"""
        if dry_run:
            print(f"\n[DRY RUN] Would create story:")
            print(f"  Summary: {summary}")
            print(f"  Description: {description}")
            return True, "DRY-RUN"
        
        print(f"\nCreating story: {summary}")
        try:
            # Create the issue
            process = subprocess.Popen(
                ["jira", "issue", "create", 
                 "-t", "Story",
                 "-P", self.epic_key,
                 "-s", summary,
                 "-b", description],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Send enter to submit (select default "Submit" option)
            stdout, stderr = process.communicate(input="\n", timeout=30)
            
            if process.returncode == 0:
                # Extract issue URL from output
                match = re.search(r'https://[^\s]+', stdout)
                if match:
                    url = match.group(0)
                    print(f"✓ Created: {url}")
                    return True, url
                else:
                    print(f"✓ Story created successfully")
                    return True, "Created"
            else:
                print(f"✗ Failed to create story: {stderr}")
                return False, stderr
                
        except Exception as e:
            print(f"✗ Error creating story: {e}")
            return False, str(e)
    
    def run(self, dry_run: bool = False, debug: bool = False):
        """Main execution flow"""
        # Fetch epic
        epic_content = self.fetch_epic()
        
        if debug:
            print("\n=== DEBUG: Epic Content ===")
            print(epic_content)
            print("=== END DEBUG ===\n")
        
        # Parse stories
        stories = self.parse_stories(epic_content)
        
        if not stories:
            print("\nNo stories found in epic description")
            print("Expected format:")
            print("Stories:")
            print("• Story title")
            print("  • (optional) Additional context")
            
            if not debug:
                print("\nRun with --debug to see raw epic content")
            return
        
        print(f"\n{'='*60}")
        print(f"Found {len(stories)} stories to create:")
        print(f"{'='*60}")
        for i, story in enumerate(stories, 1):
            print(f"\n{i}. {story['summary']}")
        
        print(f"\n{'='*60}")
        
        if dry_run:
            print("\nDRY RUN MODE - No stories will be created")
        
        # Create stories
        results = []
        for story in stories:
            success, result = self.create_story(
                story['summary'], 
                story['description'],
                dry_run
            )
            results.append({'story': story['summary'], 'success': success, 'result': result})
        
        # Summary
        print(f"\n{'='*60}")
        print("Summary:")
        print(f"{'='*60}")
        successful = sum(1 for r in results if r['success'])
        print(f"Created: {successful}/{len(results)} stories")
        
        if not dry_run:
            print("\nCreated stories:")
            for r in results:
                if r['success'] and r['result'].startswith('http'):
                    print(f"  • {r['result']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 epic-to-stories.py <EPIC-KEY> [--dry-run] [--debug]")
        print("Example: python3 epic-to-stories.py DEVOPS-43103")
        print("\nOptions:")
        print("  --dry-run    Parse stories but don't create them")
        print("  --debug      Show raw epic content for debugging")
        sys.exit(1)
    
    epic_key = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    debug = '--debug' in sys.argv
    
    tool = JiraEpicToStories(epic_key)
    tool.run(dry_run, debug)

if __name__ == "__main__":
    main()
