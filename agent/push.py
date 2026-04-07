import requests

URL = "http://127.0.0.1:8000/ingest"

def send(payload):
    try:
        requests.post(URL, json=payload, timeout=2)
    except Exception:
        pass
