import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

st.title("🎮 Video Game Sales Dashboard")
st.markdown("Interactive exploration of global video game sales.")

# -------------------------
# Load Data (cached)
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/vgsales.csv")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)
    return df

df = load_data()

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2000, 2015)
)

genre_options = sorted(df["Genre"].dropna().unique())

genre_filter = st.sidebar.multiselect(
    "Select Genre",
    genre_options,
    default=genre_options
)

# -------------------------
# Apply Filters
# -------------------------
filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Genre"].isin(genre_filter))
]

# Handle empty dataset
if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# -------------------------
# Metrics
# -------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Games", f"{len(filtered_df):,}")
col2.metric("Total Global Sales (Millions)", f"{filtered_df['Global_Sales'].sum():,.2f}")
col3.metric("Average Sales", f"{filtered_df['Global_Sales'].mean():.2f}")

# -------------------------
# Charts Layout
# -------------------------
left, right = st.columns(2)

# -------------------------
# Sales by Genre
# -------------------------
genre_sales = (
    filtered_df.groupby("Genre")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_genre = px.bar(
    genre_sales,
    x="Genre",
    y="Global_Sales",
    title="Global Sales by Genre",
    color="Global_Sales",
)

left.plotly_chart(fig_genre, use_container_width=True)

# -------------------------
# Sales by Platform
# -------------------------
platform_sales = (
    filtered_df.groupby("Platform")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig_platform = px.bar(
    platform_sales,
    x="Platform",
    y="Global_Sales",
    title="Sales by Platform",
    color="Global_Sales"
)

right.plotly_chart(fig_platform, use_container_width=True)

# -------------------------
# Sales Over Time
# -------------------------
sales_over_time = (
    filtered_df.groupby("Year")["Global_Sales"]
    .sum()
    .reset_index()
)

fig_year = px.line(
    sales_over_time,
    x="Year",
    y="Global_Sales",
    title="Video Game Sales Over Time",
    markers=True
)

st.plotly_chart(fig_year, use_container_width=True)

# -------------------------
# Top Games Table
# -------------------------
st.subheader("Top Selling Games")

top_games = (
    filtered_df.sort_values("Global_Sales", ascending=False)
    [["Name","Platform","Year","Genre","Publisher","Global_Sales"]]
    .head(10)
)

st.dataframe(top_games, use_container_width=True)