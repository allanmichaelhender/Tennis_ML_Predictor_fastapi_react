from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import settings

# engine now uses the URL loaded from your .env via pydantic
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
