# ✅ To-Do App with FastAPI & Docker 🐳

A simple project to build a task management app using FastAPI and Docker.

---

## 🐳 Docker Setup

1. Build Docker Image

```bash
docker build -t todo-fastapi .
```
2. Run Docker Container

```bash
docker run -d -p 8000:8000 todo-fastapi
```
3. Access in Browser or Postman

Open the link below:

```bash
http://localhost:8000
```

4. Docker Container Status

After running the container, you can check its status using:

```bash
docker ps
```
Example output:
```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                         NAMES
5eb28bf53ad9   todo-fastapi   "uvicorn main:app --…"   23 seconds ago   Up 23 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   condescending_cannon
```

---
## 🚀 Deployment

This project is deployed using [Liara](https://liara.ir).

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/nakhani/FastAPI/tree/4c5ef1bf57fb901963392d4e6085f0c25a385732/FastAPI_Docker
cd FastAPI_Docker

# Install dependencies (if running locally)
pip install -r requirements.txt
```
---
## 🧰 Technologies Used

- Python 3.10  
- FastAPI  
- Docker  
- Uvicorn 



