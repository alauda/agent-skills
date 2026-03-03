#!/bin/bash
# JIRA Epic to Stories Automation Script
# Usage: ./epic-to-stories-skill.sh <EPIC-KEY>

set -e

EPIC_KEY="$1"

if [ -z "$EPIC_KEY" ]; then
  echo "Usage: $0 <EPIC-KEY>"
  echo "Example: $0 DEVOPS-43103"
  exit 1
fi

echo "Fetching epic $EPIC_KEY..."

# Fetch epic content and save to temp file
TEMP_FILE=$(mktemp)
trap "rm -f $TEMP_FILE" EXIT

jira issue view "$EPIC_KEY" --no-input > "$TEMP_FILE" 2>&1 || true

# Display epic content
echo "Epic Content:"
cat "$TEMP_FILE"
echo ""
echo "---"

# Extract stories from description
# This is a simplified parser - in practice, you'd want more robust parsing
echo ""
echo "Parsing stories from epic description..."
echo "Note: This script demonstrates the automation pattern."
echo "For production use, implement proper parsing logic based on your epic format."
echo ""

# Example: Parse lines that start with "• " under "Stories:" section
# This would need to be customized based on your epic format
grep -A 100 "Stories:" "$TEMP_FILE" | grep "^  •" | sed 's/^  • //' || echo "No stories found in standard format"

echo ""
echo "To create stories, use:"
echo "jira issue create -t Story -P $EPIC_KEY -s \"Story Summary\" -b \"Story Description\""
