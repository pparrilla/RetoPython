from fastapi import APIRouter, status, HTTPException
import requests

from config.config import Config

router = APIRouter(
    prefix="/api/v1/jokes",
    tags=['jokes']
)

config = Config()
url_chuck_norris = config.URL_CHUCK_NORRIS
url_dad_jokes = config.URL_DAD_JOKES
headers = {'Accept': 'text/plain'}

@router.get('/{joke}', status_code=status.HTTP_200_OK)
async def get_joke(joke: str):
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