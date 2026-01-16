# Session 1: Setup & Foundation

This session covers account creation, tool installation, and initial configuration. By the end, you will have a complete development environment ready for the workflow in Session 2.

## Table of Contents

- [1. Create Accounts](#1-create-accounts)
  - [1.1 Create a GitHub Account](#11-create-a-github-account)
  - [1.2 Create an Atlassian (Jira) Account and Project](#12-create-an-atlassian-jira-account-and-project)
  - [1.3 Subscribe to Claude Pro](#13-subscribe-to-claude-pro)
- [2. Install Software](#2-install-software)
  - [2.1 Install Cursor](#21-install-cursor)
  - [Opening the Terminal in Cursor](#opening-the-terminal-in-cursor)
  - [2.2 Install Git](#22-install-git)
  - [2.3 Install Python 3.11+](#23-install-python-311)
  - [2.4 Install uv](#24-install-uv)
  - [2.5 Install spec-kit](#25-install-spec-kit)
  - [2.6 Install Claude Code](#26-install-claude-code)
- [3. Fork and Clone the Tutorial Repository](#3-fork-and-clone-the-tutorial-repository)
  - [3.1 Fork the Repository](#31-fork-the-repository)
  - [3.2 Clone Your Fork Locally](#32-clone-your-fork-locally)
- [4. Connect GitHub and Jira](#4-connect-github-and-jira)
- [5. Session 1 Verification](#5-session-1-verification)
- [Common Issues](#common-issues)
- [What's Next](#whats-next)

---

## What You Will Accomplish

```
┌─────────────────────────────────────────────────────────────┐
│                   Session 1 Outcomes                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Accounts Created:          Tools Installed:                │
│  ─────────────────          ─────────────────               │
│  • GitHub                   • Cursor                        │
│  • Atlassian (Jira)         • Git                           │
│  • Claude Pro               • Python 3.11+                  │
│                             • uv                            │
│                             • spec-kit                      │
│                                                             │
│  Integrations Configured:   Assets Ready:                   │
│  ───────────────────────    ─────────────                   │
│  • Claude Code in Cursor    • Forked tutorial repo          │
│  • GitHub ↔ Jira            • Jira project (ECOM)           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 1. Create Accounts

### 1.1 Create a GitHub Account

GitHub is where your code lives. It is the industry standard for version control and collaboration.

**Steps:**

1. Open your browser and go to [github.com](https://github.com)
2. Click **Sign up**
3. You can sign up using one of these options:
   - Click **Continue with Google** to use your Google account
   - Click **Continue with Apple** to use your Apple account
   - Or fill out the form manually (see below)

**If signing up manually:**

4. Enter your **Email** address
5. Create a **Password** (at least 15 characters, OR at least 8 characters with a number and lowercase letter)
6. Choose a **Username** (this will be visible publicly, so choose something professional)
   - Usernames can only contain letters, numbers, and single hyphens
   - Cannot begin or end with a hyphen
7. Select your **Country/Region**
8. Optionally check the email preferences box
9. Click **Create account**
10. Check your email for a verification code and enter it when prompted

**Checkpoint:** You should be able to log into github.com and see your dashboard.

---

### 1.2 Create an Atlassian (Jira) Account and Project

Jira is the most widely used project management tool for teams building with technology. It tracks tasks, bugs, and features. During signup, you will also create your first project.

**Steps:**

1. Go to [atlassian.com](https://www.atlassian.com)
2. Click **Get started**
3. Sign up using one of these options:
   - Enter your email address and click **Sign up**, then verify your email and create a password
   - Or click **Google**, **Microsoft**, **Apple**, or **Slack** to sign up with an existing account
4. When asked about your role, select an appropriate option (Student or Developer)
5. When asked what you want to use, select **Jira Software**
6. Name your site (this becomes your workspace URL, e.g., `yourname.atlassian.net`)

**During onboarding, Jira will ask you to create your first project. Use these answers:**

| Question | Answer |
|----------|--------|
| What kind of work do you do? | **Other** |
| Select a project template | **Scrum** |
| Name your first project | **E-Commerce Analytics** |
| What types of work do you need? | **Task** |
| How do you track work? | **To Do, In Progress, Done** |

**Important:** After creating the project, find and note the project **Key**. It should be something like `ECOM` or `ECO`. If it's different from `ECOM`, you can change it:
1. Go to **Project settings** (gear icon in the project sidebar)
2. Click **Details**
3. Change the **Key** to `ECOM`

**Checkpoint:** You should be able to access your Jira workspace at `yourname.atlassian.net` and see your ECOM project.

---

### 1.3 Subscribe to Claude Pro

Claude Pro gives you access to Claude Code, the AI assistant you will use throughout this tutorial.

**Steps:**

1. Go to [claude.ai](https://claude.ai)
2. Sign up using one of these options:
   - Click **Continue with Google** to use your Google account
   - Or enter your email and click **Continue with email**
3. Once logged in, click on your profile or settings
4. Select **Upgrade to Pro** or **Subscribe to Pro**
5. Enter your payment information ($20/month)
6. Complete the subscription

**Note:** If you encounter usage limits during the tutorial, you can upgrade to Claude Max ($100/month) for higher limits. Most students find Pro sufficient.

**Checkpoint:** When you log into claude.ai, you should see a Pro badge or indicator showing your subscription is active.

---

## 2. Install Software

### 2.1 Install Cursor

Cursor is an AI-powered code editor based on VS Code. It will feel familiar if you have used VS Code before.

**Steps for macOS:**

1. Go to [cursor.com](https://cursor.com)
2. Click **Download for macOS**
3. Open the downloaded `.dmg` file
4. Drag the Cursor icon to your Applications folder
5. Open Cursor from Applications
6. If prompted about opening an app from the internet, click **Open**
7. Complete the initial setup wizard

**Steps for Windows:**

1. Go to [cursor.com](https://cursor.com)
2. Click **Download for Windows**
3. Run the downloaded `.exe` installer
4. Follow the installation wizard (accept defaults)
5. Launch Cursor when installation completes
6. Complete the initial setup wizard

**Sign up for a Cursor account (both platforms):**

After the setup wizard, you will see the "Welcome to Cursor" sign up screen. Create an account using one of these options:
- Click **Continue with Google**
- Click **Continue with GitHub** (recommended if you already created your GitHub account)
- Click **Continue with Apple**
- Or enter your email and click **Continue**

Follow the instructions on the screen to complete sign up. You may be asked to enter a verification code sent to your email.

When you see the "Customize Your Experience" screen:
- For "How do you plan to use Cursor?" select **With a Team**
- For "Which role best describes you?" select **Student**
- Turn **off** the "Share Data" option
- Click **Continue**

If asked to "Claim a free Pro trial", you can click **Skip for now**.

When you see the "Review Settings" screen:
- Click **Connect** next to GitHub to link your GitHub account
- A GitHub authorization page will open in your browser
- Click **Authorize Cursor** to allow access to your GitHub repositories (you can authorize for all repositories)
- On the "Link GitHub Account" screen, verify your accounts and click **Link Account**
- Click **Continue**

Once you finish the onboarding in the browser, return to the Cursor desktop app and click **Log In**.

On the "Preferences" screen, accept the defaults and click **Continue**. Continue through any remaining onboarding screens.

If you already have a Cursor account, sign in instead.

**Checkpoint:** You should see the Cursor welcome screen with three options: **Open project**, **Clone repo**, and **Connect via SSH**.

---

### Opening the Terminal in Cursor

Many of the following steps require running commands in the terminal. Here's how to open it:

1. Open Cursor
2. Go to **Terminal** → **New Terminal** from the menu bar
3. A terminal panel will appear at the bottom of the Cursor window
4. This is where you will type commands throughout the tutorial

```
┌─────────────────────────────────────────────────────────────┐
│  Cursor Window                                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Your code/files appear here]                              │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Terminal                                              ─ □ x│
│  $ _                                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Tip:** You can resize the terminal by dragging the divider between the terminal and the editor area.

**Note:** Many of the commands in the following sections should be run in Cursor's terminal. If you want to get familiar with the command line first, see [Terminal Basics](02-terminal-basics.md).

---

### 2.2 Install Git

Git is the version control system that tracks changes to your code.

**Check if Git is already installed:**

With the terminal open, type:

```bash
git --version
```

If you see a version number (e.g., `git version 2.39.0`), Git is installed. Skip to the next section.

**Install Git on macOS:**

1. Type `git --version` in the terminal
2. If Git is not installed, macOS will prompt you to install Command Line Tools
3. Click **Install** on the prompt
4. Wait for installation to complete
5. Verify by running `git --version` again

**Alternative for macOS (if the above doesn't work):**

1. Go to [git-scm.com/download/mac](https://git-scm.com/download/mac)
2. Download the installer
3. Run the installer and follow the prompts

**Install Git on Windows:**

1. Go to [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the installer (64-bit recommended)
3. Run the installer
4. **Important settings during installation:**
   - Select "Use Git from Git Bash and also from 3rd-party software"
   - Select "Use the OpenSSL library"
   - Select "Checkout Windows-style, commit Unix-style line endings"
   - Accept other defaults
5. Complete installation
6. Restart Cursor
7. Open terminal and verify: `git --version`

**Configure Git (both platforms):**

After installing, configure your identity. In the terminal:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Use the same email you used for GitHub.

**Checkpoint:** Running `git --version` in Cursor's terminal shows a version number, and `git config --list` shows your name and email.

---

### 2.3 Install Python 3.11+

Python is required for spec-kit and the Streamlit dashboard you will build.

**Check your current Python version:**

```bash
python --version
```

or

```bash
python3 --version
```

If you see Python 3.11 or higher (e.g., `Python 3.11.5`), skip to the next section.

**Install Python on macOS:**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click **Download Python 3.12.x** (or the latest 3.11+)
3. Open the downloaded `.pkg` file
4. Follow the installation wizard
5. **Important:** On the final screen, click **Install Certificates** if that option appears
6. Close and reopen Cursor's terminal
7. Verify: `python3 --version`

**Install Python on Windows:**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click **Download Python 3.12.x** (or the latest 3.11+)
3. Run the downloaded installer
4. **Critical:** Check the box that says **"Add Python to PATH"** at the bottom of the first screen
5. Click **Install Now**
6. Complete installation
7. Restart Cursor
8. Open terminal and verify: `python --version`

**Checkpoint:** Running `python --version` (Windows) or `python3 --version` (macOS) shows Python 3.11 or higher.

---

### 2.4 Install uv

uv is a fast Python package manager that spec-kit requires.

**Install uv on macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, close and reopen the terminal (Terminal → New Terminal).

**Install uv on Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart Cursor.

**Verify installation (both platforms):**

```bash
uv --version
```

**Checkpoint:** Running `uv --version` shows a version number (e.g., `uv 0.4.x`).

---

### 2.5 Install spec-kit

spec-kit is GitHub's toolkit for spec-driven development.

**Install spec-kit:**

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

This command downloads and installs spec-kit globally.

**Verify installation:**

```bash
specify --help
```

You should see a help message with available commands.

**Checkpoint:** Running `specify --help` displays the spec-kit help information.

---

### 2.6 Install Claude Code

Claude Code is the CLI (command-line interface) for Claude that integrates with your development workflow.

**Install Claude Code:**

```bash
npm install -g @anthropic-ai/claude-code
```

**If you don't have npm:**

npm comes with Node.js. Install Node.js first:

1. Go to [nodejs.org](https://nodejs.org)
2. Download the **LTS** version (recommended for most users)
3. Run the installer and follow the prompts
4. Open a new terminal (Terminal → New Terminal)

Then install Claude Code:
```bash
npm install -g @anthropic-ai/claude-code
```

**Authenticate Claude Code:**

```bash
claude
```

When you run `claude` for the first time:
1. It will open a browser window
2. Log in with your Claude account (the one with Pro subscription)
3. Authorize Claude Code to access your account
4. Return to the terminal

**Checkpoint:** Running `claude` in the terminal starts an interactive session. Type `/exit` to quit.

---

## 3. Fork and Clone the Tutorial Repository

### 3.1 Fork the Repository

Forking creates your own copy of the tutorial repository on GitHub.

**Steps:**

1. Go to the tutorial repository: [github.com/LMU-ISBA/ai-dev-workflow-tutorial](https://github.com/LMU-ISBA/ai-dev-workflow-tutorial)
2. Click the **Fork** button in the upper right
3. Select your GitHub account as the destination
4. Wait for the fork to complete
5. You now have your own copy at `https://github.com/[your-username]/ai-dev-workflow-tutorial`

**Checkpoint:** You can see the repository under your GitHub account.

---

### 3.2 Clone Your Fork Locally

Cloning downloads the repository to your computer. Cursor has a built-in feature that makes this easy.

**Steps:**

1. On your forked repository page on GitHub, click the green **Code** button
2. Make sure **HTTPS** is selected
3. Copy the URL (it looks like `https://github.com/[your-username]/ai-dev-workflow-tutorial.git`)
4. Open Cursor
5. Go to **File** → **New Window**
6. In the new window, click **Clone Repository** (or press `Ctrl+Shift+P` and type "Clone")
7. Paste the repository URL you copied from GitHub
8. Choose a location to save the project:
   - **Recommended:** Create a `GitHub` folder in your home directory (e.g., `~/GitHub` on macOS or `C:\Users\YourName\GitHub` on Windows) to keep all your GitHub repositories organized in one place
9. Click **Clone** and wait for the download to complete
10. When prompted, click **Open** to open the cloned repository

**Checkpoint:** You can see the tutorial files in Cursor's file explorer (left sidebar).

---

## 4. Connect GitHub and Jira

### 4.1 Install GitHub for Jira

This integration connects your GitHub commits to Jira issues, providing full traceability.

**Steps:**

1. In Jira, click the **gear icon** (⚙️) in the top right for Settings
2. Select **Apps** from the dropdown
3. Click **Find new apps**
4. Search for "GitHub for Jira"
5. Find the official **GitHub for Jira** app by Atlassian
6. Click **Get app** or **Install**
7. Follow the authorization flow:
   - You will be redirected to GitHub
   - Select your GitHub account
   - Select the repositories to connect (choose your forked tutorial repo)
   - Click **Install & Authorize**
8. Return to Jira and verify the app is installed

**Verify the connection:**

1. In Jira, go to **Apps** → **Manage apps**
2. Find GitHub for Jira
3. Click **Get started** or **Configure**
4. You should see your GitHub account and repository listed

**Checkpoint:** The GitHub for Jira app shows your repository as connected.

---

## 5. Session 1 Verification

Before finishing Session 1, verify everything is set up correctly:

### Accounts
- [ ] Can log into github.com
- [ ] Can log into yourname.atlassian.net
- [ ] Have active Claude Pro subscription at claude.ai

### Tools
Run each command in Cursor's terminal and verify output:

```bash
git --version
# Expected: git version 2.x.x

python --version  # or python3 --version
# Expected: Python 3.11.x or higher

uv --version
# Expected: uv 0.x.x

specify --help
# Expected: spec-kit help information

claude --version
# Expected: Claude Code version information
```

### Repository
- [ ] Tutorial repo is forked to your GitHub account
- [ ] Repo is cloned locally and open in Cursor
- [ ] Can see files in Cursor's file explorer

### Jira
- [ ] ECOM project exists in Jira
- [ ] GitHub for Jira app is installed and connected

---

## Common Issues

### "Command not found" after installation

**Cause:** The terminal doesn't know where to find the new program.

**Fix:**
- Close and reopen the terminal (or restart Cursor)
- On macOS, try running `source ~/.zshrc` or `source ~/.bashrc`
- On Windows, restart Cursor completely

### Git asks for username/password on every operation

**Cause:** Git credential helper not configured.

**Fix:**
```bash
git config --global credential.helper store
```

Then run a Git command (like `git pull`), enter credentials once, and they will be saved.

### Python version is still old after installation

**Cause:** System has multiple Python versions.

**Fix on macOS:**
- Use `python3` instead of `python`
- Or create an alias: `alias python=python3`

**Fix on Windows:**
- Ensure "Add Python to PATH" was checked during installation
- Or reinstall Python with that option checked

### Claude Code authentication fails

**Cause:** Browser popup was blocked or session expired.

**Fix:**
1. Run `claude logout`
2. Run `claude` again
3. Ensure browser popup is allowed
4. Complete authentication

### Fork not visible in Cursor

**Cause:** Cloned the original repo instead of your fork.

**Fix:**
1. Check the remote URL: `git remote -v`
2. If it shows the instructor's repo, re-clone from your fork
3. Delete the current folder and clone again from `https://github.com/[your-username]/ai-dev-workflow-tutorial.git`

---

## What's Next

Session 1 is complete. You now have:

- All accounts created and verified
- All tools installed and working
- Tutorial repository forked and cloned
- Jira project ready
- GitHub and Jira connected

In [Session 2](04-session-2-workflow.md), you will:

1. Connect Claude Code to Jira via MCP
2. Use spec-kit to create a specification and plan
3. Create a Jira issue
4. Build a Streamlit dashboard with Claude Code
5. Commit, push, and deploy to Streamlit Community Cloud

