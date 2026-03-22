import re
import unicodedata


def normalizar(texto: str):

    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")

    return texto


def detectar_intencao(pergunta: str) -> list:

    pergunta = normalizar(pergunta)
    types = list()

    if re.search(r"\b(debito|debitos|credito|creditos|gasto|gastos|gastei|despesa|despesas|transacao|transações|pagamento|ganhos|registro|registros)\b", pergunta):
        types.append("transacao")

    if re.search(r"\b(investimento|investimentos|investir|aplicar|aplicacao|renda)\b", pergunta):
        types.append("investimento")

    if re.search(r"\b(meta|metas|objetivo|objetivos|planejamento)\b", pergunta):
        types.append("meta")
    
    return types if types.__sizeof__() > 0 else types.append("geral")
