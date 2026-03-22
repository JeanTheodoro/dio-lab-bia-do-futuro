from fastapi import FastAPI

from router.bank_profile.cliente import router as router_cliente  
from router.bank_transection.conta import router as router_conta
from router.ia.assistant import router as router_assistant_ia 

app = FastAPI()

app.include_router(router_cliente, prefix="/api/v1", tags=["Cliente"])
app.include_router(router_conta, prefix="/api/v1", tags=["Conta"])
app.include_router(router_assistant_ia, prefix="/api/v1", tags=["Assistent"])  

