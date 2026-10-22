
import io
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Zomato Restaurant Dashboard",
    page_icon="🍽️",
    layout="wide"
)

st.title("Zomato Restaurant Analytics Dashboard")
st.write(
    "Explore restaurant ratings, price ranges, and city-wise "
    "restaurant distributions."
)

@st.cache_data
def load_data(file_bytes):
    return pd.read_csv(io.BytesIO(file_bytes))


# Load a local CSV if present; otherwise let the user upload one.
default_file = Path("Zomato Restaurant Dataset.csv")
uploaded_file = st.sidebar.file_uploader(
    "Upload Zomato CSV",
    type=["csv"]
)

if uploaded_file is not None:
    df = load_data(uploaded_file.getvalue())
elif default_file.exists():
    df = load_data(default_file.read_bytes())
else:
    st.info("Upload your Zomato Restaurant Dataset.csv in the sidebar.")
    st.stop()


required_columns = [
    "City",
    "Aggregate rating",
    "Price range",
    "Restaurant Name",
    "Votes"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()


# Prepare numerical columns.
for col in ["Aggregate rating", "Price range", "Votes"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Sidebar filters.
st.sidebar.header("Filters")

cities = sorted(df["City"].dropna().astype(str).unique())

selected_cities = st.sidebar.multiselect(
    "Select cities",
    options=cities
)

price_ranges = sorted(
    df["Price range"].dropna().unique().tolist()
)

selected_prices = st.sidebar.multiselect(
    "Select price ranges",
    options=price_ranges
)


# Apply filters.
filtered = df.copy()

if selected_cities:
    filtered = filtered[
        filtered["City"].astype(str).isin(selected_cities)
    ]

if selected_prices:
    filtered = filtered[
        filtered["Price range"].isin(selected_prices)
    ]


# Two key metrics.
rated = filtered[filtered["Aggregate rating"] > 0]

average_rating = rated["Aggregate rating"].mean()

metric1, metric2 = st.columns(2)

metric1.metric(
    "Restaurants in Selection",
    f"{len(filtered):,}"
)

metric2.metric(
    "Average Rating",
    f"{average_rating:.2f} / 5"
    if pd.notna(average_rating)
    else "N/A"
)

st.divider()


# Chart 1: Rating distribution.
st.subheader("1. Restaurant Rating Distribution")

if rated.empty:
    st.info("No rated restaurants match your filters.")
else:
    fig1, ax1 = plt.subplots(figsize=(9, 4))

    sns.histplot(
        data=rated,
        x="Aggregate rating",
        bins=20,
        kde=True,
        ax=ax1,
        color="teal"
    )

    ax1.set_xlabel("Aggregate Rating")
    ax1.set_ylabel("Number of Restaurants")
    ax1.set_xlim(0, 5)

    fig1.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)


# Chart 2: Top 10 cities by restaurant count.
st.subheader("2. Top Cities by Restaurant Count")

if filtered.empty:
    st.info("No restaurants match your filters.")
else:
    city_counts = (
        filtered["City"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
        .sort_values()
    )

    fig2, ax2 = plt.subplots(figsize=(9, 5))

    city_counts.plot(
        kind="barh",
        ax=ax2,
        color="teal"
    )

    ax2.set_xlabel("Number of Restaurants")
    ax2.set_ylabel("City")
    ax2.set_title("Top 10 Cities")

    fig2.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)


# Chart 3: Average rating by price range.
st.subheader("3. Average Rating by Price Range")

if rated.empty:
    st.info("No rated restaurants match your filters.")
else:
    price_summary = (
        rated.groupby("Price range")["Aggregate rating"]
        .mean()
        .sort_index()
    )

    fig3, ax3 = plt.subplots(figsize=(9, 4))

    price_summary.plot(
        kind="bar",
        ax=ax3,
        color="seagreen"
    )

    ax3.set_xlabel("Price Range")
    ax3.set_ylabel("Average Rating")
    ax3.set_ylim(0, 5)
    ax3.tick_params(axis="x", rotation=0)

    fig3.tight_layout()
    st.pyplot(fig3)
    plt.close(fig3)


st.caption(
    "Ratings of zero are excluded from average-rating charts "
    "because they represent unrated restaurants."
)
