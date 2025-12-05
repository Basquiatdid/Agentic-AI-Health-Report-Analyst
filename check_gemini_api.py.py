import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # load variables from .env

# Read your Gemini API key from the environment instead of hardcoding it.
# Prefer GOOGLE_API_KEY, but fall back to GEMINI_API_KEY if needed.
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Neither GOOGLE_API_KEY nor GEMINI_API_KEY environment variables are set."
    )

# Initialize Gemini model.
# If you specifically want to use 1.5 models, upgrade `google-generativeai` and
# `langchain-google-genai` and then switch this back to "gemini-1.5-flash".
gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # widely available, avoids 404 on older API versions
    google_api_key=api_key,
)

# Send a test message
response = gemini.invoke("Say this is a test")

# Print the response
print(response)
