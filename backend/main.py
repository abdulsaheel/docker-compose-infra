import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    worker_response = requests.get("http://worker:5000/process")
    return {"message": f"Backend says: {worker_response.json()['message']}"}
