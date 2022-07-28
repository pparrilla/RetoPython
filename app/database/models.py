from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Jokes(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True)
    joke = Column(String)