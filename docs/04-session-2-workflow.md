# Session 2: Spec-Driven Development Workflow

This session covers the complete development workflow: from connecting Claude Code to Jira, through spec-driven planning, to building and saving your code.

## Table of Contents

- [Before You Begin: Prerequisites Check](#before-you-begin-prerequisites-check)
- [1. Connect Claude Code to Jira](#1-connect-claude-code-to-jira)
  - [1.1 Add Atlassian Rovo MCP Server](#11-add-atlassian-mcp-server)
- [2. Spec-Kit Workflow](#2-spec-kit-workflow)
  - [2.1 Initialize Spec-Kit](#21-initialize-spec-kit)
  - [2.2 Create the Constitution](#22-create-the-constitution)
  - [2.3 Create the Specification](#23-create-the-specification)
  - [2.4 Create the Implementation Plan](#24-create-the-implementation-plan)
  - [2.5 Generate Tasks](#25-generate-tasks)
- [3. Create Jira Issues](#3-create-jira-issues)
  - [3.1 Create the First Issue](#31-create-the-first-issue)
  - [3.2 Create Remaining Issues](#32-create-remaining-issues)
- [4. Build the Dashboard with Claude Code](#4-build-the-dashboard-with-claude-code)
  - [4.1 Set Up Python Environment](#41-set-up-python-environment)
  - [4.2 Build the Dashboard](#42-build-the-dashboard)
  - [4.3 Iterate and Improve](#43-iterate-and-improve)
- [5. Commit Your Changes](#5-commit-your-changes)
  - [5.1 Ask Claude Code to Commit](#51-ask-claude-code-to-commit)
- [6. Push to GitHub](#6-push-to-github)
  - [6.1 Ask Claude Code to Push](#61-ask-claude-code-to-push)
  - [6.2 Verify on GitHub](#62-verify-on-github)
- [7. Deploy to Streamlit Community Cloud](#7-deploy-to-streamlit-community-cloud)
  - [7.1 Sign Up for Streamlit Cloud](#71-sign-up-for-streamlit-cloud)
  - [7.2 Deploy Your App](#72-deploy-your-app)
  - [7.3 Share Your Dashboard](#73-share-your-dashboard)
- [8. Session 2 Verification](#8-session-2-verification)
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
│  • Atlassian Rovo MCP connected  • Constitution created          │
│  • Claude reads Jira        • Specification refined         │
│                             • Implementation plan           │
│                             • Task breakdown                │
│                                                             │
│  Development:               Version Control:                │
│  ────────────               ────────────────                │
│  • Jira issue ECOM-1        • Commits with Jira key         │
│  • Streamlit dashboard      • Code pushed to GitHub         │
│  • Python virtual env       • Dashboard deployed live       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Connect Claude Code to Jira

**What is MCP?** The Model Context Protocol (MCP) is a way for AI assistants like Claude Code to connect to external tools and services. Think of it as a "plugin system" that lets Claude Code talk to other applications. In this tutorial, we will use MCP to connect Claude Code to Jira so Claude can read your project tasks directly.

### 1.1 Add Atlassian Rovo MCP Server

**Steps:**

1. Open Cursor and navigate to your tutorial project
2. Use the existing terminal, or open a new one (**Terminal** → **New Terminal**)
3. **If Claude Code is currently running**, type `/exit` to quit first. You need to add the MCP server before starting Claude Code.
4. Run the following command to add the Atlassian Rovo MCP server:

   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

   You'll see a message confirming the server was added to your config.

5. Start Claude Code:
   ```bash
   claude
   ```

6. Verify the server is registered by typing:
   ```
   /mcp
   ```
   You should see `atlassian` listed. It will likely show that it requires authentication.

7. Use the **up/down arrow keys** to select `atlassian`, then press **Enter/Return** to authenticate.

8. A browser window will open for authentication:
   - Log in with your Atlassian account
   - Authorize Claude Code to access your Jira workspace
   - Return to the terminal

9. Test the connection by asking:
   ```
   What Jira projects do I have access to?
   ```

10. Claude should now list your ECOM project. You'll see something like:

   | Key | Name | Type |
   |-----|------|------|
   | ECOM | E-Commerce Analytics | Software (Team-managed) |

**Checkpoint:** Claude Code can see your Jira workspace and ECOM project.

**Note:** You may need to re-authenticate occasionally. If Claude reports it cannot access Jira, run `/mcp` to check the Atlassian server status. If it shows authentication is required, use the arrow keys to select `atlassian` and press **Enter/Return** to re-authenticate.

---

## 2. Spec-Kit Workflow

[Spec-kit](https://github.com/github/spec-kit) is GitHub's tool for turning requirements into working code through AI-assisted planning — think of it as creating a detailed project plan before you start building. It follows a structured process: Constitution → Specification → Plan → Tasks → Implementation.

### 2.1 Initialize Spec-Kit

First, initialize spec-kit in your project.

**In Cursor's terminal** (not inside Claude Code), run:

```bash
specify init . --ai claude
```

You may see a warning: "Current directory is not empty... Do you want to continue?" — type `y` and press **Enter/Return** to continue. This is expected because you cloned a repository that already has files.

When asked to "Choose script type", use the arrow keys to select:
- **macOS:** `sh` (POSIX Shell)
- **Windows:** `ps` (PowerShell)

Then press **Enter/Return** to confirm.

This creates the necessary configuration files for spec-kit to work with Claude Code, including the slash commands you will use in the following steps.

**Checkpoint:** Verify the initialization succeeded:

1. You should see output confirming the initialization completed
2. A `.specify/` directory should now exist in your project
3. A `.claude/commands/` directory should be created with the spec-kit slash commands

To verify, either:
- **In the file explorer:** Expand the `.specify/` and `.claude/commands/` folders in Cursor's left sidebar
- **In the terminal:** Run `ls -la .specify/` and `ls -la .claude/commands/`

You should see files like `speckit.constitution.md`, `speckit.specify.md`, etc. in the `.claude/commands/` directory. These `.md` files are detailed prompts that tell Claude Code exactly how to execute each slash command.

**Important:** The slash commands (`/speckit.constitution`, `/speckit.specify`, etc.) will NOT work until this initialization step completes successfully. If you don't see these directories, re-run the `specify init` command.

---

### 2.2 Create the Constitution

The constitution establishes principles and guidelines for your project. It ensures consistent decision-making throughout development.

**Steps:**

1. In the terminal, start Claude Code:
   ```bash
   claude
   ```

2. Ask Claude to help create the constitution:
   ```
   /speckit.constitution

   Create a constitution for our e-commerce analytics project.
   The project will build a Streamlit dashboard for sales data visualization.
   Key principles should include:
   - Simple, readable code
   - User-friendly interactive visualizations
   - Following Python best practices
   - Use Python virtual environment for dependency isolation
   ```

3. You'll see a permission prompt asking to use the skill. Select **Yes** to continue.

4. Claude will generate the constitution. When it wants to create or edit a file, you'll see:

   ```
   Do you want to make this edit to constitution.md?
   > 1. Yes
     2. Yes, allow all edits during this session (shift+tab)
     3. No
   ```

   Select **Yes** to approve the edit. You can also select option 2 to allow all edits for the rest of this session without being asked each time.

5. Preview the generated constitution file:
   - In Cursor's file explorer (left sidebar), navigate to `.specify/memory/constitution.md`
   - Right-click the file and select **Open Preview** to view the formatted markdown

**Checkpoint:** The constitution file exists at `.specify/memory/constitution.md` and contains the principles you specified.

---

### 2.3 Create the Specification

The specification refines the PRD (Product Requirements Document — the document in `prd/ecommerce-analytics.md` that describes what we want to build) into detailed, actionable requirements.

> **About the `@` Symbol**
>
> When you type `@` followed by a file path in Claude Code, it includes that file's content in your message. This is called a "file reference."
>
> Benefits of using `@`:
> - Claude sees the **actual file content**, not just a file name
> - No need to copy/paste — the entire file is included automatically
> - Works with any file type: code, markdown, CSV, etc.
> - You can reference multiple files: `@file1.py @file2.py`
>
> This is an example of **context engineering** — the practice of giving AI the right information to get better results. The more relevant context you provide, the more accurate and useful Claude's responses will be.

> **What to include in your prompt:**
>
> Use `/speckit.specify` to describe **what** you want to build and **why**. Focus on requirements and user needs, not the tech stack — that comes later in the planning phase.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.specify @prd/ecommerce-analytics.md
   ```

   This tells Claude to read the PRD file and use spec-kit to create a detailed specification from it.

2. Claude will analyze the PRD and create a specification

3. Preview the generated specification:
   - In Cursor's file explorer, navigate to `specs/` and find the folder for your feature (e.g., `001-sales-dashboard/`)
   - Right-click `spec.md` and select **Open Preview** to view the formatted specification

4. If a `checklists/` folder was created inside your feature folder, also preview `requirements.md` to see the detailed requirements checklist

> **Note:** Spec-kit automatically created a feature branch for this work (you may see something like `001-sales-dashboard` in your terminal prompt). This keeps your changes separate from the main branch until you're ready to merge. We'll merge back to main after implementation.

**Checkpoint:**
- A specification exists at `specs/[feature-name]/spec.md`
- (Optional) A requirements checklist exists at `specs/[feature-name]/checklists/requirements.md`

---

### 2.4 Create the Implementation Plan

The plan outlines how you will build the specification technically.

> **What to include in your prompt:**
> - **Technology preferences** — frameworks, languages, libraries you want to use
> - **Coding standards** — patterns, conventions, or best practices to follow
> - **Constraints** — any limitations like compatibility requirements or dependencies
>
> This guidance helps Claude generate a plan tailored to your preferences.

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

3. Preview the generated plan:
   - In Cursor's file explorer, navigate to `specs/` and open your feature folder (e.g., `001-sales-dashboard/`)
   - Right-click `plan.md` and select **Open Preview**

**Checkpoint:** An implementation plan exists at `specs/[feature-name]/plan.md` with clear technical direction.

---

### 2.5 Generate Tasks

Break the plan into specific, actionable tasks.

**Steps:**

1. In Claude Code, run:
   ```
   /speckit.tasks
   ```

2. Claude will automatically parse your specification and plan, then output a list of tasks

3. Preview the generated tasks:
   - In Cursor's file explorer, navigate to `specs/` and open your feature folder (e.g., `001-sales-dashboard/`)
   - Right-click `tasks.md` and select **Open Preview**

4. Review the tasks — you should see something like:
   - Set up Python virtual environment and dependencies
   - Create main Streamlit app structure
   - Implement KPI scorecards
   - Implement sales trend line chart
   - Implement category bar chart
   - Implement region bar chart

**Checkpoint:** A tasks file exists at `specs/[feature-name]/tasks.md` with clear implementation steps.

---

## 3. Create Jira Issues

Now create Jira issues based on the tasks generated by spec-kit. This connects your work to the project management system.

### 3.1 Create the First Issue

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to create the first issue:
   ```
   Based on the tasks in @specs/001-sales-dashboard/tasks.md, what should be the first Jira issue to create?
   Create it in the ECOM project.
   ```

   *Replace `001-sales-dashboard` with your actual feature folder name.*

2. Claude will:
   - Review the tasks from spec-kit in the `tasks.md` file
   - Use the **Atlassian MCP server** to connect directly to your Jira project
   - Create the first issue (likely ECOM-1)
   - Provide the issue details

> **How does Claude know to use Jira?** When you mention "Jira" or "ECOM project," Claude Code automatically uses the Atlassian MCP server you configured in Section 1. This lets Claude create and manage issues directly — no copy/paste needed.

3. Verify the issue was created:
   - Claude may provide a direct link to the issue — click it to open in your browser
   - Or manually: go to your Jira workspace, open the **ECOM (E-Commerce Analytics)** project, and click the **Backlog** tab
   - You should see the issue Claude just created (e.g., ECOM-1)

4. Click on the issue to view its **Description** — this shows the details Claude generated from your tasks

**Checkpoint:** Issue ECOM-1 is visible in the backlog with a detailed description.

---

### 3.2 Create Remaining Issues

**Steps:**

1. In Claude Code, ask it to create the remaining issues:
   ```
   Create Jira issues in the ECOM project for the remaining tasks in @specs/001-sales-dashboard/tasks.md
   ```

   *Replace `001-sales-dashboard` with your actual feature folder name.*

2. Claude will create additional issues (ECOM-2, ECOM-3, etc.) for each remaining task.

3. Verify the issues were created:
   - Refresh the Jira backlog in your browser to see all new issues — click on a few to confirm the descriptions look good, or
   - Click the direct links Claude provides to view each issue

**Checkpoint:** Multiple issues (ECOM-1, ECOM-2, etc.) are visible in your Jira backlog.

---

## 4. Build the Dashboard with Claude Code

Now you will build the dashboard using Claude Code as your AI assistant.

**What is Streamlit?** [Streamlit](https://streamlit.io/) is a Python library that makes it easy to create web-based dashboards and data apps. Instead of writing HTML, CSS, and JavaScript, you write Python code and Streamlit turns it into a web page. It's popular for data visualization because you can go from data to dashboard quickly.

### 4.1 Build the Dashboard

Now use Claude Code to build the dashboard. This step will create multiple files, so you'll see many edit permission prompts.

> **Claude Code Modes**
>
> Claude Code has different modes that control how it handles edits. Press **Shift+Tab** to cycle through them:
>
> | Mode | Behavior | When to Use |
> |------|----------|-------------|
> | **Normal** | Asks permission for each edit | Learning, reviewing changes carefully |
> | **Auto-accept** | Makes edits without asking | Trusting Claude, doing many edits |
> | **Plan mode** | Explains what it will do, waits for approval | Complex changes, want to review before executing |
>
> For this implementation phase, consider switching to **Auto-accept** mode to speed things up. You can always press **Shift+Tab** to change modes at any time.

**Steps:**

1. Ask Claude which issue to start with:
   ```
   Which Jira issue should we implement first?
   ```

   Claude will review your tasks and recommend the first issue (likely ECOM-1).

2. Implement the first task:
   ```
   /speckit.implement

   Implement ECOM-1 and move it to In Progress in Jira.
   ```

   *Replace `ECOM-1` with the issue Claude recommended in step 1.*

3. Claude will use the Jira issue description to understand and complete the work.

4. Review the generated code. Make sure you understand what it does.

5. If Claude asks where to put the file, a common choice is:
   - `app.py` in the project root, or
   - `src/dashboard.py` in a source folder

**Test the dashboard:**

In the terminal (not Claude Code), run:
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

### 4.2 Iterate and Improve

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

### 4.3 Merge Your Work to Main

Spec-kit created a feature branch for your work. Now that implementation is complete, merge your changes back to the main branch.

**Steps:**

1. In the terminal (not Claude Code), check which branch you're on:
   ```bash
   git branch
   ```
   You should see an asterisk (*) next to a branch name like `001-sales-dashboard`.

2. Ask Claude Code to merge your work into main:
   ```
   Merge my current feature branch into main
   ```

   Claude will switch to the main branch and merge your changes.

3. Verify you're now on main:
   ```bash
   git branch
   ```
   The asterisk (*) should now be next to `main`.

**Checkpoint:** You are on the `main` branch with all your dashboard changes included.

---

## 5. Commit Your Changes

Now save your work with a Git commit. Claude Code can handle all the git operations for you.

### 5.1 Ask Claude Code to Commit

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

### 5.2 Update Jira with Git Info

Now update the Jira issue with your commit information and mark it complete.

**Steps:**

1. In Claude Code:
   ```
   Update ECOM-1 in Jira:
   - Add a comment with the commit hash and branch name
   - Move the issue to Done
   ```

2. Claude will:
   - Add a comment to the issue with your git commit details
   - Update the issue status to Done

3. Verify in Jira:
   - Open ECOM-1 in your browser
   - Check the status shows "Done"
   - Look for the comment with git info

**Checkpoint:** ECOM-1 shows status "Done" with a comment containing git info.

---

## 6. Push to GitHub

Now push your code to GitHub so it's saved in the cloud and ready for deployment.

### 6.1 Ask Claude Code to Push

**Steps:**

1. In Claude Code (run `claude` if not already in a session), ask it to push your changes:
   ```
   Push my changes to GitHub.
   ```

2. Claude will push your commit to GitHub.

3. You may be prompted for GitHub credentials. If using HTTPS, enter your username and a personal access token (not your password).

**Checkpoint:** Claude confirms the push was successful.

---

### 6.2 Verify on GitHub

**Steps:**

1. Go to your repository on GitHub (`github.com/[your-username]/ai-dev-workflow-tutorial`)
2. You should see your recent commit with the message containing `ECOM-1`
3. Click on the commit to see the files you added

**Verify Jira Integration:**

1. Go to your Jira workspace
2. Open issue ECOM-1
3. Look for a "Development" panel or section
4. You should see your commit linked

**Checkpoint:** Your code is visible on GitHub and linked in Jira.

---

## 7. Deploy to Streamlit Community Cloud

Now make your dashboard publicly accessible by deploying it to Streamlit Community Cloud.

> **Note:** Spec-kit included deployment in your tasks based on the PRD requirements. We'll complete this step manually to learn the Streamlit Cloud interface.

**Steps:**

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Click **New app**
3. Select your repository: `[your-username]/ai-dev-workflow-tutorial`
4. Set the **Main file path** to `app.py` (or wherever your dashboard file is located)
5. Click **Deploy** and wait 1-2 minutes

Once deployed, you'll get a public URL like:
```
https://[your-username]-ai-dev-workflow-tutorial-app-xxxxx.streamlit.app
```

Copy this URL and share it! Anyone with the link can view your dashboard.

**Checkpoint:** Your dashboard is live and accessible via the public URL.

---

## 8. Session 2 Verification

Verify everything is complete:

### MCP Integration
- [ ] Atlassian Rovo MCP server connected to Claude Code
- [ ] Claude can access your Jira workspace

### Spec-Kit Artifacts
- [ ] Constitution created
- [ ] Specification created
- [ ] Implementation plan created
- [ ] Tasks generated

### Jira
- [ ] Multiple issues created from spec-kit tasks (ECOM-1, ECOM-2, etc.)
- [ ] ECOM-1 status is "Done" with git info comment

### Dashboard
- [ ] Streamlit app runs locally
- [ ] KPI cards display Total Sales and Total Orders
- [ ] Line chart shows sales trend
- [ ] Bar charts show category and region breakdowns

### Version Control & Deployment
- [ ] Commit message includes Jira key (ECOM-1)
- [ ] Code pushed to GitHub
- [ ] Dashboard deployed on Streamlit Community Cloud
- [ ] Public URL accessible

---

## The Complete Workflow

Congratulations! You have completed the full workflow:

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ →  │ spec-kit │ →  │  Jira   │ →  │  Code  │
└─────────┘    └──────────┘    └─────────┘    └────────┘
     ✓              ✓              ✓              ✓
                                                  ↓
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Live!  │ ←  │  Deploy  │ ←  │  Push   │ ←  │ Commit │
└─────────┘    └──────────┘    └─────────┘    └────────┘
     ✓              ✓              ✓              ✓
```

You now know how to:
1. Start with requirements (PRD)
2. Use spec-kit to plan systematically
3. Track work in Jira
4. Build with AI assistance
5. Commit with traceability
6. Push to GitHub
7. Deploy a live dashboard

This is the workflow you will use for your capstone project.

---

## What's Next

Continue to [Next Steps](06-next-steps.md) to learn how to apply this workflow to your capstone project.
