import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return result["text"]