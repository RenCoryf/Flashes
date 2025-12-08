from asyncio import run

from app.logging import setup_logging


async def main():
    setup_logging()


if __name__ == "__main__":
    run(main())
