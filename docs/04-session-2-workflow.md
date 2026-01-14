# Session 2: Spec-Driven Development Workflow

This session covers the complete development workflow: from connecting Claude Code to Jira, through spec-driven planning, to building, committing, and merging code.

## Table of Contents

- [Before You Begin: Prerequisites Check](#before-you-begin-prerequisites-check)
- [1. Connect Claude Code to Jira](#1-connect-claude-code-to-jira)
  - [1.1 Add Atlassian MCP Server](#11-add-atlassian-mcp-server)
- [2. Spec-Kit Workflow](#2-spec-kit-workflow)
  - [2.1 Initialize Spec-Kit](#21-initialize-spec-kit)
  - [2.2 Create the Constitution](#22-create-the-constitution)
  - [2.3 Create the Specification](#23-create-the-specification)
  - [2.4 Create the Implementation Plan](#24-create-the-implementation-plan)
  - [2.5 Generate Tasks](#25-generate-tasks)
- [3. Create Jira Issues](#3-create-jira-issues)
  - [3.1 Create the First Issue](#31-create-the-first-issue)
  - [3.2 Create Remaining Issues](#32-create-remaining-issues)
- [4. Create Feature Branch](#4-create-feature-branch)
  - [4.1 Ask Claude Code to Create Branch](#41-ask-claude-code-to-create-branch)
- [5. Build the Dashboard with Claude Code](#5-build-the-dashboard-with-claude-code)
  - [5.1 Set Up Python Environment](#51-set-up-python-environment)
  - [5.2 Build the Dashboard](#52-build-the-dashboard)
  - [5.3 Iterate and Improve](#53-iterate-and-improve)
- [6. Commit Your Changes](#6-commit-your-changes)
  - [6.1 Ask Claude Code to Commit](#61-ask-claude-code-to-commit)
- [7. Push and Create Pull Request](#7-push-and-create-pull-request)
  - [7.1 Ask Claude Code to Push and Create PR](#71-ask-claude-code-to-push-and-create-pr)
  - [7.2 Verify Jira Integration](#72-verify-jira-integration)
- [8. Merge the Pull Request](#8-merge-the-pull-request)
  - [8.1 Review and Merge](#81-review-and-merge)
  - [8.2 Update Local Repository](#82-update-local-repository)
- [9. Session 2 Verification](#9-session-2-verification)
- [The Complete Workflow](#the-complete-workflow)
- [What's Next](#whats-next)

---

## Before You Begin: Prerequisites Check

Before starting Session 2, verify your Session 1 setup is working. Run these commands in Cursor's terminal:

```bash
# Check Git is installed
git --version
# Expected: git version 2.x.x

# Check Python is installed
python --version
# Expected: Python 3.11.x or higher

# Check you're in the tutorial project
ls data/sales-data.csv
# Expected: data/sales-data.csv (file exists)

# Check Claude Code is installed
claude --version
# Expected: Claude Code version information
```

**If any command fails**, return to [Session 1: Setup](01-session-1-setup.md) to fix the issue before continuing.

---

## What You Will Accomplish

```
┌─────────────────────────────────────────────────────────────┐
│                   Session 2 Outcomes                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  MCP Integration:           Spec-Kit Artifacts:             │
│  ───────────────            ─────────────────               │
│  • Atlassian MCP connected  • Constitution created          │
│  • Claude reads Jira        • Specification refined         │
│                             • Implementation plan           │
│                             • Task breakdown                │
│                                                             │
│  Development:               Git Workflow:                   │
│  ────────────               ─────────────                   │
│  • Jira issue ECOM-1        • Feature branch created        │
│  • Streamlit dashboard      • Commits with Jira key         │
│  • Python virtual env       • Pull request created          │
│                             • Branch merged to main         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Connect Claude Code to Jira

**What is MCP?** The Model Context Protocol (MCP) is a way for AI assistants like Claude Code to connect to external tools and services. Think of it as a "plugin system" that lets Claude Code talk to other applications. In this tutorial, we will use MCP to connect Claude Code to Jira so Claude can read your project tasks directly.

### 1.1 Add Atlassian MCP Server

**Steps:**

1. Open Cursor and navigate to your tutorial project
2. Open the terminal (`` Ctrl+` ``)
3. Run the following command:

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

   (The `--transport sse` part specifies how Claude communicates with Atlassian's server — you don't need to understand the technical details, just include it as shown.)

4. A browser window will open for authentication
5. Log in with your Atlassian account
6. Authorize Claude Code to access your Jira workspace
7. Return to the terminal

**Verify the connection:**

```bash
claude
```

Once in the Claude Code session, type:

```
/mcp
```

You should see `atlassian` listed as an available MCP server.

**Test the connection:**

In the Claude Code session, ask:

```
What Jira projects do I have access to?
```

Claude should be able to list your ECOM project.

Type `/exit` to leave the Claude Code session for now.

**Checkpoint:** Claude Code can see your Jira workspace and ECOM project.

**Note:** You may need to re-authenticate occasionally. If Claude reports it cannot access Jira, run the `claude mcp add` command again.

---

## 2. Spec-Kit Workflow

Spec-kit follows a structured process: Constitution → Specification → Plan → Tasks → Implementation.

### 2.1 Initialize Spec-Kit

First, initialize spec-kit in your project.

**In Cursor's terminal** (not inside Claude Code), run:

```bash
specify init . --ai claude
```

This creates the necessary configuration files for spec-kit to work with Claude Code, including the slash commands you will use in the following steps.

**Checkpoint:** Verify the initialization succeeded:

1. You should see output confirming the initialization completed
2. A `.specify/` directory should now exist in your project
3. A `.claude/commands/` directory should be created with the spec-kit slash commands

To verify, run:
```bash
ls -la .specify/
ls -la .claude/commands/
```

You should see files like `speckit.constitution.md`, `speckit.specify.md`, etc. in the `.claude/commands/` directory.

**Important:** The slash commands (`/speckit.constitution`, `/speckit.specify`, etc.) will NOT work until this initialization step completes successfully. If you don't see these directories, re-run the `specify init` command.

---

### 2.2 Create the Constitution

The constitution establishes principles and guidelines for your project. It ensures consistent decision-making throughout development.

**Steps:**

1. Start Claude Code:
   ```bash
   claude
   ```

2. Ask Claude to help create the constitution:
   ```
   /speckit.constitution

   Create a constitution for our e-commerce analytics project.
   The project will build a Streamlit dashboard for sales data visualization.
   Key principles should include:
   - Simplicity over complexity
   - Clear, readable code
   - User-friendly visualizations
   - Following Python best practices
   ```

3. Claude will generate a constitution file. Review the output and confirm.

**Checkpoint:** A constitution file exists in your project (typically in `.specify/` or a `specs/` directory).

---

### 2.3 Create the Specification

The specification refines the PRD (Product Requirements Document — the document in `prd/ecommerce-analytics.md` that describes what we want to build) into detailed, actionable requirements.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.specify

   Based on the PRD in prd/ecommerce-analytics.md, create a detailed specification for the sales dashboard.

   The dashboard should have:
   - 2 KPI cards at the top (Total Sales, Total Orders)
     (KPI = Key Performance Indicator, a metric that shows important business data at a glance)
   - A line chart showing sales trend over time
   - A bar chart showing sales by category
   - A bar chart showing sales by region

   The data source is data/sales-data.csv
   ```

2. Claude will analyze the PRD and create a specification
3. Review the specification for clarity and completeness

**Checkpoint:** A specification document is created with clear, detailed requirements.

---

### 2.4 Create the Implementation Plan

The plan outlines how you will build the specification technically.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.plan

   Create an implementation plan for the sales dashboard specification.

   Consider:
   - Python with Streamlit for the web app
   - Pandas for data handling
   - Plotly for interactive charts
   - Clean code organization
   ```

2. Claude will generate a technical plan covering:
   - Architecture decisions
   - Technology choices
   - Component structure
   - Data flow

**Checkpoint:** An implementation plan document exists with clear technical direction.

---

### 2.5 Generate Tasks

Break the plan into specific, actionable tasks.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.tasks

   Generate implementation tasks from the plan.
   ```

2. Claude will output a list of tasks
3. Review the tasks — you should see something like:
   - Set up Python virtual environment and dependencies
   - Create main Streamlit app structure
   - Implement KPI scorecards
   - Implement sales trend line chart
   - Implement category bar chart
   - Implement region bar chart

**Checkpoint:** You have a clear list of implementation tasks.

---

## 3. Create Jira Issues

Now create Jira issues based on the tasks generated by spec-kit. This connects your work to the project management system.

### 3.1 Create the First Issue

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to create the first issue:
   ```
   Based on the tasks generated by spec-kit, what should be the first Jira issue to create?
   Create it in the ECOM project as a Story.
   ```

2. Claude will:
   - Review the tasks from spec-kit
   - Recommend and create the first issue (likely ECOM-1)
   - Provide the issue details

**Checkpoint:** Issue ECOM-1 exists in your Jira project.

---

### 3.2 Create Remaining Issues

**Steps:**

1. In Claude Code, ask it to create the remaining issues:
   ```
   Create Jira issues in the ECOM project for the remaining tasks from spec-kit.
   ```

2. Claude will create additional issues (ECOM-2, ECOM-3, etc.) for each task.

**Checkpoint:** Multiple issues exist in your Jira project based on the spec-kit tasks.

---

## 4. Create Feature Branch

Now create a Git branch for your work. This keeps your changes isolated from the main codebase.

**What is a feature branch?** Think of branches like parallel universes for your code. The `main` branch is the "official" version that always works. When you create a feature branch, you get your own copy where you can make changes without affecting anyone else. If something goes wrong, the main branch is still safe. Once your feature is complete and tested, you merge it back into main. This is how professional teams work together without stepping on each other's toes.

### 4.1 Ask Claude Code to Create Branch

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to create a feature branch:
   ```
   Create a feature branch for Jira issue ECOM-1 to add a sales dashboard.
   ```

2. Claude will:
   - Ensure you're on the main branch and up to date
   - Create a new branch named `feature/ECOM-1-add-sales-dashboard`
   - Switch to the new branch

**Understanding branch naming:**
- `feature/` is a prefix indicating this is a feature branch
- `ECOM-1` is the Jira issue key (this enables traceability)
- `add-sales-dashboard` describes what the branch does

**Checkpoint:** Claude confirms you are on the new feature branch.

---

## 5. Build the Dashboard with Claude Code

Now you will build the dashboard using Claude Code as your AI assistant.

**What is Streamlit?** Streamlit is a Python library that makes it easy to create web-based dashboards and data apps. Instead of writing HTML, CSS, and JavaScript, you write Python code and Streamlit turns it into a web page. It's popular for data visualization because you can go from data to dashboard quickly.

### 5.1 Set Up Python Environment

First, create a virtual environment for your project dependencies.

**Steps:**

1. In Claude Code (run `claude` if not already in a session):
   ```
   Help me set up a Python virtual environment for this project.
   I need to install streamlit, pandas, and plotly for a dashboard.
   Create a requirements.txt file as well.
   ```

   **What is requirements.txt?** This file lists all the Python packages your project needs. When someone else downloads your project, they can run `pip install -r requirements.txt` to install all the same packages you used. It's like a recipe that ensures everyone has the same ingredients.

2. Claude will guide you through:
   - Creating the virtual environment
   - Activating it
   - Installing dependencies
   - Creating requirements.txt

**Manual steps (if you prefer):**

```bash
# Create virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install streamlit pandas plotly

# Create requirements.txt
pip freeze > requirements.txt
```

**How do I know the virtual environment is activated?**

When the virtual environment is active, you will see `(venv)` at the beginning of your terminal prompt:

```
(venv) $ _
```

If you don't see `(venv)`, run the activation command again (see Manual steps above).

**Checkpoint:**
- Your terminal prompt shows `(venv)` prefix
- A `venv` folder exists in your project
- Running `pip list` shows streamlit, pandas, and plotly installed
- A `requirements.txt` file exists

---

### 5.2 Build the Dashboard

Now use Claude Code to build the dashboard.

**Steps:**

1. In Claude Code:
   ```
   /speckit.implement

   Implement ECOM-1: Build the Streamlit sales dashboard based on our specification.

   Requirements:
   - Load data from data/sales-data.csv
   - Display 2 KPI cards: Total Sales and Total Orders
   - Line chart showing sales trend over time
   - Bar chart showing sales by category
   - Bar chart showing sales by region

   Use Plotly for the charts. Make the dashboard clean and professional.
   ```

2. Claude will:
   - Analyze the CSV data structure
   - Create the dashboard code
   - Explain what each part does

3. Review the generated code. Make sure you understand what it does.

4. If Claude asks where to put the file, a common choice is:
   - `app.py` in the project root, or
   - `src/dashboard.py` in a source folder

**Test the dashboard:**

```bash
streamlit run app.py
```

(Replace `app.py` with wherever Claude placed the dashboard file)

**What you should see:**

1. In the terminal, Streamlit shows:
   ```
   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501
   ```

2. Your browser should open automatically. If it doesn't, open http://localhost:8501 manually.

3. The dashboard should display your KPIs and charts.

**To stop the dashboard:** Press `Ctrl+C` in the terminal.

**Checkpoint:** The dashboard runs and displays KPIs and charts.

---

### 5.3 Iterate and Improve

If something doesn't look right, ask Claude to help:

```
The category bar chart is showing categories in the wrong order.
Can you sort them by sales value descending?
```

Or:

```
Can you add a title to the dashboard and format the Total Sales KPI as currency?
```

Claude Code can read your existing code and make modifications.

**Checkpoint:** The dashboard looks professional and displays data correctly.

---

## 6. Commit Your Changes

Now save your work with a Git commit. Claude Code can handle all the git operations for you.

### 6.1 Ask Claude Code to Commit

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to commit your changes:
   ```
   Commit my changes for the sales dashboard.
   Make sure venv/ is in .gitignore.
   Use the Jira issue key ECOM-1 in the commit message.
   ```

2. Claude will:
   - Check the `.gitignore` file and add `venv/` if needed
   - Stage the appropriate files (app.py, requirements.txt, etc.)
   - Create a commit with a properly formatted message

**What is .gitignore?** This file tells Git which files and folders to ignore and NOT track. The `venv/` folder contains installed packages that can be recreated from `requirements.txt`, so we don't need to store it in Git.

**Commit Message Format:**

Claude Code will format the commit message as: `ECOM-1: description`

| Part | Example | Rule |
|------|---------|------|
| Issue key | `ECOM-1:` | Uppercase, followed by colon and space |
| Description | `add sales dashboard` | Lowercase, present tense verb (add, fix, update) |

This format ensures:
- `ECOM-1:` — Links this commit to the Jira issue (for traceability)
- `add sales dashboard` — Describes what was added (present tense, lowercase)

**Checkpoint:** Claude confirms the commit was created with the Jira key in the message.

---

## 7. Push and Create Pull Request

Now push your changes to GitHub and create a pull request. Claude Code can handle this for you.

### 7.1 Ask Claude Code to Push and Create PR

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to push and create a pull request:
   ```
   Push my branch and create a pull request.
   Include "Resolves ECOM-1" in the PR description.
   ```

2. Claude will:
   - Push your branch to GitHub
   - Create a pull request with a summary of your changes
   - Include the Jira issue reference

3. You may be prompted for GitHub credentials. If using HTTPS, enter your username and a personal access token (not your password).

4. Claude will provide a link to the pull request — click it to view on GitHub.

**Note:** "Resolves ECOM-1" is a special keyword that tells GitHub and Jira this pull request completes the ECOM-1 task. When the PR is merged, Jira can automatically update the issue status.

**Checkpoint:** Pull request is created and visible on GitHub.

---

### 7.2 Verify Jira Integration

If the GitHub-Jira integration is working:

1. Go to your Jira workspace
2. Open issue ECOM-1
3. Look for a "Development" panel or section
4. You should see your branch and/or pull request linked

**Checkpoint:** Jira issue ECOM-1 shows the linked GitHub activity.

---

## 8. Merge the Pull Request

Normally, a team member would review your pull request. For this tutorial, you will merge it yourself.

### 8.1 Review and Merge

Before merging, review your own code using this checklist:

**Self-Review Checklist:**
- [ ] Does the code do what the Jira issue describes?
- [ ] Did I test it? (Did the Streamlit dashboard run without errors?)
- [ ] Are there any obvious mistakes or typos?
- [ ] Is the commit message formatted correctly with the Jira key?

**Steps:**

1. On the pull request page in GitHub, review the "Files changed" tab
2. Verify the code looks correct (use the checklist above)
3. Click **Merge pull request**
4. Click **Confirm merge**
5. Optionally, click **Delete branch** to clean up the feature branch

**Checkpoint:** The pull request shows as "Merged" with a purple icon.

---

### 8.2 Update Local Repository

After merging, update your local main branch.

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to update your local repository:
   ```
   Switch to main and pull the latest changes.
   ```

2. Claude will switch to the main branch and pull the merged code.

**Checkpoint:** Claude confirms you are on main with the latest changes.

**What just happened?** Your dashboard code is now part of the `main` branch — the "official" version of your project. In a real team environment, this code would be deployed to a server for users to access. The feature branch (`feature/ECOM-1-add-sales-dashboard`) is no longer needed and can be deleted.

This completes the full development cycle: **Requirement → Plan → Code → Review → Merge**.

---

## 9. Session 2 Verification

Verify everything is complete:

### MCP Integration
- [ ] Atlassian MCP server connected to Claude Code
- [ ] Claude can access your Jira workspace

### Spec-Kit Artifacts
- [ ] Constitution created
- [ ] Specification created
- [ ] Implementation plan created
- [ ] Tasks generated

### Jira
- [ ] Multiple issues created from spec-kit tasks (ECOM-1, ECOM-2, etc.)
- [ ] ECOM-1 shows linked GitHub activity (branch, commits, PR)

### Dashboard
- [ ] Streamlit app runs successfully
- [ ] KPI cards display Total Sales and Total Orders
- [ ] Line chart shows sales trend
- [ ] Bar charts show category and region breakdowns

### Git Workflow
- [ ] Feature branch created with correct naming
- [ ] Commit message includes Jira key
- [ ] Pull request created and merged
- [ ] Main branch updated locally

---

## The Complete Workflow

Congratulations! You have completed the full workflow:

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ →  │ spec-kit │ →  │  Jira   │ →  │ Branch │
└─────────┘    └──────────┘    └─────────┘    └────────┘
     ✓              ✓              ✓              ✓
                                                  ↓
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Merge  │ ←  │    PR    │ ←  │ Commit  │ ←  │  Code  │
└─────────┘    └──────────┘    └─────────┘    └────────┘
     ✓              ✓              ✓              ✓
```

You now know how to:
1. Start with requirements (PRD)
2. Use spec-kit to plan systematically
3. Track work in Jira
4. Create isolated branches for features
5. Build with AI assistance
6. Commit with traceability
7. Create pull requests for review
8. Merge changes safely

This is the workflow you will use for your capstone project.

---

## What's Next

Continue to [Next Steps](06-next-steps.md) to learn how to apply this workflow to your capstone project.
