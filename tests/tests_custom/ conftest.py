import pytest
from database.Custom.model import *

@pytest.fixture
def account_factory():
    def create_account(session,initial_balance):
        return Account()
    return create_account

@pytest.fixture
def transaction_factory():
    def create_transaction(session, type, amount, account):
        return Transaction()
    return create_transaction