from pydantic import BaseModel
from datetime import date

class PredictionCreate(BaseModel):
    player1_id: str
    player2_id: str
    match_date: date

class PredictionOut(PredictionCreate):
    player1_id: str
    player2_id: str
    match_date: date
    player1WinOddsLogistic: float
    player2WinOddsLogistic: float
    player1WinOddsRForest: float
    player2WinOddsRForest: float
    player1WinOddsDTree: float
    player2WinOddsDTree: float
    
    
    
    class Config:
        from_attributes = True
