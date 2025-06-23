
# 🔁 Project Workflow: Sustainable Smart City Assistant

This document outlines the workflow of the **Sustainable Smart City Assistant** project and how users interact with the system through the frontend dashboard and backend services.

---

## 🧩 Project Flow

### 👤 User Input

Users interact with the **Streamlit-based frontend dashboard**, where they can:

- 📄 **Submit textual prompts** (for chat queries or policy summarization)
- 📁 **Upload policy documents** (`.txt`, `.csv`) for:
  - Summarization via IBM Watsonx Granite LLM
  - Semantic vector search using Pinecone
- 🌆 **Choose a city** to view real-time KPIs (e.g., water usage, air quality, energy stats)
- 📝 **Submit citizen feedback**, including:
  - Name
  - Category (e.g., Water, Roads, Energy)
  - Message or complaint
- 💬 **Ask sustainability questions** via a built-in chat assistant
- 🌱 **Search for eco-friendly tips** by entering a relevant topic or keyword (e.g., "solar", "plastic")

---

## 🖼️ UI Components Involved

The main frontend components used in the Streamlit interface include:

- `smart_dashboard.py` – Core dashboard for navigating between modules
- `feedback_form.py` – UI for collecting citizen feedback
- `chat_assistant.py` – Interface for natural language interactions using IBM Granite LLM
- `policy_summary.py` – Document upload and summarization panel
- `kpi_forecast.py` – Visual dashboard for forecasted KPIs
- `eco_tips.py` – Keyword-based eco-advice generator
- `anomaly_detection.py` – Upload and highlight outlier values in energy or utility usage

---

## ⚙️ Behind the Scenes

Once a user submits input:

1. **Streamlit** captures and forwards the data to corresponding **FastAPI** endpoints.
2. **FastAPI backend** processes the input using:
   - IBM Watsonx Granite LLM for summarization and responses
   - Machine Learning models for KPI forecasting
   - Pinecone for semantic search
3. **Data responses** are rendered back to the user in Streamlit as tables, text, or charts.

---

## 🔄 Workflow Diagram (Logical Flow)

```
[User Input] → [Streamlit UI] → [FastAPI Backend] → [Processing (ML/LLM)] → [Response] → [Streamlit Output]
```

---

This modular approach ensures the system remains scalable, adaptable, and maintainable for future smart city applications.
