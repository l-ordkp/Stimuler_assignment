import requests
import json

def score_pronunciation(post_id, audio_url, scale=100):
    url = f"https://thefluentme.p.rapidapi.com/score/{post_id}"
    
    querystring = {"scale": scale}
    
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Host": "thefluentme.p.rapidapi.com",
        "X-RapidAPI-Key": "934f92e478msh282578002482f1p1027abjsna66f1dbf0b67"
    }
    
    payload = {
        "audio_provided": audio_url
    }
    
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"

# Example usage
post_id =  'P340820643'
audio_url = "https://storage.googleapis.com/thefluentme01.appspot.com/audio/example.mp3"
scale = 100  # This is optional, defaults to 100 as shown in the image

result = score_pronunciation(post_id, audio_url, scale)
print(json.dumps(result, indent=2))