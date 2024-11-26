from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get('/')
async def root():
    return {
        'status': '200',
        'message': 'Hello, World!',
    }
