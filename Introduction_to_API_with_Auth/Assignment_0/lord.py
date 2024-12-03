import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()

url = "https://the-one-api.dev/v2//movie"

Api_key = os.getenv("API_Lord_Key")


headers = {
    "Authorization": Api_key
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())