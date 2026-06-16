from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    email = Column(String(255), unique=True)

    password_hash = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )