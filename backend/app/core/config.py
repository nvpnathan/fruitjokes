import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, BaseModel, PostgresDsn, validator, Field


class DbModel(BaseModel):
    dbClusterIdentifier: str
    password: str
    dbname: str
    engine: str
    port: str
    host: str
    username: str


class DbSettings(BaseSettings):
    FRUITJOKESBACKENDCLUSTER_SECRET: DbModel

    class Config:
        case_sensitive = True
        env_file = "./.env"


dbsettings = DbSettings()


class Settings(BaseSettings):
    APP_NAME: str = "FruitJokes"
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = Field(env="FRONTEND")

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        if isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: Optional[str] = dbsettings.FRUITJOKESBACKENDCLUSTER_SECRET.host
    POSTGRES_USER: Optional[str] = dbsettings.FRUITJOKESBACKENDCLUSTER_SECRET.username
    POSTGRES_PASSWORD: Optional[str] = dbsettings.FRUITJOKESBACKENDCLUSTER_SECRET.password
    POSTGRES_DB: Optional[str] = dbsettings.FRUITJOKESBACKENDCLUSTER_SECRET.dbname
    POSTGRES_PORT: Optional[str] = dbsettings.FRUITJOKESBACKENDCLUSTER_SECRET.port
    TORTOISE_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("TORTOISE_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgres",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = "./.env"


settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": f"{settings.TORTOISE_DATABASE_URI}"},
    "apps": {
        "models": {
            "models": [
                "app.db.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}