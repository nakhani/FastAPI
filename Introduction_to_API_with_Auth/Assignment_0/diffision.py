import os
import requests
import dotenv 

dotenv = dotenv.load_dotenv()


url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"

Api_key = os.getenv("API_Dif_Key")


headers = {
    "Content-Type": "application/json",
    "Authorization": Api_key

}

payload = {
     "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
     "prompt": "(masterpiece:1.4), (best quality), (detailed), Medieval village scene with busy streets and castle in the distance",
     "negative-prompt": "worst quality"
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)