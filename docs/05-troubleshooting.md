# Troubleshooting Guide

This guide covers common issues you may encounter and how to resolve them. Remember: **Claude Code can help diagnose most problems.** When in doubt, describe the issue to Claude and ask for help.

## How to Use This Guide

1. Find your issue in the table of contents below
2. Follow the solution steps
3. If the solution doesn't work, ask Claude Code for help
4. If still stuck, post in the Teams channel with:
   - What you were trying to do
   - The exact error message
   - What you have already tried

---

## Table of Contents

- [Installation Issues](#installation-issues)
  - ["Command not found" after installing a tool](#command-not-found-after-installing-a-tool)
  - [Python version is wrong after installation](#python-version-is-wrong-after-installation)
  - [npm/Node.js not found](#npmnodejs-not-found)
- [Git Issues](#git-issues)
  - ["Not a git repository"](#not-a-git-repository)
  - [Git asks for password repeatedly](#git-asks-for-password-repeatedly)
  - ["Your branch is behind"](#your-branch-is-behind)
  - [Accidentally committed to main](#accidentally-committed-to-main)
- [GitHub Issues](#github-issues)
  - [Can't push — "Permission denied"](#cant-push--permission-denied)
  - [Pull request can't be merged — conflicts](#pull-request-cant-be-merged--conflicts)
- [Jira Issues](#jira-issues)
  - [Can't create project — "Key already exists"](#cant-create-project--key-already-exists)
  - [GitHub integration not showing in Jira](#github-integration-not-showing-in-jira)
- [Claude Code Issues](#claude-code-issues)
  - [Authentication fails](#authentication-fails)
  - ["API rate limit exceeded"](#api-rate-limit-exceeded)
  - [Claude Code seems slow](#claude-code-seems-slow)
- [Spec-Kit Issues](#spec-kit-issues)
  - ["specify: command not found"](#specify-command-not-found)
  - [Spec-kit commands don't work in Claude Code](#spec-kit-commands-dont-work-in-claude-code)
- [Python/Streamlit Issues](#pythonstreamlit-issues)
  - ["ModuleNotFoundError: No module named 'streamlit'"](#modulenotfounderror-no-module-named-streamlit)
  - ["Port 8501 is already in use"](#port-8501-is-already-in-use)
  - [Dashboard shows no data or errors](#dashboard-shows-no-data-or-errors)
- [MCP Connection Issues](#mcp-connection-issues)
  - [Atlassian MCP not connecting](#atlassian-mcp-not-connecting)
  - ["MCP server disconnected"](#mcp-server-disconnected)
- [General Debugging Tips](#general-debugging-tips)
- [Still Stuck?](#still-stuck)

---

## Installation Issues

### "Command not found" after installing a tool

**Symptoms:**
```
zsh: command not found: uv
bash: git: command not found
```

**Cause:** The terminal doesn't know where to find the newly installed program.

**Solutions:**

1. **Restart Cursor** — Close Cursor completely and reopen it

2. **Reload shell configuration:**
   - macOS: `source ~/.zshrc` or `source ~/.bashrc`
   - Windows: Restart PowerShell

3. **Check if the tool is in PATH:**
   ```bash
   echo $PATH
   ```
   The installation directory should be listed.

4. **Reinstall the tool** — Sometimes installation is incomplete

---

### Python version is wrong after installation

**Symptoms:**
```
$ python --version
Python 2.7.x  # or Python 3.8.x when you need 3.11+
```

**Solutions:**

**macOS:**
- Use `python3` instead of `python`:
  ```bash
  python3 --version
  ```
- If you have multiple versions, use the specific version:
  ```bash
  python3.11 --version
  ```

**Windows:**
- Ensure "Add Python to PATH" was checked during installation
- Reinstall Python from python.org with this option checked
- Use the Python launcher:
  ```bash
  py -3.11 --version
  ```

---

### npm/Node.js not found

**Symptoms:**
```
npm: command not found
```

**Solutions:**

1. **Install Node.js:**
   - Go to [nodejs.org](https://nodejs.org)
   - Download and install the LTS version
   - Restart Cursor

2. **Verify installation:**
   ```bash
   node --version
   npm --version
   ```

---

## Git Issues

### "Not a git repository"

**Symptoms:**
```
fatal: not a git repository (or any of the parent directories): .git
```

**Cause:** You are not inside a Git repository folder.

**Solutions:**

1. **Navigate to the correct folder:**
   ```bash
   cd ~/Documents/ai-dev-workflow-tutorial
   ```

2. **Check you are in the right place:**
   ```bash
   ls -la
   ```
   You should see a `.git` folder listed.

3. **If you haven't cloned yet:** Follow the clone steps in Session 1.

---

### Git asks for password repeatedly

**Symptoms:**
- Every `git push` or `git pull` asks for username/password
- Password doesn't work (GitHub no longer accepts passwords)

**Solutions:**

1. **Use a Personal Access Token (PAT):**
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate a new token with `repo` permissions
   - Use this token as your password

2. **Cache credentials:**
   ```bash
   git config --global credential.helper store
   ```
   Then enter credentials once; they will be saved.

3. **Use SSH instead of HTTPS** (more advanced):
   - Generate SSH key: `ssh-keygen -t ed25519`
   - Add key to GitHub: Settings → SSH and GPG keys
   - Clone using SSH URL

---

### "Your branch is behind"

**Symptoms:**
```
Your branch is behind 'origin/main' by 3 commits
```

**Cause:** The remote repository has changes you don't have locally.

**Solution:**
```bash
git pull origin main
```

If you have local changes that conflict, Git will tell you. Ask Claude Code for help resolving conflicts.

---

### Accidentally committed to main

**Symptoms:**
- You made commits directly to `main` instead of a feature branch

**Solution:**

If you haven't pushed yet:
```bash
# Create a new branch with your commits
git branch feature/ECOM-1-my-feature

# Reset main to match remote
git checkout main
git reset --hard origin/main

# Switch to your feature branch
git checkout feature/ECOM-1-my-feature
```

If you already pushed, ask Claude Code for help — the solution depends on your specific situation.

---

## GitHub Issues

### Can't push — "Permission denied"

**Symptoms:**
```
remote: Permission to user/repo.git denied
fatal: unable to access 'https://github.com/...'
```

**Cause:** You don't have write access to the repository.

**Solutions:**

1. **Make sure you are pushing to YOUR fork**, not the original repo:
   ```bash
   git remote -v
   ```
   The URL should include your GitHub username.

2. **If the URL is wrong, fix it:**
   ```bash
   git remote set-url origin https://github.com/YOUR-USERNAME/ai-dev-workflow-tutorial.git
   ```

3. **Authenticate properly** — Use a Personal Access Token or SSH.

---

### Pull request can't be merged — conflicts

**Symptoms:**
- GitHub shows "This branch has conflicts that must be resolved"

**Cause:** Changes in main conflict with your branch.

**Solution:**

1. Update your branch with main:
   ```bash
   git checkout feature/ECOM-1-my-feature
   git fetch origin
   git merge origin/main
   ```

2. If there are conflicts, Git will mark them in the files
3. Ask Claude Code: "Help me resolve the merge conflicts in my files"
4. After resolving, commit and push:
   ```bash
   git add .
   git commit -m "ECOM-1: resolve merge conflicts"
   git push
   ```

---

## Jira Issues

### Can't create project — "Key already exists"

**Symptoms:**
- Error when creating project with key ECOM

**Solution:**
- Choose a different project key (e.g., ECOM2, MYECOM)
- Update your branch naming to match the new key

---

### GitHub integration not showing in Jira

**Symptoms:**
- No "Development" panel on Jira issues
- Commits/PRs not linked

**Solutions:**

1. **Verify app is installed:**
   - Jira Settings → Apps → Manage apps
   - Find "GitHub for Jira"

2. **Check repository connection:**
   - Click Configure on the GitHub for Jira app
   - Ensure your repository is selected

3. **Wait a few minutes** — synchronization can be slow

4. **Verify commit message format:**
   - Must include Jira key: `ECOM-1: description`

---

## Claude Code Issues

### Authentication fails

**Symptoms:**
```
Error: Authentication required
```

**Solutions:**

1. **Log out and back in:**
   ```bash
   claude logout
   claude
   ```

2. **Allow browser popups** — The auth flow opens a browser window

3. **Check subscription** — Ensure Claude Pro is active at claude.ai

---

### "API rate limit exceeded"

**Symptoms:**
- Claude stops responding
- Error about rate limits or quota

**Solutions:**

1. **Wait** — Limits reset periodically (typically every 5 hours)

2. **Upgrade to Max** — If you need more capacity ($100/month)

3. **Work in smaller chunks** — Break your requests into smaller pieces

---

### Claude Code seems slow

**Solutions:**

1. **Simplify your request** — Complex multi-file requests take longer

2. **Be more specific** — Vague requests require more processing

3. **Check your internet connection**

---

## Spec-Kit Issues

### "specify: command not found"

**Solution:**

Reinstall spec-kit:
```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then restart your terminal.

---

### Spec-kit commands don't work in Claude Code

**Symptoms:**
- `/speckit.specify` doesn't do anything

**Solutions:**

1. **Make sure you initialized spec-kit:**
   ```bash
   specify init . --ai claude
   ```

2. **Try alternative syntax:**
   - Instead of `/speckit.specify`, describe what you want:
   - "Use spec-kit to create a specification for the dashboard"

---

## Python/Streamlit Issues

### "ModuleNotFoundError: No module named 'streamlit'"

**Cause:** Streamlit is not installed in your current environment.

**Solutions:**

1. **Activate your virtual environment:**
   - macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

2. **Install the dependency:**
   ```bash
   pip install streamlit
   ```

3. **Verify installation:**
   ```bash
   pip list | grep streamlit
   ```

---

### "Port 8501 is already in use"

**Cause:** Streamlit is already running in another terminal.

**Solutions:**

1. **Use a different port:**
   ```bash
   streamlit run app.py --server.port 8502
   ```

2. **Find and kill the existing process:**
   - macOS/Linux: `lsof -i :8501` then `kill <PID>`
   - Windows: `netstat -ano | findstr :8501` then `taskkill /PID <PID> /F`

---

### Dashboard shows no data or errors

**Solutions:**

1. **Check CSV path:**
   - Is `data/sales-data.csv` in the right place?
   - Is the path in your code correct?

2. **Check CSV format:**
   - Open the CSV and verify it has the expected columns
   - Ask Claude: "Read data/sales-data.csv and tell me its structure"

3. **Check for errors:**
   - Look at the terminal where Streamlit is running
   - Error messages appear there

---

## MCP Connection Issues

### Atlassian MCP not connecting

**Symptoms:**
- `/mcp` doesn't show `atlassian`
- Claude can't access Jira

**Solutions:**

1. **Re-add the MCP server:**
   ```bash
   claude mcp add --transport sse atlassian https://mcp.atlassian.com/v1/sse
   ```

2. **Complete authentication in browser** — Don't close the popup

3. **Check your Atlassian account** — Make sure you can log into Jira directly

4. **Try again later** — MCP servers occasionally have issues

---

### "MCP server disconnected"

**Solution:**

Exit and restart Claude Code:
```bash
/exit
claude
```

The MCP connection should re-establish.

---

## General Debugging Tips

### Ask Claude Code for help

Claude Code can diagnose most issues. Try:

```
I'm getting this error: [paste error message]

I was trying to: [describe what you were doing]

How do I fix this?
```

### Read error messages carefully

Error messages usually tell you:
- What went wrong
- Which file has the problem
- What line number

### Check the basics

Before diving deep:
- Are you in the right directory?
- Is your virtual environment activated?
- Did you save your files?
- Did you restart after installing tools?

### Use `git status` frequently

`git status` tells you:
- What branch you are on
- What files have changed
- What is staged for commit

If you are unsure what state your repository is in, start with `git status`.

---

## Still Stuck?

1. **Describe the problem to Claude Code** — It can often diagnose and fix issues

2. **Search online** — Error messages are often searchable

3. **Post in Teams** with:
   - What you were trying to do
   - The exact error message (copy/paste, don't paraphrase)
   - What you have already tried
   - Screenshots if helpful

4. **Ask during office hours** for complex issues
