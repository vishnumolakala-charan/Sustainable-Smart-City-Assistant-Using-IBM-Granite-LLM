# test_routers.py

from fastapi import FastAPI
from app.api import (
    chat_router, 
    policy_router, 
    eco_tips_router, 
    feedback_router, 
    report_router, 
    vector_router, 
    kpi_upload_router, 
    dashboard_router
)

app = FastAPI(title="Sustainable Smart City Assistant")

# Include routers
app.include_router(chat_router.router, prefix="/api")
app.include_router(policy_router.router, prefix="/api")
app.include_router(eco_tips_router.router, prefix="/api")
app.include_router(feedback_router.router, prefix="/api")
app.include_router(report_router.router, prefix="/api")
app.include_router(vector_router.router, prefix="/api")
app.include_router(kpi_upload_router.router, prefix="/api")
app.include_router(dashboard_router.router, prefix="/api")


# Run this app using:
# uvicorn test_routers:app --reload

@app.get("/")
def root():
    return {"message": "Sustainable Smart City Assistant API is running."}