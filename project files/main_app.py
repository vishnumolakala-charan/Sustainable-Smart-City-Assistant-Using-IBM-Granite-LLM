# main_app.py

"""
Main Streamlit App
-------------------
Integrates all UI modules of the Sustainable Smart City Assistant.
Provides sidebar navigation and connects to real-time FastAPI endpoints.

Skill Tags:
- Streamlit Navigation
- Modular Page Integration
- Real-time API Interaction
"""

import streamlit as st
from streamlit_option_menu import option_menu

# Import UI modules (each must be in frontend/components/)
from components.chat_assistant import display_chat_ui
from components.kpi_forecasting import display_forecasting_ui
from components.anomaly_file_checker import display_anomaly_checker
from components.report_generator import display_report_ui
from components.report_display_download import display_report_download_options
from components.feedback_form import display_feedback_form
from components.eco_tips import display_eco_tips

# Streamlit page config
st.set_page_config(page_title="Sustainable Smart City Assistant", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Chat Assistant", "KPI Forecasting", "Anomaly Detection", "Report Generator", "Eco Advice", "Feedback"],
        icons=["chat", "bar-chart", "activity", "file-earmark-text", "leaf", "envelope"],
        menu_icon="building", default_index=0,
    )

# Route to selected page
if selected == "Chat Assistant":
    display_chat_ui()  # Interacts with /chat/ask FastAPI endpoint

elif selected == "KPI Forecasting":
    display_forecasting_ui()

elif selected == "Anomaly Detection":
    display_anomaly_checker()

elif selected == "Report Generator":
    display_report_ui()

elif selected == "Eco Advice":
    display_eco_tips()

elif selected == "Feedback":
    display_feedback_form()

# Footer
st.markdown("---")
st.markdown("© 2025 Sustainable Smart City Assistant | Built with Streamlit, FastAPI & IBM Watsonx")
