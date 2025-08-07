import asyncio
import aiohttp
import sys

API_KEY = "YOUR_API_KEY"  
MY_STATE_NAME = "تهران"        
MY_CITY_NAME = "تهران"         

# Async function to find rhymes for a word
async def rhyme_finder(word: str) -> list:
    url = f"https://rhyming.ir/api/rhyme-finder?api={API_KEY}&w={word}&sb=1&mfe=2&eq=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data

# Async function to get list of states 
async def get_states() -> list:
    url = "https://iran-locations-api.vercel.app/api/v1/fa/states"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data 


# Async function to get cities of a specific state
async def get_cities(state_id: int) -> list:
    url = f"https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data  


# Async function to get coordinates of city
async def get_coordinates(state_name: str, city_name: str) -> dict:
    states = await get_states()
    state = next((s for s in states if s["name"] == state_name), None)
    if not state:
        raise ValueError(f"State '{state_name}' not found.")

    cities = await get_cities(state["id"])
    city = next((c for c in cities if c["name"] == city_name), None)
    if not city:
        raise ValueError(f"City '{city_name}' not found in state '{state_name}'.")

    return {
        "latitude": city["latitude"],
        "longitude": city["longitude"]
    }


async def main():
    word = "عشق"  
    rhyme_task = asyncio.create_task(rhyme_finder(word))
    coord_task = asyncio.create_task(get_coordinates(MY_STATE_NAME, MY_CITY_NAME))

    rhymes = await rhyme_task
    coordinates = await coord_task

   
    print(f"\n قافیه‌های واژه «{word}»:\n")
    print("{:<6} {:<10}".format("شماره", "واژه"))
    print("-" * 20)
    for idx, item in enumerate(rhymes.get("data_items", []), start=1):
        print("{:<6} {:<10}".format(idx, item["word"]))

    
    print(f"\n Coordinates of city«{MY_CITY_NAME}، {MY_STATE_NAME}»:\n")
    print(f"- Latitude: {coordinates['latitude']}")
    print(f"- Longitude: {coordinates['longitude']}")

# 
if __name__ == "__main__":
    if sys.platform.startswith('win'):
       asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
