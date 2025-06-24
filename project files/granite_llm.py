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
# Example Utilities
# ---------------------------

def summarize_policy(text: str):
    prompt = f"Summarize the following urban policy for sustainability:\n{text}"
    return call_watsonx(prompt)

def generate_eco_tips(topic: str):
    prompt = f"Give 3 eco-friendly tips on the topic: {topic}"
    return call_watsonx(prompt)

def generate_city_report(city_name: str):
    prompt = f"Generate a sustainability report summary for the city: {city_name}"
    return call_watsonx(prompt)

def chat_with_city_assistant(query: str):
    prompt = f"You are a smart city assistant. Answer this query: {query}"
    return call_watsonx(prompt)


# ---------------------------
# Test Calls (for development)
# ---------------------------
if __name__ == "__main__":
    print("--- TESTING WATSONX LLM ---")
    print("Policy Summary Test:\n", summarize_policy("The city will implement water recycling units in all new housing projects by 2026."))
    print("Eco Tips Test:\n", generate_eco_tips("urban gardening"))
    print("City Report Test:\n", generate_city_report("Hyderabad"))
    print("Chat Assistant Test:\n", chat_with_city_assistant("What are the upcoming green initiatives in Bengaluru?"))
