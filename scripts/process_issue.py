import os
import re

issue_title = os.getenv("ISSUE_TITLE", "")
issue_body = os.getenv("ISSUE_BODY", "")
dummy_api = os.getenv("DUMMY_API", "")

def extract_field(label, text):
    pattern = rf"### {label}\s+([^\n]+)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else "Not provided"

# Extract all fields from the issue body
agent_name = extract_field("Agent Name", issue_body)
image = extract_field("Image", issue_body)
model = extract_field("Model", issue_body)
test_type = extract_field("Test Type", issue_body)
tool_call_eval = extract_field("Tool Call Evaluation", issue_body)

# Print all variables
output = f"""
### ✅ Issue {issue_title} Processed Successfully

**Agent Name:** {agent_name}  
**Image:** {image}  
**Model:** {model}  
**Test Type:** {test_type}  
**Tool Call Evaluation:** {tool_call_eval}  
**Dummy API:** {dummy_api}

🔧 _This information was auto-processed by GitHub Actions._
"""

print(output.strip())

# Made with Bob
