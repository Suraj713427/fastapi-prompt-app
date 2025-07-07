import uuid

USERS = {
    "alice": "password123",
    "bob": "secret"
}

TOKENS = {}

def authenticate(username: str, password: str) -> str:
    if USERS.get(username) == password:
        token = str(uuid.uuid4())
        TOKENS[token] = username
        return token
    return None

def get_user_from_token(token: str) -> str:
    return TOKENS.get(token)