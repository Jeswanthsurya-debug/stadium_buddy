import os
from dotenv import load_dotenv
from google import genai

# Load env variables from .env file
load_dotenv()

# Securely grab the key from the environment
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_stadium_assistance(user_query: str, user_language: str, role: str) -> str:
    """
    Formulates a response using the new google-genai SDK.
    """
    system_instruction = (
        "You are 'StadiumBuddy AI', an elite operations assistant for the FIFA World Cup 2026. "
        f"The user is a {role}. "
        "You must assist them with: navigation, crowd bottlenecks, accessible paths (wheelchair ramps), "
        "transportation options, and emergency steps. "
        "Provide direct, concise, and helpful advice. "
        f"You MUST respond in this language: {user_language}."
    )
    
    # Call the model using the updated client API
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=f"{system_instruction}\n\nUser Question: {user_query}"
    )
    return response.text