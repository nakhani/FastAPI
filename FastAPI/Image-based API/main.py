import io
import numpy as np
import cv2
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from deepface import DeepFace
from concurrent.futures import ThreadPoolExecutor
import asyncio

app = FastAPI()

executor = ThreadPoolExecutor()

def process_image(image_rgb):
   
    image_analysis = DeepFace.analyze(
        img_path=image_rgb, 
        actions=['age', 'gender', 'race', 'emotion'],
        enforce_detection=False
    )

    print(image_analysis)  

    if isinstance(image_analysis, list) and len(image_analysis) > 0:
        result = image_analysis[0]
    else:
        raise ValueError("Unexpected analysis result format")

    
    age_text = f"Age: {result['age']}"
    gender_text = f"Gender: {result['gender']}"
    race_text = f"Race: {result['dominant_race']}"
    emotion_text = f"Emotion: {result['dominant_emotion']}"

    
    y0, dy = 30, 30
    for i, line in enumerate([age_text, gender_text, race_text, emotion_text]):
        y = y0 + i * dy
        cv2.putText(image_rgb, line, (10, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 0, 0), 1)

    _, encode_image = cv2.imencode(".jpg", image_rgb)
    image_bytes = encode_image.tobytes()

    with open('processed_image.jpg', 'wb') as f: 
        f.write(image_bytes)
    
    return image_bytes

@app.post("/FaceAnalysis")
async def facial_analysis(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    loop = asyncio.get_event_loop()
    image_bytes = await loop.run_in_executor(executor, process_image, image_rgb)
   
    
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
