import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def show_prediction():

    st.title("🤖 Grocery Demand Prediction (ML Model)")

    uploaded_file = st.file_uploader("Upload Sales CSV", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Data")
        st.dataframe(df)

        # Check columns
        if "Item" not in df.columns or "Sales" not in df.columns:
            st.error("CSV must contain Item and Sales columns")
            return

        # Add Day column automatically
        df["Day"] = range(1, len(df) + 1)

        # Item selection
        selected_item = st.selectbox("Select Item", df["Item"].unique())

        item_data = df[df["Item"] == selected_item]

        if len(item_data) < 2:
            st.warning("Not enough data to train model")
            return

        # ---------------- ML MODEL TRAINING ----------------

        X = item_data[["Day"]]   # Feature
        y = item_data["Sales"]   # Target

        model = LinearRegression()
        model.fit(X, y)

        st.success("Linear Regression Model Trained Successfully")

        # ---------------- Prediction ----------------

        future_days = st.slider("Select Future Days", 1, 30, 7)

        last_day = item_data["Day"].max()
        future_X = np.array(range(last_day+1, last_day+future_days+1)).reshape(-1,1)

        predictions = model.predict(future_X)

        total_prediction = int(sum(predictions))

        st.success(f"Predicted demand for {selected_item}: {total_prediction} units")

        # ---------------- Graph ----------------

        fig, ax = plt.subplots()

        ax.scatter(X, y)
        ax.plot(future_X, predictions)
        ax.set_xlabel("Days")
        ax.set_ylabel("Sales")
        ax.set_title("Linear Regression Prediction")

        st.pyplot(fig)

    else:
        st.info("Please upload dataset")
