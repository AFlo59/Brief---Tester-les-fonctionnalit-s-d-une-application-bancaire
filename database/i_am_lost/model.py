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
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    transactions = relationship("Transaction", secondary="account_transaction_association", back_populates="accounts")

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    accounts = relationship("Account", secondary="account_transaction_association", back_populates="transactions")

class AccountTransactionAssociation(Base):
    __tablename__ = 'account_transaction_association'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    transaction_id = Column(Integer, ForeignKey('transaction.id'), primary_key=True)
    account = relationship("Account", backref="account_transactions")
    transaction = relationship("Transaction", backref="transaction_accounts")