from langchain_core.messages import SystemMessage, HumanMessage
from sqlalchemy.ext.asyncio import AsyncSession

from llm.prompt.bank_system import SYSTEM_PROMPT
from llm.prompt.bank_human import HUMAN_PROMPT
from llm.serializer.serialization import serialize_to_json

from service.ia.assistant import AssistanteIaService

from llm.services.intent_classifier import detectar_intencao
from llm.services.context_builder import ContextBuilder

class BankAssistant:

    def __init__(self, provider):
        self.provider = provider

    async def ask(self, question: str, cod_conta: int, session_db: AsyncSession):

        tipo = detectar_intencao(question)

        context = await ContextBuilder.build(
            tipo,
            cod_conta,
            session_db
        )

        new_human_prompt = HUMAN_PROMPT.format(
            PERGUNTA=question,
            DADOS_CLIENTE=context["cliente"],
            TRANSACOES_BANCARIAS=context["transacoes"],
            METAS=context["metas"],
            PRODUTOS_DISPONIVEIS=context["investimentos"]
        )

        print("$$$$$$$$$$$$$$$$$")
        print(new_human_prompt)
        print("$$$$$$$$$$$$$$$$$")
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=new_human_prompt)
        ]

        print("$$$$$$$$$$$$$$$$$\n")
        print(messages)
        print("$$$$$$$$$$$$$$$$$")
        return await self.provider.ainvoke(messages)
