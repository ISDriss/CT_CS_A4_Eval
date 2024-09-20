from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image, ImageFilter
import numpy as np
from generation_methods.rorschgen3 import generate_rorschach_heightmap

app = FastAPI()

@app.get("/")
def home():
    html_content = """
    <html>
        <head>
            <title>Rorschach Test</title>
        </head>
        <body>
            <h1>Randomly Generated Rorschach Test</h1>
            <img src="/rorschach-image" alt="Rorschach Test Image" />
        </body>
    </html>
    """
    return html_content

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
