# 🚀 FastAPI Projects Repository

Welcome to a comprehensive collection of hands-on **FastAPI** projects — designed to help you master API development, authentication, deployment, Docker, SQL integration, and asynchronous programming in Python. Each folder contains a standalone project with its own `README.md` and setup instructions.

---

## 📁 Project Structure

### 1. 📡 Introduction to API
- 🌤️ **GUI Weather App**  
  Search for a city and fetch weather data using [GoWeather API](https://goweather.herokuapp.com/weather/Mashhad). Design the GUI using Tkinter, Qt, Arcade, or HTML/CSS. Handle API errors gracefully.

- 🌐 **Multi-language API Usage**  
  Use your favorite programming language to interact with 4 different APIs (e.g., Fruit 🍉, Number 🔢, Harry Potter ⚡️, Quran 📖). Postman scripts can help you get started.

- 🔐 **API with Auth Token**  
  Find and test an API that requires an authentication token. Share your results with the group.

---

### 2. 🔐 Introduction to API with Auth
- 🌿 **Plant Recognition App**  
  Accept a plant name via CLI using `argparse`, generate its image using [Illusion Diffusion](https://fal.ai/models/illusion-diffusion/api), and identify it with [PlantNet](https://my.plantnet.org/doc/openapi). Use `.env` for API keys and handle errors with `try...except`.

- 📦 **Requests Module Explorer**  
  Extract metadata from Python’s `requests` module (version, license, author, etc.).  
  👉 [Sample Solution](https://www.w3resource.com/python-exercises/requests/python-request-exercise-1.php)

- 👥 **GitHub API Integration**  
  Use GitHub’s public API to display your followers and followings.  
  `https://api.github.com/users/{your_username}`

---

### 3. 🌐 Hello FastAPI
- 🪐 **Solar System API**  
  Serve data about planets, stars, and moons. Raise `HTTPException` for invalid inputs. Deploy on [Render](https://render.com) or [Liara](https://liara.ir).

- ♟️ **Chess API**  
  Provide info and images for six chess pieces. Includes multiple endpoints:
  - `/` → Intro paragraph  
  - `/pieces` → List all pieces  
  - `/pieces/{piece_name}` → Info about a specific piece  
  - `/pieces/{piece_name}/image` → Image of the piece

- 🍎 **7 Sins of Nowruz API**  
  Share cultural insights about Iranian New Year traditions. Similar endpoint structure as the Chess API.

---

### 4. ✅ FastAPI Core Projects
- ☑️ **To-Do App**  
  Create a SQLite database (`todo.db`) and build CRUD endpoints (`GET`, `POST`, `PUT`, `DELETE`). Raise `HTTPException` for invalid inputs.

- 🏞️ **Image-Based API**  
  Upload and process images for services like:
  - Face analysis → [DeepFace](https://github.com/serengil/deepface)  
  - OCR → [EasyOCR](https://github.com/JaidedAI/EasyOCR)  
  - Object detection → [YOLO](https://github.com/ultralytics/ultralytics)

---

### 5. 🐳 FastAPI with Docker
- ☑️ **Dockerized To-Do App**  
  Add `requirements.txt` and `Dockerfile`. Build and run your Docker image/container. Deploy on [Liara](https://liara.ir) and document all Docker commands used.

---

### 6. 🧑🏻‍🎓 FastAPI with SQL (PostgreSQL)
- 🎓 **University System**  
  Follow [FastAPI SQL tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/). Replace `User` and `Item` with `Student` and `Course` models. Use PostgreSQL via Docker and deploy on Liara.

  Example Docker commands:
  ```bash
  docker pull postgres
  docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=your_password -e POSTGRES_USER=your_user -e POSTGRES_DB=your_db -d postgres
  ```
---

### 7. ⚡ FastAPI Async

- 🎵 **Rhyme Finder**
   Use [rhyming.ir](https://rhyming.ir/) API to find rhymes for Persian words.

- 🗺️ **Iran Location API**
   Fetch states and cities using:
   - `https://iran-locations-api.vercel.app/api/v1/fa/states`
   - `https://iran-locations-api.vercel.app/api/v1/fa/cities?state_id={state_id}`

- 📍 **Get Coordinates**
   Combine state and city lookups to return latitude and longitude. Use `asyncio` to optimize performance.

---

### 📚 How to Use
Each folder includes:

- ✅ Project-specific instructions
- 📄 `README.md` with setup and usage
- 🧪 Sample endpoints and expected outputs
- 🖼️ Screenshots or deployment links (where applicable)

---




