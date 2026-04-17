from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cashflow import (
    CashflowCreate,
    CashflowResponse,
    CashflowItem,
    CashflowSummary,
)
from app.services.cashflow_service import (
    create_cashflow_entry,
    list_cashflow,
    get_summary,
)
from app.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/cashflow", response_model=CashflowResponse)
def create_cashflow(data: CashflowCreate, db: Session = Depends(get_db)):
    return create_cashflow_entry(data, db)


@router.get("/cashflow", response_model=List[CashflowItem])
def get_cashflow(db: Session = Depends(get_db)):
    return list_cashflow(db)


@router.get("/cashflow/summary", response_model=CashflowSummary)
def summary_cashflow(db: Session = Depends(get_db)):
    return get_summary(db)