import os
import re

issue_title = os.getenv("ISSUE_TITLE", "")
issue_body = os.getenv("ISSUE_BODY", "")
dummy_api = os.getenv("DUMMY_API", "")

def extract_field(label, text):
    pattern = rf"### {label}\s+([^\n]+)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else "Not provided"

service_name = extract_field("Service Name", issue_body)
environment = extract_field("Environment", issue_body)
version = extract_field("Version", issue_body)

# Concatenate or process as needed
output = f"""
### ✅ Issue {issue_title} Processed Successfully

**Service Name:** {service_name}  
**Environment:** {environment}  
**Version:** {version}
**Dummy Env:** {dummy_api}

🔧 _This information was auto-processed by GitHub Actions._
"""

print(output.strip())
