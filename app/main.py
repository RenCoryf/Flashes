<<<<<<< HEAD
from asyncio import run

from app.logging import setup_logging


async def main():
    setup_logging()


if __name__ == "__main__":
    run(main())
=======
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Add any startup tasks here
    yield
    # Add any shutdown tasks here


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/health_check")
async def health_check():
    return {"status": "ok"}
>>>>>>> origin/containers
