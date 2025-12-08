# logging_config.py
import logging
import logging.config

from pythonjsonlogger.json import JsonFormatter


def setup_logging():
    log_level = "INFO"

    log_format = (
        "%(asctime)s %(levelname)s %(name)s "
        "%(message)s %(filename)s:%(lineno)d"
    )

    formatter = JsonFormatter(log_format)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    config = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "json": {
                "()": JsonFormatter,
                "fmt": log_format,
            }
        },

        "handlers": {
            "default": {
                "level": log_level,
                "class": "logging.StreamHandler",
                "formatter": "json",
            },
        },

        "loggers": {
            "": {  # root logger
                "handlers": ["default"],
                "level": log_level,
                "propagate": True,
            },

            "uvicorn.error": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["default"],
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(config)
