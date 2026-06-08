---
name: test-rail-skill
description: Procedural guidance for interacting with the TestRail API to upload test cases.
---

# TestRail Skill

This skill provides instructions for uploading test cases to TestRail using `curl`.

## Prerequisites
- Credentials must be configured in the `.env` file at the project root.
- Variables: `TESTRAIL_USER`, `TESTRAIL_KEY`, `TESTRAIL_BASE_URL`, `TESTRAIL_PROJECT_ID`, `TESTRAIL_SUITE_ID`.

## Lookup Information
Before adding a case, you may need to find the IDs for a Project, Suite, or Section by name.

### Get Projects
```bash
curl --request GET \
  --url "${TESTRAIL_BASE_URL}/index.php?/api/v2/get_projects" \
  --user "${TESTRAIL_USER}:${TESTRAIL_KEY}" \
  --header 'Content-Type: application/json'
```

### Get Suites
```bash
curl --request GET \
  --url "${TESTRAIL_BASE_URL}/index.php?/api/v2/get_suites/{project_id}" \
  --user "${TESTRAIL_USER}:${TESTRAIL_KEY}" \
  --header 'Content-Type: application/json'
```

### Get Sections
```bash
curl --request GET \
  --url "${TESTRAIL_BASE_URL}/index.php?/api/v2/get_sections/{project_id}&suite_id={suite_id}" \
  --user "${TESTRAIL_USER}:${TESTRAIL_KEY}" \
  --header 'Content-Type: application/json'
```

## Upload Test Case
To add a test case, first source the `.env` file and then use the `curl` command:

```bash
# Load environment variables
export $(grep -v '^#' .env | xargs)

# Execute API call
curl --request POST \
  --url "${TESTRAIL_BASE_URL}/index.php?/api/v2/add_case/{section_id}" \
  --user "${TESTRAIL_USER}:${TESTRAIL_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "title": "Test Case Title",
    "type_id": 1,
    "priority_id": 2,
    "estimate": "5m",
    "refs": "JIRA-123",
    "custom_steps_separated": [
      {
        "content": "Step 1",
        "expected": "Expected 1"
      }
    ]
  }'
```

Refer to the [TestRail API documentation](https://www.gurock.com/testrail/docs/api/reference/cases) for more details on the payload structure.
