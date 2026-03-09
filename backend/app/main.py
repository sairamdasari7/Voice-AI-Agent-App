
from fastapi import FastAPI
from app.api.voice import router as voice_router
from app.api.appointments import router as appointment_router

app = FastAPI()

app.include_router(voice_router)
app.include_router(appointment_router)

@app.get("/")
def home():
    return {"message": "Voice AI Clinical Agent Running"}
