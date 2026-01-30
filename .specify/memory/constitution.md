<!--
Sync Impact Report
==================
Version change: NEW → 1.0.0
Modified principles: N/A (initial creation)
Added sections:
  - Core Principles (5 principles)
  - Development Standards
  - Quality Gates
  - Governance
Templates requiring updates:
  ✅ plan-template.md - Constitution Check section aligns with principles
  ✅ spec-template.md - User story structure supports educational focus
  ✅ tasks-template.md - Task organization supports incremental delivery
Follow-up TODOs: None
-->

# E-Commerce Analytics Dashboard Constitution

## Core Principles

### I. Educational Clarity

All code, documentation, and development practices MUST prioritize clarity and learning value over optimization or brevity.

**Rules**:
- Code MUST be self-documenting with descriptive variable and function names
- Comments MUST explain the "why" behind non-obvious implementation choices
- Documentation MUST be written for students learning both the technical stack AND professional workflows
- Complex patterns or advanced techniques MUST NOT be used when simpler alternatives exist

**Rationale**: This project is an educational tutorial teaching spec-driven AI-assisted development. Students are learning Python, Streamlit, data visualization, AND professional workflows (Git, Jira, spec-kit) simultaneously. Code that prioritizes cleverness over clarity defeats the educational mission.

### II. Dependency Isolation

All Python dependencies MUST be managed within a virtual environment. Global Python installations MUST NOT be used.

**Rules**:
- Virtual environment (`venv/`) MUST be created before any package installation
- All dependencies MUST be explicitly listed in `requirements.txt`
- Installation commands MUST reference the virtual environment's pip
- Documentation MUST include virtual environment activation instructions for all platforms

**Rationale**: Students work across different machines (personal, lab computers) with varying Python configurations. Virtual environments prevent conflicts, ensure reproducibility, and teach professional Python development practices.

### III. User-Centered Visualization

All data visualizations MUST be designed for business stakeholders, not technical audiences.

**Rules**:
- Charts MUST have clear, descriptive titles and axis labels
- Currency values MUST be formatted with appropriate symbols and separators (e.g., "$650,482")
- Large numbers MUST use appropriate formatting (e.g., "482 orders" not "482.0")
- Interactive tooltips MUST provide exact values on hover
- Color schemes MUST be professional and suitable for executive presentations

**Rationale**: The dashboard is built for ShopSmart management (finance managers, marketing directors, regional managers, CEO) to make business decisions. Technical visualizations with raw numbers, unclear labels, or poor formatting undermine the tool's business value.

### IV. Incremental Development

Features MUST be built and deployed in working increments, not as a single monolithic release.

**Rules**:
- Each user story MUST be independently testable and deliverable
- Work MUST be committed frequently with meaningful commit messages including Jira issue keys
- Feature branches MUST be merged to `main` only when fully functional
- Deployment to Streamlit Community Cloud MUST happen after code is on `main` branch

**Rationale**: The tutorial teaches students professional development workflows with full traceability (Jira issue → commit → GitHub → deployment). Incremental development enables learning from failures, getting feedback early, and understanding how features integrate. Students see the connection between their Jira task and a live, working dashboard.

### V. Python Best Practices

All Python code MUST follow community-standard conventions and idioms.

**Rules**:
- Code MUST follow PEP 8 style guidelines (snake_case for variables/functions, proper spacing)
- Functions MUST have single, clear responsibilities
- Magic numbers MUST NOT appear in code; use named constants or configuration
- Error handling MUST be explicit with informative messages
- File I/O operations MUST handle common errors (file not found, invalid format)

**Rationale**: Students are learning Python as a professional skill. Following standard conventions ensures their code is recognizable to other Python developers, passes code reviews in professional settings, and demonstrates understanding of the language's idioms.

## Development Standards

### Technology Stack

**Required Technologies**:
- **Language**: Python 3.11+
- **Dashboard Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualizations**: Plotly
- **Deployment**: Streamlit Community Cloud

**Constraints**:
- MUST work in modern web browsers without plugins
- MUST load and render within 5 seconds on standard hardware
- MUST deploy successfully to Streamlit Community Cloud from `main` branch

### Code Organization

**Structure** (single-project layout):
```
project-root/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── data/
│   └── sales-data.csv       # Sample dataset
├── docs/                    # Tutorial documentation
├── prd/                     # Product requirements
├── specs/                   # Spec-kit generated specifications
└── .specify/                # Spec-kit configuration
```

**File Responsibilities**:
- `app.py`: Dashboard UI, KPI cards, charts, data loading
- `requirements.txt`: Exact versions of streamlit, pandas, plotly
- `data/sales-data.csv`: Transaction data (date, order_id, product, category, region, quantity, unit_price, total_amount)

### Commit Message Convention

All commits MUST include the Jira issue key in the format: `KEY-NUMBER: description`

**Examples**:
- ✅ `ECOM-1: add KPI cards for total sales and orders`
- ✅ `ECOM-2: implement sales trend line chart`
- ❌ `add dashboard` (missing Jira key)
- ❌ `ECOM-1 add stuff` (missing colon, vague description)

**Rationale**: Traceability between Jira issues, commits, and deployed features is a core learning objective. Every deliverable must trace back to a business requirement.

## Quality Gates

### Pre-Commit Checklist

Before committing code, verify:
- [ ] Code runs without errors in local Streamlit instance
- [ ] All KPIs and charts display correct data from CSV
- [ ] Currency and number formatting is professional
- [ ] Virtual environment is activated and dependencies are in `requirements.txt`
- [ ] Commit message includes Jira issue key
- [ ] No sensitive data (credentials, API keys) in committed files

### Pre-Merge Checklist

Before merging feature branch to `main`:
- [ ] All tasks for the user story are completed
- [ ] Feature branch is up to date with `main`
- [ ] Dashboard displays all required components (KPIs, trend, category, region)
- [ ] No errors or warnings in Streamlit console
- [ ] Code follows Python best practices (PEP 8, clear naming, comments where needed)

### Pre-Deploy Checklist

Before deploying to Streamlit Community Cloud:
- [ ] Code is merged to `main` branch
- [ ] Repository is pushed to GitHub
- [ ] `app.py` exists at repository root
- [ ] `requirements.txt` includes all dependencies with versions
- [ ] `data/sales-data.csv` is committed and accessible

## Governance

### Amendment Process

This constitution governs all development decisions for the e-commerce analytics project. Any changes to these principles MUST:

1. Be documented with clear rationale
2. Be reflected in updated version number (semantic versioning)
3. Propagate to all dependent templates (plan, spec, tasks)
4. Not contradict the core educational mission of the project

### Version Control

**Versioning Format**: MAJOR.MINOR.PATCH

- **MAJOR**: Fundamental principle changes (e.g., removing "Educational Clarity" principle)
- **MINOR**: New principle additions or material expansions
- **PATCH**: Clarifications, typo fixes, non-semantic improvements

### Compliance

All code reviews, pull requests, and task implementations MUST verify compliance with these principles. When principles conflict, prioritize in this order:

1. Educational Clarity (this is a tutorial project)
2. User-Centered Visualization (business stakeholders are the audience)
3. Python Best Practices (students learning professional skills)
4. Dependency Isolation (reproducibility and professionalism)
5. Incremental Development (learning and feedback)

### Complexity Justification

Any deviation from these principles MUST be documented in the implementation plan with:
- What principle is being violated
- Why the violation is necessary
- What simpler alternative was considered and why it was rejected

### Runtime Guidance

For development workflow guidance specific to Claude Code and spec-kit, refer to `CLAUDE.md` in the repository root.

**Version**: 1.0.0 | **Ratified**: 2026-01-29 | **Last Amended**: 2026-01-29
