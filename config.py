# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the project root
load_dotenv()

# Get the Google API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.")