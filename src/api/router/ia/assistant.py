from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.shared.dependencies import get_session_db 
from core.shared.dependencies import get_bank_assistant
from schemas.ai.assistant import Assistant

router = APIRouter()

@router.post("/ask_assistent_ia")
async def ask_ai(
    data:Assistant,
    session_db: AsyncSession = Depends(get_session_db),
    ):
    
    assistant = await get_bank_assistant()
    response_text = await assistant.ask(
        data.question,
        data.cod_conta, 
        session_db
        )
   
    return {"answer": response_text}
