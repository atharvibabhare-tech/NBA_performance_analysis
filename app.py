import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Page config
st.set_page_config(page_title="NBA Analysis", layout="wide")

# Title
st.title("🏀 NBA Player Performance Analysis")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("NBA_Player.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Player filter (if column exists)
if "player" in df.columns:
    selected_players = st.sidebar.multiselect(
        "Select Player(s)",
        options=df["player"].unique(),
        default=df["player"].unique()[:10]
    )
    df = df[df["player"].isin(selected_players)]

# Show dataset
st.subheader("📂 Dataset Preview")
st.dataframe(df.head())

# Layout columns
col1, col2 = st.columns(2)

# Scatter Plot
with col1:
    st.subheader("📊 Rebounds vs Points")
    fig, ax = plt.subplots()
    sb.scatterplot(data=df, x="trb", y="pts", ax=ax)
    ax.set_xlabel("Rebounds (trb)")
    ax.set_ylabel("Points (pts)")
    st.pyplot(fig)

# KDE Plot
with col2:
    st.subheader("📉 Points Distribution")
    fig2, ax2 = plt.subplots()
    sb.kdeplot(data=df, x="pts", fill=True, ax=ax2)
    st.pyplot(fig2)

# Top players
st.subheader("Top 10 Players by Points")
top_players = df.sort_values(by="pts", ascending=False).head(10)

st.dataframe(top_players[["player", "pts", "trb"]] if "player" in df.columns else top_players)

st.bar_chart(top_players.set_index("player")["pts"] if "player" in df.columns else top_players["pts"])

# Insights
st.subheader("📌 Key Insights")
st.markdown("""
- 📈 Positive trend between rebounds and points  
- 📊 Most players fall in average performance range  
- ⭐ Few players dominate with very high scores  
- 📉 Points distribution is right-skewed  
""")
