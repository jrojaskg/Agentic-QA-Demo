import json
import os
import re
import requests

# Load environment variables
def load_env():
    env_vars = {}
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env_vars[key] = value
    return env_vars

env = load_env()
BASE_URL = env.get('TESTRAIL_BASE_URL')
USER = env.get('TESTRAIL_USER')
KEY = env.get('TESTRAIL_KEY')

def parse_test_cases(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    test_cases = []
    # Split by ## Test Case <number>.
    parts = re.split(r'## Test Case \d+:', content)
    for part in parts[1:]:
        lines = part.strip().split('\n')
        title = lines[0].strip()
        
        steps = []
        step_regex = re.compile(r'^\s*(\d+)\.\s+(.*)')
        expected_regex = re.compile(r'^\s*Expected:\s+(.*)')
        
        current_step = None
        
        for line in lines:
            step_match = step_regex.match(line)
            if step_match:
                if current_step:
                    steps.append(current_step)
                current_step = {"content": step_match.group(2), "expected": ""}
                continue
            
            exp_match = expected_regex.match(line)
            if exp_match and current_step:
                current_step["expected"] = exp_match.group(1)
        
        if current_step:
            steps.append(current_step)
            
        test_cases.append({"title": title, "steps": steps})
    return test_cases

def upload_test_cases(ticket_id, section_id, test_cases):
    url = f"{BASE_URL}/index.php?/api/v2/add_case/{section_id}"
    
    for case in test_cases:
        payload = {
            "title": case["title"],
            "type_id": 1,
            "priority_id": 2,
            "estimate": "5m",
            "refs": ticket_id,
            "custom_steps_separated": case["steps"]
        }
        
        response = requests.post(
            url,
            json=payload,
            auth=(USER, KEY),
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            print(f"Successfully uploaded: {case['title']}")
        else:
            print(f"Failed to upload {case['title']}: {response.text}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python upload_script.py <ticket_id> <section_id>")
        sys.exit(1)
        
    ticket_id = sys.argv[1]
    section_id = sys.argv[2]
    
    file_path = f".gemini/Artifacts/testCases/{ticket_id}.md"
    test_cases = parse_test_cases(file_path)
    upload_test_cases(ticket_id, section_id, test_cases)
