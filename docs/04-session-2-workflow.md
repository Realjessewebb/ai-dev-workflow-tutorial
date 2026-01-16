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
  - [4.1 Build the Dashboard](#41-build-the-dashboard)
  - [4.2 Commit, Push, and Update Jira](#42-commit-push-and-update-jira)
  - [4.3 Continue with Remaining Issues](#43-continue-with-remaining-issues)
  - [4.4 Merge Your Work to Main](#44-merge-your-work-to-main)
- [5. Deploy to Streamlit Community Cloud](#5-deploy-to-streamlit-community-cloud)
  - [5.1 Start the Deployment Issue](#51-start-the-deployment-issue)
  - [5.2 Deploy to Streamlit Cloud](#52-deploy-to-streamlit-cloud)
  - [5.3 Update Jira with Deployment Evidence](#53-update-jira-with-deployment-evidence)
- [6. Session 2 Verification](#6-session-2-verification)
- [7. The Complete Workflow](#7-the-complete-workflow)
- [8. What to Submit](#8-what-to-submit)
- [9. What's Next](#9-whats-next)

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

> **Why not just ask Claude to build the dashboard?** You could prompt Claude Code directly: "Build me a sales dashboard." But without clear specifications, Claude has to make assumptions about what you want — leading to errors, missing features, or unwanted extras. Spec-kit avoids this by creating a detailed plan first, so Claude knows exactly what to build.

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

4. Review the generated code. You can ask Claude to explain the main files:
   ```
   What are the main code files you created? Help me understand what each one does.
   ```

**Test the dashboard:**

When the implementation completes successfully, Claude will show a summary with instructions on how to run the app. Follow those instructions to test your dashboard.

Typically this involves:
1. Activating the virtual environment
2. Running `streamlit run app.py` (or similar command)
3. Opening http://localhost:8501 in your browser

**To stop the dashboard:** Press `Ctrl+C` in the terminal.

**Checkpoint:** The dashboard runs and confirms Streamlit is working. You may not see charts yet — most likely just the dashboard title. That's expected at this stage.

---

### 4.2 Commit, Push, and Update Jira

After completing the first issue, save your work and update Jira to show evidence of completion.

> **What is a commit?** A commit is a snapshot of your code at a specific point in time. Think of it like saving a version of a document — you can always go back to any previous commit if something goes wrong.
>
> **What is a push?** A push uploads your commits to GitHub (the cloud). Until you push, your commits only exist on your computer. Pushing ensures your work is backed up and visible to others.
>
> **Best practice:** Commit frequently at meaningful moments — like after implementing a Jira issue, completing a feature, or fixing a bug. This way you never lose much progress, and each commit tells a clear story of what changed.

**Steps:**

1. Ask Claude to commit your changes with the Jira issue key:
   ```
   Commit my changes for ECOM-1.
   Make sure venv/ is in .gitignore.
   ```

   *Replace `ECOM-1` with your actual issue key.*

   > **Tip:** With Claude Code, you don't need to memorize git commands. Just describe what you want in natural language, and Claude handles the rest.

   > **What is .gitignore?** This file tells Git which files to ignore. The `venv/` folder contains installed packages that can be recreated from `requirements.txt`, so we don't store it in Git.

   You'll see output like: `Commit: abc123 on branch 001-sales-dashboard`

   > **What is a branch?** A branch is a separate copy of your code where you can make changes without affecting the main version. Spec-kit created a feature branch (like `001-sales-dashboard`) so your work stays isolated until it's ready. This is a professional best practice — you never work directly on `main`. Once your feature is complete and tested, you merge it back to `main` (we'll do this in section 4.4).

2. Push to GitHub:
   ```
   Push my changes to GitHub.
   ```

   **View your branch on GitHub:**
   - Go to your repository on GitHub
   - Click the branch dropdown (it shows "main" by default)
   - Select your feature branch (e.g., `001-sales-dashboard`)
   - You'll see your committed files on this branch

3. Update Jira with evidence of completion:
   ```
   Update ECOM-1 in Jira:
   - Add a comment summarizing what was implemented, the commit hash, branch name, and GitHub link
   - Move the issue to Done
   ```

   *Replace `ECOM-1` with your actual issue key.*

   > **Need to re-authenticate?** If Claude reports it can't access Jira, run `/mcp`, select **atlassian**, then select **Re-authenticate** to sign in again.

   > **What is a commit hash?** A commit hash (like `05a9ada`) is a unique ID for each commit. It's like a fingerprint — no two commits have the same hash. This lets you reference a specific snapshot of your code.
   >
   > **What does the GitHub link point to?** The link goes directly to your commit on GitHub, showing exactly what files changed and what was added or removed. Anyone clicking the link can see the evidence of your work.

   This creates a record of your work — helpful for tracking progress and for anyone reviewing the project later.

4. Verify in Jira:
   - Open ECOM-1 in your browser
   - Check the status shows "Done"
   - Look for the comment with what was implemented and the git info (commit hash, branch, GitHub link)

5. Verify tasks were marked complete:
   - Open your tasks file (e.g., `specs/001-sales-dashboard/tasks.md`)
   - Completed tasks show `[x]` instead of `[ ]`:
     ```
     - [x] T001 Create requirements.txt with dependencies
     - [x] T002 Create app.py with basic configuration
     ```

**Checkpoint:** ECOM-1 shows status "Done" with a comment, and tasks are marked `[x]` in tasks.md.

---

### 4.3 Continue with Remaining Issues

Now repeat the cycle for each remaining Jira issue:

1. **Ask Claude which issue to work on next:**
   ```
   Which Jira issue should we implement next?
   ```

2. **Implement the issue:**
   ```
   /speckit.implement

   Implement ECOM-2 and move it to In Progress in Jira.
   ```

   *Replace `ECOM-2` with the issue Claude recommended.*

3. **Test your changes** — follow Claude's instructions to verify the implementation works.

   > **Review the code:** Take a moment to look at what Claude changed. For this project, most edits will be in `app.py`. Ask Claude to explain anything you don't understand.

4. **Commit, push, and update Jira** (same as section 4.2):
   ```
   Commit my changes for ECOM-2 and push to GitHub.

   Update the Jira issue with:
   - Summary of what was implemented
   - Commit hash, branch name, and GitHub link
   - Mark it Done
   ```

   *Replace `ECOM-2` with your actual issue key.*

5. **Verify completion:**
   - Jira issue shows "Done" with a detailed comment
   - Tasks marked `[x]` in tasks.md

> **🔁 Repeat steps 1-5 for each remaining Jira issue until all are complete.**

> ⚠️ **Skip the deployment task for now!** If you have a Jira issue for deployment, leave it — we'll handle deployment in section 5 after merging to main. You can't deploy until your code is on the `main` branch.

> **Tip:** Watch Claude Code's output as it works. You'll see what files it creates, what commands it runs, and how it solves problems — it may even launch a virtual browser to test the application automatically. This is a great way to learn!
>
> **Want to see the dashboard yourself?** Ask Claude: `How do I run the dashboard in my own browser?`
>
> **Suggested prompts:** Claude Code may suggest the next prompt to run — press **Tab** to accept it. While you're learning, it's good to write your own prompts so you understand the workflow. As you get comfortable, you can trust and accept the suggestions.

You can also ask Claude to fix or improve things:

```
The chart colors don't match our brand. Can you update them?
```

**Checkpoint:** All implementation issues are marked "Done" with comments showing what was implemented and git info. All implementation tasks marked `[x]` in tasks.md. (Deployment task remains — we'll do that in section 5.)

---

### 4.4 Merge Your Work to Main

Spec-kit created a feature branch for your work. Now that implementation is complete, merge your changes back to the main branch.

> **What is a merge?** Merging combines your feature branch changes into the main branch. It's like saying "my feature is done and tested — add it to the official version." After merging, main contains all your new code.

**Steps:**

1. Ask Claude to check which branch you're on:
   ```
   Which git branch am I on?
   ```

   You should be on your feature branch (e.g., `001-sales-dashboard`).

2. Ask Claude to merge your work into main:
   ```
   Merge my current feature branch into main
   ```

   Claude will switch to the main branch and merge your changes.

3. Push main to GitHub:
   ```
   Push main to GitHub
   ```

   This updates GitHub with your merged code.

4. Verify on GitHub:
   - Go to your repository on GitHub
   - Make sure you're viewing the **main** branch
   - You should see all your dashboard files

**Checkpoint:** The `main` branch on GitHub contains all your dashboard code.

---

## 5. Deploy to Streamlit Community Cloud

Now make your dashboard publicly accessible by deploying it to Streamlit Community Cloud.

> **Important:** Make sure you've completed section 4.4 (Merge Your Work to Main) before deploying. Streamlit Cloud deploys from the `main` branch, so your code needs to be there first.

### 5.1 Start the Deployment Issue

If you have a Jira issue for deployment, let's complete it now.

**Steps:**

1. Ask Claude which deployment issue to work on:
   ```
   Which Jira issue is for deployment?
   ```

2. If a deployment issue exists, implement it:
   ```
   /speckit.implement

   Implement the deployment issue and move it to In Progress in Jira.
   ```

   Claude will provide instructions for deploying to Streamlit Community Cloud.

### 5.2 Deploy to Streamlit Cloud

Follow these steps to deploy (Claude may guide you through this):

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Click **Create app**
3. Select your repository: `[your-username]/ai-dev-workflow-tutorial`
4. Select the **Branch**: `main`
5. Set the **Main file path** to `app.py` (or wherever your dashboard file is located)
6. (Optional) Set a custom **App URL** like `sales-dashboard-yourname` for a cleaner URL
7. Click **Deploy** and wait 1-2 minutes

Once deployed, you'll get a public URL like:
```
https://sales-dashboard-yourname.streamlit.app
```

### 5.3 Update Jira with Deployment Evidence

Complete the deployment issue with evidence:

```
Update the deployment Jira issue:
- Add a comment with the live Streamlit URL
- Mark it Done
```

**Checkpoint:** Your dashboard is live and accessible via the public URL. The deployment Jira issue is marked "Done" with the live URL in the comments.

---

## 6. Session 2 Verification

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
- [ ] All issues marked "Done" with comments (implementation summary, commit hash, branch, GitHub link)
- [ ] Tasks marked `[x]` in tasks.md

### Dashboard
- [ ] Streamlit app runs locally
- [ ] KPI cards display Total Sales and Total Orders
- [ ] Line chart shows sales trend
- [ ] Bar charts show category and region breakdowns

### Version Control
- [ ] Commits include Jira issue keys
- [ ] Feature branch merged to main
- [ ] Code pushed to GitHub

### Deployment
- [ ] Dashboard deployed on Streamlit Community Cloud
- [ ] Public URL accessible
- [ ] Deployment Jira issue marked "Done" with live URL in comments

---

## 7. The Complete Workflow

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

## 8. What to Submit

**Due: January 25** — Submit the following to Brightspace under the **AI Dev Workflow Tutorial** assignment:

1. **GitHub repository link** - Your public repo URL (e.g., `https://github.com/yourusername/ai-dev-workflow-tutorial`)

2. **Streamlit dashboard link** - Your live deployed dashboard URL (e.g., `https://sales-dashboard-yourname.streamlit.app`)

3. **Jira issue screenshot(s)** - Screenshot of one completed Jira issue showing:
   - Issue status is "Done"
   - Comment with implementation summary, commit hash, branch name, and GitHub link

   If the entire issue doesn't fit in one screenshot, submit multiple screenshots. Name them:
   - `jira-01.png`
   - `jira-02.png`
   - etc.

---

## 9. What's Next

Continue to [Capstone Project Dev Environment](06-capstone-project-dev-environment.md) to set up your capstone project.
