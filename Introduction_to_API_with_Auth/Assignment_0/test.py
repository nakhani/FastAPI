import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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

try:
    response = requests.post(url, headers=headers, params=payload, files=files)
    response.raise_for_status()  
    print(response.status_code)
    print(response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(response.text)  
except Exception as err:
    print(f"An error occurred: {err}")
