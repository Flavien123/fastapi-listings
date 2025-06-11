from fastapi import FastAPI
from uvicorn import run

from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    run("main:app", port=settings.run.port, host=settings.run.host, reload=True)
