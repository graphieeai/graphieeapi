from fastapi import APIRouter
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()

@router.get("/")
async def root():
    return {"status": 200, "message": "root api"}


class Message(BaseModel):
    message: str

@router.post('/chat')
async def chat(message: Message):
    chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")
    response = chatbot(message.message, max_length=50, do_sample=True)
    return {"message": response[0]['generated_text']}