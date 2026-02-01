from sqlalchemy.orm import Mapped, mapped_column
from db.base_class import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    predictions = relationship("Prediction", back_populates="author", cascade="all, delete-orphan")


