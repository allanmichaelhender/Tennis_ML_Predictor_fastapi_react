from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from deps import get_db
from models.players import Player as Player_model
import schemas.player as player_schema

router = APIRouter()

@router.get("/", response_model=List[player_schema.PlayerOut])
def get_players(db: Session = Depends(get_db)):
    return db.query(Player_model).all()
