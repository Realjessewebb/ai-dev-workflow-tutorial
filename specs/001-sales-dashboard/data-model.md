# Data Model: E-Commerce Sales Analytics Dashboard

**Phase**: 1 (Design & Contracts)
**Date**: 2026-01-29
**Purpose**: Define data structures, validation rules, and transformations for the sales dashboard

## Overview

The dashboard operates on a single data entity (Transaction) loaded from a CSV file. No database schema or ORM is required. All data processing happens in-memory using Pandas DataFrames.

---

## Source Data: Sales Transaction CSV

### File Location
```
data/sales-data.csv
```

### Schema

| Column | Data Type | Constraints | Description | Example |
|--------|-----------|-------------|-------------|---------|
| `date` | Date | NOT NULL | Transaction date in ISO format (YYYY-MM-DD) | `2024-01-15` |
| `order_id` | String | NOT NULL, UNIQUE per order | Unique order identifier | `ORD-001234` |
| `product` | String | NOT NULL | Product name | `Wireless Headphones` |
| `category` | String | NOT NULL, ENUM(Electronics, Accessories, Audio, Wearables, Smart Home) | Product category | `Electronics` |
| `region` | String | NOT NULL, ENUM(North, South, East, West) | Geographic sales region | `North` |
| `quantity` | Integer | NOT NULL, >= 1 | Units sold in transaction | `2` |
| `unit_price` | Decimal | NOT NULL, > 0 | Price per unit in USD | `49.99` |
| `total_amount` | Decimal | NOT NULL, > 0, MUST EQUAL quantity × unit_price | Total transaction value in USD | `99.98` |

### Data Volume
- **Row Count**: ~1,000 transactions
- **Date Range**: 12 months of historical data
- **Categories**: 5 distinct values (Electronics, Accessories, Audio, Wearables, Smart Home)
- **Regions**: 4 distinct values (North, South, East, West)
- **File Size**: ~150-200 KB

### Sample Data
```csv
date,order_id,product,category,region,quantity,unit_price,total_amount
2024-01-15,ORD-001234,Wireless Headphones,Electronics,North,2,49.99,99.98
2024-01-15,ORD-001235,Phone Case,Accessories,South,1,15.99,15.99
2024-01-16,ORD-001236,Smart Speaker,Smart Home,East,1,89.99,89.99
```

---

## Entity: Transaction

**Purpose**: Represents a single sales transaction in the e-commerce system.

**Attributes**:

```python
# Conceptual representation (Pandas DataFrame row)
{
    'date': datetime.date(2024, 1, 15),           # Transaction date
    'order_id': 'ORD-001234',                      # Unique order ID
    'product': 'Wireless Headphones',              # Product name
    'category': 'Electronics',                     # Product category
    'region': 'North',                             # Sales region
    'quantity': 2,                                 # Units sold
    'unit_price': 49.99,                           # Price per unit (USD)
    'total_amount': 99.98                          # Total value (USD)
}
```

**Validation Rules**:
1. `date` must be parseable as a valid date
2. `order_id` must not be null or empty string
3. `category` must be one of: Electronics, Accessories, Audio, Wearables, Smart Home
4. `region` must be one of: North, South, East, West
5. `quantity` must be positive integer (>= 1)
6. `unit_price` must be positive decimal (> 0)
7. `total_amount` must be positive decimal (> 0)
8. `total_amount` should equal `quantity × unit_price` (within floating-point tolerance)

**Relationships**:
- No relationships (single flat table)
- Each transaction is independent
- Multiple transactions can have the same `order_id` (multi-item orders) - **for KPI calculation, count UNIQUE order_ids**

**State**: Immutable (read-only data)

---

## Derived Metrics (Calculated at Runtime)

### KPI Metrics

**Total Sales**
```python
total_sales = df['total_amount'].sum()
# Type: float
# Format: Currency with 2 decimal places (e.g., "$650,482.37")
# Business Rule: Sum of all transaction amounts
```

**Total Orders**
```python
total_orders = df['order_id'].nunique()
# Type: int
# Format: Whole number with thousand separators (e.g., "482")
# Business Rule: Count of UNIQUE order IDs (not row count!)
```

### Time-Series Aggregation

**Daily Sales**
```python
daily_sales = df.groupby('date')['total_amount'].sum().reset_index()
# Type: DataFrame with columns ['date', 'total_amount']
# Purpose: Line chart showing sales trend over time
# Sort: Ascending by date (chronological)
```

### Category Aggregation

**Sales by Category**
```python
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)
# Type: Series with category names as index, sales totals as values
# Purpose: Bar chart showing category performance
# Sort: Descending by sales value (highest to lowest)
# Expected Categories: Electronics, Accessories, Audio, Wearables, Smart Home
```

### Regional Aggregation

**Sales by Region**
```python
region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
# Type: Series with region names as index, sales totals as values
# Purpose: Bar chart showing regional performance
# Sort: Descending by sales value (highest to lowest)
# Expected Regions: North, South, East, West
```

---

## Data Loading and Validation

### Loading Function Signature

```python
@st.cache_data
def load_data(filepath: str) -> pd.DataFrame:
    """
    Load sales transaction data from CSV file with validation.

    Args:
        filepath: Path to CSV file (e.g., 'data/sales-data.csv')

    Returns:
        pandas.DataFrame: Validated transaction data

    Raises:
        FileNotFoundError: If CSV file doesn't exist at filepath
        ValueError: If CSV has missing columns or invalid data types
    """
```

### Validation Logic

```python
def validate_data(df: pd.DataFrame) -> None:
    """
    Validate loaded DataFrame meets schema requirements.

    Checks:
    1. All required columns present
    2. No null values in critical columns (date, order_id, total_amount)
    3. Data types correct (date is datetime, numeric columns are numeric)
    4. Category and region values are from expected enums
    5. Positive values for quantity, unit_price, total_amount

    Raises:
        ValueError: If any validation check fails, with descriptive message
    """
    required_columns = ['date', 'order_id', 'product', 'category',
                       'region', 'quantity', 'unit_price', 'total_amount']

    # Check 1: Required columns
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # Check 2: Null values
    if df['total_amount'].isnull().any():
        raise ValueError("Data contains missing transaction amounts")

    if df['order_id'].isnull().any():
        raise ValueError("Data contains missing order IDs")

    # Check 3: Positive numeric values
    if (df['total_amount'] <= 0).any():
        raise ValueError("Data contains non-positive transaction amounts")

    if (df['quantity'] < 1).any():
        raise ValueError("Data contains invalid quantities (must be >= 1)")

    # Check 4: Valid categorical values
    valid_categories = {'Electronics', 'Accessories', 'Audio', 'Wearables', 'Smart Home'}
    invalid_cats = df[~df['category'].isin(valid_categories)]['category'].unique()
    if len(invalid_cats) > 0:
        raise ValueError(f"Data contains invalid categories: {', '.join(invalid_cats)}")

    valid_regions = {'North', 'South', 'East', 'West'}
    invalid_regions = df[~df['region'].isin(valid_regions)]['region'].unique()
    if len(invalid_regions) > 0:
        raise ValueError(f"Data contains invalid regions: {', '.join(invalid_regions)}")
```

---

## Data Transformations

### 1. Date Parsing
```python
# During CSV load
df = pd.read_csv(filepath, parse_dates=['date'])
# Converts 'date' column from string to datetime64 type
```

### 2. KPI Calculation
```python
def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate dashboard KPI metrics."""
    return {
        'total_sales': df['total_amount'].sum(),
        'total_orders': df['order_id'].nunique()
    }
```

### 3. Time-Series Aggregation
```python
def aggregate_daily_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Group transactions by date and sum sales."""
    return df.groupby('date')['total_amount'].sum().reset_index()
```

### 4. Category/Region Aggregation
```python
def aggregate_by_dimension(df: pd.DataFrame, dimension: str) -> pd.Series:
    """
    Group transactions by dimension (category or region) and sum sales.
    Returns sorted series (descending by sales).
    """
    return df.groupby(dimension)['total_amount'].sum().sort_values(ascending=False)
```

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                   data/sales-data.csv                        │
│                    (1,000 rows × 8 columns)                  │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  load_data()     │
                  │  - Read CSV      │
                  │  - Parse dates   │
                  │  - Validate      │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌─────────────────────┐
                  │  Pandas DataFrame    │
                  │  (in-memory cache)   │
                  └────────┬────────────┘
                           │
           ┌───────────────┼───────────────┬───────────────┐
           │               │               │               │
           ▼               ▼               ▼               ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │   KPIs   │   │  Daily   │   │Category  │   │ Regional │
    │          │   │  Sales   │   │  Sales   │   │  Sales   │
    │ .sum()   │   │.groupby()│   │.groupby()│   │.groupby()│
    │.nunique()│   │          │   │          │   │          │
    └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
         │              │              │              │
         ▼              ▼              ▼              ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ KPI Cards│   │Line Chart│   │Bar Chart │   │Bar Chart │
    │ (Metric) │   │ (Plotly) │   │ (Plotly) │   │ (Plotly) │
    └──────────┘   └──────────┘   └──────────┘   └──────────┘
```

---

## Performance Considerations

**Caching Strategy**:
- `load_data()` decorated with `@st.cache_data` - caches DataFrame in memory
- Cache invalidates automatically if CSV file changes
- Subsequent dashboard interactions use cached data (no file I/O)

**Memory Footprint**:
- 1,000 rows × 8 columns ≈ 80 KB in Pandas DataFrame
- Aggregated datasets (daily, category, region) < 1 KB each
- Total memory usage < 1 MB (well within Streamlit limits)

**Query Performance**:
- `.groupby()` operations on 1,000 rows: < 10 ms
- Chart rendering (Plotly): 50-200 ms per chart
- Total page load (cached data): < 1 second

---

## Edge Cases and Error Handling

| Edge Case | Detection | Handling |
|-----------|-----------|----------|
| CSV file missing | `os.path.exists()` check | Display error message in Streamlit UI, stop execution |
| Malformed CSV (wrong columns) | Column name validation | Display error listing missing columns, stop execution |
| Empty CSV (0 rows) | `df.empty` check | Display warning "No data available", show empty state |
| Missing values in critical fields | `df['column'].isnull().any()` | Display error message, stop execution |
| Invalid category/region values | Check against enum sets | Display error listing invalid values, stop execution |
| Negative or zero amounts | Numeric range validation | Display error message, stop execution |
| Date parsing failures | Pandas raises exception | Catch and display user-friendly error message |

---

## Assumptions and Constraints

**Assumptions**:
1. CSV file structure never changes (columns, order, types)
2. All monetary values are in USD (no currency conversion needed)
3. Dates are in ISO format (YYYY-MM-DD) or parseable by Pandas
4. order_id uniqueness represents distinct orders (not transactions)
5. Data is pre-cleaned (no duplicate rows, consistent formatting)

**Constraints**:
1. Read-only access (no writes back to CSV)
2. No historical versioning (single snapshot of data)
3. No real-time updates (manual CSV refresh required)
4. No data filtering or drill-down (Phase 1 scope)
5. Single data source (no joins with other datasets)

---

## Testing Validation

**Data Model Tests** (manual validation during development):

1. ✅ Load valid CSV with 1,000 rows → Success
2. ✅ Load CSV with missing required column → Error displayed
3. ✅ Load CSV with null `total_amount` values → Error displayed
4. ✅ Load CSV with invalid category ("Toys") → Error displayed
5. ✅ Load CSV with zero/negative `total_amount` → Error displayed
6. ✅ Load CSV with invalid date format → Error displayed
7. ✅ Calculate KPIs on valid data → Matches expected values (~$650-700K, 482 orders)
8. ✅ Aggregate by category → 5 categories returned, sorted descending
9. ✅ Aggregate by region → 4 regions returned, sorted descending
10. ✅ Cache persistence → Second page load uses cached data (instant)

---

## Conclusion

The data model is intentionally simple to prioritize educational clarity (Constitution principle I):
- Single flat CSV file (no complex joins or relationships)
- Straightforward Pandas operations (sum, groupby, sort)
- Clear validation rules with user-friendly error messages
- Efficient performance with caching strategy

No API contracts needed (Phase 1 requirement for API-based features - N/A for CSV-based dashboard).

Ready to proceed with quickstart.md generation.
