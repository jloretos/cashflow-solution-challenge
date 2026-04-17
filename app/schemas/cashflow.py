from pydantic import BaseModel
from datetime import date


class CashflowCreate(BaseModel):
    description: str
    amount: float
    type: str
    transaction_date: date


class CashflowItem(BaseModel):
    id: int
    description: str
    amount: float
    type: str
    transaction_date: date

    class Config:
        from_attributes = True


class CashflowResponse(BaseModel):
    message: str
    id: int


class CashflowSummary(BaseModel):
    total_income: float
    total_expense: float
    balance: float