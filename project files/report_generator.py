# report_generator.py

"""
AI-Based Sustainability Report Generator
----------------------------------------
Generates a natural-language report using AI from user-provided KPI data.
Uses prompt engineering with IBM Watsonx Granite LLM or any OpenAI-compatible API.

Skill Tags:
- Prompt Engineering
- LLM Report Generation
- Sustainability Insights
"""

import streamlit as st

# Import your Watsonx/OpenAI SDK or define a mock function for now
def generate_ai_report(prompt: str) -> str:
    """
    Sends prompt to LLM and returns the generated report.
    Replace this with actual LLM API integration (e.g., Watsonx, OpenAI).
    """
    # Mock response for demo
    return "📝 AI-Generated Sustainability Report:\n\n" + prompt.replace("Generate a detailed report based on the following KPIs:\n", "").replace("\n", " ")

def build_prompt(kpi_inputs: dict) -> str:
    """
    Construct a structured prompt using KPI inputs.

    Args:
        kpi_inputs (dict): Dictionary of KPI metrics

    Returns:
        str: Structured prompt for LLM
    """
    prompt = "Generate a detailed report based on the following KPIs:\n"
    for kpi, value in kpi_inputs.items():
        prompt += f"- {kpi.replace('_', ' ').capitalize()}: {value}\n"
    prompt += "\nFocus on sustainability impact, trends, and recommendations."
    return prompt

def display_report_ui():
    st.header("📄 Sustainability Report Generator")
    st.write("Enter KPI values below to generate an AI-written sustainability report.")

    # User input section
    with st.form("report_form"):
        water = st.number_input("Water Usage (liters)", min_value=0.0, value=500.0)
        energy = st.number_input("Energy Consumption (kWh)", min_value=0.0, value=120.0)
        air_quality = st.slider("Air Quality Index (AQI)", 0, 500, 110)
        waste = st.number_input("Waste Generated (kg)", min_value=0.0, value=80.0)

        submitted = st.form_submit_button("Generate Report")

    if submitted:
        kpi_data = {
            "water_usage": water,
            "energy_consumption": energy,
            "air_quality_index": air_quality,
            "waste_generated": waste
        }

        st.subheader("🔧 Prompt Sent to LLM")
        prompt = build_prompt(kpi_data)
        st.code(prompt, language="markdown")

        st.subheader("📋 AI-Generated Report")
        report = generate_ai_report(prompt)
        st.markdown(report)

