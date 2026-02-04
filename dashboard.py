

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    st.title("🛒 Grocery Prediction Dashboard")

    # ---------------- CSS ----------------
    st.markdown("""
    <style>
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        text-align: center;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #2aa66a;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- Sample Sales Data ----------------
    data = {
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Sales": [1200, 1500, 1100, 1800, 2000, 2500, 2200]
    }
    df = pd.DataFrame(data)

    # ---------------- Top Metrics ----------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<div class='card'>Total Sales</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-value'>₹12,100</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>Total Orders</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-value'>320</div>", unsafe_allow_html=True)

    with col3:
        st.markdown("<div class='card'>Profit</div>", unsafe_allow_html=True)
        st.markdown("<div class='metric-value'>₹3,850</div>", unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- Sales Trend Graph ----------------
    st.subheader("📈 Weekly Sales Trend")

    fig, ax = plt.subplots()
    ax.plot(df["Day"], df["Sales"], marker='o')
    ax.set_xlabel("Day")
    ax.set_ylabel("Sales Amount")
    ax.set_title("Sales Trend")

    st.pyplot(fig)

    st.markdown("---")

    # ---------------- Popular Items Table ----------------
    st.subheader("🔥 Top Selling Items")

    items_data = {
        "Item": ["Rice", "Sugar", "Oil", "Wheat", "Milk"],
        "Units Sold": [120, 95, 80, 110, 150],
        "Revenue (₹)": [3600, 1900, 3200, 2750, 3000]
    }

    items_df = pd.DataFrame(items_data)
    st.dataframe(items_df, use_container_width=True)