from fastapi import FastAPI

from .gemini.routes import router as gemini_router


app = FastAPI()

# Register routes
app.include_router(gemini_router)
