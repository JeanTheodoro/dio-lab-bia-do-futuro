from pydantic import BaseModel


class Assistant(BaseModel):
    question: str
    cod_conta: int
