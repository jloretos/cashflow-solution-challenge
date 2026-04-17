from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base


class CashFlow(Base):
    __tablename__ = "cashflow"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    transaction_date = Column(Date, nullable=False)