from dependency_injector import containers, providers

from app.core.database import Database


class BaseRepositoryContainer(containers.DeclarativeContainer):
    database_config = providers.Configuration()

    database = providers.Singleton(Database, url=database_config.url)
