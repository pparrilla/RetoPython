from fastapi import APIRouter, status, HTTPException, Depends
import requests
from sqlalchemy.orm import Session
from sqlalchemy import func


from config.config import Config
from app.models.joke import Joke
from app.database.main import get_db, models

router = APIRouter(
    prefix="/api/v1/jokes",
    tags=['jokes']
)

config = Config()
url_chuck_norris = config.URL_CHUCK_NORRIS
url_dad_jokes = config.URL_DAD_JOKES
headers = {'Accept': 'text/plain'}

@router.get('/{joke}', status_code=status.HTTP_200_OK)
async def get_joke(joke: str, db: Session = Depends(get_db)):
    if joke == 'Chuck':
        response = requests.get(url_chuck_norris, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    elif joke == 'Dad':
        response = requests.get(url_dad_jokes, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")

@router.get('/', status_code=status.HTTP_200_OK)
async def get_joke(db: Session = Depends(get_db)):
    return db.query(models.Jokes).order_by(func.random()).first()

@router.post('/', status_code=status.HTTP_200_OK)
async def post_joke(joke: Joke, db: Session = Depends(get_db)):

    joke_model = models.Jokes()
    joke_model.joke = joke.joke

    db.add(joke_model)
    db.commit()

    return joke

@router.put('/{id}', status_code=status.HTTP_200_OK)
async def put_joke(id: int, joke: Joke, db: Session = Depends(get_db)):

    joke_model = db.query(models.Jokes).filter(models.Jokes.id == id).first()

    if joke_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    joke_model.joke = joke.joke

    db.add(joke_model)
    db.commit()

    return joke

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_joke(id: int, db: Session = Depends(get_db)):

        joke_model = db.query(models.Jokes).filter(models.Jokes.id == id).first()

        if joke_model is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        db.query(models.Jokes).filter(models.Jokes.id == id).delete()
        db.commit()