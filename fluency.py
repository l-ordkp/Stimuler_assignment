from user_profile import UserProfile
def calculate_fluency_with_pauses(user_profile,transcription_data, pause_threshold=0.5):
    
    total_words = 0
    total_pauses = 0
    total_pause_duration = 0  # Accumulate the duration of all significant pauses
    prev_end_time = None  # Track end time of the previous utterance
    word_counter = {}

    for utterance in transcription_data:
        words = utterance['text'].split()
        total_words += len(words)
        
        # Calculate pauses between consecutive utterances
        if prev_end_time is not None:
            pause_duration = (utterance['start_time'] - prev_end_time) / 1000  # convert to seconds
            if pause_duration > pause_threshold:
                total_pauses += 1
                total_pause_duration += pause_duration  # accumulate the total pause duration

        # Update the end time for next pause calculation
        prev_end_time = utterance['end_time']

    # Total duration of the conversation
    duration_seconds = (transcription_data[-1]['end_time'] - transcription_data[0]['start_time']) / 1000  # in seconds
    wpm = (total_words / duration_seconds)*60
    ideal_wpm = 150
    
    if ideal_wpm>=wpm:
        fluency_score = (1-(1-(wpm/ideal_wpm)) -(total_pause_duration/duration_seconds))*100 
    else:
        fluency_score =  (1-((wpm/ideal_wpm)-1) -(total_pause_duration/duration_seconds))*100

    

    user_profile.update_grammar(fluency_score)
    return None

    








