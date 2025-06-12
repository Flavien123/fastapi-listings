from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

base_dir = Path(__file__).resolve().parent.parent


class Db(BaseModel):
    db_url: str = "sqlite+aiosqlite:///./app/db.sqlite3"
    db_echo: bool = False


class Names(BaseModel):
    title: str = "FastAPI"


class Run(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Cors(BaseModel):
    allow_origins: list[str] = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:3000",
        "*",
    ]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class Settings(BaseSettings):
    db: Db = Db()
    names: Names = Names()
    run: Run = Run()
    env: Env = Env()
    cors: Cors = Cors()


settings = Settings()
