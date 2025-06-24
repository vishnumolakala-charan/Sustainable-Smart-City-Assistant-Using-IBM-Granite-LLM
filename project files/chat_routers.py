# app/api/chat_router.py
from fastapi import APIRouter, Body
from services.granite_llm import ask_granite

router = APIRouter()

@router.post("/chat")
def chat_with_assistant(prompt: str = Body(..., embed=True)):
    return {"response": ask_granite(prompt)}


# app/api/policy_router.py
from fastapi import APIRouter, Body
from services.granite_llm import generate_summary

router = APIRouter()

@router.post("/summarize")
def summarize_policy(text: str = Body(..., embed=True)):
    return {"summary": generate_summary(text)}


# app/api/eco_tips_router.py
from fastapi import APIRouter, Body
from services.granite_llm import generate_eco_tip

router = APIRouter()

@router.post("/eco-tip")
def eco_tip(topic: str = Body(..., embed=True)):
    return {"tips": generate_eco_tip(topic)}


# app/api/feedback_router.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/feedback")
def collect_feedback():
    return {"message": "Feedback endpoint (to be implemented)."}


# app/api/report_router.py
from fastapi import APIRouter, Body
from services.granite_llm import generate_city_report

router = APIRouter()

@router.post("/report")
def sustainability_report(kpi_data: str = Body(..., embed=True)):
    return {"report": generate_city_report(kpi_data)}


# app/api/vector_router.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/vector/search")
def vector_search():
    return {"message": "Vector search endpoint (to be implemented)."}


# app/api/kpi_upload_router.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/upload-kpi")
def upload_kpi():
    return {"message": "KPI upload endpoint (to be implemented)."}


# app/api/dashboard_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def get_dashboard_data():
    return {"message": "Dashboard data endpoint (to be implemented)."}
