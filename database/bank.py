from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

from init_db import Base, engine, Session

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0)
    transactions = relationship("Transaction", back_populates="account")

    def __init__(self, balance):
        self.balance = balance
    
    def create_account(self, balance):
        pass
        #Function in Account to create new account with initial balance if value exist or par default 0
        # new_account = Account(balance)
        # session = Session()
        # session.add(new_account)
        # session.commit()

    def get_balance(self):
        #Function in Account to return the balance amount on your account
        # return self.balance
        pass

    def __repr__(self):
	    return f"<Account(id='{self.id}', balance='{self.balance}')>"
    

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account", back_populates="transactions")
    
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type
    
    def deposit(self, amount):
        pass
        # if amount < 0:
        #     raise ValueError("Deposit amount must be superior to zero.")
        # self.type = "Deposit"
        # self.amount += self.account.balance
        # return self.account.balance
    
    def withdraw(self, amount):
        pass
        # if amount < 0:
        #     raise ValueError("Withdrawal amount must be superior to zero.")
        # if amount > self.balance:
        #     raise ValueError("Insufficient funds.")
        # self.type = "Withdraw"
        # self.amount -= self.account.balance
        # return self.account.balance

    def transfer(self):
        pass
        # if amount < 0:
        #     raise ValueError("Transfer amount must be positive")
        

class AccountTransactionAssociation(Base):
    __tablename__ = 'account_transaction_association'
    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    transaction_id = Column(Integer, ForeignKey('transaction.id'), primary_key=True)
    account = relationship("Account", back_populates="transactions")
    transaction = relationship("Transaction", back_populates="account")


Base.metadata.create_all(engine)