import streamlit as st
import base64


from dashboard import show_dashboard
from order import show_order
from prediction import show_prediction


# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SiMi Shop", layout="wide")


# ---------- BACKGROUND FUNCTION ----------
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        .login-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .login-box {{
            background: rgba(255, 255, 255, 0.92);
            padding: 30px;
            border-radius: 12px;
            width: 360px;
            height: 360px;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ---------- LOGIN PAGE ----------
def login_page():
    set_background("background.jpg")

    # Center using Streamlit layout (safe way)
    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        st.markdown(
            "<h2 style='text-align:center;'>🛒 Shopkeeper Login</h2>",
            unsafe_allow_html=True
        )

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        if st.button("Login", use_container_width=True):
            if username == "shopkeeper" and password == "1234":
                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

        st.markdown("</div>", unsafe_allow_html=True)



# ---------- SESSION STATE ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# ---------- MAIN APP ----------
if not st.session_state.logged_in:
    login_page()

else:
    # ---------- SIDEBAR ----------
    st.sidebar.markdown("## 🛒 SiMi Shop")
    st.sidebar.markdown("---")

    menu_items = [
        ("Dashboard", "📊"),
        ("Order", "🛒"),
        ("Prediction", "🧠"),
    ]

    for name, icon in menu_items:
        if st.session_state.page == name:
            st.sidebar.markdown(f"👉 **{icon} {name}**")
        else:
            if st.sidebar.button(f"{icon} {name}", key=name):
                st.session_state.page = name
                st.rerun()

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Log Out"):
        st.session_state.logged_in = False
        st.session_state.page = "Dashboard"
        st.rerun()

    # ---------- PAGE ROUTING ----------
    page = st.session_state.page

    if page == "Dashboard":
        show_dashboard()

    elif page == "Order":
        show_order()

    elif page == "Prediction":

        show_prediction()

