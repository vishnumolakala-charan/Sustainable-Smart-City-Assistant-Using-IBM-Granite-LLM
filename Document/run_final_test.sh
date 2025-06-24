#!/bin/bash

# run_final_test.sh

# -----------------------------
# Final Integration Test Runner
# -----------------------------
# This script launches both the FastAPI backend and the Streamlit frontend
# for the Sustainable Smart City Assistant project.

# Skill Tags:
# - FastAPI Server Launch
# - Streamlit Dashboard Launch
# - Final Testing Automation

# Optional: Activate virtual environment
# source venv/bin/activate

echo "✅ Starting FastAPI backend..."
gnome-terminal -- bash -c "uvicorn app.main:app --reload; exec bash"

sleep 3  # Delay to ensure FastAPI starts before frontend

echo "✅ Launching Streamlit dashboard..."
streamlit run smart_dashboard.py
