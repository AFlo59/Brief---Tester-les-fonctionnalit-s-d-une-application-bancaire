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
        print("Initial Balance:", initial_balance)
        new_account = models.Account(balance=initial_balance)
        session.add(new_account)
        session.commit()
        return new_account
    return create_account



class TestDeposit:
    def test_deposit_normal(self, session, account_factory):
        account = account_factory(50)
        solde = account.balance

        transaction = models.Transaction()
        transaction.deposit(session, 50, account)
        montant = transaction.amount
        
        assert account.balance == solde + montant
        assert transaction.type == "Deposit"

    def test_deposit_zero(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()

        solde = account.balance

        assert account.balance == solde
        with pytest.raises(ValueError, match="Deposit amount must be greater than zero."):
            transaction.deposit(session, 0, account)
        

    def test_deposit_negative(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        solde = account.balance

        assert account.balance == solde
        with pytest.raises(ValueError, match="Deposit amount must be greater than zero."):
            transaction.deposit(session, -50, account)
        
class TestWithdraw:
    def test_withdraw_normal(self, session, account_factory):
        account = account_factory(100)
        solde = account.balance

        transaction = models.Transaction()
        transaction.withdraw(session, 50, account)
        montant = transaction.amount
        
        assert account.balance == solde - montant
        assert transaction.type == "Withdraw"

    def test_withdraw_zero(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        solde = account.balance

        assert account.balance == solde
        with pytest.raises(ValueError, match="Withdrawal amount must be greater than zero."):
            transaction.withdraw(session, 0, account)

        
    def test_withdraw_negative(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        solde = account.balance

        assert account.balance == solde
        with pytest.raises(ValueError, match="Withdrawal amount must be greater than zero."):
            transaction.withdraw(session, -50, account)
    
    def test_withdraw_debt(self, session, account_factory):
        account = account_factory(50)
        transaction = models.Transaction()
        
        solde = account.balance

        assert account.balance == solde
        with pytest.raises(ValueError, match="Insufficient funds."):
            transaction.withdraw(session, 100, account)


class TestTransfer:
    def test_transfer_normal(self, session, account_factory):
        account1 = account_factory(1000)
        solde1 = account1.balance

        account2 = account_factory()
        solde2 = account2.balance

        transaction = models.Transaction()
        transaction.transfer(session, 1000, account_source=account1, account_target=account2)
        montant = transaction.amount

        assert account1.balance == solde1 - montant
        assert account2.balance == solde2 + montant
        # "Withdraw" "Deposit"

    def test_transfer_same_account(self, session, account_factory):
        account1 = account_factory(500)
        solde1 = account1.balance

        account2 = account1
        solde2 = account2.balance

        transaction = models.Transaction()
        
        assert account1.balance == solde1
        assert account2.balance == solde2
        with pytest.raises(ValueError, match="The target account must be different from the source account."):
            transaction.transfer(session, 1000, account_source=account1, account_target=account2)

    def test_transfer_debt(self, session, account_factory):
        account1 = account_factory(500)
        solde1 = account1.balance

        account2 = account_factory(0)
        solde2 = account2.balance

        transaction = models.Transaction()
        
        assert account1.balance == solde1
        assert account2.balance == solde2
        with pytest.raises(ValueError, match="Insufficient funds."):
            transaction.transfer(session, 1000, account_source=account1, account_target=account2)

    def test_transfer_zero(self, session, account_factory):
        account1 = account_factory(1000)
        solde1 = account1.balance

        account2 = account_factory(500)
        solde2 = account2.balance

        transaction = models.Transaction()
        
        assert account1.balance == solde1
        assert account2.balance == solde2
        with pytest.raises(ValueError, match="Transfer amount must be greater than zero."):
            transaction.transfer(session, 0, account_source=account1, account_target=account2)

    def test_transfer_zero(self, session, account_factory):
        account1 = account_factory(1000)
        solde1 = account1.balance

        account2 = account_factory(500)
        solde2 = account2.balance
        transaction = models.Transaction()
        
        assert account1.balance == solde1
        assert account2.balance == solde2
        with pytest.raises(ValueError, match="Transfer amount must be greater than zero."):
            transaction.transfer(session, -1000, account_source=account1, account_target=account2)