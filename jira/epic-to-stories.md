# JIRA Epic to Stories Agent

## Purpose
Automate the creation of JIRA stories from an epic's description by parsing the epic content and creating child stories.

## Capabilities
- Fetch JIRA epic content using the jira CLI
- Parse epic description to extract story items
- Create JIRA stories as children of the epic
- Handle interactive jira CLI prompts automatically

## Usage
When a user requests to create stories from an epic, this agent will:
1. Retrieve the epic using `jira issue view <EPIC-KEY>`
2. Parse the description to identify story items (typically bullet points under "Stories:" section)
3. Create each story using `jira issue create` with:
   - Type: Story
   - Parent: The epic key
   - Summary: Extracted from the story item
   - Description: Expanded context from the story item

## Example Commands
```bash
# View epic
jira issue view DEVOPS-43103

# Create story from epic
jira issue create -t Story -P DEVOPS-43103 -s "Story Summary" -b "Story Description"
```

## Workflow Pattern
1. Call `jira issue view <EPIC-KEY>` to fetch epic
2. Parse the description field for story items (look for "Stories:" section)
3. For each story item:
   - Extract summary (main bullet point text)
   - Extract description (sub-bullets or context)
   - Call `jira issue create` with appropriate flags
   - Handle interactive prompt by sending `{enter}` to select "Submit"
4. Report created story URLs

## Key Implementation Details
- The jira CLI shows output in a pager (use 'q' to quit)
- Interactive prompts require `write_bash` with `{enter}` input
- Stories should maintain context from the epic's goal and phases
- Always link stories to parent epic using `-P` flag
