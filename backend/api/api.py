from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from deps import get_db

api_router = APIRouter()


@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

@api_router.get("/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT version();"))
        version = result.fetchone()
        return {"status": "connected", "database_version": version[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")