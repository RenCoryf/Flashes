from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

_ = load_dotenv()


@dataclass
class Config:
    # ------------------ Database ------------------
    POSTGRES_USER: str = str(getenv("POSTGRES_USER"))
    POSTGRES_PASSWORD: str = str(getenv("POSTGRES_PASSWORD"))
    POSTGRES_HOST: str = str(getenv("POSTGRES_HOST"))
    POSTGRES_PORT: str = str(getenv("POSTGRES_PORT"))
    POSTGRES_DB: str = str(getenv("POSTGRES_DB"))
    # ------------------ Minio ------------------
    MINIO_ENDPOINT: str = str(getenv("MINIO_ENDPOINT"))
    MINIO_ROOT_USER: str = str(getenv("MINIO_ROOT_USER"))
    MINIO_ROOT_PASSWORD: str = str(getenv("MINIO_ROOT_PASSWORD"))
    MINIO_SECURE: bool = bool(getenv("MINIO_SECURE"))
    MINIO_MAIN_BUCKET: str = str(getenv("MINIO_MAIN_BUCKET"))
    # ------------------ Redis ------------------
    REDIS_HOST: str = str(getenv("REDIS_HOST"))
    REDIS_PORT: str = str(getenv("REDIS_PORT"))
    REDIS_PASSWORD: str = str(getenv("REDIS_PASSWORD"))

config = Config()
