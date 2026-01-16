# Capstone Project Development Environment

You have completed the tutorial and learned the full AI-assisted development workflow. Now it's time to apply these skills to your actual capstone project.

This guide walks you through setting up your capstone project using the same workflow you learned in the tutorial.

---

## Table of Contents

1. [What You Have Learned](#1-what-you-have-learned)
2. [Capstone Project Setup Checklist](#2-capstone-project-setup-checklist)
3. [Update Your PRD](#3-update-your-prd)
4. [Spec-Kit Workflow for Capstone](#4-spec-kit-workflow-for-capstone)
5. [Team Workflow](#5-team-workflow)
6. [Best Practices for Capstone Success](#6-best-practices-for-capstone-success)
7. [Common Capstone Patterns](#7-common-capstone-patterns)
8. [Capstone Resources](#8-capstone-resources)
9. [Final Reminders](#9-final-reminders)
10. [Quick Reference Card](#10-quick-reference-card)

---

## 1. What You Have Learned

```
┌─────────────────────────────────────────────────────────────┐
│                    Skills Acquired                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  AI-Assisted Development:    Professional Workflow:         │
│  ────────────────────────    ────────────────────           │
│  • Claude Code for coding    • Git version control          │
│  • Spec-kit for planning     • Branch-based development     │
│  • Natural language prompts  • Jira task tracking           │
│  • AI as thinking partner    • Evidence-based completion    │
│                                                             │
│  Technical Skills:           Deployment:                    │
│  ─────────────────           ───────────                    │
│  • Python/Streamlit          • Streamlit Community Cloud    │
│  • Virtual environments      • Public URL sharing           │
│  • GitHub repositories       • Traceability                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Capstone Project Setup Checklist

Use this checklist when setting up your actual capstone project. Each team member should complete these steps.

### Repository Setup

- [ ] **Create a new GitHub repository** for your capstone
  - One team member creates the repo
  - Others are added as collaborators (Settings → Collaborators)
  - Add `lontok` as a collaborator (your instructor)
  - Choose a clear, descriptive name (e.g., `capstone-inventory-system`)

- [ ] **Initialize the repository** with:
  - README.md with project description
  - .gitignore for your tech stack
  - LICENSE if applicable

- [ ] **Clone the repository** to your local machine using Cursor

   1. On your repository page on GitHub, click the green **Code** button
   2. Make sure **HTTPS** is selected and copy the URL
   3. Open Cursor → **File** → **New Window**
   4. Click **Clone Repo**
   5. Paste the repository URL and press **Enter/Return**
   6. Choose a location (e.g., your `GitHub` folder)
   7. Click **Open** when prompted

### Jira Setup (For Teams)

One team member creates the Jira project, then invites the rest of the team.

- [ ] **Create a shared Jira project**

   1. Use your existing Atlassian account (or create one at [atlassian.com](https://www.atlassian.com/))
   2. Access Jira by clicking the **menu icon** (four squares) in the top left, then click **Jira**
   3. In the left sidebar, click the **+** next to **Spaces** to create a new space
   4. For the space template, select **Software Development** on the left, then click **Use Template**
   5. When asked how your space is managed, select **Team-managed space**
   6. Name your project something descriptive and meaningful (e.g., `Inventory Management System`)
   7. Click **Show more** on the bottom left to set the **Project key** — this is important because you'll reference Jira issues by key and number (e.g., `INV-1`, `INV-2`)
   8. If prompted to connect to Confluence, skip this — we'll save documentation in GitHub
   9. If prompted to invite team members, you can add them now (see below) or do it later

   **After setup**, you'll see your board with three columns: **To Do**, **In Progress**, and **Done**. Click **Backlog** (tab to the left of "Board") — this is where Jira issues created via Claude Code will appear.

- [ ] **Invite team members** ([Atlassian docs](https://support.atlassian.com/jira-software-cloud/docs/add-people-to-team-managed-projects/))

   1. Next to your project name in the sidebar, click **More actions** (•••), then **Project settings**
   2. Select **Access**
   3. Click **Add people**
   4. Enter team members' email addresses (the ones they used for Atlassian)
   5. Set their role to **Member**

- [ ] **Connect Claude Code to your new Jira project**
  - Each team member must connect the Atlassian MCP to the new project
  - Follow the same steps from [Section 1 of the tutorial](04-session-2-workflow.md#1-connect-claude-code-to-jira): run `/mcp`, select **atlassian**, and authenticate
  - This time you'll be connecting to your capstone Jira project instead of the tutorial project

### Development Environment

- [ ] **Each team member** should have:
  - Cursor installed with Claude Code
  - Git configured with their name/email
  - Python 3.11+ (if using Python)
  - uv and spec-kit installed
  - Access to the shared Jira project

- [ ] **Create initial project structure**
  - Ask Claude Code to help set up a standard structure
  - Create requirements.txt or package.json
  - Set up virtual environment

### Spec-Kit Initialization

- [ ] **Initialize spec-kit** in your capstone repo. In the terminal:
  ```bash
  specify init . --ai claude
  ```

---

## 3. Update Your PRD

In the tutorial, you used a provided PRD. For your capstone, you'll revise the PRD you submitted last semester.

### Organize Your Notes

To help you update your PRD, create a `notes/` directory in your repo to collect:

- Meeting notes with your team or sponsor
- Your own thoughts and ideas
- Meeting transcripts or AI-generated meeting summaries
- Feedback from stakeholders

```
your-capstone-repo/
├── notes/
│   ├── sponsor-meeting-01.md
│   ├── team-brainstorm.md
│   └── feedback-summary.md
├── prd/
│   └── your-project-name.md    ← Your PRD goes here
├── specs/                       ← spec-kit will create this
└── ...
```

### Creating Your PRD with Claude Code

Use Claude Code and reference your notes using the `@` symbol:

```
Help me write a PRD based on @notes/sponsor-meeting-01.md and @notes/team-brainstorm.md

Include:
- Problem statement
- Target users
- Key features with acceptance criteria
- Technical constraints
```

You can also reference the entire notes directory:

```
Review @notes/ and help me update my PRD with the key requirements discussed.
```

### What a PRD Should Include

1. **Problem Statement** — What problem are you solving? Why does it matter?
2. **Target Users** — Who will use this? What are their needs?
3. **Features** — What will the solution do? (Be specific)
4. **Acceptance Criteria** — How do you know each feature is "done"?
5. **Constraints** — Technology requirements, timeline, team size

---

## 4. Spec-Kit Workflow for Capstone

Follow the same spec-kit workflow you learned in the tutorial:

```
┌─────────────────────────────────────────────────────────────┐
│                 Spec-Kit Workflow                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Constitution    → Project principles and standards      │
│         ↓                                                   │
│  2. Specification   → What to build (from your PRD)         │
│         ↓                                                   │
│  3. Plan            → How to build it (technical approach)  │
│         ↓                                                   │
│  4. Tasks           → Atomic work items                     │
│         ↓                                                   │
│  5. Jira Issues     → Create issues from tasks              │
│         ↓                                                   │
│  6. Implement       → Build with /speckit.implement         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Step-by-Step

1. **Create constitution** — Define your project's coding standards and principles:
   ```
   /speckit.constitution
   ```

2. **Create specification** — Convert your PRD into a technical specification:
   ```
   /speckit.specify @prd/your-project-name.md
   ```

3. **Create plan** — Generate an implementation plan:
   ```
   /speckit.plan
   ```

4. **Generate tasks** — Break the plan into atomic tasks:
   ```
   /speckit.tasks
   ```

5. **Create Jira issues** — Use Claude Code to create issues from your tasks:
   ```
   Create Jira issues from @specs/[your-spec]/tasks.md
   ```

6. **Implement** — Work through issues one at a time:
   ```
   /speckit.implement

   Implement [ISSUE-KEY] and move it to In Progress in Jira.
   ```

> **Remember:** After completing each issue, commit, push, and update Jira with evidence (implementation summary, commit hash, branch, GitHub link).

---

## 5. Team Workflow

When working as a team, the workflow expands slightly:

```
┌─────────────────────────────────────────────────────────────┐
│                    Team Workflow                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Pick up a Jira issue (assign to yourself)               │
│                 ↓                                           │
│  2. Create a feature branch                                 │
│     feature/PROJ-123-description                            │
│                 ↓                                           │
│  3. Build with Claude Code                                  │
│                 ↓                                           │
│  4. Commit with Jira key                                    │
│     "PROJ-123: add user login"                              │
│                 ↓                                           │
│  5. Push and create Pull Request                            │
│                 ↓                                           │
│  6. Update Jira with evidence                               │
│     (commit hash, branch, GitHub link)                      │
│                 ↓                                           │
│  7. Request review from teammate                            │
│                 ↓                                           │
│  8. Address feedback, push updates                          │
│                 ↓                                           │
│  9. Merge when approved                                     │
│                 ↓                                           │
│ 10. Move Jira issue to Done                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Code Review Guidelines

When reviewing a teammate's pull request:

1. **Check functionality** — Does the code do what the Jira issue describes?
2. **Read the code** — Is it clear and understandable?
3. **Look for issues** — Bugs, edge cases, security concerns
4. **Be constructive** — Suggest improvements, don't just criticize
5. **Approve or request changes** — Be timely; don't block teammates

When your code is reviewed:

1. **Respond to all comments** — Even if just "Done" or "Addressed"
2. **Don't take it personally** — Reviews improve code quality
3. **Ask questions** — If feedback is unclear, ask for clarification
4. **Push updates** — Address feedback in new commits

---

## 6. Best Practices for Capstone Success

### Use Branches Consistently

**Never commit directly to main.** Always:

1. Create a feature branch from main
2. Do your work on the branch
3. Create a PR when ready
4. Merge after review

This prevents conflicts and keeps main stable.

### Keep Jira Updated

- **Move cards** as work progresses (To Do → In Progress → Done)
- **Add evidence** when completing issues (implementation summary, commit hash, branch, GitHub link)
- **Add comments** when you encounter blockers
- **Link related issues** if they depend on each other

This keeps the whole team informed and creates traceability.

### Commit Often, Push Regularly

- **Commit** when you complete a logical unit of work
- **Push** at least once per work session
- This creates backup and enables collaboration

### Communicate with Your Team

- **Daily standups** — What did you do? What will you do? Any blockers?
- **Slack/Teams** — Quick questions and updates
- **PR comments** — Technical discussions about code

### Use Claude Code Effectively

Claude Code is most helpful when you:

1. **Provide context** — Tell it about your project and constraints
2. **Ask specific questions** — "How do I..." not "Fix this"
3. **Iterate** — Build on Claude's suggestions
4. **Verify** — Don't blindly accept generated code
5. **Learn** — Ask Claude to explain what it did

---

## 7. Common Capstone Patterns

### Starting a New Feature

With Claude Code, you can use natural language instead of memorizing git commands:

```
# In Claude Code:

Pull latest main and create a feature branch for PROJ-123 user dashboard

# Work with Claude to implement...

Commit my changes for PROJ-123 and push to GitHub

# Then update Jira with evidence
Update PROJ-123 in Jira with a comment summarizing what was implemented,
the commit hash, branch name, and GitHub link
```

> **Tip:** Claude Code handles the git commands for you. Just describe what you want in plain English.

<details>
<summary>Traditional git commands (for reference)</summary>

```bash
# 1. Make sure main is up to date
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/PROJ-123-add-user-dashboard

# 3. Start Claude Code and implement...

# 4. Commit and push
git add .
git commit -m "PROJ-123: add user dashboard with recent activity"
git push -u origin feature/PROJ-123-add-user-dashboard

# 5. Create PR on GitHub
```

</details>

### Handling Merge Conflicts

When you see "This branch has conflicts", ask Claude Code for help:

```
Help me resolve the merge conflicts with main
```

Claude Code will fetch the latest changes, identify conflicts, and guide you through resolving them.

<details>
<summary>Traditional git commands (for reference)</summary>

```bash
# 1. Get latest main
git fetch origin

# 2. Merge main into your branch
git merge origin/main

# 3. If conflicts, ask Claude for help
# "Help me resolve merge conflicts in src/app.py"

# 4. After resolving
git add .
git commit -m "PROJ-123: resolve merge conflicts"
git push
```

</details>

### Debugging with Claude Code

When something breaks:

```
I'm seeing this error: [paste error]

The relevant code is in [filename].

What's causing this and how do I fix it?
```

Claude can read your code and provide specific solutions.

---

## 8. Capstone Resources

### Documentation to Create

- [ ] **README.md** — Project overview, setup instructions, team members
- [ ] **CONTRIBUTING.md** — How to contribute, coding standards
- [ ] **Architecture doc** — System design, component overview

### Tools to Consider

| Tool | Purpose |
|------|---------|
| **GitHub Projects** | Kanban board integrated with GitHub |
| **GitHub Actions** | Automated testing on every PR |
| **Figma** | UI/UX design and prototyping |
| **Notion** | Team wiki and documentation |

### Getting Help

- **Claude Code** — First line of defense for technical issues
- **Team members** — Pair programming, code reviews
- **Instructor** — Office hours for complex problems
- **Online resources** — Stack Overflow, documentation

### Deployment Options

The tutorial used Streamlit Community Cloud, but your capstone may use different technology:

| Technology | Deployment Options |
|------------|-------------------|
| **Streamlit** | Streamlit Community Cloud (free) |
| **Flask/Django** | Heroku, Railway, Render, AWS |
| **React/Vue** | Vercel, Netlify, GitHub Pages |
| **API only** | Heroku, Railway, AWS Lambda |

Ask Claude Code for help with deployment:
```
Help me deploy my [Flask/React/etc.] app. What are my options?
```

> **Key principle:** Merge your feature branch to `main` before deploying. Most deployment platforms deploy from the `main` branch.

---

## 9. Final Reminders

1. **Start with the PRD** — Know what you are building before coding

2. **Use spec-kit** — Plan before you implement

3. **Keep Jira current** — Move cards, add evidence when done (commit hash, GitHub link)

4. **Commit with Jira keys** — Traceability matters

5. **Review each other's code** — Fresh eyes catch bugs

6. **Ask Claude for help** — It's there to make you more productive

7. **Have fun** — You are building something real with industry tools

---

## 10. Quick Reference Card

**With Claude Code (recommended):**
```
┌─────────────────────────────────────────────────────────────┐
│              Quick Reference - Claude Code                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Start new work:                                            │
│  "Pull latest main and create branch for PROJ-123"          │
│                                                             │
│  Save work:                                                 │
│  "Commit my changes for PROJ-123 and push to GitHub"        │
│                                                             │
│  Update Jira:                                               │
│  "Update PROJ-123 with commit hash, branch, and GitHub      │
│   link. Mark it Done."                                      │
│                                                             │
│  Update from main:                                          │
│  "Pull latest changes from main into my branch"             │
│                                                             │
│  Check status:                                              │
│  "What's the git status?"                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

<details>
<summary>Traditional git commands (for reference)</summary>

```
┌─────────────────────────────────────────────────────────────┐
│              Quick Reference - Git Commands                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Start new work:                                            │
│  git checkout main && git pull                              │
│  git checkout -b feature/PROJ-123-description               │
│                                                             │
│  Save work:                                                 │
│  git add . && git commit -m "PROJ-123: description"         │
│  git push -u origin feature/PROJ-123-description            │
│                                                             │
│  Update from main:                                          │
│  git fetch origin && git merge origin/main                  │
│                                                             │
│  Check status:                                              │
│  git status && git log --oneline -5                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

</details>

Good luck with your capstone! You have the skills and tools to succeed.
