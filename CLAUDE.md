# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational tutorial repository that teaches AI-assisted development workflows. It guides students through building a Streamlit sales dashboard using Claude Code, spec-kit, GitHub, and Jira.

**This is a documentation-first project** — the main content is Markdown files in `docs/`, not application code.

## Repository Structure

```
docs/               # Tutorial documentation (numbered for reading order)
├── 00-overview.md          # Tutorial objectives
├── 01-session-1-setup.md   # Account creation and tool installation
├── 02-terminal-basics.md   # Terminal reference guide
├── 03-git-concepts.md      # Git reference guide
├── 04-session-2-workflow.md # Main workflow tutorial
├── 05-troubleshooting.md   # Common issues
├── 06-next-steps.md        # Capstone guidance
├── 07-faq.md               # FAQs
└── 08-glossary.md          # Terminology
prd/                # Product requirements document for the demo project
data/               # Sample sales data (CSV) for the dashboard tutorial
```

## Naming Conventions

| Item | Convention | Example |
|------|------------|---------|
| Jira Project Key | UPPERCASE | `ECOM` |
| Jira Issue | KEY-NUMBER | `ECOM-1` |
| Commit Message | KEY-NUMBER: description | `ECOM-1: add sales dashboard` |

## When Editing Documentation

- Maintain consistent structure: `**Steps:**` followed by numbered lists
- Use `**Checkpoint:**` for verification points
- Clarify where commands run: "In the terminal:" vs "In Claude Code:"
- Add beginner explanations for technical terms using `**What is X?**` format
- Keep Table of Contents in sync with section headers
