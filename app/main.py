from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

from gemini.routes import router as gemini_router

# Initialize app
app = FastAPI()

# CORs
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_HEADERS,
    allow_headers=settings.CORS_METHODS,
)

# Register routes
app.include_router(gemini_router)
