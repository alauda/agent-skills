---
name: jira-epic-to-stories
description: Automatically parse JIRA epic descriptions and create child stories. Use when user wants to generate stories from an epic.
---

# JIRA Epic to Stories Skill

This skill teaches Copilot how to automatically create JIRA stories from epic descriptions using the jira CLI.

## Prerequisites

This skill requires the [Jira CLI (ankitpokhrel/jira-cli)](https://github.com/ankitpokhrel/jira-cli) to be installed and properly authenticated on the host machine. The scripts within this skill invoke the `jira` binary directly.

## When to Use This Skill

Activate this skill when:
- User asks to "create stories from epic"
- User provides an epic key and wants to generate child stories
- User mentions "parse epic description" or "generate stories"

## Epic Format Expected

The skill parses epics with this description structure:

```markdown
**Stories**:

• First story title
    • (optional) Additional context or sub-task
• Second story title
    • (optional) Additional context
```

Also supports:
- `Stories:` (without bold)
- Different indentation (2-6 spaces for bullets)
- ANSI escape codes in CLI output

Besides Stories, there are other issues that can be created from epics, such as:
- Jobs: These are identified as `Steps` or `Progression`

These are also to be created as jira issues using the type `Job`

## Implementation Pattern

### Step 1: Fetch Epic Content

```python
import subprocess
import time

process = subprocess.Popen(
    ["jira", "issue", "view", epic_key],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Wait for content to load
time.sleep(3)

# Send 'q' to quit pager
stdout, stderr = process.communicate(input='q', timeout=5)
```

### Step 2: Parse Stories from Description

```python
import re

def parse_stories(epic_content: str) -> list:
    """Extract story items from epic description"""
    stories = []

    # Remove ANSI escape codes
    clean_content = re.sub(r'\x1b\[[0-9;]+m', '', epic_content)
    lines = clean_content.split('\n')

    in_stories_section = False
    current_story = None

    for line in lines:
        # Find Stories section (with or without bold)
        if re.search(r'\*?\*?Stories\*?\*?:', line):
            in_stories_section = True
            continue

        # Exit at next section
        if in_stories_section and ('————' in line or 'Linked Issues' in line):
            break

        if in_stories_section:
            # Top-level bullet (2 spaces): "  • Story title"
            match = re.match(r'^(\s{2})•\s+(.+)', line)
            if match:
                if current_story:
                    stories.append(current_story)

                text = match.group(2).strip()
                current_story = {
                    'summary': text,
                    'description': text
                }
            # Sub-bullet (6 spaces): "      • Additional context"
            elif current_story:
                sub_match = re.match(r'^\s{6,}•\s+(.+)', line)
                if sub_match:
                    context = sub_match.group(1).strip()
                    current_story['description'] += f"\n\n{context}"

    if current_story:
        stories.append(current_story)

    return stories
```

### Step 3: Create Stories

```python
def create_story(epic_key: str, summary: str, description: str) -> tuple:
    """Create a story as child of epic"""

    process = subprocess.Popen(
        ["jira", "issue", "create",
         "-t", "Story",
         "-P", epic_key,
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
        # Extract URL from output
        match = re.search(r'https://[^\s]+', stdout)
        if match:
            return True, match.group(0)

    return False, stderr
```

## Complete Automation Script

A full Python script is available in `/jira/epic-to-stories.py` with:

```bash
# Create stories from epic
python3 jira/epic-to-stories.py DEVOPS-43103

# Preview without creating (dry-run)
python3 jira/epic-to-stories.py DEVOPS-43103 --dry-run

# Debug mode to see raw content
python3 jira/epic-to-stories.py DEVOPS-43103 --debug
```

## Key Implementation Details

### Handling ANSI Escape Codes

JIRA CLI output includes formatting codes. Always clean them:

```python
clean_text = re.sub(r'\x1b\[[0-9;]+m', '', raw_output)
```

### Handling Interactive Prompts

The CLI shows an interactive menu after `jira issue create`. Handle it:

```python
# Automatically submit by sending enter
stdout, stderr = process.communicate(input="\n", timeout=30)
```

### Parsing Indentation

Stories use 2-space indent, sub-bullets use 6+ spaces:

```python
# Main story: "  • Title"
main_match = re.match(r'^(\s{2})•\s+(.+)', line)

# Sub-bullet: "      • Context"
sub_match = re.match(r'^\s{6,}•\s+(.+)', line)
```

## Error Handling

Always handle:
- Timeout errors when fetching epics
- Failed story creation (report which ones failed)
- Invalid epic keys
- Empty story lists

## Output Format

Provide clear output:

```
============================================================
Found 2 stories to create:
============================================================

1. Create ACP SRE Agent Plugin with Incident Investigation Capabilities
2. Adds Incident Remediation capabilities to agent for quick incident recovery

============================================================

✓ Created: https://jira.alauda.cn/browse/DEVOPS-43119
✓ Created: https://jira.alauda.cn/browse/DEVOPS-43120

============================================================
Summary:
============================================================
Created: 2/2 stories
```

## Dry-Run Mode

Always support `--dry-run` flag to preview without creating:

```
[DRY RUN] Would create story:
  Summary: Story title
  Description: Story description with context
```

## Validation Steps

Before creating stories:
1. Validate epic key format (PROJECT-NUMBER)
2. Verify epic exists and is accessible
3. Check if stories already exist as children
4. Confirm at least one story found in description

## Resources

- Python script: `/jira/epic-to-stories.py`
- Shell script: `/jira/epic-to-stories-skill.sh`
- Documentation: `/jira/epic-to-stories.md`
