from pydantic import BaseModel, ConfigDict
from typing import List
from schemas.bank.cliente import ClientResponse
from schemas.bank.transacao import TransectionResponse


class AccountServiceResponse(BaseModel):
    client: ClientResponse
    transection: List[TransectionResponse]

    model_config = ConfigDict(from_attributes=True)