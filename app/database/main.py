import app.database.models as models
from app.database.database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()