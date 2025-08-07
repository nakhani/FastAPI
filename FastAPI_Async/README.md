# 📡 Async Rhyming & Location Finder (Iran)

This Python project uses `asyncio` and `aiohttp` to asynchronously interact with two Iranian APIs. It fetches rhyming words for a given Persian word and retrieves the geographic coordinates of a specified city in Iran.

---

## 🚀 Features

- 🔤 Find rhyming words using [Rhyming.ir](https://rhyming.ir)
- 🗺️ Fetch list of Iranian provinces and cities via [Iran Locations API](https://iran-locations-api.vercel.app)
- 📍 Get latitude and longitude of a selected city
- ⚡ Asynchronous execution for faster performance using `asyncio`

---

## 🧰 Requirements

Make sure you have the following Python package installed:

```bash
pip install requirements.txt
```

---

## 📝 How to Run
1. Open the `Async_API.py` file.
2. Set your desired province and city:
```bash
 MY_STATE_NAME = "تهران"
 MY_CITY_NAME = "تهران"
```
3. Add your API key from [rhyming.ir](https://rhyming.ir/):
```bash
 API_KEY = "YOUR_API_KEY"
```
4. Run the script:
```bash
 python Async_API.py
```
---

## 📦 Program Structure

- `rhyme_finder(word)`: Fetches rhyming words for the input
- `get_states()`: Retrieves list of provinces
- `get_cities(state_id)`: Retrieves cities within a province
- `get_coordinates(state_name, city_name)`: Gets latitude and longitude of a city
- `main()`: Executes rhyme and coordinate tasks concurrently and prints results

---

## 🖥️ Sample Output
```bash
 Rhymes for the word "عشق":

Index   Word      
--------------------
1       مشق       
2       وشق       
3       نشق       
4       بشق       
5       تشق       

 Coordinates of city «تهران, تهران»:

- Latitude: 35.410
- Longitude: 51.240
```

---

## ⚠️ Notes
- To avoid RuntimeError: Event loop is closed on Windows, the following is included:
```bash
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```
---
## Technologies List

- Python
- asyncio
- aiohttp
- Iran Locations API
- [Rhyming.ir](https://rhyming.ir/) API

