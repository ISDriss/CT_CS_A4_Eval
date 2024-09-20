from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageFilter
import numpy as np
from generation_methods.rorschgen3 import generate_rorschach_heightmap

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_index():
  with open('index.html', 'r') as file:
    return file.read()

@app.get("/rorschach-image")
def get_rorschach_image():
    # Generate the Rorschach image
    image = generate_rorschach_heightmap()

    # Save the image to a bytes buffer
    img_buffer = BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Return the image as a streaming response
    return StreamingResponse(img_buffer, media_type="image/png")

# Run this app using the command below:
# uvicorn filename:app --reload
