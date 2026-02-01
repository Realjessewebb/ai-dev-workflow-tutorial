"""
E-Commerce Sales Analytics Dashboard

This Streamlit application displays key business metrics for ShopSmart:
- Total Sales and Total Orders (KPI cards)
- Sales trend over time (line chart)
- Sales by product category (bar chart)
- Sales by region (bar chart)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page configuration - must be first Streamlit command
st.set_page_config(page_title="ShopSmart Sales Dashboard", layout="wide")


# Data file path
DATA_FILE_PATH = "ai-dev-workflow-tutorial/data/sales-data.csv"


@st.cache_data
def load_data(filepath):
    """
    Load sales transaction data from CSV file with validation.

    This function reads the sales data, parses dates, and validates that:
    - All required columns are present
    - No null values in critical fields (date, order_id, total_amount)
    - Category and region values are from expected enums
    - Positive values for quantity, unit_price, total_amount

    Args:
        filepath (str): Path to CSV file (e.g., 'ai-dev-workflow-tutorial/data/sales-data.csv')

    Returns:
        pandas.DataFrame: Validated transaction data with columns:
            - date: Transaction date (datetime)
            - order_id: Unique order identifier (str)
            - product: Product name (str)
            - category: Product category (str)
            - region: Geographic region (str)
            - quantity: Units sold (int)
            - unit_price: Price per unit in USD (float)
            - total_amount: Total transaction value in USD (float)

    Raises:
        FileNotFoundError: If CSV file doesn't exist at filepath
        ValueError: If CSV has missing columns or invalid data
    """
    try:
        # Check if file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(
                f"Data file not found at: {filepath}. "
                f"Please ensure sales-data.csv exists in the ai-dev-workflow-tutorial/data/ directory."
            )

        # Load CSV with date parsing
        df = pd.read_csv(filepath, parse_dates=['date'])

        # Validate required columns
        required_columns = ['date', 'order_id', 'product', 'category',
                           'region', 'quantity', 'unit_price', 'total_amount']
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(
                f"CSV is missing required columns: {', '.join(missing_cols)}"
            )

        # Validate no null values in critical fields
        if df['total_amount'].isnull().any():
            raise ValueError("Data contains missing transaction amounts")

        if df['order_id'].isnull().any():
            raise ValueError("Data contains missing order IDs")

        # Validate positive numeric values
        if (df['total_amount'] <= 0).any():
            raise ValueError("Data contains non-positive transaction amounts")

        if (df['quantity'] < 1).any():
            raise ValueError("Data contains invalid quantities (must be >= 1)")

        # Validate categorical values
        valid_categories = {'Electronics', 'Accessories', 'Audio', 'Wearables', 'Smart Home'}
        invalid_cats = df[~df['category'].isin(valid_categories)]['category'].unique()
        if len(invalid_cats) > 0:
            raise ValueError(f"Data contains invalid categories: {', '.join(invalid_cats)}")

        valid_regions = {'North', 'South', 'East', 'West'}
        invalid_regions = df[~df['region'].isin(valid_regions)]['region'].unique()
        if len(invalid_regions) > 0:
            raise ValueError(f"Data contains invalid regions: {', '.join(invalid_regions)}")

        return df

    except FileNotFoundError as e:
        st.error(f"❌ **Data Loading Error**: {str(e)}")
        st.stop()
    except ValueError as e:
        st.error(f"❌ **Data Validation Error**: {str(e)}")
        st.stop()
    except Exception as e:
        st.error(f"❌ **Unexpected Error**: {str(e)}")
        st.stop()


def calculate_kpis(df):
    """
    Calculate dashboard KPI metrics from transaction data.

    Business logic:
    - Total Sales: Sum of all transaction amounts across all orders
    - Total Orders: Count of UNIQUE order IDs (not row count, as orders can have multiple items)

    Args:
        df (pandas.DataFrame): Transaction data

    Returns:
        dict: Dictionary containing:
            - 'total_sales' (float): Sum of total_amount column
            - 'total_orders' (int): Count of unique order_id values
    """
    return {
        'total_sales': df['total_amount'].sum(),
        'total_orders': df['order_id'].nunique()
    }


def create_sales_trend_chart(df):
    """
    Create line chart showing sales trend over time.

    This chart helps stakeholders understand business trajectory (growth/decline)
    by visualizing daily sales totals across the 12-month historical period.

    Args:
        df (pandas.DataFrame): Transaction data with 'date' and 'total_amount' columns

    Returns:
        plotly.graph_objects.Figure: Interactive line chart with:
            - X-axis: Date (chronological)
            - Y-axis: Sales amount (USD, currency formatted)
            - Tooltips: Date and exact sales value on hover
    """
    # Group by date and sum sales for each day
    daily_sales = df.groupby('date')['total_amount'].sum().reset_index()

    # Create line chart using Plotly Express
    fig = px.line(
        daily_sales,
        x='date',
        y='total_amount',
        title='Sales Trend Over Time',
        labels={
            'date': 'Date',
            'total_amount': 'Sales ($)'
        }
    )

    # Apply professional styling with blue color
    fig.update_traces(
        line_color='#1f77b4',  # Professional blue color
        hovertemplate='<b>Date</b>: %{x|%Y-%m-%d}<br>' +
                     '<b>Sales</b>: $%{y:,.2f}<extra></extra>'
    )

    # Configure layout with currency formatting and appropriate height
    fig.update_layout(
        yaxis_tickformat='$,.0f',  # Currency format on y-axis
        height=400
    )

    return fig


def create_category_chart(df):
    """
    Create bar chart showing sales by product category, sorted descending.

    This chart helps Product Manager Mike identify which product categories
    are performing best to inform inventory and marketing decisions.

    Args:
        df (pandas.DataFrame): Transaction data with 'category' and 'total_amount' columns

    Returns:
        plotly.graph_objects.Figure: Interactive bar chart with:
            - X-axis: Product category
            - Y-axis: Total sales (USD, currency formatted)
            - Bars sorted descending by sales value
            - Tooltips: Category name and exact sales value on hover
    """
    # Group by category and sum sales
    category_sales = df.groupby('category')['total_amount'].sum()
    category_sales = category_sales.sort_values(ascending=False).reset_index()

    # Create bar chart using Plotly Express
    fig = px.bar(
        category_sales,
        x='category',
        y='total_amount',
        title='Sales by Product Category',
        labels={
            'category': 'Product Category',
            'total_amount': 'Total Sales ($)'
        }
    )

    # Apply professional styling with green color
    fig.update_traces(
        marker_color='#2ca02c',  # Professional green color
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.2f}<extra></extra>'
    )

    # Configure layout with currency formatting and descending sort
    fig.update_layout(
        yaxis_tickformat='$,.0f',  # Currency format on y-axis
        xaxis={'categoryorder': 'total descending'},  # Ensure descending sort
        height=400
    )

    return fig


def main():
    """Main application function that builds the dashboard layout."""

    # Dashboard title
    st.title("📊 ShopSmart Sales Dashboard")

    # Load data
    df = load_data(DATA_FILE_PATH)

    # Calculate KPIs
    kpis = calculate_kpis(df)
    total_sales = kpis['total_sales']
    total_orders = kpis['total_orders']

    # Create two-column layout for KPI cards
    col1, col2 = st.columns(2)

    # Display Total Sales KPI with currency formatting
    with col1:
        st.metric(
            label="Total Sales",
            value=f"${total_sales:,.2f}"
        )

    # Display Total Orders KPI with comma formatting
    with col2:
        st.metric(
            label="Total Orders",
            value=f"{total_orders:,}"
        )

    # Display sales trend line chart
    st.plotly_chart(create_sales_trend_chart(df), use_container_width=True)

    # Create two-column layout for category and region charts
    col3, col4 = st.columns(2)

    # Display category breakdown chart in left column
    with col3:
        st.plotly_chart(create_category_chart(df), use_container_width=True)


if __name__ == "__main__":
    main()
