# granite_llm.py

import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID", "granite-13b-chat-v2")

# Endpoint and headers setup
WATSONX_ENDPOINT = f"https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2024-05-29"
HEADERS = {
    "Authorization": f"Bearer {WATSONX_API_KEY}",
    "Content-Type": "application/json"
}

# Function to call Watsonx LLM

def call_watsonx(prompt: str, temperature: float = 0.5, max_tokens: int = 300):
    payload = {
        "model_id": WATSONX_MODEL_ID,
        "project_id": WATSONX_PROJECT_ID,
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": max_tokens,
            "temperature": temperature
        }
    }
    response = requests.post(WATSONX_ENDPOINT, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json().get("results", [{}])[0].get("generated_text", "")
    else:
        return f"Error {response.status_code}: {response.text}"


# ---------------------------
# LLM Service Functions
# ---------------------------

def ask_granite(prompt: str):
    prompt_formatted = f"You are a smart city assistant. Answer this user query: {prompt}"
    return call_watsonx(prompt_formatted)

def generate_summary(text: str):
    prompt = f"Summarize this smart city policy for sustainability:\n{text}"
    return call_watsonx(prompt)

def generate_eco_tip(topic: str):
    prompt = f"Provide 3 eco-friendly tips on the topic: {topic}"
    return call_watsonx(prompt)

def generate_city_report(kpi_data: str):
    prompt = f"Create a sustainability report summary based on these KPIs:\n{kpi_data}"
    return call_watsonx(prompt)


# ---------------------------
# Test Calls (for development)
# ---------------------------
if __name__ == "__main__":
    print("--- TESTING WATSONX LLM SERVICE FUNCTIONS ---")
    print("Chat Test:\n", ask_granite("How can I reduce energy usage in smart buildings?"))
    print("Policy Summary Test:\n", generate_summary("The government mandates rainwater harvesting for all new constructions starting 2025."))
    print("Eco Tips Test:\n", generate_eco_tip("urban composting"))
    print("City Report Test:\n", generate_city_report("Air Quality Index: 85, Water Usage: 120L/person, Renewable Energy: 30%"))
