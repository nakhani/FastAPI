from fastapi import FastAPI, HTTPException
import dotenv
import os
import requests

dotenv.load_dotenv()

app = FastAPI()

solar_system = {
    "sun": {
        "radius": 695508000,
        "distanceFromSun": 0,
        "didYouKnow": "The color of the Sun in space is actually mostly white, not yellow or orange. The reason it appears yellow or orange on Earth is due to atmospheric scattering, especially when it is low in the sky."
    },
    "mercury": {
        "distanceFromSun": 57900000000,
        "radius": 2439000,
        "didYouKnow": "Mercury is actually smaller than some moons of our solar system including Ganymede of Jupiter and Titan of Saturn."
    },
    "venus": {
        "distanceFromSun": 108200000000,
        "radius": 6051000,
        "didYouKnow": "While having the second hottest surface temperature in the solar system after The Sun, which is 450C (842F), its atmosphere is so dense that it actually crushes CO2 at the surface and turns it into an exotic material called \"super critical fluid\" which is neither a gas nor a liquid but has properties of both."
    },
    "earth": {
        "distanceFromSun": 149600000000,
        "radius": 6371000,
        "didYouKnow": "Earth's first line of defense against harmful radiation from The Sun is its magnetosphere which extends much further out than the atmosphere. Occasionally charged particles from The Sun will get trapped in the funnel and fall down to Earth, interacting with our atmosphere. This causes the visual phenomenon called an aurora."
    }
}

@app.get("/")
def read_root():
    return {
        "message": "Hi! Welcome to my API. The Solar System API provides information for thousands of solar system planets and their moons."
    }

@app.get("/planets")
def get_planets():
    return solar_system

@app.get("/planets/{planet_name}")
def get_planet_info(planet_name: str):
    planet = solar_system.get(planet_name.lower())
    if planet is None:
        raise HTTPException(status_code=404, detail="Planet not found")
    return planet

@app.get("/planets/{planet_name}/image")
def get_planet_image(planet_name: str):
    planet = solar_system.get(planet_name.lower())
    if planet is None:
        raise HTTPException(status_code=404, detail="Planet not found")
    
    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
    api_key = os.getenv("API_Dif_key")

    payload = {
        "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/pattern.png",
        "prompt": f"{planet_name} planet",
        "negative-prompt": "worst quality"
    }
    
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)  
        response.raise_for_status()  
        print(response.status_code)
        response_json = response.json()
        image_url = response_json.get("image", {}).get("url")
        print (response_json )
        
        if not image_url:
            raise HTTPException(status_code=500, detail="Image URL not found in response")
        
        return {"image_url": image_url}

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Request timed out")
    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"An error occurred: {err}")
