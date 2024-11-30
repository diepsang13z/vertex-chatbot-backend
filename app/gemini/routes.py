from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from .models import MessageRequest
from .services import send_message
from .prompts import IntroductionPrompt

router = APIRouter(
    prefix='/gemini',
    tags=['gemini'],
)


@router.get('/example-prompt')
def get_exp_prompt():
    return {
        'prompt': 'What is GDGoCs?'
    }


@router.post('/chat')
async def chat(request: MessageRequest):
    try:
        request_message = request.message

        assistant_message = send_message(
            message=request_message,
            introduction_prompt=IntroductionPrompt.GDG_INFORMATION_ASSISTANT,
        )

        return JSONResponse(content={
            'message': request_message,
            'assistant': assistant_message,
        }, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
