from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from config import settings
from gemini.routes import router as gemini_router

# Initialize app
app = FastAPI()

# Middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# CORS
cors_origins = ['0.0.0.0']
cors_methods = ['GET', 'POST', 'PUT', 'DELETE']
cors_headers = ['Content-Type']

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_methods=cors_methods,
    allow_headers=cors_headers,
    allow_credentials=True,
)


# Register routes
app.include_router(gemini_router)
