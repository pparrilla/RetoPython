from pydantic import BaseModel, Field

class Joke(BaseModel):
    joke: str = Field(min_length=1)