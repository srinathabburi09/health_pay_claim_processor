from fastapi import FastAPI
from app.api import router

app = FastAPI(title="HealthPay Claim Processor")
app.include_router(router)
