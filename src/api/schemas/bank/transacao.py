from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransectionResponse(BaseModel):
    id: int
    categoria: str
    descricao: str
    tipo_operacao: str
    conta_corrente_id: int
    valor: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
