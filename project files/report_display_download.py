# report_display_download.py

"""
Report Display and Download Module
-----------------------------------
Displays the AI-generated sustainability report on the frontend.
Allows users to download the report in Markdown or PDF format.

Skill Tags:
- Report Rendering
- Markdown/PDF Export
- Streamlit Integration
"""

import streamlit as st
import base64
from fpdf import FPDF
from io import BytesIO

def render_report(report_text: str):
    """
    Render the AI-generated report on the Streamlit frontend.
    """
    st.header("📄 Final Sustainability Report")
    st.markdown(report_text)

def get_markdown_download(report_text: str, filename="sustainability_report.md"):
    """
    Allow users to download the report as a Markdown file.
    """
    b64 = base64.b64encode(report_text.encode()).decode()
    href = f'<a href="data:file/md;base64,{b64}" download="{filename}">📥 Download Markdown Report</a>'
    st.markdown(href, unsafe_allow_html=True)

def get_pdf_download(report_text: str, filename="sustainability_report.pdf"):
    """
    Convert report to PDF and enable download.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    for line in report_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    buffer = BytesIO()
    pdf.output(buffer)
    pdf_bytes = buffer.getvalue()
    b64 = base64.b64encode(pdf_bytes).decode()

    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">📥 Download PDF Report</a>'
    st.markdown(href, unsafe_allow_html=True)

def display_report_download_options(report_text: str):
    """
    Combined display and download options for the sustainability report.
    """
    render_report(report_text)
    st.divider()
    st.subheader("📤 Download Options")
    get_markdown_download(report_text)
    get_pdf_download(report_text)
