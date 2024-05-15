import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from database.Custom.model import *

@pytest.fixture
def my_session(engine, tables):

    session = UnifiedAlchemyMagicMock()
    yield session
    session.rollback()

@pytest.fixture
def account_factory(my_session):
    def create_account(initial_balance):
        new_account = Account(session = my_session,balance=initial_balance)
        my_session.add(new_account)
        my_session.commit()
        return new_account
    return create_account

