from minio import Minio

from .config import config


class MinioDB:
    def __init__(self):
        self._client = Minio(
            endpoint=config.MINIO_ENDPOINT,
            access_key=config.MINIO_ROOT_USER,
            secret_key=config.MINIO_ROOT_PASSWORD,
            secure=config.MINIO_SECURE,
        )
        self.bucket_name = config.MINIO_MAIN_BUCKET

    @property
    def client(self):
        return self._client
