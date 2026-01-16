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
6. [What to Submit](#6-what-to-submit)
7. [Best Practices for Capstone Success](#7-best-practices-for-capstone-success)
8. [Common Capstone Patterns](#8-common-capstone-patterns)
9. [Capstone Resources](#9-capstone-resources)
10. [Final Reminders](#10-final-reminders)
11. [Quick Reference Card](#11-quick-reference-card)

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
  - **Keep the repository private** — This protects your sponsor's proprietary information, prevents other teams from copying your work, and follows professional practices for client projects
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

**Copy your existing PRD** to the `prd/` folder in your repo. This gives Claude Code access to your current requirements, and you'll pass it to the `/speckit.specify` command later to generate your technical specification.

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
│   └── your-project-name.md    ← Copy your existing PRD here
├── specs/                       ← spec-kit will create this
└── ...
```

### Updating Your PRD with Claude Code

Use Claude Code and reference your PRD and notes using the `@` symbol:

```
Review @prd/your-project-name.md and update it based on @notes/sponsor-meeting-01.md and @notes/team-brainstorm.md

Make sure the PRD includes:
- Problem statement
- Target users
- Key features with acceptance criteria
- Technical constraints
```

You can also reference the entire notes directory:

```
Review @prd/your-project-name.md and @notes/ and help me update my PRD with the key requirements discussed.
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
│         ↓                                                   │
│  7. Commit & Push   → Save and share your work              │
│         ↓                                                   │
│  8. Update Jira     → Add evidence, move to Done            │
│                                                             │
│  (Repeat 6-8 for each issue)                                │
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

7. **Commit and push** — After completing the implementation:
   ```
   Commit my changes for [ISSUE-KEY] and push to GitHub.
   ```

8. **Update Jira** — Add evidence and mark the issue complete:
   ```
   Update [ISSUE-KEY] in Jira with a comment summarizing what was implemented,
   the commit hash, branch name, and GitHub link. Move it to Done.
   ```

Repeat steps 6-8 for each issue.

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
│  5. Push to GitHub                                          │
│                 ↓                                           │
│  6. Update Jira with evidence                               │
│     (commit hash, branch, GitHub link)                      │
│                 ↓                                           │
│  7. Merge to main and move Jira issue to Done               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Avoiding Conflicts

When multiple people work on the same codebase, coordination is key:

1. **Assign yourself to a Jira issue before starting** — This signals to teammates that you're working on it. Only one person should be assigned to an issue at a time.

2. **Check the Jira board before picking up work** — Make sure no one else is already working on the issue or a related feature.

3. **Work on separate files when possible** — Coordinate with your team so you're not editing the same files simultaneously.

4. **Pull from main frequently** — Before starting new work and before merging, pull the latest changes:
   ```
   Pull the latest changes from main into my branch
   ```

5. **Push your work regularly** — Don't wait until everything is perfect. Frequent pushes help the team see what's changing.

6. **Communicate** — Use your team chat to announce when you're starting and finishing work on an issue.

---

## 6. What to Submit

**Due: January 28** — Submit the following to Brightspace under the **Capstone Project Development Environment** assignment:

1. **GitHub repository link** — Your team's repo URL (e.g., `https://github.com/team/capstone-project`). Make sure `lontok` is added as a collaborator.

2. **Jira board screenshot** — Screenshot of your Jira board showing:
   - Your project name and key
   - The board columns (To Do, In Progress, Done)

3. **PRD file screenshot** — Screenshot showing your PRD file exists in the `prd/` folder of your repository

---

## 7. Best Practices for Capstone Success

### Use Branches Consistently

**Never commit directly to main.** Always:

1. Create a feature branch from main
2. Do your work on the branch
3. Merge to main when complete

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

### Use Claude Code Effectively

Claude Code is most helpful when you:

1. **Provide context** — Tell it about your project and constraints
2. **Ask specific questions** — "How do I..." not "Fix this"
3. **Iterate** — Build on Claude's suggestions
4. **Verify** — Don't blindly accept generated code
5. **Learn** — Ask Claude to explain what it did

---

## 8. Common Capstone Patterns

### Working on a Jira Issue

After completing the spec-kit setup (steps 1-5 in [Section 4](#4-spec-kit-workflow-for-capstone)), work through each issue:

1. **Pick a Jira issue** and assign it to yourself
2. **Implement** using `/speckit.implement`:
   ```
   /speckit.implement

   Implement PROJ-123 and move it to In Progress in Jira.
   ```
3. **Commit and push**:
   ```
   Commit my changes for PROJ-123 and push to GitHub
   ```
4. **Update Jira** with evidence:
   ```
   Update PROJ-123 in Jira with a comment summarizing what was implemented,
   the commit hash, branch name, and GitHub link. Move it to Done.
   ```

Repeat steps 1-4 for each issue. When all issues are complete, merge your feature branch to main:
```
Merge my branch to main and push
```

> **Tip:** Claude Code handles the git commands for you. Just describe what you want in plain English.

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

## 9. Capstone Resources

### Documentation to Create

- [ ] **README.md** — Project overview, setup instructions, team members
- [ ] **CONTRIBUTING.md** — How to contribute, coding standards
- [ ] **Architecture doc** — System design, component overview

### Tools to Consider

| Tool | Purpose |
|------|---------|
| **GitHub Projects** | Kanban board integrated with GitHub |
| **GitHub Actions** | Automated testing on every push |
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

## 10. Final Reminders

1. **Start with the PRD** — Know what you are building before coding

2. **Use spec-kit** — Plan before you implement

3. **Keep Jira current** — Move cards, add evidence when done (commit hash, GitHub link)

4. **Commit with Jira keys** — Traceability matters

5. **Review each other's code** — Fresh eyes catch bugs

6. **Ask Claude for help** — It's there to make you more productive

7. **Have fun** — You are building something real with industry tools

---

## 11. Quick Reference Card

**With Claude Code (recommended):**
```
┌─────────────────────────────────────────────────────────────┐
│              Quick Reference - Claude Code                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Implement an issue:                                        │
│  /speckit.implement                                         │
│  "Implement PROJ-123 and move it to In Progress in Jira"    │
│                                                             │
│  Save work:                                                 │
│  "Commit my changes for PROJ-123 and push to GitHub"        │
│                                                             │
│  Update Jira:                                               │
│  "Update PROJ-123 with commit hash, branch, and GitHub      │
│   link. Move it to Done."                                   │
│                                                             │
│  Update from main:                                          │
│  "Pull latest changes from main into my branch"             │
│                                                             │
│  Merge when all issues are done:                            │
│  "Merge my branch to main and push"                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Good luck with your capstone! You have the skills and tools to succeed.
