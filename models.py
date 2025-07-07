from pydantic import BaseModel
from typing import List
from datetime import datetime

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

class HistoryEntry(BaseModel):
    timestamp: str
    prompt: str
    response: str