from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

app = FastAPI()

@app.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return StreamingResponse(BytesIO(output_data), media_type="image/png")
