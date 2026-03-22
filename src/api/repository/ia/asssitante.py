from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from datetime import datetime, timedelta

from models.bank.models_bank import ( 
    Client,
    CurrentAccount,
    Objective, 
    Transection,
    FinancialProduct
    )


class AssistanteIaRepository:

    @staticmethod
    async def busca_resumo_finaceiro(
        session_db: AsyncSession,
        cod_conta: int):

        stmt = (
            select(
                Client.nome,
                Client.idade,
                Client.perfil_investidor,
                Client.aceita_risco,
                Client.renda_mensal,
                CurrentAccount.saldo_atual
            )
            .join(Client, CurrentAccount.cliente_id == Client.id)
            .where(CurrentAccount.cod_conta_corrente == cod_conta)
        )

        result = await session_db.execute(stmt)
        row = result.mappings().first()

        return row
    
    @staticmethod
    async def busca_trasacoes(
        session_db: AsyncSession,
        cod_conta: int):

        data_limite = datetime.now() - timedelta(days=30)

        stmt = (
            select(
                Transection.descricao,
                Transection.categoria,
                Transection.valor,
                Transection.tipo_operacao,
                Transection.created_at
            )
            .select_from(CurrentAccount)
            .join(
                Transection,
                CurrentAccount.id == Transection.conta_corrente_id
            )
            .where(
                CurrentAccount.cod_conta_corrente == cod_conta
            )
            .order_by(Transection.created_at.desc())
            .limit(7)
        )

        result = await session_db.execute(stmt)
        rows = result.mappings().all()

        return rows
    
    @staticmethod
    async def busca_metas(
        session_db: AsyncSession,
        cod_conta: int):

        stmt = (
            select(
                Objective.objetivo,
                Objective.valor_necessario,
                Objective.prazo
            )
            .join(
                CurrentAccount,
                CurrentAccount.cliente_id == Objective.cliente_id
            )
            .where(CurrentAccount.cod_conta_corrente == cod_conta)
        )

        result = await session_db.execute(stmt)
        return result.mappings().all()

    @staticmethod
    async def busca_investimento(
        session_db: AsyncSession,
        perfil_investidor: str):

        perfil_para_risco_max = {
                "conservador": ["baixo"],
                "moderado": ["baixo", "medio"],
                "arrojado": ["baixo", "medio", "alto"]
            }
        
        riscos_permitidos = perfil_para_risco_max.get(perfil_investidor, [])

        stmt = select(
            FinancialProduct.nome,
            FinancialProduct.categoria,
            FinancialProduct.risco,
            FinancialProduct.rentabilidade_descricao,
            FinancialProduct.aporte_minimo,
            FinancialProduct.liquidez,
            FinancialProduct.prazo_minimo_dias
        ).where(
            FinancialProduct.risco.in_(riscos_permitidos)
        )

        result = await session_db.execute(stmt)
        produtos = result.mappings().all()
        return produtos
