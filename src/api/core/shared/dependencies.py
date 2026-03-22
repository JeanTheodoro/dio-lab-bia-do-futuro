from core.database import AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession

async def get_session_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# src/api/core/shared/dependencies.py
from llm.factory.factory_llm import LLMFactory
from llm.services.bank_assistente import BankAssistant

async def get_bank_assistant() -> BankAssistant:
    """
    Retorna uma instância do assistente de banco com o provider LLM correto.
    """
    # Cria o provider (Ollama ou Grok)
    provider = await LLMFactory.create()
    
    # Instancia o assistente com o provider configurado
    assistant = BankAssistant(provider=provider)
    
    return assistant
