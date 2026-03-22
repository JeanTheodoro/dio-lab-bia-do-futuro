from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage
from typing import List
from .base_proviser import BaseLLMProvider
from core.shared.settings import settings

class OllamaProvider(BaseLLMProvider):

    def __init__(
        self,
        model: str = settings.OLLAMA_MODEL,
        base_url: str = settings.OLLAMA_BASE_URL,
        temperature: float = 0.2,
    ):
        self.llm = ChatOllama(
            model=model,
            base_url=base_url,
            temperature=temperature,
        )

    def invoke(self, messages: List[BaseMessage]) -> str:
        response = self.llm.invoke(messages)
        return response.content

    async def ainvoke(self, messages: List[BaseMessage]) -> str:
        response = await self.llm.ainvoke(messages)
        return response.content
