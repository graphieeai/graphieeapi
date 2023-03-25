from fastapi import APIRouter
from routes.router import router as api_routes

base_router = APIRouter()
base_router.include_router(api_routes, prefix="/api/v1", tags=["retraining"])

@base_router.get("/")
async def index():
    return { "response_status": 200, "message": "Welcome to Graphiee API"}
