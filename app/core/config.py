from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

_ = load_dotenv()


@dataclass
class ConfigContainer:
    # ------------------ Database ------------------
    POSTGRES_USER: str = str(getenv("POSTGRES_USER"))
    POSTGRES_PASSWORD: str = str(getenv("POSTGRES_PASSWORD"))
    POSTGRES_HOST: str = str(getenv("POSTGRES_HOST"))
    POSTGRES_PORT: str = str(getenv("POSTGRES_PORT"))
    POSTGRES_DB: str = str(getenv("POSTGRES_DB"))


config = ConfigContainer()
