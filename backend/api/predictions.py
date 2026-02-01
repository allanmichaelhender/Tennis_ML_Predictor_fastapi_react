from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from deps import get_db, get_current_user
from models import user, predictions # Ensure these models exist
from models.predictions import Prediction
import schemas
from schemas.predictions import PredictionOut as PredictionOut_schema, PredictionCreate as PredictionCreate_schema
import crud

from api.predictor_functions import (
    logistic_regression_predict, 
    random_forest_predict, 
    decision_tree_predict
)

router = APIRouter()

@router.get("/", response_model=List[PredictionOut_schema])
def get_my_predictions(
    db: Session = Depends(get_db),
    current_user: user = Depends(get_current_user)
):
    return db.query(Prediction).filter(Prediction.author_id == current_user.id).all()

@router.post("/", response_model=PredictionOut_schema)
def create_prediction(
    prediction_in: PredictionCreate_schema,
    db: Session = Depends(get_db),
    current_user: user = Depends(get_current_user)
):
    p1, p2, m_date = prediction_in.player1_id, prediction_in.player2_id, prediction_in.match_date

    [[p2_log, p1_log]] = logistic_regression_predict(p1, p2, m_date)
    [[p2_rf, p1_rf]] = random_forest_predict(p1, p2, m_date)
    [[p2_dt, p1_dt]] = decision_tree_predict(p1, p2, m_date)

    db_obj = Prediction(
        **prediction_in.model_dump(),
        author_id=current_user.id,
        player1WinOddsLogistic=float(p1_log),
        player2WinOddsLogistic=float(p2_log),
        player1WinOddsRForest=float(p1_rf),
        player2WinOddsRForest=float(p2_rf),
        player1WinOddsDTree=float(p1_dt),
        player2WinOddsDTree=float(p2_dt)
    )
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.delete("/{prediction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prediction(
    prediction_id: int,
    db: Session = Depends(get_db),
    current_user: user = Depends(get_current_user)
):
    prediction = db.query(Prediction).filter(Prediction.id == prediction_id).first()

    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")

    if prediction.author_id != current_user.id:
        raise HTTPException(
            status_code=403, 
            detail="Not authorized to delete this prediction"
        )

    db.delete(prediction)
    db.commit()
    return None

@router.post("/guest", response_model=PredictionOut_schema)
def create_prediction_guest(
    prediction_in: PredictionCreate_schema,
    db: Session = Depends(get_db) 
):
    p1, p2, m_date = prediction_in.player1_id, prediction_in.player2_id, prediction_in.match_date

    [[p2_log, p1_log]] = logistic_regression_predict(p1, p2, m_date)
    [[p2_rf, p1_rf]] = random_forest_predict(p1, p2, m_date)
    [[p2_dt, p1_dt]] = decision_tree_predict(p1, p2, m_date)

    return {
        **prediction_in.model_dump(),
        "id": 0,
        "player1WinOddsLogistic": float(p1_log),
        "player2WinOddsLogistic": float(p2_log),
        "player1WinOddsRForest": float(p1_rf),
        "player2WinOddsRForest": float(p2_rf),
        "player1WinOddsDTree": float(p1_dt),
        "player2WinOddsDTree": float(p2_dt)
    }
