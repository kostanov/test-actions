from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Time Backend")


@app.get("/time")
def get_current_time():
    return {"server_time": datetime.now().isoformat()}


@app.get("/date")
def get_current_date():
    return {"server_date": datetime.now().date().isoformat()}


@app.get("/")
def root():
    return {"message": "Use /time or /date endpoints"}
