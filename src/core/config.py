from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env"
    )
    run: RunConfig = RunConfig()
    db_url: str = "sqlite+aiosqlite:///./db.sqlite3"

settings = Settings()