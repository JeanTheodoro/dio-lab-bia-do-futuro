from llm.serializer.serialization import serialize_to_json
from service.ia.assistant import AssistanteIaService


class ContextBuilder:

    @staticmethod
    async def build(tipo, cod_conta, session_db):

        cliente = await AssistanteIaService.buscar_resumo(
            session_db,
            cod_conta
        )

        context = {
            "cliente": cliente,
            "transacoes": None,
            "metas": None,
            "investimentos": None
        }

        if "transacao" in tipo:

            context["transacoes"] = await AssistanteIaService.busca_trasacoes(
                session_db,
                cod_conta
            )

        if  "investimento" in tipo:

            context["metas"] = await AssistanteIaService.busca_metas(
                session_db,
                cod_conta
            )

            context["investimentos"] = await AssistanteIaService.busca_investimentos(
                session_db,
                cliente.perfil_investidor
            )

            context["transacoes"] = await AssistanteIaService.busca_trasacoes(
                session_db,
                cod_conta
            )


        if "meta" in tipo:

            context["metas"] = await AssistanteIaService.busca_metas(
                session_db,
                cod_conta
            )

        return {
            "cliente": serialize_to_json(context["cliente"]),
            "transacoes": serialize_to_json(context["transacoes"]),
            "metas": serialize_to_json(context["metas"]),
            "investimentos": serialize_to_json(context["investimentos"]),
        }
