from abc import ABC, abstractmethod
from langchain_core.messages import BaseMessage
from typing import List


class BaseLLMProvider(ABC):

    @abstractmethod
    def invoke(self, messages: List[BaseMessage]) -> str:
        pass

    @abstractmethod
    async def ainvoke(self, messages: List[BaseMessage]) -> str:
        pass