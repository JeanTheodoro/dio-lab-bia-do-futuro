from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from models.bank.models_bank import CurrentAccount, Client


class ContaRepository:

    @staticmethod
    async def buscar_por_codigo(
        session_db: AsyncSession,
        cod_conta: int
    ):
        stmt = (
            select(CurrentAccount)
            .where(CurrentAccount.cod_conta_corrente == cod_conta)
            .options(
                selectinload(CurrentAccount.cliente),
                selectinload(CurrentAccount.transacoes)
            )
        )

        result = await session_db.execute(stmt)
        return result.scalars().first()
    

    @staticmethod
    async def create_account(
        session_db: AsyncSession,
        client: Client
    ):
        account = CurrentAccount(
        cliente_id=client.id
    )

        session_db.add(account)
        await session_db.commit()
        await session_db.refresh(account)

        return account
