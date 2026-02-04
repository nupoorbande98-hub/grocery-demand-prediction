import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_prediction():

    st.title("🤖 Grocery Demand Prediction")

    # ---------------- Upload CSV ----------------
    uploaded_file = st.file_uploader("📂 Upload Sales CSV File", type=["csv"])

    # ---------------- Default Sample Data ----------------
    sample_data = pd.DataFrame({
        "Item": ["Apple", "Apple", "Orange", "Orange", "Kiwi", "Kiwi", "Apricot", "Apricot"],
        "Sales": [50, 60, 30, 35, 20, 25, 15, 18]
    })

    # ---------------- Decide Data Source ----------------
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("✅ Using Uploaded CSV Data")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return
    else:
        df = sample_data
        st.info("📌 No CSV uploaded. Using Sample Data.")

    # ---------------- Show Data ----------------
    st.subheader("📊 Sales Data")
    st.dataframe(df)

    # ---------------- Check Required Columns ----------------
    required_columns = ["Item", "Sales"]

    if not all(col in df.columns for col in required_columns):
        st.error("❌ Data must contain 'Item' and 'Sales' columns")
        return

    # Remove missing values
    df = df.dropna()

    # ---------------- Item Selection ----------------
    item_list = df["Item"].unique()
    selected_item = st.selectbox("🛒 Select Grocery Item", item_list)

    days = st.slider("📅 Select Number of Future Days", 1, 30, 7)

    # ---------------- Prediction Logic ----------------
    item_data = df[df["Item"] == selected_item]

    if item_data.empty:
        st.warning("⚠ No sales data available for selected item")
        return

    avg_sales = item_data["Sales"].mean()
    predicted_sales = avg_sales * days

    # ---------------- Prediction Output ----------------
    st.success(
        f"📦 Predicted Sales for **{selected_item}** in **{days} days**: "
        f"**{int(predicted_sales)} units**"
    )

    # ---------------- Graph ----------------
    future_days = list(range(1, days + 1))
    future_prediction = [avg_sales * d for d in future_days]

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(future_days, future_prediction, marker='o')
    ax.set_xlabel("Days")
    ax.set_ylabel("Predicted Sales")
    ax.set_title(f"Prediction Trend for {selected_item}")
    ax.grid(True)

    st.pyplot(fig)
