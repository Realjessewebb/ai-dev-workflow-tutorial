# Tasks: E-Commerce Sales Analytics Dashboard

**Input**: Design documents from `/specs/001-sales-dashboard/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: No automated tests requested - manual testing in local Streamlit instance

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

This project uses a **single-file structure** - all code in `app.py` at repository root. No `src/` or `tests/` directories needed for educational clarity.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and environment setup

- [x] T001 Create Python virtual environment at project root using `python -m venv venv`
- [x] T002 Create `requirements.txt` in project root with dependencies: streamlit>=1.28, pandas>=2.0, plotly>=5.17
- [x] T003 Install dependencies in virtual environment using `pip install -r requirements.txt`
- [x] T004 Verify data file exists at `ai-dev-workflow-tutorial/data/sales-data.csv` with required columns
- [x] T005 Create `.gitignore` in project root to exclude venv/, __pycache__/, .env, .streamlit/

**Checkpoint**: Environment ready - can now begin dashboard implementation

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data loading and error handling that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create `app.py` in project root with imports (streamlit, pandas, plotly.express, os)
- [x] T007 Add Streamlit page configuration in app.py: `st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")`
- [x] T008 Implement `load_data(filepath)` function in app.py with @st.cache_data decorator, CSV loading using `pd.read_csv()` with `parse_dates=['date']`, and FileNotFoundError handling per data-model.md validation logic
- [x] T009 Implement data validation in `load_data()` function in app.py: check required columns exist, check for null values in critical fields (total_amount, order_id), validate category and region enums, validate positive numeric values per data-model.md
- [x] T010 Add error display logic in app.py using `st.error()` and `st.stop()` for validation failures per research.md error handling patterns

**Checkpoint**: Foundation ready - data loading works with proper error handling, user story implementation can now begin

---

## Phase 3: User Story 1 - Quick Performance Overview (Priority: P1) 🎯 MVP

**Goal**: Display Total Sales and Total Orders as prominent KPI cards at top of dashboard

**Independent Test**: Open dashboard, verify two KPI cards show Total Sales (~$650K-$700K) with currency formatting and Total Orders (482) as whole number

### Implementation for User Story 1

- [x] T011 [US1] Add dashboard title in app.py using `st.title("📊 ShopSmart Sales Dashboard")`
- [x] T012 [US1] Implement `calculate_kpis(df)` function in app.py that returns dict with 'total_sales' (sum of total_amount) and 'total_orders' (nunique of order_id) per data-model.md
- [x] T013 [US1] Create two-column layout in app.py using `st.columns(2)` for KPI cards
- [x] T014 [US1] Format and display Total Sales KPI in app.py using `st.metric()` with formatted value `f"${total_sales:,.2f}"` per FR-003
- [x] T015 [US1] Format and display Total Orders KPI in app.py using `st.metric()` with formatted value `f"{total_orders:,}"` per FR-004
- [x] T016 [US1] Add main() function in app.py that calls load_data(), calculate_kpis(), and displays KPI cards
- [x] T017 [US1] Add `if __name__ == "__main__": main()` block to app.py
- [x] T018 [US1] Test locally using `streamlit run app.py` and verify KPI cards display correctly with proper formatting

**Checkpoint**: MVP complete - KPI cards functional and testable independently. Can deploy this as first working version.

---

## Phase 4: User Story 2 - Sales Trends Analysis (Priority: P2)

**Goal**: Add line chart showing sales over time with interactive tooltips

**Independent Test**: View dashboard, confirm line chart displays with time on x-axis, sales on y-axis, and tooltips show exact values on hover

### Implementation for User Story 2

- [x] T019 [US2] Implement `create_sales_trend_chart(df)` function in app.py that groups by date, sums total_amount, creates Plotly line chart per research.md section 3
- [x] T020 [US2] Configure line chart in app.py with title "Sales Trend Over Time", axis labels per FR-013/FR-014, professional blue color (#1f77b4)
- [x] T021 [US2] Add custom hover template to line chart in app.py showing date and sales amount formatted as currency per research.md
- [x] T022 [US2] Update layout in app.py to include y-axis currency formatting `yaxis_tickformat='$,.0f'` and height=400
- [x] T023 [US2] Add line chart to main() function in app.py after KPI cards using `st.plotly_chart(create_sales_trend_chart(df), use_container_width=True)`
- [x] T024 [US2] Test locally and verify line chart displays all 12 months of data with correct chronological order and interactive tooltips per SC-009

**Checkpoint**: User Stories 1 AND 2 complete - Dashboard shows KPIs + trend analysis, both independently testable

---

## Phase 5: User Story 3 - Category Performance Comparison (Priority: P3)

**Goal**: Add bar chart showing sales by product category, sorted descending

**Independent Test**: View dashboard, confirm bar chart displays all 5 categories sorted by sales value with tooltips

### Implementation for User Story 3

- [x] T025 [US3] Implement `create_category_chart(df)` function in app.py that groups by category, sums total_amount, sorts descending, creates Plotly bar chart per research.md
- [x] T026 [US3] Configure category bar chart in app.py with title "Sales by Product Category", axis labels per FR-013/FR-014, professional green color (#2ca02c)
- [x] T027 [US3] Add custom hover template to category chart in app.py showing category name and sales amount formatted as currency
- [x] T028 [US3] Update layout in app.py to include y-axis currency formatting, height=400, and `xaxis={'categoryorder': 'total descending'}` to ensure sort per FR-008
- [x] T029 [US3] Create two-column layout in main() function in app.py after trend chart for category and region charts
- [x] T030 [US3] Add category chart to left column in app.py using `st.plotly_chart(create_category_chart(df), use_container_width=True)`
- [x] T031 [US3] Test locally and verify all 5 categories display sorted correctly (Electronics, Accessories, Audio, Wearables, Smart Home in descending sales order)

**Checkpoint**: User Stories 1, 2, AND 3 complete - Dashboard shows KPIs + trend + category analysis

---

## Phase 6: User Story 4 - Regional Performance Comparison (Priority: P4)

**Goal**: Add bar chart showing sales by region, sorted descending

**Independent Test**: View dashboard, confirm bar chart displays all 4 regions sorted by sales value with tooltips

### Implementation for User Story 4

- [ ] T032 [US4] Implement `create_region_chart(df)` function in app.py that groups by region, sums total_amount, sorts descending, creates Plotly bar chart per research.md
- [ ] T033 [US4] Configure region bar chart in app.py with title "Sales by Region", axis labels per FR-013/FR-014, professional color scheme
- [ ] T034 [US4] Add custom hover template to region chart in app.py showing region name and sales amount formatted as currency
- [ ] T035 [US4] Update layout in app.py to include y-axis currency formatting, height=400, and `xaxis={'categoryorder': 'total descending'}` to ensure sort per FR-010
- [ ] T036 [US4] Add region chart to right column in app.py (created in T029) using `st.plotly_chart(create_region_chart(df), use_container_width=True)`
- [ ] T037 [US4] Test locally and verify all 4 regions display sorted correctly (North, South, East, West in descending sales order)

**Checkpoint**: All user stories complete - Full dashboard functional with KPIs + trend + category + region analysis

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, documentation, and deployment preparation

- [ ] T038 Run complete validation testing per quickstart.md success criteria checklist (SC-001 through SC-009)
- [ ] T039 Verify dashboard loads within 5 seconds (SC-001) and charts render within 7 seconds total (SC-002)
- [ ] T040 Verify all metrics match expected values: Total Sales ~$650K-$700K, Total Orders = 482 (SC-006)
- [ ] T041 Test edge cases: missing CSV file, malformed CSV, empty CSV per spec.md edge cases section
- [ ] T042 Verify no errors or warnings displayed in terminal when running with valid data (SC-007)
- [ ] T043 Add code comments in app.py explaining business logic for KPI calculations and chart configurations per Constitution principle I (Educational Clarity)
- [ ] T044 Review code for PEP 8 compliance: check snake_case naming, proper spacing, clear function names per Constitution principle V
- [ ] T045 Update main project README.md with quickstart instructions, dashboard description, and local setup steps
- [ ] T046 Commit all changes with Jira issue key: `git commit -m "ECOM-X: implement sales dashboard with KPIs and charts"`
- [ ] T047 Push feature branch to GitHub: `git push origin 001-sales-dashboard`
- [ ] T048 Merge to main branch: `git checkout main && git merge 001-sales-dashboard && git push origin main`
- [ ] T049 Deploy to Streamlit Community Cloud from main branch per quickstart.md section 6
- [ ] T050 Verify production deployment and update Jira issue with public URL

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001-T005) - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational completion (T006-T010) - MVP, can deploy after this
- **User Story 2 (Phase 4)**: Depends on Foundational completion (T006-T010) - Adds to existing KPIs, no dependency on US1
- **User Story 3 (Phase 5)**: Depends on Foundational completion (T006-T010) - Adds new chart, no dependency on US1/US2
- **User Story 4 (Phase 6)**: Depends on Foundational completion (T006-T010) and US3 creating two-column layout (T029)
- **Polish (Phase 7)**: Depends on all user stories being complete (T011-T037)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (T010) - No dependencies on other stories ✅ MVP
- **User Story 2 (P2)**: Can start after Foundational (T010) - Independently adds trend chart
- **User Story 3 (P3)**: Can start after Foundational (T010) - Independently adds category chart
- **User Story 4 (P4)**: Depends on US3 creating two-column layout (T029) - Uses same layout structure

### Within Each User Story

All tasks within a user story are sequential because they modify the same file (`app.py`):
- US1: T011 → T012 → T013 → T014 → T015 → T016 → T017 → T018
- US2: T019 → T020 → T021 → T022 → T023 → T024
- US3: T025 → T026 → T027 → T028 → T029 → T030 → T031
- US4: T032 → T033 → T034 → T035 → T036 → T037

**Note**: No parallelization possible within user stories due to single-file structure.

### Parallel Opportunities

**Phase 1 (Setup)**: Tasks T001-T005 can all run in parallel (different operations, no dependencies)

**Phase 2 (Foundational)**: Sequential execution required (T006 → T007 → T008 → T009 → T010) as each builds on previous

**User Stories**: After Foundational is complete, US1, US2, and US3 are **theoretically parallel** but **practically sequential** because:
- All modify the same `app.py` file
- Git merge conflicts likely if developed in parallel
- Educational project - students work individually

**Recommended order**: P1 → P2 → P3 → P4 (priority-based sequential implementation)

---

## Parallel Example: Foundational Phase

```bash
# These CANNOT run in parallel (sequential dependencies):
T006: Create app.py structure
  ↓
T007: Add page configuration
  ↓
T008: Implement load_data() function
  ↓
T009: Implement validation logic
  ↓
T010: Add error display logic
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005) ✅ ~15 minutes
2. Complete Phase 2: Foundational (T006-T010) ✅ ~30 minutes
3. Complete Phase 3: User Story 1 (T011-T018) ✅ ~45 minutes
4. **STOP and VALIDATE**: Test KPI cards independently
5. **Deploy MVP**: Merge to main, deploy to Streamlit Cloud
6. **Total time for MVP**: ~90 minutes

**Value delivered**: Stakeholders can view Total Sales and Total Orders - replaces weekly Excel reports!

### Incremental Delivery

1. **Release 1 (MVP)**: Setup + Foundational + US1 → Deploy KPI cards
   - Test: Open dashboard, see Total Sales ($650K) and Total Orders (482)
   - Value: Immediate visibility into core metrics

2. **Release 2**: Add US2 → Deploy with trend analysis
   - Test: See KPIs + line chart showing sales over time
   - Value: Understand business trajectory (growth/decline)

3. **Release 3**: Add US3 → Deploy with category breakdown
   - Test: See KPIs + trend + category bars
   - Value: Identify high-performing product categories

4. **Release 4 (Complete)**: Add US4 → Deploy with regional breakdown
   - Test: See KPIs + trend + category + region bars
   - Value: Full analytics dashboard for all stakeholders

Each release adds value without breaking previous functionality!

### Parallel Team Strategy

**Single-file structure makes parallel development impractical.** Recommended approach:

1. **Solo developer** (tutorial context): Sequential implementation P1 → P2 → P3 → P4
2. **Team of 2**:
   - Developer A: Setup + Foundational + US1 + US2 (core metrics + trend)
   - Developer B: US3 + US4 (category + region breakdowns) after A completes Foundational
3. **Team of 3+**: Not recommended for single-file project - merge conflicts likely

---

## Task Breakdown Summary

| Phase | Tasks | Estimated Time | Can Deploy? |
|-------|-------|----------------|-------------|
| Setup | T001-T005 (5 tasks) | 15 minutes | No |
| Foundational | T006-T010 (5 tasks) | 30 minutes | No |
| User Story 1 (P1) | T011-T018 (8 tasks) | 45 minutes | ✅ Yes - MVP |
| User Story 2 (P2) | T019-T024 (6 tasks) | 30 minutes | ✅ Yes |
| User Story 3 (P3) | T025-T031 (7 tasks) | 30 minutes | ✅ Yes |
| User Story 4 (P4) | T032-T037 (6 tasks) | 20 minutes | ✅ Yes |
| Polish | T038-T050 (13 tasks) | 45 minutes | ✅ Yes - Production |
| **TOTAL** | **50 tasks** | **~3.5 hours** | |

---

## Notes

- All tasks modify single `app.py` file - no parallel work within user stories
- **[P]** marker only used in Setup phase (T001-T005) - different independent operations
- **[Story]** label (US1, US2, US3, US4) maps each task to its user story for traceability
- Each user story checkpoint enables independent testing and deployment
- Commit after completing each user story phase for incremental Git history
- MVP (US1) delivers immediate value - stakeholders see KPIs replacing Excel reports
- Single-file structure prioritizes educational clarity over modularity (Constitution principle I)
- Manual testing only - no automated test suite required per plan.md
- All file paths use repository root location (no src/ or subdirectories)
