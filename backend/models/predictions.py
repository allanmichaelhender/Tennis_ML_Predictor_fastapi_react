from datetime import date, datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base # Ensure this matches your Base import

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    player1_id = Column(String(50), nullable=False)
    player2_id = Column(String(50), nullable=False)
    match_date = Column(Date, default=date.today)
    
    # Using Numeric to match Django's DecimalField
    player1WinOddsLogistic = Column(Numeric(precision=20, scale=3), default=0.0)
    player2WinOddsLogistic = Column(Numeric(precision=20, scale=3), default=0.0)
    player1WinOddsRForest = Column(Numeric(precision=20, scale=3), default=0.0)
    player2WinOddsRForest = Column(Numeric(precision=20, scale=3), default=0.0)
    player1WinOddsDTree = Column(Numeric(precision=20, scale=3), default=0.0)
    player2WinOddsDTree = Column(Numeric(precision=20, scale=3), default=0.0)

    submission_date = Column(DateTime, default=datetime.utcnow)
    
    # ForeignKey linking to your 'users' table id
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Optional: Relationship to access user info from prediction (prediction.author)
    author = relationship("User", back_populates="predictions")
