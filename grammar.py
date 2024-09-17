
import os
import requests
from dotenv import load_dotenv
from user_profile import UserProfile

# Load the environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")

# Function to calculate grammar score
def calculate_grammar_score(gemini_api_key, transcription, user_profile):
    # Combine transcription texts with space
    text = ' '.join([entry['text'] for entry in transcription])

    # Prompt for the Gemini API
    prompt = (
        f"You are a grammar score calculator which provides a score using this formula: "
        f"(Total Number of Grammatically Correct Sentences / Total Number of Sentences) * 100. "
        f"Just provide the score, nothing else. Here is the text: {text}"
    )

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={gemini_api_key}",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        response_json = response.json()
        content = response_json.get('candidates', [{}])[0].get('content', {})
        score = content.get('parts', [{}])[0].get('text', '').strip()

        # Update grammar score for the specific user
        user_profile.update_grammar(score)

        return None
    else:
        raise Exception(f"Failed to get response from Gemini API: {response.status_code}, {response.text}")
