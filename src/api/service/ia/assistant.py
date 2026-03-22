from repository.ia.asssitante import AssistanteIaRepository
from sqlalchemy.ext.asyncio import AsyncSession


class AssistanteIaService:

    @staticmethod
    async def buscar_resumo(
        db: AsyncSession, 
        cod_conta: int):

        resumo = await AssistanteIaRepository.busca_resumo_finaceiro(db, cod_conta)

        if not resumo:
            return None

        return resumo
    
    @staticmethod
    async def busca_trasacoes(
        db: AsyncSession, 
        cod_conta: int):

        trasacoes = await AssistanteIaRepository.busca_trasacoes(db, cod_conta)

        if not trasacoes:
            return None

        return trasacoes
    
    @staticmethod
    async def busca_metas(
        db: AsyncSession, 
        cod_conta: int):

        metas = await AssistanteIaRepository.busca_metas(db, cod_conta)

        if not metas:
            return None

        return metas


    @staticmethod
    async def busca_investimentos(
        db: AsyncSession,
        client: str):

        investimento = await AssistanteIaRepository.busca_investimento(db, client)

        if not investimento:
            return None

        return investimento
