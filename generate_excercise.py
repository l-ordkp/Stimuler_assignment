import os
import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")

# Function to call Gemini API and generate the exercise
def get_gemini_exercise(user_profile):
    # Get the lowest score type from the user's profile
    lowest_score_type = user_profile.lowest_score()
    
    

    # Construct the personalized prompt using the user's profile data
    prompt = (
        f"This is {user_profile.get_name()}, aged {user_profile.get_age()}, from {user_profile.get_country()}, "
        f"and has interests in {user_profile.random_interest()}. They want to improve their English language skills. "
        f"Please provide a personalized practice exercise focusing on {lowest_score_type} for learning English."
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

    # Make the API call to Gemini
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={gemini_api_key}",
        headers=headers,
        json=data
    )

    # Check if the response was successful
    if response.status_code == 200:
        response_json = response.json()
        # Extract the generated content from the response
        content = response_json.get('candidates', [{}])[0].get('content', '')
        return content
    else:
        raise Exception(f"Failed to get response from Gemini API: {response.status_code}, {response.text}")
