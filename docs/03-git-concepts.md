# Git Concepts

Git is a **version control system** — software that tracks changes to your files over time. This guide explains the core concepts you need to understand before using Git.

## Why Version Control?

Imagine writing a paper and saving multiple copies:

```
essay.docx
essay_v2.docx
essay_final.docx
essay_final_REAL.docx
essay_final_REAL_v2.docx
```

This approach has problems:
- Hard to know which version is actually current
- No record of what changed between versions
- Difficult to collaborate with others
- Takes up storage space with duplicates

**Git solves these problems** by tracking changes intelligently, storing only what changed, and maintaining a complete history.

## Core Concepts

### Repository (Repo)

A **repository** is a project folder that Git is tracking. It contains:

- Your project files
- A hidden `.git` folder with the complete history

```
my-project/           ← This is a repository
├── .git/             ← Hidden folder with Git data
├── README.md
├── src/
│   └── app.py
└── data/
    └── sales.csv
```

There are two types of repositories:

- **Local repository:** On your computer
- **Remote repository:** On a server (like GitHub)

---

### Commit

A **commit** is a snapshot of your project at a specific moment. Think of it as a "save point" in a video game.

```
┌─────────────────────────────────────────────────────────────┐
│                    Project History                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Commit 1        Commit 2        Commit 3        Commit 4   │
│  "Initial"  →   "Add login" →  "Fix bug"   →  "Add tests"  │
│  Jan 1          Jan 5           Jan 7          Jan 10       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Each commit has:
- A unique ID (hash): `a1b2c3d4...`
- A message describing the change: `"Add login functionality"`
- A timestamp: when the commit was made
- An author: who made the commit

**Key insight:** You can go back to any previous commit if something goes wrong.

---

### Branch

A **branch** is an independent line of development. It lets you work on features without affecting the main code.

```
                    feature/add-login
                    ┌─── C4 ─── C5
                   ╱
main: C1 ─── C2 ─── C3 ─── C6 ─── C7
                            ╲
                             └─── C8
                             feature/fix-bug
```

- **main** (or **master**): The primary branch with stable code
- **feature branches**: Separate lines for new features or fixes

**Why branches?**
- Work on features without breaking the main code
- Multiple people can work on different features simultaneously
- Easy to abandon a feature if it doesn't work out

---

### Clone

**Cloning** creates a local copy of a remote repository.

```
┌─────────────────┐                    ┌─────────────────┐
│     GitHub      │     git clone      │  Your Computer  │
│                 │  ───────────────►  │                 │
│  my-project     │                    │  my-project     │
│  (remote)       │                    │  (local copy)   │
└─────────────────┘                    └─────────────────┘
```

After cloning, you have the complete project with all its history.

---

### Fork

A **fork** is your personal copy of someone else's repository on GitHub.

```
┌─────────────────┐                    ┌─────────────────┐
│  Original Repo  │       Fork         │   Your Fork     │
│  owner/project  │  ───────────────►  │  you/project    │
│  (GitHub)       │                    │  (GitHub)       │
└─────────────────┘                    └─────────────────┘
```

**Fork vs Clone:**
- **Fork:** Copy on GitHub (your own remote repository)
- **Clone:** Copy on your computer (local repository)

**Typical workflow:**
1. Fork a repository (creates your copy on GitHub)
2. Clone your fork (downloads to your computer)
3. Make changes locally
4. Push changes to your fork
5. Create a pull request to the original repository

---

### Staging Area

Before committing, you choose which changes to include. The **staging area** (or "index") holds changes ready to be committed.

```
┌─────────────┐    git add    ┌─────────────┐   git commit   ┌─────────────┐
│  Working    │ ───────────► │   Staging   │ ─────────────► │  Repository │
│  Directory  │              │    Area     │                │   (Commits) │
│             │              │             │                │             │
│ (your files)│              │ (ready to   │                │ (permanent  │
│             │              │  commit)    │                │  history)   │
└─────────────┘              └─────────────┘                └─────────────┘
```

**Why staging?**
- Commit related changes together
- Leave unfinished work out of the commit
- Review changes before making them permanent

---

### Push and Pull

Communication between your local repository and the remote:

```
┌─────────────┐                           ┌─────────────┐
│   Local     │         git push          │   Remote    │
│   Repo      │  ──────────────────────►  │   (GitHub)  │
│             │                           │             │
│             │         git pull          │             │
│             │  ◄──────────────────────  │             │
└─────────────┘                           └─────────────┘
```

- **Push:** Send your local commits to the remote
- **Pull:** Get changes from the remote to your local repository

---

### Pull Request (PR)

A **pull request** is a proposal to merge changes from one branch into another. It's how code review happens on GitHub.

```
┌─────────────────────────────────────────────────────────────┐
│                      Pull Request                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  From: feature/ECOM-1-add-dashboard                         │
│  To:   main                                                 │
│                                                             │
│  Title: "Add sales dashboard with KPIs and charts"          │
│                                                             │
│  Changes:                                                   │
│  + app.py (new file)                                        │
│  + requirements.txt (new file)                              │
│                                                             │
│  [Review] [Approve] [Merge]                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Pull Request workflow:**
1. Create a feature branch
2. Make commits on the branch
3. Push the branch to GitHub
4. Open a pull request
5. Review and discuss changes
6. Merge when approved

---

### Merge

**Merging** combines changes from one branch into another.

```
Before merge:
                    feature/add-login
                    ┌─── C4 ─── C5
                   ╱
main: C1 ─── C2 ─── C3

After merge:
                    feature/add-login
                    ┌─── C4 ─── C5 ──┐
                   ╱                  ╲
main: C1 ─── C2 ─── C3 ──────────────── M (merge commit)
```

After merging a pull request:
- Changes from the feature branch are now in main
- The feature branch can be deleted
- The project history shows where the branches joined

## The Git Workflow

Here's how all these concepts fit together:

```
┌─────────────────────────────────────────────────────────────┐
│                    Complete Git Workflow                     │
└─────────────────────────────────────────────────────────────┘

1. FORK (on GitHub)
   Original repo → Your fork

2. CLONE (to your computer)
   Your fork → Local copy

3. BRANCH (create workspace)
   main → feature/ECOM-1-description

4. EDIT (make changes)
   Modify files in your working directory

5. STAGE (prepare changes)
   git add → Staging area

6. COMMIT (save snapshot)
   git commit → Local repository

7. PUSH (upload changes)
   Local → Your fork on GitHub

8. PULL REQUEST (propose merge)
   Your branch → main branch

9. MERGE (integrate changes)
   Feature branch → main
```

## Common Git Commands

| Command | Purpose |
|---------|---------|
| `git clone URL` | Download a repository |
| `git status` | See current state |
| `git branch` | List branches |
| `git checkout -b name` | Create and switch to new branch |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Create a commit |
| `git push` | Upload to remote |
| `git pull` | Download from remote |

You don't need to memorize these now — we'll use them step-by-step in the tutorial.

## Connecting to Jira

When you use a Jira issue key in your branch names and commit messages, Git and Jira can connect:

```
Jira Issue: ECOM-1 "Create sales dashboard"
                ↓
Branch: feature/ECOM-1-add-sales-dashboard
                ↓
Commit: "ECOM-1: implement KPI scorecards"
                ↓
GitHub sees ECOM-1 and links to Jira
                ↓
Jira shows the commits and pull request
```

This **traceability** is valuable because:
- You can see what code relates to what task
- Project managers can track progress
- Anyone can understand why a change was made

## Visual Summary

```
┌─────────────────────────────────────────────────────────────┐
│                         GitHub                              │
│  ┌─────────────────┐              ┌─────────────────┐       │
│  │ Original Repo   │    fork      │   Your Fork     │       │
│  │                 │ ──────────►  │                 │       │
│  └─────────────────┘              └────────┬────────┘       │
│                                            │                │
└────────────────────────────────────────────│────────────────┘
                                             │ clone
                                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      Your Computer                          │
│                                                             │
│  ┌─────────────┐  add   ┌─────────┐ commit ┌─────────────┐  │
│  │  Working    │ ────►  │ Staging │ ─────► │   Local     │  │
│  │  Directory  │        │  Area   │        │   Repo      │  │
│  └─────────────┘        └─────────┘        └──────┬──────┘  │
│        ▲                                          │         │
│        │                                          │ push    │
│        │ edit files                               ▼         │
│        │                              ┌─────────────────┐   │
│        └───────────────────────────── │   Your Fork     │   │
│                                       │   (on GitHub)   │   │
│                                       └─────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## Key Takeaways

1. **Repository:** A project folder tracked by Git
2. **Commit:** A snapshot of your project at a point in time
3. **Branch:** An independent line of development
4. **Fork:** Your copy of a repository on GitHub
5. **Clone:** Your local copy of a repository
6. **Push/Pull:** Sync between local and remote
7. **Pull Request:** A proposal to merge changes

## Next Steps

Now that you understand Git concepts, continue to [Session 2: Workflow](04-session-2-workflow.md) where you'll put these concepts into practice.
