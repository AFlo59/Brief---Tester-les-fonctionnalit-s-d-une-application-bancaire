import pytest
from database.Custom.model import *

@pytest.fixture
def account_factory():
    def create_account():
        return Account()
    return create_account

@pytest.fixture
def deposit_factory():
    def deposit():
        return Transaction()
    return deposit

@pytest.fixture
def withdraw_factory():
    def withdraw():
        return Transaction()
    return withdraw

@pytest.fixture
def transfer_factory():
    def transfer():
        return Transaction()
    return transfer