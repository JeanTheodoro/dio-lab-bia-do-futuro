from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload


from schemas.bank.cliente import ClientCreate, ClientUpdate
from models.bank.models_bank import (
    Client, 
    CurrentAccount
    )


class ClienteRepository:

    @staticmethod
    async def create(db: AsyncSession, cliente_in: ClientCreate) -> Client:
        client = Client(**cliente_in.model_dump())
        db.add(client)
        await db.commit()
        await db.refresh(client)
        return client

    @staticmethod
    async def get_by_id(db: AsyncSession, cod_conta: int):

        stmt = (
            select(CurrentAccount)
            .options(
                selectinload(CurrentAccount.cliente),
                selectinload(CurrentAccount.transacoes)
            )
            .where(CurrentAccount.cod_conta_corrente == cod_conta)
        )

        result = await db.execute(stmt)
        return result.scalars().first()

    @staticmethod
    async def get_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Client]:
        stmt = select(Client).offset(skip).limit(limit)
        result = await db.execute(stmt)
        return result.scalars().all()

    @staticmethod
    async def update(
        db: AsyncSession,
        cliente_id: int,
        cliente_in: ClientUpdate
    ) -> Optional[Client]:

        result = await db.execute(
            select(Client).where(Client.id == cliente_id)
        )
        cliente = result.scalar_one_or_none()

        if not cliente:
            return None

        update_data = cliente_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(cliente, field, value)

        await db.commit()
        await db.refresh(cliente)

        return cliente

    @staticmethod
    async def delete(db: AsyncSession, cliente_id: int) -> bool:
        result = await db.execute(
            select(Client).where(Client.id == cliente_id)
        )
        cliente = result.scalar_one_or_none()

        if not cliente:
            return False

        await db.delete(cliente)
        await db.commit()
        return True
