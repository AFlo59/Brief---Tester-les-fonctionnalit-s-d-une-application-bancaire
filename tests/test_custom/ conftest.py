import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.Custom.model import Base, Account, Transaction
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

 
@pytest.fixture(scope="function")
def session():
    session = UnifiedAlchemyMagicMock()
    yield session
    session.rollback()


@pytest.fixture(scope="function")
def account_factory(session):
    def create_account(initial_balance):
        account = Account(balance=initial_balance)
        session.add(account)
        session.commit()
        return account
    return create_account
