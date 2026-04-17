from app.models.cashflow import CashFlow
from sqlalchemy import func


def create_cashflow_entry(data, db):
    entry = CashFlow(
        description=data.description,
        amount=data.amount,
        type=data.type,
        transaction_date=data.transaction_date
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {
        "message": "Cashflow entry created successfully",
        "id": entry.id
    }


def list_cashflow(db):
    return db.query(CashFlow).all()


def get_summary(db):
    income = db.query(func.sum(CashFlow.amount)).filter(CashFlow.type == "income").scalar() or 0
    expense = db.query(func.sum(CashFlow.amount)).filter(CashFlow.type == "expense").scalar() or 0

    return {
        "total_income": income,
        "total_expense": expense,
        "balance": income - expense
    }