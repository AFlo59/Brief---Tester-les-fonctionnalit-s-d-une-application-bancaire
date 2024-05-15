import pytest
from database.Custom.model import *

@pytest.fixture
def account_factory():
    def create_account(initial_balance):
        return Account(balance=initial_balance)
    return create_account

@pytest.fixture
def deposit_factory():
    def deposit(amount, account):
        return Transaction(amount=amount, account=account)
    return deposit

@pytest.fixture
def withdraw_factory():
    def withdraw(amount, account):
        return Transaction(amount=amount, account=account)
    return withdraw

@pytest.fixture
def transfer_factory():
    def transfer( amount, account_source, account_target):
        return Transaction(amount=amount, account_source=account_source, account_target=account_target)
    return transfer