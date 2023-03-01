import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, BaseModel, PostgresDsn, validator, Field


class AppConfig(BaseModel):
    """Application configurations."""

    APP_NAME: str = "fruitjokes.backend.app"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300


class DbConfig(BaseModel):
    dbClusterIdentifier: Optional[str]
    password: Optional[str]
    dbname: Optional[str]
    engine: Optional[str]
    port: Optional[str]
    host: Optional[str]
    username: Optional[str]


class GlobalConfig(BaseSettings):
    """Global configurations."""
    APP_CONFIG: AppConfig = AppConfig()

    PROJECT_NAME: str
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
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    class Config:
        """Loads the dotenv file."""
        env_file = str = "../.env"


class DevConfig(GlobalConfig):
    """Development configurations."""
    PYROSCOPE_HOST: Optional[str] = None

    POSTGRES_SERVER: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_DB: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    TORTOISE_DATABASE_URI: Optional[PostgresDsn] = Field(env="DATABASE_URL")

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
        env_file = str = "../.env"
        # env_prefix: str = "DEV_"


class ProdConfig(GlobalConfig):
    """Production configurations."""
    PYROSCOPE_HOST: Optional[str] = None

    FRUITJOKESBACKENDCLUSTER_SECRET: DbConfig = DbConfig()

    POSTGRES_SERVER: Optional[str] = FRUITJOKESBACKENDCLUSTER_SECRET.host
    POSTGRES_USER: Optional[str] = FRUITJOKESBACKENDCLUSTER_SECRET.username
    POSTGRES_PASSWORD: Optional[str] = FRUITJOKESBACKENDCLUSTER_SECRET.password
    POSTGRES_DB: Optional[str] = FRUITJOKESBACKENDCLUSTER_SECRET.dbname
    POSTGRES_PORT: Optional[str] = FRUITJOKESBACKENDCLUSTER_SECRET.port
    TORTOISE_DATABASE_URI: Optional[PostgresDsn]

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
        env_file = str = "../.env"
        # env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


settings = FactoryConfig(GlobalConfig().ENV_STATE)()

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