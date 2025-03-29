import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Correct Groq API URL
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Model Name
MODEL_NAME = "llama3-8b-8192"  # Use correct model name
