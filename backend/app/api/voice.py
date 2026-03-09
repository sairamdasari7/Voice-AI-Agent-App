
from fastapi import APIRouter, WebSocket
from app.services.speech_to_text import transcribe
from app.services.text_to_speech import generate_voice
from app.agents.voice_agent import handle_conversation
import time

router = APIRouter()

@router.websocket("/voice")
async def voice_agent(ws: WebSocket):

    await ws.accept()

    while True:

        audio = await ws.receive_bytes()

        text = transcribe(audio)

        start = time.time()

        response = handle_conversation(text)

        latency = time.time() - start

        print("Latency:", latency)

        voice = generate_voice(response)

        await ws.send_bytes(voice)
