from pydantic import BaseModel

class PlayerOut(BaseModel):
    player_id: str
    full_name: str

    class Config:
        from_attributes = True