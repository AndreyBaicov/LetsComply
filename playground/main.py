from fastapi import FastAPI, File, UploadFile
import whisper
import tempfile

app = FastAPI()
model = whisper.load_model("base")

@app.post("/asr")
async def transcribe(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return {"text": result["text"]}