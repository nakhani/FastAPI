import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()

url = "https://api.iconfinder.com/v4/icons/search"

Api_key = os.getenv("API_Icon_Key")

payload ={ 
    "query": "arrow",
    "count": "10"
}


headers = {
    "accept": "application/json",
    "Authorization": Api_key
}

response = requests.get(url, headers=headers, params=payload)

print(response.status_code)
print(response.json)
print(response.text)