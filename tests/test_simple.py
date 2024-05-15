import pytest
from database.custom.model import Account, Transaction

def test_deposit(session, account_factory):
    account = account_factory()
    transaction = Transaction(session=session)
    transaction.deposit(amount=100, account=account)
    assert account.balance == 100

def test_withdraw(session, account_factory):
    account = account_factory(balance=100)
    transaction = Transaction(session=session)
    transaction.withdraw(amount=50, account=account)
    assert account.balance == 50

def test_transfer(session, account_factory):
    account_source = account_factory(balance=100)
    account_target = account_factory()
    
    transaction = Transaction(session=session)
    withdrawal, deposit = transaction.transfer(amount=50, account_source=account_source, account_target=account_target)
    
    assert withdrawal.amount == 50
    assert deposit.amount == 50
