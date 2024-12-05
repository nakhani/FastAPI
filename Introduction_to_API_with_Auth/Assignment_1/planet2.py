import os
import requests
import argparse
import dotenv 

dotenv = dotenv.load_dotenv()

def get_arguments():
    parser = argparse.ArgumentParser(description="Generate and recognize plant images")
    parser.add_argument("plant_name", type=str, help="Name of the flower or plant")
    return parser.parse_args()

def generate_image(plant_name):
    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/" 
    api_key = os.getenv("API_Dif_key")

    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        "prompt": f"{plant_name}",
        "negative-prompt": "worst quality"
        
        
}
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print(response.status_code)
        response_json = response.json()
        response_json= response_json.get("image", {}).get("url")
        print (response_json )

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def recognize_plant(image_url):
    url = "https://my-api.plantnet.org/v2/identify/all"

    Api_key = os.getenv("API_planet_key")
    print(f"API Key: {Api_key}")  

    headers = {
    }

    payload = {
        "api-key": Api_key
    }

    files = {
        "images": ("image.jpg", requests.get(image_url).content, "image/jpeg")
    }

    try:
        response = requests.post(url, headers=headers, params=payload, files=files)
        print(response.status_code)
        print(response.json())
        return response.json().get("results")[0].get("species").get("scientificNameWithoutAuthor")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)  
    except Exception as err:
        print(f"An error occurred: {err}")

def main():
    args = get_arguments()
    plant_name = args.plant_name
    

    image_url = generate_image(plant_name)
    if not image_url:
        print("Failed to generate image.")
        return
    
    plant_recognition_result = recognize_plant(image_url)
    if plant_recognition_result:
        print(f"The recognized plant name is: {plant_recognition_result}")
    else:
        print("Failed to recognize the plant.")

if __name__ == "__main__":
    main()
