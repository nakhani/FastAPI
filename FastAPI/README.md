# 🎯 FastAPI Projects Collection

A collection of beginner-friendly APIs built with FastAPI. Each project demonstrates useful functionalities—from image-based face analysis to managing to-do tasks with a SQLite database.

---

## 📁 Projects Overview

### 🧠 Face Analysis API
Analyze facial attributes such as **age**, **gender**, **race**, and **emotion** using the DeepFace library.

🔗 [Explore the Face Analysis API](./Image-based%20API/README.md)

📸 Features:
- Detect age, gender, emotion, and race from images
- Annotated output image returned as JPEG
- Endpoint: `POST /FaceAnalysis`

---

### 📝 To-Do App
A simple task manager that lets you add, update, and delete tasks stored in a SQLite database.

🔗 [Explore the To-Do App](./To-Do%20App/README.md)

📋 Features:
- CRUD operations for tasks
- Interactive JSON responses
- Endpoint: `/items` (GET, POST, PUT, DELETE)

---

## 🚀 Getting Started

Each project has its own setup. Visit the respective folders for detailed instructions:

```bash
cd Image-based API   # For Face Analysis API
cd To-Do App         # For To-Do App
```
To run the APIs:
```bash
uvicorn main:app --reload
```
---

## 🧪 Technologies Used
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- DeepFace
- Python 3.9+