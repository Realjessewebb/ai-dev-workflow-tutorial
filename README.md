# AI-Assisted Development Workflow Tutorial

A hands-on tutorial for establishing a complete, end-to-end, AI-assisted workflow for building technology solutions using Cursor, Claude Code, GitHub, and Jira.

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│   PRD   │ →  │ spec-kit │ →  │  Jira   │ →  │  Code  │
└─────────┘    └──────────┘    └─────────┘    └────────┘
                                                  ↓
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌────────┐
│  Live!  │ ←  │  Deploy  │ ←  │  Push   │ ←  │ Commit │
└─────────┘    └──────────┘    └─────────┘    └────────┘
```

## Why This Matters

### The Industry Has Changed

Building with technology in 2026 looks fundamentally different than it did just two years ago. AI assistants have moved from novelty to necessity. Companies expect new hires to work effectively with AI tools, and those who can are dramatically more productive.

**This is not about becoming a software engineer — it's about being able to build solutions with technology and data.**

Whether you become a business analyst, data scientist, product manager, consultant, or entrepreneur, you will need to:
- Build dashboards and data applications
- Automate workflows and processes
- Create prototypes to test ideas
- Collaborate with technical teams using shared tools

Professionals who use AI assistants effectively:
- Build solutions faster while maintaining quality
- Spend less time on technical details and more on business problems
- Debug issues more efficiently with AI-powered analysis
- Learn new technologies faster with AI as a teaching partner

### Professional Workflows Create Professional Results

Every successful team building technology solutions follows a structured workflow. This isn't bureaucracy — it's how teams coordinate, maintain quality, and move quickly without breaking things.

```
┌─────────────────────────────────────────────────────────────┐
│                    Why Workflows Matter                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Without Workflow:              With Workflow:              │
│  ─────────────────              ───────────────             │
│  • "Who changed this?"          • Full audit trail          │
│  • "Is this the latest?"        • Single source of truth    │
│  • "What broke it?"             • Easy to trace and fix     │
│  • "What are we building?"      • Clear requirements        │
│  • Chaos at scale               • Scales to any team size   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

The workflow you learn in this tutorial is used at companies from startups to Fortune 500:
- **GitHub** for version control (used by 100M+ developers and teams)
- **Jira** for task tracking (used by 65K+ companies)
- **Streamlit Community Cloud** for deployment (free hosting for data apps)

### Your Competitive Advantage

By completing this tutorial, you will have skills that set you apart:

1. **AI-Assisted Building**: Using Claude Code as a thinking and implementation partner
2. **Spec-Driven Development**: Turning requirements into working solutions systematically
3. **Full Traceability**: Connecting every deliverable to a business requirement
4. **Industry Tooling**: Hands-on experience with the tools companies actually use

These are not "student skills" — these are professional skills that will set you apart in interviews and on the job, regardless of your specific role.

---

## What You Will Learn

By the end of this tutorial, you will be able to:

- Move from a tracked task to a deployed, shareable solution
- Use Claude Code as a thinking and implementation assistant
- Maintain full traceability: Jira issue → commit → push → deploy
- Apply spec-driven development using GitHub's spec-kit

## Tutorial Structure

This tutorial is designed for two 100-minute sessions. **Read documents in the numbered order shown.**

### Session 1: Setup & Foundation

| Order | Document | Description |
|:-----:|----------|-------------|
| 1 | [Overview](docs/00-overview.md) | Tutorial objectives and what you'll build |
| 2 | [Session 1: Setup](docs/01-session-1-setup.md) | Account creation and tool installation |
| — | [Terminal Basics](docs/02-terminal-basics.md) | *Reference:* Read if unfamiliar with command line |
| — | [Git Concepts](docs/03-git-concepts.md) | *Reference:* Read if unfamiliar with version control |

### Session 2: Spec-Driven Workflow

| Order | Document | Description |
|:-----:|----------|-------------|
| 3 | [Session 2: Workflow](docs/04-session-2-workflow.md) | Complete development workflow |

### Reference Materials

| Document | Description |
|----------|-------------|
| [Troubleshooting](docs/05-troubleshooting.md) | Common issues and solutions |
| [Capstone Project Dev Environment](docs/06-capstone-project-dev-environment.md) | Setting up your capstone project |
| [FAQ](docs/07-faq.md) | Frequently asked questions |
| [Glossary](docs/08-glossary.md) | Key terms and definitions |

## Project Materials

| Resource | Description |
|----------|-------------|
| [E-Commerce PRD](prd/ecommerce-analytics.md) | Product requirements document |
| [Sales Data](data/sales-data.csv) | Sample dataset for the dashboard |

## Prerequisites

No prior experience with Git, Jira, or AI tools is required. You should have:

- A computer running macOS or Windows
- Basic Python knowledge
- Familiarity with VS Code (Cursor is VS Code-based)

## Tools You Will Use

| Tool | Purpose | Industry Context |
|------|---------|------------------|
| **GitHub** | Version control and collaboration | Used by 100M+ professionals worldwide |
| **Jira** | Project and task management | Used by 65,000+ companies |
| **Cursor** | AI-powered code editor | Leading AI-native IDE |
| **Claude Code** | AI assistant (CLI) | State-of-the-art AI for building |
| **spec-kit** | Spec-driven development toolkit | Modern requirements-to-solution workflow |

## Quick Start

1. Fork this repository to your GitHub account
2. Follow [Session 1: Setup](docs/01-session-1-setup.md) to configure your environment
3. Continue with [Session 2: Workflow](docs/04-session-2-workflow.md) to build the dashboard

## Running the Dashboard

Once you've completed the tutorial, you can run the sales analytics dashboard locally:

```bash
# Ensure you're in the project root directory
cd ai-dev-workflow-tutorial

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run the dashboard
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501` and display:
- **KPI Cards**: Total Sales (~$650K-700K) and Total Orders (482)
- **Sales Trend**: Line chart showing sales over 12 months
- **Category Breakdown**: Bar chart of sales by product category (5 categories)
- **Regional Breakdown**: Bar chart of sales by region (4 regions)

Press `Ctrl+C` in the terminal to stop the server.

## Naming Conventions

This tutorial uses consistent naming conventions:

| Item | Convention | Example |
|------|------------|---------|
| Jira Project Key | UPPERCASE | `ECOM` |
| Jira Issue | KEY-NUMBER | `ECOM-1` |
| Commit Message | KEY-NUMBER: description | `ECOM-1: add sales dashboard` |

## Getting Help

- **During class**: Ask your instructor
- **Outside class**: Post in the Teams channel
- **Technical issues**: Ask Claude Code for help — it can diagnose and fix most problems

## License

This tutorial is provided for educational purposes.
