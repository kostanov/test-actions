from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Time Backend")


@app.get("/time")
def get_current_time():
    return {"server_time": datetime.now().isoformat()}


@app.get("/")
def root():
    return {"message": "Use /time endpoint to get current server time"}
