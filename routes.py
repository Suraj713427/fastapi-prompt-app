from fastapi import APIRouter, HTTPException, Header
from models import LoginRequest, LoginResponse, PromptRequest, PromptResponse, HistoryEntry
from auth import authenticate, get_user_from_token
from memory import USER_HISTORY
from datetime import datetime
import random

router = APIRouter()

fake_responses = [
    "Interesting... Let's explore that idea.",
    "Let me think...",
    "Hmm... fascinating question.",
    "Great point! Let’s dig deeper.",
    "That's worth thinking about!"
]

@router.post("/login/", response_model=LoginResponse)
def login(data: LoginRequest):
    token = authenticate(data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": token}

@router.post("/prompt/", response_model=PromptResponse)
def submit_prompt(data: PromptRequest, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = authorization.split(" ")[1]
    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=403, detail="Unauthorized")

    response = random.choice(fake_responses)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": data.prompt,
        "response": response
    }
    USER_HISTORY[user].append(entry)

    return {"response": response}

@router.get("/history/", response_model=list[HistoryEntry])
def get_history(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = authorization.split(" ")[1]
    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=403, detail="Unauthorized")

    return USER_HISTORY[user]