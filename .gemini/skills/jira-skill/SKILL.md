---
name: jira-skill
description: Procedural guidance for interacting with the Jira REST API to fetch ticket details.
---

# Jira Skill

This skill provides instructions for fetching ticket details from Jira using `curl`.

## Prerequisites
- Credentials must be configured in the `.env` file at the project root.
- Variables: `JIRA_API_TOKEN`, `JIRA_USER_EMAIL`, `JIRA_BASE_URL`.

## Fetch Ticket Details
To fetch a ticket's details, first source the `.env` file and then use the `curl` command:

```bash
# Load environment variables
export $(grep -v '^#' .env | xargs)

# Execute API call
curl --request GET \
  --url "${JIRA_BASE_URL}/rest/api/3/issue/{ticket_id}" \
  --user "${JIRA_USER_EMAIL}:${JIRA_API_TOKEN}" \
  --header 'Accept: application/json'
```

### Data Extraction
From the response JSON, extract:
- `fields.summary` (Title)
- `fields.description` (Description)
- `fields.customfield_XXXXX` (Acceptance Criteria - verify the field ID for your instance)
- `fields.customfield_YYYYY` (Testing Details - verify the field ID for your instance)

Note: In Jira Cloud, the description is often in Atlassian Document Format (ADF). You may need to parse the JSON content accordingly.
