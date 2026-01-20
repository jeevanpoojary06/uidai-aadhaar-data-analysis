import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="UIDAI Data Analysis", layout="wide")

st.title("📊 UIDAI Aadhaar Data Analysis & Prediction")
st.write("Analysis and future trend prediction for age group 5–17 using UIDAI data")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_uidai_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["total_5_17"] = df["bio_age_5_17"] + df["demo_age_5_17"]
    return df

df = load_data()

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Choose Section",
    ["Dataset", "Analysis", "Correlation", "Prediction"]
)

# ================= DATASET =================
if option == "Dataset":
    st.subheader("📁 Cleaned Dataset")
    st.dataframe(df.head(200))

# ================= ANALYSIS =================
elif option == "Analysis":
    st.subheader("📈 State-wise Aadhaar Updates (Age 5–17)")

    state_data = df.groupby("state")["total_5_17"].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots()
    state_data.plot(kind="bar", ax=ax)
    ax.set_ylabel("Total Updates")
    st.pyplot(fig)

# ================= CORRELATION =================
elif option == "Correlation":
    st.subheader("🔗 Correlation Table")
    corr = df.select_dtypes(include="number").corr()
    st.dataframe(corr)

# ================= PREDICTION =================
elif option == "Prediction":
    st.subheader("🔮 Future Trend Prediction")

    daily = df.groupby("date")["total_5_17"].sum().reset_index()
    daily = daily.sort_values("date")
    daily["prediction"] = daily["total_5_17"].rolling(7).mean()

    fig, ax = plt.subplots()
    ax.plot(daily["date"], daily["total_5_17"], label="Actual")
    ax.plot(daily["date"], daily["prediction"], linestyle="--", label="Predicted")
    ax.legend()
    st.pyplot(fig)

    st.success("Trend-based prediction using moving average")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")