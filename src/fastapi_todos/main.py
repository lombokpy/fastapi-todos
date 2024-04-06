import logging

# from api.api_v1.api import api_router
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# from core.events import create_start_app_handler
import router
from core.config import settings

# Suppress specific warnings
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# warnings.filterwarnings("ignore", category=urllib3.exceptions.SecurityWarning)

# Adjust logging levels
log = logging.getLogger("uvicorn")
# log.setLevel(logging.INFO)


def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # application.add_event_handler("startup", create_start_app_handler(application))
    application.include_router(router.api_router, prefix=settings.API_V1_STR)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    # init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
