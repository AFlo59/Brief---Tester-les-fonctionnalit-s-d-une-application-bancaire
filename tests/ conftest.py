import pytest
from database.custom.model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy_mock.mocking import UnifiedAlchemyMagicMock

# Fixture pour créer la session
@pytest.fixture(scope="function")
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()

@pytest.fixture(scope="function")
def account_factory(session):
    def create_account(balance=0.0):
        account = Account(balance=balance)
        session.add(account)
        session.commit()
        return account
    return create_account
