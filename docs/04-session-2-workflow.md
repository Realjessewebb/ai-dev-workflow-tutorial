# Session 2: Spec-Driven Development Workflow

This session covers the complete development workflow: from connecting Claude Code to Jira, through spec-driven planning, to building, committing, and merging code.

## Table of Contents

- [1. Connect Claude Code to Jira](#1-connect-claude-code-to-jira)
  - [1.1 Add Atlassian MCP Server](#11-add-atlassian-mcp-server)
- [2. Spec-Kit Workflow](#2-spec-kit-workflow)
  - [2.1 Initialize Spec-Kit](#21-initialize-spec-kit)
  - [2.2 Create the Constitution](#22-create-the-constitution)
  - [2.3 Create the Specification](#23-create-the-specification)
  - [2.4 Create the Implementation Plan](#24-create-the-implementation-plan)
  - [2.5 Generate Tasks](#25-generate-tasks)
- [3. Create Jira Issue](#3-create-jira-issue)
- [4. Create Feature Branch](#4-create-feature-branch)
- [5. Build the Dashboard with Claude Code](#5-build-the-dashboard-with-claude-code)
  - [5.1 Set Up Python Environment](#51-set-up-python-environment)
  - [5.2 Build the Dashboard](#52-build-the-dashboard)
  - [5.3 Iterate and Improve](#53-iterate-and-improve)
- [6. Commit Your Changes](#6-commit-your-changes)
  - [6.1 Stage Your Changes](#61-stage-your-changes)
  - [6.2 Create the Commit](#62-create-the-commit)
- [7. Push and Create Pull Request](#7-push-and-create-pull-request)
  - [7.1 Push Your Branch](#71-push-your-branch)
  - [7.2 Create Pull Request](#72-create-pull-request)
  - [7.3 Verify Jira Integration](#73-verify-jira-integration)
- [8. Merge the Pull Request](#8-merge-the-pull-request)
  - [8.1 Review and Merge](#81-review-and-merge)
  - [8.2 Update Local Repository](#82-update-local-repository)
- [9. Session 2 Verification](#9-session-2-verification)
- [The Complete Workflow](#the-complete-workflow)
- [What's Next](#whats-next)

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

The Model Context Protocol (MCP) allows Claude Code to interact with external services like Jira. This means Claude can read your Jira issues directly.

### 1.1 Add Atlassian MCP Server

**Steps:**

1. Open Cursor and navigate to your tutorial project
2. Open the terminal (`` Ctrl+` ``)
3. Run the following command:

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

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

First, initialize spec-kit in your project:

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

The specification refines the PRD into detailed, actionable requirements.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.specify

   Based on the PRD in prd/ecommerce-analytics.md, create a detailed specification for the sales dashboard.

   The dashboard should have:
   - 2 KPI cards at the top (Total Sales, Total Orders)
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
   Create tasks that are small enough to complete in 30-60 minutes each.
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

## 3. Create Jira Issue

Now create a Jira issue for the dashboard task. This connects your work to the project management system.

### 3.1 Create Issue in Jira

**Option A: Use Claude Code (if MCP is working)**

In Claude Code:
```
Create a Jira issue in the ECOM project:
- Type: Story
- Title: Create sales dashboard with KPIs and charts
- Description: Implement a Streamlit dashboard showing Total Sales and Total Orders KPIs,
  a sales trend line chart, and bar charts for sales by category and region.
  Data source: data/sales-data.csv
```

**Option B: Create manually in Jira**

1. Go to your Jira workspace
2. Navigate to the ECOM project
3. Click **Create** (or the + button)
4. Fill in:
   - **Issue Type:** Story (or Task)
   - **Summary:** Create sales dashboard with KPIs and charts
   - **Description:**
     ```
     Implement a Streamlit dashboard showing:
     - Total Sales KPI
     - Total Orders KPI
     - Sales trend line chart
     - Sales by category bar chart
     - Sales by region bar chart

     Data source: data/sales-data.csv
     ```
5. Click **Create**

**Checkpoint:** Issue ECOM-1 exists in your Jira project.

---

## 4. Create Feature Branch

Now create a Git branch for your work. This keeps your changes isolated from the main codebase.

### 4.1 Create and Switch to Branch

**Steps:**

1. Make sure you are in your project directory in Cursor's terminal
2. Ensure you are on the main branch and up to date:
   ```bash
   git checkout main
   git pull origin main
   ```

3. Create a new feature branch:
   ```bash
   git checkout -b feature/ECOM-1-add-sales-dashboard
   ```

**Understanding this command:**
- `git checkout -b` creates a new branch AND switches to it
- `feature/` is a prefix indicating this is a feature branch
- `ECOM-1` is the Jira issue key (this enables traceability)
- `add-sales-dashboard` describes what the branch does

4. Verify you are on the new branch:
   ```bash
   git branch
   ```
   The current branch will have an asterisk (*) next to it.

**Checkpoint:** Running `git branch` shows `feature/ECOM-1-add-sales-dashboard` with an asterisk.

---

## 5. Build the Dashboard with Claude Code

Now you will build the Streamlit dashboard using Claude Code as your AI assistant.

### 5.1 Set Up Python Environment

First, create a virtual environment for your project dependencies.

**Steps:**

1. In Claude Code (run `claude` if not already in a session):
   ```
   Help me set up a Python virtual environment for this project.
   I need to install streamlit, pandas, and plotly for a dashboard.
   Create a requirements.txt file as well.
   ```

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

**Checkpoint:**
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

   Build the Streamlit sales dashboard based on our specification.

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

This will open your browser with the running dashboard.

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

Now save your work with a Git commit.

### 6.1 Stage Your Changes

**Steps:**

1. See what files have changed:
   ```bash
   git status
   ```
   You should see new files (app.py, requirements.txt, venv/) and modified files.

2. Check the `.gitignore` file — make sure `venv/` is listed (you don't want to commit the virtual environment).

   If `venv/` is not in `.gitignore`, add it:
   ```bash
   echo "venv/" >> .gitignore
   ```

3. Stage the files you want to commit:
   ```bash
   git add app.py requirements.txt .gitignore
   ```

   Or stage all changes (except ignored files):
   ```bash
   git add .
   ```

4. Verify what will be committed:
   ```bash
   git status
   ```
   Files should appear under "Changes to be committed" in green.

**Checkpoint:** Running `git status` shows your files staged for commit.

---

### 6.2 Create the Commit

**Steps:**

1. Create a commit with a message that includes the Jira key:
   ```bash
   git commit -m "ECOM-1: add sales dashboard with KPIs and charts"
   ```

   **Understanding the message format:**
   - `ECOM-1:` — Links this commit to the Jira issue
   - `add sales dashboard` — Describes what was added (use present tense)
   - Keep it concise but descriptive

2. Verify the commit:
   ```bash
   git log --oneline -1
   ```
   You should see your commit with the message.

**Checkpoint:** `git log` shows your commit with the Jira key in the message.

---

## 7. Push and Create Pull Request

Now push your changes to GitHub and create a pull request.

### 7.1 Push Your Branch

**Steps:**

1. Push the branch to your GitHub fork:
   ```bash
   git push -u origin feature/ECOM-1-add-sales-dashboard
   ```

   **Understanding this command:**
   - `git push` — Uploads commits to the remote repository
   - `-u origin` — Sets up tracking between local and remote branch
   - `feature/ECOM-1-add-sales-dashboard` — The branch to push

2. You may be prompted for GitHub credentials. If using HTTPS, enter your username and a personal access token (not your password).

**Checkpoint:** Git reports the push was successful.

---

### 7.2 Create Pull Request

**Steps:**

1. Go to your forked repository on GitHub
2. You should see a banner saying "feature/ECOM-1-add-sales-dashboard had recent pushes" with a **Compare & pull request** button
3. Click **Compare & pull request**
4. Fill in the pull request:
   - **Title:** `ECOM-1: Add sales dashboard with KPIs and charts`
   - **Description:**
     ```
     ## Summary
     - Added Streamlit dashboard for e-commerce sales analytics
     - Implemented Total Sales and Total Orders KPI cards
     - Added sales trend line chart
     - Added sales by category and region bar charts

     ## Test Plan
     - Run `streamlit run app.py` to verify dashboard works
     - Confirm all charts display correct data from CSV

     Resolves ECOM-1
     ```
5. Verify the base branch is `main` and the compare branch is your feature branch
6. Click **Create pull request**

**Checkpoint:** Pull request is created and visible on GitHub.

---

### 7.3 Verify Jira Integration

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

**Steps:**

1. On the pull request page in GitHub, review the "Files changed" tab
2. Verify the code looks correct
3. Click **Merge pull request**
4. Click **Confirm merge**
5. Optionally, click **Delete branch** to clean up the feature branch

**Checkpoint:** The pull request shows as "Merged" with a purple icon.

---

### 8.2 Update Local Repository

After merging, update your local main branch:

```bash
git checkout main
git pull origin main
```

Your local main branch now includes the dashboard code.

**Checkpoint:** Running `git log --oneline` on main shows your merged commit.

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
- [ ] Issue ECOM-1 created
- [ ] Issue shows linked GitHub activity (branch, commits, PR)

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
