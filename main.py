from fastapi import FastAPI
from rembg import remove
from fastapi import UploadFile, File
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    contents = await file.read()
    input_image = Image.open(BytesIO(contents))
    output_image = remove(input_image)
    output_buffer = BytesIO()
    output_image.save(output_buffer, format="PNG")
    output_buffer.seek(0)
    return StreamingResponse(output_buffer, media_type="image/png")


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

