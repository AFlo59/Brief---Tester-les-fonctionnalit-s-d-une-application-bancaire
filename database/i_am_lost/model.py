from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'
    account_id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    transactions = relationship("Transaction", back_populates="accounts")

class Transaction(Base):
    __tablename__ = 'transaction'
    transaction_id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    account = relationship("Account", back_populates="transactions")

