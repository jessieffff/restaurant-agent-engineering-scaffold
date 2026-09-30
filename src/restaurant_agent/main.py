from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from restaurant_agent.api.routes.health import router as health_router
from restaurant_agent.core.config import get_settings

WEB_DIRECTORY = Path(__file__).resolve().parent / "web"


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(
        title=settings.name,
        version="0.1.0",
        description="Restaurant AI agent backend scaffold",
    )
    application.include_router(health_router)
    application.mount(
        "/assets",
        StaticFiles(directory=WEB_DIRECTORY / "assets"),
        name="restaurant-assets",
    )

    @application.get("/", include_in_schema=False)
    async def restaurant_home() -> FileResponse:
        return FileResponse(WEB_DIRECTORY / "index.html")

    return application


app = create_app()
