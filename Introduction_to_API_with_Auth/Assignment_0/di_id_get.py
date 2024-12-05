import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()

url = "https://api.d-id.com/clips/clp_ky_Cwa42_bYmLyB20JeEB"

Api_key = os.getenv("API_Di_id_Key")


headers = {
    "accept": "application/json",
    "Authorization": Api_key
           
           
}

response = requests.get(url, headers=headers)

print(response.text)