# from user_profile import UserProfile
# import spacy

# def extract_personaldata_from_transcription(transcription):
#     text = ''.join([entry['text'] for entry in transcription])
#     # Load the SpaCy model for English

#     nlp = spacy.load('en_core_web_sm')
#     # Process the transcription using SpaCy
#     doc = nlp(text)

#     # Extract and display named entities
#     entities = []
#     for ent in doc.ents:
#         entities.append(ent.text)

#     UserProfile.set_intrests(entities)
#     return None
from user_profile import UserProfile
import spacy

# Function to extract personal data (interests) from transcription and update the user profile
def extract_personaldata_from_transcription(user_profile, transcription):
    text = ''.join([entry['text'] for entry in transcription])
    
    # Load the SpaCy model for English
    nlp = spacy.load('en_core_web_sm')
    
    # Process the transcription using SpaCy
    doc = nlp(text)

    # Extract named entities (which might contain personal interests)
    entities = []
    for ent in doc.ents:
        entities.append(ent.text)
    
    # Update the user profile with extracted entities as interests
    for entity in entities:
        user_profile.set_intrests(entity)
    
    return None



