import sys
import subprocess

# Define the script path
UPLOAD_SCRIPT = ".gemini/agents/upload_test_cases.py"

def run():
    if len(sys.argv) < 3:
        print("Usage: test-rail-uploader <ticket_id> <section_id>")
        sys.exit(1)
        
    ticket_id = sys.argv[1]
    section_id = sys.argv[2]
    
    # Execute the existing upload script
    subprocess.run(["python3", UPLOAD_SCRIPT, ticket_id, section_id])

if __name__ == "__main__":
    run()
