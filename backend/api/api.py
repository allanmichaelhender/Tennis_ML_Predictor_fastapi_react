from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.deps import get_db

api_router = APIRouter()

# Example: Including user endpoints
# api_router.include_router(users.router, prefix="/users", tags=["users"])

# For now, let's add a health check directly
@api_router.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

@api_router.get("/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # Executes a simple 'SELECT 1' to verify the connection
        result = db.execute(text("SELECT version();"))
        version = result.fetchone()
        return {"status": "connected", "database_version": version[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")