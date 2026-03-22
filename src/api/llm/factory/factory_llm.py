# src/api/llm/factory/factory_llm.py
from core.shared.settings import settings
from llm.provider.ollma_provider import OllamaProvider
from llm.provider.grok_provider import GrokProvider


class LLMFactory:

    @staticmethod
    async def create():

        if settings.LLM_PROVIDER == "ollama":
            return OllamaProvider()

        elif settings.LLM_PROVIDER == "grok":
            return GrokProvider()

        raise ValueError("LLM_PROVIDER inválido")
