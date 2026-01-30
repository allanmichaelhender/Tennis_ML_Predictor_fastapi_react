from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.api import api_router   
from backend.core.config import settings

def get_application() -> FastAPI:
    # Initialize FastAPI with project metadata
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set up CORS (Cross-Origin Resource Sharing)
    # Essential for allowing your frontend to talk to this backend
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include all routes from our API router
    # This automatically prefixes all endpoints with /api/v1
    _app.include_router(api_router, prefix=settings.API_V1_STR)

    return _app

app = get_application()
