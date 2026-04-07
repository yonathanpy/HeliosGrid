from fastapi import FastAPI
from store import add, latest

app = FastAPI()

@app.post("/ingest")
def ingest(payload: dict):
    add(payload)
    return {"ok": True}

@app.get("/data")
def data():
    return latest()
