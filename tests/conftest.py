import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.Custom import model as models


@pytest.fixture(scope='function')
def session():
    engine = create_engine('sqlite:///:memory:')
    models.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture()
def account_factory(session):
    def create_account(initial_balance=0):
        if initial_balance is None:
            initial_balance = 0
        new_account = models.Account(balance=initial_balance)
        session.add(new_account)
        session.commit()
        return new_account
    return create_account