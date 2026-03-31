from fastapi import FastAPI
import time
from datetime import datetime

app = FastAPI()

START_TIME = time.time()

@app.get("/health")
def health_check():
    uptime_seconds = time.time() - START_TIME
    return {
        "nama": "Muhammad-Akhdan-Alwaafy",
        "nrp": "5025241223",
        "status": "UP",
        "timestamp": datetime.now().isoformat(),
        "uptime": f"{uptime_seconds:.2f} seconds"
    }