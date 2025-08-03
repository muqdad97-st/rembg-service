from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO
from PIL import Image
import os
import uvicorn

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
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
