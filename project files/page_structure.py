# page_structure.py

import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Smart City Assistant",
        options=[
            "Dashboard",
            "Feedback",
            "Eco Tips",
            "Chat",
            "Policy Search",
            "Anomaly Checker",
            "KPI Forecasting"
        ],
        icons=[
            "bar-chart", 
            "chat-dots", 
            "leaf", 
            "robot", 
            "file-earmark-text", 
            "exclamation-triangle", 
            "graph-up-arrow"
        ],
        menu_icon="globe",
        default_index=0
    )

# Page Routing
if selected == "Dashboard":
    st.title("🌇 City Dashboard")
    st.write("Real-time KPIs and urban data visualization.")

elif selected == "Feedback":
    st.title("🗣️ Citizen Feedback")
    st.write("Collect and analyze feedback from citizens.")

elif selected == "Eco Tips":
    st.title("🌿 Eco Tips")
    st.write("Receive environment-friendly suggestions.")

elif selected == "Chat":
    st.title("💬 Chat Assistant")
    st.write("Talk to the smart city assistant.")

elif selected == "Policy Search":
    st.title("📄 Policy Search & Summary")
    st.write("Upload and search urban policy documents.")

elif selected == "Anomaly Checker":
    st.title("📉 Anomaly Detection")
    st.write("Identify unusual trends in city metrics.")

elif selected == "KPI Forecasting":
    st.title("📊 KPI Forecasting")
    st.write("Predict future sustainability KPIs.")