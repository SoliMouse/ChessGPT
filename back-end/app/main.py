# internal
from app.routers import games, moves, ping
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_application() -> FastAPI:
    load_dotenv()
    application = FastAPI(
        title="gameGPT",
        version="0.0.1",
        description="Experimental open-source project exploring the potential of LLMs, specifically ChatGPT, in generating original and customizable musical compositions.",
    )
    # middlewares
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # ping pong
    application.include_router(ping.router, prefix="", tags=["Ping"])
    # models following rest guidelines
    application.include_router(moves.router, prefix="/moves", tags=["Moves"])
    application.include_router(games.router, prefix="/games", tags=["Games"])
    return application


app = create_application()
