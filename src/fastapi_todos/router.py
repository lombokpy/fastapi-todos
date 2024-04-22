from fastapi import APIRouter

from auth.apiv1.handler import router as auth_router
from user.apiv1.handler import router as user_router
from project.apiv1.handler import router as project_router

api_router = APIRouter()
api_router.include_router(auth_router, tags=["auth"])
api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(project_router, prefix="/projects", tags=["projects"])
