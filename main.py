from fastapi import FastAPI
import uvicorn

from app.controllers.jokes import router as jokes_router
from app.controllers.maths import router as maths_router

description = ""

tags_metadata = [
    {
        "name": "jokes",
        "description": "Jokes API"
    }
]

def create_app():
    app = FastAPI(
        title="Jokes API",
        description=description,
        version="1.0",
        openapi_tags=tags_metadata,
    )
    app.include_router(jokes_router)
    app.include_router(maths_router)
    return app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)