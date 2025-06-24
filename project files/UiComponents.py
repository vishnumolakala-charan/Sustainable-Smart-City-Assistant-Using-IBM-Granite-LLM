# summary_card.py
import streamlit as st

def summary_card(title, value, icon=None, color="blue"):
    st.markdown(f"""
    <div style='padding:1rem;border-radius:10px;background-color:{color};color:white'>
        <h4 style='margin:0'>{icon or ''} {title}</h4>
        <h2 style='margin:0'>{value}</h2>
    </div>
    """, unsafe_allow_html=True)


# chat_assistant.py
import streamlit as st

def chat_ui():
    prompt = st.text_input("Ask the Smart City Assistant:")
    if st.button("Submit") and prompt:
        return prompt
    return None


# feedback_form.py
import streamlit as st

def feedback_form():
    st.subheader("Submit your feedback")
    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")
    submit = st.button("Send Feedback")
    if submit and feedback:
        return {"name": name, "feedback": feedback}
    return None


# eco_tips.py
import streamlit as st

def eco_tip_ui():
    topic = st.text_input("Enter an environmental topic:")
    if st.button("Get Tips") and topic:
        return topic
    return None


# policy_summarizer.py
import streamlit as st

def policy_ui():
    text = st.text_area("Paste policy text:")
    if st.button("Summarize") and text:
        return text
    return None


# report_generator.py
from fpdf import FPDF

def generate_pdf_report(city, report_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Sustainability Report for {city}", ln=True, align="C")
    pdf.multi_cell(0, 10, txt=report_text)
    filename = f"{city}_report.pdf"
    pdf.output(filename)
    return filename
