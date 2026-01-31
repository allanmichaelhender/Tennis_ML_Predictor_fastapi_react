from sqlalchemy import Column, String
from db.base_class import Base 

class Player(Base):
    __tablename__ = "players"

    player_id = Column(String(50), primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)
