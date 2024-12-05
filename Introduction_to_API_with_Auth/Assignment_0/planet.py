import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()


url = "https://my-api.plantnet.org/v2/identify/all"

Api_key = os.getenv("API_planet_key")
print(f"API Key: {Api_key}")  

headers = {
    
}

payload = {
    "api-key": Api_key
}

files = {
    "images": open("photos/sample_planet.jpg", 'rb')  
}

response = requests.post(url, headers=headers, params=payload, files=files)
print(response.status_code)
print(response.json())
