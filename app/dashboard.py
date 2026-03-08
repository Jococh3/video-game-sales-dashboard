import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

st.title("🎮 Video Game Sales Dashboard")

# Load data
df = pd.read_csv("data/vgsales.csv")

# Drop rows with missing year
df = df.dropna(subset=["Year"])

df["Year"] = df["Year"].astype(int)

# Sidebar filters
st.sidebar.header("Filters")

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2000, 2015)
)

genre_filter = st.sidebar.multiselect(
    "Select Genre",
    df["Genre"].unique(),
    default=df["Genre"].unique()
)

# Apply filters
filtered_df = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Genre"].isin(genre_filter))
]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Games", len(filtered_df))
col2.metric("Total Global Sales", round(filtered_df["Global_Sales"].sum(),2))
col3.metric("Average Sales", round(filtered_df["Global_Sales"].mean(),2))

# Sales by Genre
genre_sales = filtered_df.groupby("Genre")["Global_Sales"].sum().reset_index()

fig_genre = px.bar(
    genre_sales,
    x="Genre",
    y="Global_Sales",
    title="Global Sales by Genre"
)

st.plotly_chart(fig_genre, use_container_width=True)

# Sales by Platform
platform_sales = filtered_df.groupby("Platform")["Global_Sales"].sum().reset_index()

fig_platform = px.bar(
    platform_sales,
    x="Platform",
    y="Global_Sales",
    title="Global Sales by Platform"
)

st.plotly_chart(fig_platform, use_container_width=True)

# Sales Over Time
sales_over_time = filtered_df.groupby("Year")["Global_Sales"].sum().reset_index()

fig_year = px.line(
    sales_over_time,
    x="Year",
    y="Global_Sales",
    title="Video Game Sales Over Time"
)

st.plotly_chart(fig_year, use_container_width=True)

# Top Games Table
st.subheader("Top Selling Games")

top_games = filtered_df.sort_values(
    "Global_Sales",
    ascending=False
).head(10)

st.dataframe(top_games)