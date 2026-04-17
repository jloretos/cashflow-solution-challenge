from fastapi import FastAPI
from app.core.config import settings
from app.routers import health, cashflow
from app.database import Base, engine
from app.models.cashflow import CashFlow

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(health.router)
app.include_router(cashflow.router)