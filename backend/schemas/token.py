from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str | None = None

class TokenPayload(BaseModel):
    sub: str | None = None  # This is the user_id/username
    exp: int | None = None  # Expiration timestamp



