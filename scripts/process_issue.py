import os

issue_title = os.getenv("ISSUE_TITLE", "")
issue_body = os.getenv("ISSUE_BODY", "")

# Example: extract simple fields from issue body
# (works well with issue templates)
lines = issue_body.splitlines()
fields = [line for line in lines if ":" in line]

result = "### 🔍 Processed Issue Data\n\n"
result += f"**Title:** {issue_title}\n\n"
result += "**Extracted Fields:**\n"

for field in fields:
    result += f"- {field}\n"

print(result)
