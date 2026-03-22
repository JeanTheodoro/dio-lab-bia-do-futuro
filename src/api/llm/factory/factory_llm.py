# src/api/llm/factory/factory_llm.py
from core.shared.settings import settings
from llm.provider.ollma_provider import OllamaProvider

class LLMFactory:

    @staticmethod
    async def create():

        if settings.LLM_PROVIDER == "ollama":
            return OllamaProvider()

        raise ValueError("LLM_PROVIDER inválido")
