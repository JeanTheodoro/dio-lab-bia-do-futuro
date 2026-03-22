from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
    )

from core.shared.dependencies import get_session_db 
from service.bank_transection.conta import AccountService
from schemas.bank.conta import AccountServiceResponse

router = APIRouter()

from core.shared.config_logging import LoggerHandler
logger = LoggerHandler().instace_logging()

@router.get("/{cod_conta}", response_model=AccountServiceResponse)
async def get_account(
    cod_account: int,
    session_db: AsyncSession = Depends(get_session_db)
):
    account = await AccountService.get_account(session_db, cod_account)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    logger.info("$$$$$$$")
    print(account)
    logger.info("$$$$$$")
    return {
        "client": account.cliente,
        "transection": account.transacoes
    }