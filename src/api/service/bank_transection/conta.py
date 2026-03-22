from sqlalchemy.ext.asyncio import AsyncSession

from repository.bank_transection.conta import ContaRepository
from models.bank.models_bank import Client

class AccountService:

    @staticmethod
    async def get_account(db: AsyncSession, cod_conta: int):
        account = await ContaRepository.buscar_por_codigo(db, cod_conta)

        if not account:
            return None

        return account

    @staticmethod
    async def create_account(db: AsyncSession, client: Client):
        account = await ContaRepository.create_account(db, client)

        if not account:
            return None
        
        return account
