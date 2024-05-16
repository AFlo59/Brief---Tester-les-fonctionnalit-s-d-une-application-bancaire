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
        new_account = models.Account(balance=initial_balance)
        session.add(new_account)
        session.commit()
        return new_account
    return create_account


class TestDeposit:
    def test_deposit_normal(self, session, account_factory):
        account = account_factory()
        transaction = models.Transaction()
        transaction.deposit(session, 50, account)
        
        assert account.balance == 50
        assert transaction.type == "Deposit"

    def test_deposit_zero(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        with pytest.raises(ValueError, match="Deposit amount must be greater than zero."):
            transaction.deposit(session, 0, account)

            assert account.balance == 50
        

    def test_deposit_negative(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        with pytest.raises(ValueError, match="Deposit amount must be greater than zero."):
            transaction.deposit(session, -10, account)

            assert account.balance == 50
        

