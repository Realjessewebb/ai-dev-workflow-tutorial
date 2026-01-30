# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an educational tutorial repository teaching spec-driven AI-assisted development workflows. The tutorial guides students through building an e-commerce analytics Streamlit dashboard using GitHub, Jira, spec-kit, and Claude Code as development tools.

The workflow follows: **PRD → spec-kit (constitution, specification, plan, tasks) → Jira issues → Implementation → Commit → Push → Deploy**

## Key Concepts

### Spec-Kit Workflow
This repository uses [spec-kit](https://github.com/github/spec-kit), GitHub's tool for spec-driven development. The workflow is:

1. **Constitution** (`.specify/memory/constitution.md`) - Project principles and guidelines
2. **Specification** (`specs/[feature]/spec.md`) - Detailed requirements from PRD
3. **Plan** (`specs/[feature]/plan.md`) - Technical implementation approach
4. **Tasks** (`specs/[feature]/tasks.md`) - Actionable breakdown of work
5. **Implementation** - Build features based on tasks

Spec-kit automatically creates feature branches for each spec. Work is done on feature branches and merged to `main` when complete.

### Jira Integration
The tutorial teaches students to:
- Connect Claude Code to Jira via the Atlassian Rovo MCP server
- Create Jira issues from spec-kit tasks
- Track work with the ECOM project key (e.g., ECOM-1, ECOM-2)
- Include Jira issue keys in commit messages
- Update Jira issues with implementation evidence (commit hash, branch, GitHub link)

### Commit Message Convention
All commits must include the Jira issue key:
```
ECOM-1: add sales dashboard
ECOM-2: implement KPI scorecards
```

## Development Commands

### Spec-Kit
```bash
# Initialize spec-kit in project
specify init . --ai claude

# Use spec-kit slash commands in Claude Code:
/speckit.constitution    # Create project constitution
/speckit.specify         # Create specification from PRD
/speckit.plan           # Create implementation plan
/speckit.tasks          # Generate task breakdown
/speckit.implement      # Implement a specific task
```

### Python Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Streamlit Dashboard
```bash
# Run the dashboard locally
streamlit run app.py

# Stop the server: Ctrl+C
```

### Git Operations
```bash
# Check current branch
git branch

# View status
git status

# Commit changes (include Jira key)
git commit -m "ECOM-1: description"

# Push to GitHub
git push origin <branch-name>

# Merge feature branch to main
git checkout main
git merge <feature-branch>
git push origin main
```

## Project Structure

```
ai-dev-workflow-tutorial/
├── .specify/              # Spec-kit configuration and memory
│   └── memory/
│       └── constitution.md
├── specs/                 # Feature specifications (created by spec-kit)
│   └── [feature-name]/
│       ├── spec.md       # Detailed specification
│       ├── plan.md       # Implementation plan
│       ├── tasks.md      # Task breakdown
│       └── checklists/   # Optional requirements checklists
├── data/
│   └── sales-data.csv    # Sample sales dataset for dashboard
├── docs/                 # Tutorial documentation
├── prd/
│   └── ecommerce-analytics.md  # Product requirements document
├── app.py                # Main Streamlit application (created during tutorial)
├── requirements.txt      # Python dependencies (created during tutorial)
└── README.md            # Tutorial overview and instructions
```

## Expected Implementation Artifacts

When students complete the tutorial, they will have created:

### Python Files
- `app.py` - Main Streamlit dashboard with KPI cards, trend chart, category/region breakdowns
- `requirements.txt` - Python dependencies (streamlit, pandas, plotly)

### Data Processing
The dashboard loads `data/sales-data.csv` containing:
- date, order_id, product, category, region, quantity, unit_price, total_amount
- ~1,000 transaction records
- 5 categories: Electronics, Accessories, Audio, Wearables, Smart Home
- 4 regions: North, South, East, West

### Dashboard Components
1. **KPI Cards** - Total Sales (~$650K-700K) and Total Orders (482)
2. **Sales Trend** - Line chart showing sales over time
3. **Category Breakdown** - Bar chart sorted by sales value
4. **Regional Breakdown** - Bar chart sorted by sales value

## Important Constraints

### What NOT to Include in .gitignore
The `.gitignore` already includes comprehensive exclusions. Do NOT commit:
- `venv/` or `.venv/` (Python virtual environment)
- `__pycache__/` (compiled Python files)
- `.env` (environment variables)
- `.specify/cache/` (spec-kit cache)
- `.streamlit/secrets.toml` (Streamlit secrets)

### Development Principles (from Tutorial Context)
- **Simple, readable code** - Students are learning
- **User-friendly visualizations** - Dashboard for business stakeholders
- **Python best practices** - Standard formatting and structure
- **Virtual environment isolation** - Always use venv for dependencies

## MCP Server Integration

The tutorial configures the Atlassian Rovo MCP server:
```bash
claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
```

This enables Claude Code to:
- Read Jira projects and issues
- Create and update Jira issues
- Move issues between statuses (Backlog → In Progress → Done)

## Deployment

The dashboard deploys to **Streamlit Community Cloud**:
1. Must be on `main` branch (Streamlit deploys from main)
2. Repository must be public on GitHub
3. Main file path: `app.py`
4. Creates public URL like `https://[app-name].streamlit.app`

## Workflow Best Practices

1. **Never work directly on main** - Use feature branches created by spec-kit
2. **Always include Jira keys in commits** - Enables traceability
3. **Update Jira issues with evidence** - Commit hash, branch name, GitHub link
4. **Mark tasks complete in tasks.md** - Change `[ ]` to `[x]`
5. **Merge to main after implementation** - Before deploying to Streamlit

## Tutorial Learning Objectives

This repository teaches students to:
- Use AI assistants (Claude Code) as implementation partners
- Follow spec-driven development (requirements → specification → plan → tasks → code)
- Maintain traceability (Jira issue → commit → GitHub → deployment)
- Work with professional tools (GitHub, Jira, Streamlit Cloud)
- Apply version control best practices (branching, meaningful commits)

When working with this codebase, prioritize clarity and educational value over optimization. Students are learning both the technical stack AND the professional workflow.

## Active Technologies
- Python 3.11+ + Streamlit (dashboard framework), Pandas (data processing), Plotly (interactive visualizations) (001-sales-dashboard)
- CSV file (`data/sales-data.csv`) - no database required (001-sales-dashboard)

## Recent Changes
- 001-sales-dashboard: Added Python 3.11+ + Streamlit (dashboard framework), Pandas (data processing), Plotly (interactive visualizations)
