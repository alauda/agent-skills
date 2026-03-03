#!/bin/bash

ISSUES="$@"


function say {
    echo "[$(date)] $1"
}

function save_jira {
    jira issue view $1 --raw > $1.json
}

function get_epic_children {
    children=$(jira issue list --jql="\"Epic Link\" = $1" --columns=KEY --plain --no-headers)
}

echo "${ISSUES[@]}"



