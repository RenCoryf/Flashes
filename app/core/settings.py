from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class DatabaseSettings(ConfigBase):
    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
    )

    HOST: str
    PORT: int
    DB: str
    USER: str
    PASSWORD: str

    @property
    def url(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB}"


class Settings(ConfigBase):
    database_settings: DatabaseSettings


settings = Settings()
