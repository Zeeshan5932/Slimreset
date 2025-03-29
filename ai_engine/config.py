import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key and API URL from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL")  # Now loading from .env

# Model Name
MODEL_NAME = "llama3-8b-8192"  # Use correct model name

# Debugging (Optional: Remove in Production)
# print("API Key:", GROQ_API_KEY)
# print("API URL:", GROQ_API_URL)
