import os
import re
import sys

def extract_field(body, field_name):
    """
    Extracts field value from GitHub issue template body
    """
    pattern = rf"### {field_name}\s*(.+)"
    match = re.search(pattern, body)
    return match.group(1).strip() if match else "NOT_FOUND"


def main():
    issue_body = os.getenv("ISSUE_BODY")

    if not issue_body:
        print("ERROR: ISSUE_BODY not found")
        sys.exit(1)

    service = extract_field(issue_body, "Service Name")
    environment = extract_field(issue_body, "Environment")
    version = extract_field(issue_body, "Version")

    # Your business logic
    combined = f"{service}-{environment}-{version}"

    # This exact format will be read by GitHub Actions
    print("SERVICE=" + service)
    print("ENVIRONMENT=" + environment)
    print("VERSION=" + version)
    print("COMBINED=" + combined)


if __name__ == "__main__":
    main()
