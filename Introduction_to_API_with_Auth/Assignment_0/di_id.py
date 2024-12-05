import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()


url = "https://api.d-id.com/clips"

Api_key = os.getenv("API_Di_id_Key")



payload = {
    "presenter_id": "amy-Aq6OmGZnMt",
    "script": {
        "type": "text",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": "Sara"
        },
        "input": "Making videos is easy with D-ID",
        "ssml": "false"
    },
    "config": { "result_format": "mp4" },
    "presenter_config": { "crop": { "type": "wide" } }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": Api_key
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)