# Testing_Github_Actions

This repository triggers cross-repository GitHub Actions workflows when issues are created. It sends issue data to the `Triggering_Github_Actions` repository for processing.

## Features

- **Automated Issue Processing**: When a new issue is created using the template, a GitHub Action automatically extracts and processes the information
- **Cross-Repository Dispatch**: Sends issue data to another repository for processing
- **Automatic Comments**: Posts acknowledgment and final results as comments on the issue

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

2. **Image** (Text Input): Container image to use (e.g., `icr.io/wxa4z-agentic-development/upgrade-agent:granite-4-8b`)

3. **Model** (Dropdown): Select the model
   - meta-llama/llama-3-3-70b-instruct
   - ibm/granite-3-3-8b-instruct
   - ibm-granite/granite-3-z-8b-instruct
   - ibm-granite/granite-4.0-micro
   - openai/gpt-oss-20b
   - ibm-granite/granite-4.0-8b

4. **Test Type** (Dropdown): Select test type
   - direct
   - wxo

5. **Tool Call Evaluation** (Dropdown): Enable or disable tool call evaluation
   - true
   - false

## Workflow

The GitHub Actions workflow (`.github/workflows/issue_python_comment.yml`) performs the following steps:

1. Triggers when a new issue is opened
2. Extracts all field values from the issue body
3. Sends a repository dispatch event to `Triggering_Github_Actions` with all issue data
4. Posts an acknowledgment comment on the issue
5. The remote repository processes the data and posts results back

## Setup Requirements

### Required Secrets

Configure the following secret in repository settings (Settings → Secrets and variables → Actions):

- `DISPATCH_TOKEN`: A GitHub Personal Access Token with `repo` and `workflow` permissions

### Setup Instructions

See the [SETUP_GUIDE.md](../../SETUP_GUIDE.md) in the root directory for complete setup instructions.

## How It Works

1. User creates an issue using the template
2. Workflow extracts issue data
3. Repository dispatch sent to `Triggering_Github_Actions`
4. Remote workflow runs Python script with issue data
5. Script output posted as comment on original issue

## Files Structure

```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── request.yml                    # Issue template configuration
│   └── workflows/
│       └── issue_python_comment.yml       # GitHub Actions workflow
└── README.md                              # This file
```

## Related Repository

- **Triggering_Github_Actions**: Contains the Python processing script that handles the issue data

## Troubleshooting

If the workflow doesn't trigger or comments aren't posted:

1. Verify `DISPATCH_TOKEN` is configured correctly
2. Check the Actions tab for workflow run logs
3. Ensure the token has proper permissions
4. See [SETUP_GUIDE.md](../../SETUP_GUIDE.md) for detailed troubleshooting

---

**Made with Bob** 🤖
