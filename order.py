import streamlit as st
import pandas as pd
from datetime import datetime

def show_order():
    st.title("📦 Order Management")

    st.markdown("""
    <style>
    .order-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize order list
    if "orders" not in st.session_state:
        st.session_state.orders = []

    # ---------------- Order Form ----------------
    st.subheader("📝 Place New Order")

    with st.form("order_form"):
        st.markdown("<div class='order-card'>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            item = st.selectbox(
                "Select Grocery Item",
                ["Rice", "Wheat", "Sugar", "Oil", "Milk", "Vegetables", "Fruits"]
            )

        with col2:
            quantity = st.number_input(
                "Enter Quantity (kg / units)",
                min_value=1,
                step=1
            )

        submit = st.form_submit_button("📥 Place Order")

        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Save Order ----------------
    if submit:
        order_data = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Item": item,
            "Quantity": quantity
        }
        st.session_state.orders.append(order_data)
        st.success(f"✅ Order placed for {quantity} units of {item}")

    st.markdown("---")

    # ---------------- Order History ----------------
    st.subheader("📊 Order History")

    if st.session_state.orders:
        df = pd.DataFrame(st.session_state.orders)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No orders placed yet.")
