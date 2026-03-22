from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ClientCreate(BaseModel):
    nome: str
    idade: int | None = None
    profissao: str | None = None
    renda_mensal: float | None = None
    perfil_investidor: str | None = None
    objetivo_principal: str | None = None
    aceita_risco: bool = False


class ClientUpdate(BaseModel):
    profissao: str | None = None
    renda_mensal: float | None = None
    perfil_investidor: str | None = None
    objetivo_principal: str | None = None
    aceita_risco: bool = False

class ClientResponse(BaseModel):
    nome: str
    idade: int
    renda_mensal: float
    objetivo_principal: str
    created_at: datetime
    profissao: str
    perfil_investidor: str
    aceita_risco: bool

    model_config = ConfigDict(from_attributes=True)
