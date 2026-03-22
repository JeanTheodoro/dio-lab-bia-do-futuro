from sqlalchemy.ext.asyncio import AsyncSession

from schemas.bank.cliente import ClientCreate, ClientUpdate
from repository.bank_profile.cliente import ClienteRepository


class ClientService:

    @staticmethod
    async def create_client(db: AsyncSession, cliente_in: ClientCreate):
        return await ClienteRepository.create(db, cliente_in)

    @staticmethod
    def get_client(db: AsyncSession, cliente_id: int):
        return ClienteRepository.get_by_id(db, cliente_id)

    @staticmethod
    def list_cliente(db: AsyncSession, skip: int = 0, limit: int = 100):
        return ClienteRepository.get_all(db, skip, limit)
    

    @staticmethod
    async def update_client(db: AsyncSession, cliente_id: int, cliente_in: ClientUpdate):
        return await ClienteRepository.update(db, cliente_id, cliente_in)

    @staticmethod
    async def delete_client(db: AsyncSession, cliente_id: int):
        return await ClienteRepository.delete(db, cliente_id)
