import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.Custom import model as models

# Define a fixture for the SQLAlchemy session
@pytest.fixture(scope='function')
def session():
    # Create an in-memory SQLite database for testing
    engine = create_engine('sqlite:///:memory:')
    models.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

class TestDeposit:
    def test_deposit_normal(self, session):
        account = models.Account()
        account.create_account(session)
        transaction = models.Transaction()
        transaction.deposit(session, 50, account)
        
        assert account.balance == 50
        assert transaction.type == "Deposit"

