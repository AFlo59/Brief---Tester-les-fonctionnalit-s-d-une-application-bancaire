from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, Session
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
    balance = Column(Integer)
    transactions = relationship('Transaction', secondary=account_transaction_association, back_populates='accounts', overlaps="transaction_accounts")

    def create_account(self,Session, initial_balance=None):
        if initial_balance is not None:
            self.balance = initial_balance
        else:
            self.balance = 0.0
            Session.add(self)
            Session.commit()

    def get_balance(self):
        return self.balance


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    accounts = relationship('Account', secondary=account_transaction_association, back_populates='transactions', overlaps="accounts")

    def deposit(self, Session, amount):
        self.amount = amount
        self.type = "Deposit"
        self.timestamp = datetime.now()

        Session.add(self)
        Session.commit()

 

    def withdraw(self, Session, amount):
        self.amount = amount
        self.type = "Withdraw"
        self.timestamp = datetime.now()

        Session.add(self)
        Session.commit()

 

    def transfer(self, Session, amount, account_target):
        if account_target == self.accounts[0]:
            raise ValueError("Le compte cible doit être différent du compte source.")
        self.withdraw(amount)
        deposit_transaction = Transaction(amount=amount, type="Deposit")
        deposit_transaction.accounts.append(account_target)
        self.accounts[0].transactions.append(deposit_transaction)

        Session.add(self)
        Session.add(deposit_transaction)
        Session.commit()

