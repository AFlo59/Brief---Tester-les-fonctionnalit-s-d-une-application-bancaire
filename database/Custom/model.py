from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

account_transaction_association = Table(
    'account_transaction_association',
    Base.metadata,
    Column('account_id', Integer, ForeignKey('account.id')),
    Column('transaction_id', Integer, ForeignKey('transaction.id'))
)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    transactions = relationship('Transaction', secondary=account_transaction_association, back_populates='accounts', overlaps="transaction_accounts")

    def __init__(self, balance=0.0):
        self.balance = balance

    def create_account(self, session, initial_balance=None):
        if initial_balance is not None:
            self.balance = initial_balance
        else:
            self.balance = 0.0
        session.add(self)
        session.commit()

    def get_balance(self):
        return self.balance
    
    def __repr__(self):
        return f"Account(id={self.id}, balance={self.balance:.2f})"


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    accounts = relationship('Account', secondary=account_transaction_association, back_populates='transactions', overlaps="accounts")

    def __init__(self, session=None):
        self.session = session

    def deposit(self, amount, account):
        if amount <= 0:
            raise ValueError("Deposit amount must be superior to zero.")
        
        self.amount = amount
        self.type = "Deposit"
        self.timestamp = datetime.now()
        self.accounts.append(account)

        self.session.add(self)
        account.balance += amount
        self.session.add(account)

        self.session.commit()
        return self  


    def withdraw(self, amount, account):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be superior to zero.")
        
        self.amount = amount
        self.type = "Withdraw"
        self.timestamp = datetime.now()
        self.accounts.append(account)

        if self.amount > account.balance:
            raise ValueError("Insufficient funds.")
        
        self.session.add(self)
        account.balance -= amount
        self.session.add(account)

        self.session.commit()
        return self


    def transfer(self, amount, account_source, account_target):
        if account_source == account_target:
            raise ValueError("Le compte cible doit être différent du compte source.")
        
        withdrawal = Transaction(session=self.session)
        withdrawal.withdraw(amount, account_source)
    
        if withdrawal.amount != amount:
            raise ValueError("Withdrawal failed.")
        
        deposit = Transaction(session=self.session)
        deposit.deposit(amount, account_target)
            
        self.session.add(withdrawal)
        self.session.add(deposit)

        self.session.commit()
        return withdrawal, deposit
