from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float, Table
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

from init_db import *

account_transaction_association = Table(
    'account_transaction_association',
    Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('transaction_id', Integer, ForeignKey('transaction.id'))
)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    balance = Column(Integer)
    transactions = relationship('Transaction', secondary=account_transaction_association, back_populates='accounts', overlaps="transaction_accounts")

    def create_account(self, session, initial_balance=None):
        if initial_balance is not None:
            self.balance = initial_balance
        else:
            self.balance = 0.0
        session.add(self)
        session.commit()

    def get_balance(self):
        return self.balance


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    accounts = relationship('Account', secondary=account_transaction_association, back_populates='transactions', overlaps="accounts")

    def deposit(self, session, amount, account):
        self.amount = amount
        self.type = "Deposit"
        self.timestamp = datetime.now()
        self.accounts.append(account)

        session.add(self)
        session.commit()

    def withdraw(self, session, amount, account):
        self.amount = amount
        self.type = "Withdraw"
        self.timestamp = datetime.now()
        self.accounts.append(account)

        session.add(self)
        session.commit()

    def transfer(self, session, amount, account_source, account_target):
        if account_source == account_target:
            raise ValueError("Le compte cible doit être différent du compte source.")
        
        withdrawal = Transaction(amount=-amount, type="Withdraw")
        withdrawal.accounts.append(account_source)
        session.add(withdrawal)

        account_source.balance -= amount
        session.add(account_source)
        
        deposit = Transaction(amount=amount, type="Deposit")
        deposit.accounts.append(account_target)
        session.add(deposit)

        account_target.balance += amount
        session.add(account_target)
        
        session.commit()

