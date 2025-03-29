import sys
import os
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_engine.config import GROQ_API_KEY, GROQ_API_URL, MODEL_NAME

def call_groq_api(prompt):
    """Sends a request to Groq API and returns the response."""
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",  # FIXED: Correct API key usage
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    # FIXED: Send request to the correct URL
    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    # Debugging logs
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
    else:
        return f"Error: {response.status_code} - {response.text}"

# Test API Call
if __name__ == "__main__":
    print(call_groq_api("Hello, how are you?"))
