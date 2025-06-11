from fastapi import FastAPI
from uvicorn import run

from api import router as api_router
from core import settings

app = FastAPI(title=settings.names.title)

app.include_router(api_router)

if __name__ == "__main__":
    run("main:app", host=settings.run.host, port=settings.run.port, reload=settings.run.reload)