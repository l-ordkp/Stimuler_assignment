import os
import assemblyai as aai
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv('ASSEMBLYAI_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set the ASSEMBLYAI_API_KEY environment variable.")

transcriber = aai.Transcriber()
# Set AssemblyAI API key
aai.settings.api_key = api_key

def transcribe_audio(audio_url):

    print("trans")
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcription = transcriber.transcribe(audio_url,config)

    # Store transcriptions and timestamps in a list 
    transcription_data = []
    for utterance in transcription.utterances:
        start_time = utterance.start / 1000  # Convert milliseconds to seconds
        end_time = utterance.end / 1000      # Convert milliseconds to seconds
        transcription_data.append({
            'text': utterance.text,
            'start_time': start_time,
            'end_time': end_time
        })

    return transcription_data

