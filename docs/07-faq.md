# Frequently Asked Questions

## General Questions

### What is the purpose of this tutorial?

This tutorial teaches you a complete, industry-standard workflow for building technology solutions using modern AI tools. You will learn how professional teams go from requirements to shipped solutions with full traceability.

### Do I need prior experience with these tools?

No. This tutorial assumes no prior experience with Git, Jira, Claude Code, or AI-assisted development. You should have basic Python knowledge and familiarity with VS Code.

### How long does the tutorial take?

The tutorial is designed for two 100-minute sessions. If you work independently, budget 3-4 hours total.

### Can I use this workflow for my actual capstone project?

Yes! That is exactly the intention. The skills and workflow you learn here transfer directly to your capstone and future professional work.

---

## Account and Subscription Questions

### Why do I need a Claude Pro subscription?

Claude Code (the CLI tool) requires a Claude Pro subscription ($20/month) to function. The subscription gives you access to Claude's AI capabilities for coding assistance.

### What if I hit usage limits during the tutorial?

Claude Pro includes generous limits for most use cases. If you hit limits:
1. Wait — limits reset every 5 hours
2. Upgrade to Claude Max ($100/month) for higher limits
3. Work in smaller chunks to use fewer tokens

### Can I share accounts with other students?

No. Each person should have their own GitHub, Atlassian, and Claude accounts. Sharing accounts creates confusion and is against terms of service.

### Is there a free alternative to Claude Pro?

Claude Code specifically requires a Claude Pro subscription. For the capstone, this is a worthwhile investment in your productivity and learning.

---

## Git and GitHub Questions

### What is the difference between Git and GitHub?

- **Git** is the version control software that runs on your computer
- **GitHub** is a website that hosts Git repositories in the cloud

You use Git to manage your code locally, and GitHub to share it with others.

### Why do we use branches?

Branches let you work on features without affecting the main codebase. This means:
- Your incomplete work doesn't break things for others
- You can experiment safely
- Multiple people can work on different features simultaneously

### What if I forget to create a branch before making changes?

If you haven't committed yet:
```bash
# Create branch and switch to it — your changes come with you
git checkout -b feature/ECOM-1-my-feature
```

If you already committed to main, see the Troubleshooting guide for recovery steps.

### How often should I commit?

Commit when you complete a logical unit of work. This might be:
- After implementing a single function
- After fixing a bug
- After making a UI component work

A good rule: if you can describe it in one sentence, it's a good commit size.

### What makes a good commit message?

Good: `ECOM-1: add KPI cards showing total sales and orders`
- Includes Jira key for traceability
- Describes what was added/changed
- Uses present tense ("add" not "added")

Bad: `fixed stuff` / `work in progress` / `asdfasdf`
- No context
- No Jira reference
- Meaningless to others

---

## Jira Questions

### Why do we use Jira?

Jira is the most widely used project management tool for teams building with technology. Learning it prepares you for professional environments. It provides:
- Visibility into what everyone is working on
- Tracking of progress toward goals
- Connection between tasks and code changes

### Can I use a different project management tool?

For this tutorial, please use Jira. For your capstone, ask your instructor about alternatives.

### What do the Jira issue types mean?

- **Story** — A user-facing feature ("As a user, I want to...")
- **Task** — A technical task (set up database, configure deployment)
- **Bug** — Something that is broken and needs fixing
- **Epic** — A collection of related stories/tasks

For this tutorial, Story or Task both work fine.

### How should I write Jira issue descriptions?

Include:
1. What needs to be done (specific and clear)
2. Why it matters (context)
3. Acceptance criteria (how do we know it's done?)
4. Any technical notes or constraints

---

## Claude Code Questions

### What can Claude Code do?

Claude Code can:
- Read and understand your codebase
- Write new code based on your descriptions
- Modify existing code
- Explain what code does
- Debug errors
- Answer questions about programming
- Run terminal commands

### How is Claude Code different from ChatGPT?

Claude Code:
- Runs in your terminal, integrated with your project
- Can read your actual files
- Can make changes directly
- Designed specifically for coding workflows

ChatGPT:
- Web-based chat interface
- Cannot access your local files
- Copy/paste-based workflow
- General purpose, not code-focused

### What are good prompts for Claude Code?

Good prompts are:
- **Specific**: "Add a function to calculate total sales from the DataFrame"
- **Contextual**: "In app.py, modify the bar chart to sort by value descending"
- **Bounded**: "Create a single function that..." (not "build an entire app")

Bad prompts:
- **Vague**: "Make it better"
- **Too broad**: "Build an entire e-commerce platform"
- **Lacking context**: "Fix the bug" (which bug?)

### Should I trust everything Claude generates?

No. Always:
1. Read the generated code
2. Understand what it does
3. Test that it works
4. Verify it meets your requirements

Claude is powerful but not perfect. Treat it as a knowledgeable assistant, not an oracle.

---

## Spec-Kit Questions

### Why use spec-kit instead of just coding?

Spec-kit enforces a "think before you code" approach:
1. **Specification** clarifies what you are building
2. **Planning** identifies the technical approach
3. **Task breakdown** makes work manageable
4. **Implementation** is guided by the spec

This reduces wasted effort from building the wrong thing.

### What if spec-kit commands don't work?

Try:
1. Ensure spec-kit is initialized: `specify init . --ai claude`
2. Use natural language instead: "Use spec-kit to create a specification for..."
3. Check that spec-kit is installed: `specify --help`

### Can I skip spec-kit for small tasks?

For very small tasks (single function, quick fix), spec-kit might be overkill. For anything substantial, the time spent planning pays off in better results.

---

## Integration Questions

### Why connect GitHub to Jira?

The integration provides:
- **Traceability**: See which code relates to which task
- **Visibility**: Project managers see progress without asking developers
- **Automation**: Some actions can update Jira automatically
- **Context**: Anyone can understand why code was written

### What if the integration isn't working?

1. Verify the GitHub for Jira app is installed in Jira
2. Check that your repository is connected
3. Ensure commit messages include the Jira key exactly (ECOM-1, not ecom-1)
4. Wait a few minutes — sync isn't instant

### What is MCP (Model Context Protocol)?

MCP is a protocol that allows Claude Code to connect to external services like Jira. With the Atlassian MCP, Claude can:
- Read your Jira issues
- Understand project context
- Create or update issues (if configured)

---

## Streamlit and Dashboard Questions

### Why Streamlit?

Streamlit is:
- Easy to learn (Python-based)
- Fast to prototype with
- Good for data dashboards
- Popular in data science/analytics

It's a great fit for ISBA students building data-focused applications.

### How do I run the dashboard?

```bash
streamlit run app.py
```

This starts a local server and opens your browser. Press Ctrl+C in the terminal to stop.

### Can I use a different visualization library?

Yes. Common alternatives:
- **Plotly** (recommended) — Interactive charts
- **Altair** — Declarative visualization
- **Matplotlib** — Classic Python plotting
- **Built-in Streamlit charts** — Simplest option

---

## Technical Questions

### What Python version do I need?

Python 3.11 or higher. Check with:
```bash
python --version  # or python3 --version
```

### Do I need to learn terminal commands?

You need basic commands (cd, ls, git). See the [Terminal Basics](02-terminal-basics.md) guide. Claude Code can help you with most terminal operations.

### What if I'm more comfortable with VS Code than Cursor?

Cursor is nearly identical to VS Code — it's built on the same foundation. Everything you know from VS Code works in Cursor. The main difference is Cursor has built-in AI features.

---

## Team and Collaboration Questions

### How should teams divide work?

Options:
- **By feature**: Each person owns a feature end-to-end
- **By layer**: Frontend/backend/data split
- **By expertise**: Each person handles what they're best at

The best approach depends on your team and project.

### What if my teammate and I have merge conflicts?

1. Communicate — "I'm working on file X"
2. Pull frequently — `git pull origin main`
3. Merge main into your branch before PR
4. Ask Claude for help resolving conflicts

### How do we handle code reviews?

- Be respectful and constructive
- Focus on the code, not the person
- Explain why, not just what
- Respond to all comments
- Don't let PRs sit unreviewed for days

---

## If Your Question Isn't Here

1. **Ask Claude Code**: "How do I [your question]?"
2. **Check Troubleshooting**: [05-troubleshooting.md](05-troubleshooting.md)
3. **Search online**: Error messages are usually searchable
4. **Ask in Teams**: Post with context and what you've tried
5. **Office hours**: For complex issues
