from math import gcd
from fastapi import APIRouter, Response, status, HTTPException
import requests


router = APIRouter(
    prefix="/api/v1/maths",
    tags=['maths']
)

@router.get('/lcm', status_code=status.HTTP_200_OK)
async def get_lcm(numbers: str):
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]
    lcm = numbers[0]

    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // gcd(lcm, numbers[i])

    result = str(lcm)

    return Response(
        status_code=status.HTTP_200_OK,
        content=result
    )

# endpoint return number + 1
@router.get('/number-plus-one', status_code=status.HTTP_200_OK)
async def get_number_plus_one(number: int):
    number_plus_one = str(number + 1)
    return Response(
        status_code=status.HTTP_200_OK,
        content=number_plus_one
    )