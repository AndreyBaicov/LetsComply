FROM python:3.10-slim

RUN pip install --upgrade pip && \
    pip install openai-whisper fastapi uvicorn[standard] python-multipart

RUN apt-get update && apt-get install -y curl xz-utils && \
    mkdir -p /opt/ffmpeg && \
    curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    | tar -xJ --strip-components=1 -C /opt/ffmpeg && \
    ln -s /opt/ffmpeg/ffmpeg /usr/local/bin/ffmpeg && \
    ln -s /opt/ffmpeg/ffprobe /usr/local/bin/ffprobe && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app /app

RUN python -c "import whisper; whisper.load_model('base')"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--log-level", "debug"]