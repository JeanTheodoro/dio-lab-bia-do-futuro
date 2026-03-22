from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
    )

from core.shared.dependencies import get_session_db 
from schemas.bank.cliente import ClientCreate  
from service.bank_profile.cliente import ClientService
from service.bank_transection.conta import AccountService

router = APIRouter()


@router.post("/")
async def create_cliente(cliente:ClientCreate, session_db: AsyncSession = Depends(get_session_db)):
    client = await ClientService.create_client(session_db, cliente)
    account = await AccountService.create_account(session_db, client)
    
    return {
        "client":client,
        "account": account
    } 

@router.get("/")
async def get_client(cod_account: int, session_db: AsyncSession = Depends(get_session_db)):
    cliente = await ClientService.get_client(session_db, cod_account)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return cliente
