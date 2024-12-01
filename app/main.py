from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gemini.routes import router as gemini_router

# Initialize app
app = FastAPI()

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
