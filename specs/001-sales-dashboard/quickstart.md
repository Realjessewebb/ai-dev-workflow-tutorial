# Quickstart: E-Commerce Sales Analytics Dashboard

**Phase**: 1 (Design & Contracts)
**Date**: 2026-01-29
**Purpose**: Step-by-step guide to set up, develop, and deploy the sales dashboard

---

## Prerequisites

Before starting, ensure you have:

- [ ] Python 3.11 or higher installed
- [ ] Git installed and configured
- [ ] GitHub account created
- [ ] Code editor (VS Code, Cursor, or similar)
- [ ] Terminal/command line access
- [ ] Jira account with ECOM project created (for issue tracking)

**Check Python version**:
```bash
python --version  # Should show Python 3.11 or higher
```

---

## Step 1: Set Up Development Environment

### 1.1 Clone Repository and Navigate to Project

```bash
# If starting fresh, ensure you're in the project root
cd /path/to/ISBA\ AI\ Workflow

# Verify you're on the feature branch
git branch  # Should show * 001-sales-dashboard
```

### 1.2 Create Python Virtual Environment

**macOS/Linux**:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (prompt should show (venv))
which python  # Should point to venv/bin/python
```

**Windows (PowerShell)**:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Verify activation (prompt should show (venv))
where python  # Should point to venv\Scripts\python.exe
```

**Windows (Command Prompt)**:
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Verify activation
where python
```

### 1.3 Create `requirements.txt`

Create a file named `requirements.txt` in the project root with:

```txt
streamlit>=1.28
pandas>=2.0
plotly>=5.17
```

### 1.4 Install Dependencies

```bash
# Ensure venv is activated (prompt shows (venv))
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
pip list  # Should show streamlit, pandas, plotly with versions
```

---

## Step 2: Verify Data File Exists

The dashboard requires the sales data CSV file:

```bash
# Check if data file exists
ls ai-dev-workflow-tutorial/data/sales-data.csv

# If file exists, you should see the path printed
# If "No such file or directory", contact your instructor
```

**Expected file location**: `ai-dev-workflow-tutorial/data/sales-data.csv`

---

## Step 3: Create the Dashboard Application

### 3.1 Create `app.py` in Project Root

Create a file named `app.py` in the project root (not in any subdirectory).

**File location**: `/path/to/ISBA AI Workflow/app.py`

### 3.2 Implement Dashboard Components

Follow this implementation order (see [data-model.md](data-model.md) and [research.md](research.md) for detailed patterns):

1. **Import libraries and configure page**
   ```python
   import streamlit as st
   import pandas as pd
   import plotly.express as px
   import os

   st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")
   ```

2. **Implement data loading function** (with error handling)
   ```python
   @st.cache_data
   def load_data(filepath):
       # See research.md section 2 for full implementation
       pass
   ```

3. **Implement KPI calculation functions**
   ```python
   def calculate_kpis(df):
       # See data-model.md "Derived Metrics" section
       pass
   ```

4. **Implement chart generation functions**
   ```python
   def create_sales_trend_chart(df):
       # See research.md section 3 for Plotly patterns
       pass

   def create_category_chart(df):
       pass

   def create_region_chart(df):
       pass
   ```

5. **Implement main application layout**
   ```python
   def main():
       st.title("📊 ShopSmart Sales Dashboard")

       # Load data
       df = load_data("ai-dev-workflow-tutorial/data/sales-data.csv")

       # KPI cards
       col1, col2 = st.columns(2)
       with col1:
           st.metric(label="Total Sales", value=f"${total_sales:,.2f}")
       with col2:
           st.metric(label="Total Orders", value=f"{total_orders:,}")

       # Charts
       st.plotly_chart(create_sales_trend_chart(df))

       col3, col4 = st.columns(2)
       with col3:
           st.plotly_chart(create_category_chart(df))
       with col4:
           st.plotly_chart(create_region_chart(df))

   if __name__ == "__main__":
       main()
   ```

---

## Step 4: Run Dashboard Locally

### 4.1 Start Streamlit Server

```bash
# Ensure venv is activated
streamlit run app.py
```

**Expected output**:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.x:8501
```

### 4.2 Test in Browser

1. Browser should open automatically to `http://localhost:8501`
2. If not, manually open that URL
3. Dashboard should display:
   - Title: "📊 ShopSmart Sales Dashboard"
   - KPI Cards: Total Sales (~$650,000-$700,000) and Total Orders (482)
   - Sales Trend chart (line chart)
   - Category Breakdown chart (bar chart, 5 categories)
   - Regional Breakdown chart (bar chart, 4 regions)

### 4.3 Validate Success Criteria

Check against [spec.md](spec.md) Success Criteria:

- [ ] SC-001: Dashboard loads within 5 seconds
- [ ] SC-002: Charts render within 7 seconds total
- [ ] SC-006: Total Sales ≈ $650K-$700K, Total Orders = 482
- [ ] SC-007: No errors or warnings in terminal
- [ ] SC-008: Professional appearance, suitable for executives
- [ ] SC-009: Hovering over charts shows exact values

### 4.4 Stop Server

Press `Ctrl+C` in terminal to stop the Streamlit server.

---

## Step 5: Commit and Push Changes

### 5.1 Check Git Status

```bash
git status
# Should show:
#   Modified: requirements.txt (if created)
#   New file: app.py
```

### 5.2 Create Jira Issue

Before committing, create a Jira issue:

1. Go to your Jira project (ECOM)
2. Create new issue:
   - **Type**: Story or Task
   - **Summary**: "Implement sales dashboard KPI cards and charts"
   - **Description**: Link to this spec, user stories P1-P4
3. Note the issue key (e.g., `ECOM-1`)

### 5.3 Commit with Jira Key

```bash
# Stage files
git add app.py requirements.txt

# Commit with Jira key in message
git commit -m "ECOM-1: implement sales dashboard with KPI cards and charts

- Add Streamlit app.py with data loading and error handling
- Implement KPI calculations (total sales, total orders)
- Create Plotly visualizations (trend, category, region)
- Add requirements.txt with streamlit, pandas, plotly dependencies

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

### 5.4 Push to GitHub

```bash
# Push feature branch to remote
git push origin 001-sales-dashboard

# If this is the first push, use -u flag:
git push -u origin 001-sales-dashboard
```

### 5.5 Update Jira Issue

Update the Jira issue with implementation evidence:
- **Status**: Move to "In Progress" or "Done"
- **Comment**: Add commit hash and branch name
- **Link**: Add GitHub branch URL

---

## Step 6: Deploy to Streamlit Community Cloud

### 6.1 Merge Feature Branch to Main

**IMPORTANT**: Streamlit Community Cloud deploys from `main` branch only.

```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge 001-sales-dashboard

# Push to GitHub
git push origin main
```

### 6.2 Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Sign in with GitHub account
3. Click "New app"
4. Configure deployment:
   - **Repository**: Select your GitHub repo
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy!"

**Deployment time**: 2-5 minutes

### 6.3 Get Public URL

After deployment completes:
- Copy the public URL (e.g., `https://your-app-name.streamlit.app`)
- Share with stakeholders
- Add to Jira issue as deployment link

---

## Step 7: Validate Production Deployment

### 7.1 Test Public URL

Open the public URL in a browser and verify:

- [ ] Dashboard loads successfully
- [ ] All KPIs display correct values
- [ ] All charts render with proper formatting
- [ ] Interactive tooltips work on hover
- [ ] Professional appearance suitable for executives
- [ ] No errors displayed

### 7.2 Update Documentation

Update the main README.md with:
- Public dashboard URL
- Quick start instructions
- Link to this quickstart guide

---

## Troubleshooting

### Virtual Environment Issues

**Problem**: `venv` not activating or wrong Python version
**Solution**:
```bash
# Delete existing venv
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Recreate with specific Python version
python3.11 -m venv venv

# Reactivate and reinstall
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Data File Not Found

**Problem**: `FileNotFoundError: data file not found`
**Solution**:
```bash
# Check current directory
pwd

# Verify data file path
ls ai-dev-workflow-tutorial/data/sales-data.csv

# If file is elsewhere, update filepath in app.py
# Use relative path from project root
```

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**:
```bash
# Ensure venv is activated (prompt shows (venv))
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt

# Verify installation
pip list | grep streamlit
```

### Port Already in Use

**Problem**: `Port 8501 is already in use`
**Solution**:
```bash
# Stop existing Streamlit process
# Find process ID
lsof -i :8501  # macOS/Linux
netstat -ano | findstr :8501  # Windows

# Kill process (use PID from above)
kill -9 <PID>  # macOS/Linux

# Or use alternative port
streamlit run app.py --server.port 8502
```

### Streamlit Cloud Deployment Fails

**Problem**: Deployment fails with dependency errors
**Solution**:
1. Verify `requirements.txt` is in repository root
2. Ensure `app.py` is in repository root (not in subdirectory)
3. Check that `ai-dev-workflow-tutorial/data/sales-data.csv` exists and is committed
4. Review deployment logs in Streamlit Cloud dashboard
5. Verify Python version compatibility (Streamlit Cloud uses Python 3.11)

---

## Development Workflow Summary

```
┌────────────────────────────────────────────────────────────┐
│  Daily Development Workflow                                 │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  1. Activate venv                                          │
│     └─ source venv/bin/activate                            │
│                                                            │
│  2. Make code changes                                      │
│     └─ Edit app.py                                         │
│                                                            │
│  3. Test locally                                           │
│     └─ streamlit run app.py                                │
│     └─ Validate in browser                                 │
│     └─ Ctrl+C to stop                                      │
│                                                            │
│  4. Commit changes                                         │
│     └─ git add app.py                                      │
│     └─ git commit -m "ECOM-X: description"                 │
│     └─ git push origin 001-sales-dashboard                 │
│                                                            │
│  5. Deploy (when feature complete)                         │
│     └─ git checkout main                                   │
│     └─ git merge 001-sales-dashboard                       │
│     └─ git push origin main                                │
│     └─ Streamlit Cloud auto-deploys                        │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## Next Steps

After completing this quickstart:

1. ✅ Run `/speckit.tasks` to generate detailed task breakdown
2. ✅ Create Jira issues from tasks using `/speckit.taskstoissues`
3. ✅ Implement tasks incrementally (P1 → P2 → P3 → P4)
4. ✅ Commit after each task completion with Jira keys
5. ✅ Update Jira issues with implementation evidence
6. ✅ Deploy to production after each user story completion

---

## Reference Documentation

- **Specification**: [spec.md](spec.md) - User stories and requirements
- **Implementation Plan**: [plan.md](plan.md) - Technical approach and structure
- **Data Model**: [data-model.md](data-model.md) - Data structures and validation
- **Research**: [research.md](research.md) - Technology choices and patterns

---

## Success Criteria Checklist

Final validation before considering feature complete:

- [ ] **SC-001**: Dashboard loads within 5 seconds
- [ ] **SC-002**: Charts render within 7 seconds total
- [ ] **SC-003**: Non-technical users understand dashboard without training
- [ ] **SC-004**: Finance team reports 6+ hours/week saved
- [ ] **SC-005**: 80% of managers access dashboard weekly (4 weeks post-launch)
- [ ] **SC-006**: Metrics match Excel calculations (Total Sales ~$650-700K, Orders = 482)
- [ ] **SC-007**: Zero errors or warnings in production
- [ ] **SC-008**: Professional appearance for executive meetings
- [ ] **SC-009**: Tooltips respond within 1 second on hover

---

**Questions or Issues?**
- Consult [troubleshooting](#troubleshooting) section above
- Review tutorial documentation in `docs/`
- Ask in Teams channel or contact instructor
- Claude Code can help debug errors: paste error messages and ask for guidance
