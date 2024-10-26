# api_gateway/main.py
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Gateway"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    try:
        response = requests.get(f"http://user_service:8001/user/{user_id}")
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=502, detail="User service unavailable")
