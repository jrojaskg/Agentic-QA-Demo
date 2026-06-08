---
name: playwright-smoke-skill
description: Guidance for executing smoke tests using the Playwright MCP tools.
---

# Playwright Skill

Use the Playwright MCP to execute smoke tests based on test cases in `.gemini/Artifacts/testCases/{ticket_id}.md`.

## Steps
1. Navigate to `BASE_URL` from `.env` using `mcp_playwright_browser_navigate`
2. Take a snapshot with `mcp_playwright_browser_snapshot` before interacting
3. Execute each test case step using the appropriate tool:
   - `mcp_playwright_browser_click` — clicks
   - `mcp_playwright_browser_fill_form` — form inputs
   - `mcp_playwright_browser_wait_for` — waiting for elements
4. Take a screenshot after each test case with `mcp_playwright_browser_take_screenshot`
5. Report: test title, steps executed, Pass/Fail, screenshot path

## Rules
- Always use `BASE_URL` from `.env`, never hardcode URLs
- Always snapshot before interacting
- Never mark a test as passed without verifying the expected result