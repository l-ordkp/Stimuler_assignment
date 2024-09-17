from user_profile import UserProfileManager
from transcription import transcribe_audio
from fluency import calculate_fluency_with_pauses
from intrests_extractor import extract_personaldata_from_transcription
import concurrent.futures
import os
from dotenv import load_dotenv
from grammar import calculate_grammar_score
from generate_excercise import get_gemini_exercise
from questions import QuestionnaireManager

# Load the environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")

# Predefined questions
QUESTIONS = [
    "Describe your favorite book and why you like it.",
    "What are your career aspirations?",
    "How do you spend your weekends?",
    "What is the importance of learning English?",
    "Tell us about a recent travel experience."
]

class App:
    def __init__(self):
        self.user_profile_manager = UserProfileManager()
        self.questionnaire_manager = QuestionnaireManager(QUESTIONS)

    def sign_in_user(self, username):
        if not self.user_profile_manager.user_exists(username):
            self.user_profile_manager.create_user_profile(username)
            print("New user detected, please complete KYC.")
            self.user_profile_manager.kyc_form(username)
            return self.user_profile_manager.get_user_profile(username)
        
        user_profile = self.user_profile_manager.get_user_profile(username)
        if user_profile.get_name() is None:
            print("Please complete KYC.")
            self.user_profile_manager.kyc_form(username)
        
        return user_profile

    def ask_question(self, user_profile):
        next_question = self.questionnaire_manager.get_next_question(user_profile.asked_questions)
        if next_question:
            print(f"Question: {next_question}")
            user_profile.mark_question_asked(next_question)
            return next_question
        else:
            print("No more questions available. Well done!")
            return None

    def process_audio(self, audio_url, user_profile):
        if audio_url.strip():
            try:
                print("Transcribing the audio from URL, please wait...")
                transcription_data = transcribe_audio(audio_url)
                
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future_fluency = executor.submit(calculate_fluency_with_pauses, user_profile,transcription_data)
                    future_grammar = executor.submit(calculate_grammar_score, gemini_api_key, transcription_data,user_profile)
                    future_personaldata = executor.submit(extract_personaldata_from_transcription, user_profile,transcription_data)

                    concurrent.futures.wait([future_fluency, future_grammar, future_personaldata])

                generated_exercise = get_gemini_exercise(user_profile)
                print("Personalized Exercise:")
                print(generated_exercise)
            
            except Exception as e:
                print(f"An error occurred while processing the audio: {str(e)}")
        else:
            print("Please provide a valid audio URL.")

    def run(self, username, audio_url):
        user_profile = self.sign_in_user(username)
        if user_profile:
            self.ask_question(user_profile)
            self.process_audio(audio_url, user_profile)

if __name__ == "__main__":
    # Example usage
    username = input("Enter your username: ")
    audio_url = input("Enter the audio URL: ")
    app = App()
    app.run(username, audio_url)
