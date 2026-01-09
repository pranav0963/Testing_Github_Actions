# Testing_Github_Actions

This repository contains a GitHub Actions workflow that automatically processes issue templates and posts formatted comments.

## Features

- **Automated Issue Processing**: When a new issue is created using the template, a GitHub Action automatically extracts and processes the information
- **Python Script Integration**: Uses a Python script to parse issue data and format output
- **Automatic Comments**: Posts a formatted comment back to the issue with the processed information

## Issue Template Fields

The issue template (`.github/ISSUE_TEMPLATE/request.yml`) collects the following information:

1. **Agent Name** (Dropdown): Select from available agents
   - db2
   - operationsagent
   - cics
   - cics-pd-agent
   - ims
   - ims-mcp-agent
   - upgradeagent
   - upgradeagent-zosmf-v2
   - tls-agent
   - aiopsagent
   - automation-insights
   - workload-scheduler-agent

2. **Image** (Text Input): Container image to use (e.g., `myregistry/myimage:latest`)

3. **Model** (Text Input): Model that decides the namespace in deployment

4. **Test Type** (Dropdown): Select test type
   - direct
   - wxo

5. **Tool Call Evaluation** (Dropdown): Enable or disable tool call evaluation
   - true
   - false

## Workflow

The GitHub Actions workflow (`.github/workflows/issue_python_comment.yml`) performs the following steps:

1. Triggers when a new issue is opened
2. Checks out the repository
3. Sets up Python 3.10
4. Runs the `scripts/process_issue.py` script with issue data
5. Posts the processed output as a comment on the issue

## Environment Variables

The workflow uses the following environment variables:

- `ISSUE_BODY`: The body content of the created issue
- `ISSUE_TITLE`: The title of the created issue
- `DUMMY_API`: A secret variable (configured in repository secrets)

## Script Output

The Python script extracts all fields from the issue and outputs a formatted summary including:

- Agent Name
- Image
- Model
- Test Type
- Tool Call Evaluation
- Dummy API (from secrets)

## Setup

1. Ensure the `DUMMY_API` secret is configured in your repository settings
2. Create a new issue using the "Pipeline Trigger Request" template
3. Fill in all required fields
4. Submit the issue
5. The workflow will automatically process the issue and post a comment with the extracted information

## Files Structure

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── request.yml          # Issue template configuration
│   └── workflows/
│       └── issue_python_comment.yml  # GitHub Actions workflow
├── scripts/
│   └── process_issue.py         # Python script to process issues
└── README.md                    # This file
