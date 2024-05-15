import pytest
from database.Custom.model import Base, Account, Transaction
from unittest.mock import patch

# def session(engine, tables):
#     # Créez une mock session utilisant UnifiedAlchemyMagicMock
#     session = UnifiedAlchemyMagicMock()
#     yield session
#     session.rollback()
class TestDeposit:

    def test_deposit(self):
        account = Account.create_account(session, 0.0)
        self.deposit = Transaction.deposit(session, 50, account)

        assert Account.balance == 50.0
    def test_deposit_amount_null(self):
        account = Account.create_account(session, 50.0)
        self.deposit = Transaction.deposit(session, 0, account)

        assert Account.balance == 50.0

    def test_deposit_amount_negatif(self):
        account = Account.create_account(session, 50.0)
        self.deposit = Transaction.deposit(session, -50.0, account)

        assert Account.balance == 50.0

class TestWithdraw:
    def test_withdraw(self):
        account = Account.create_account(session, 100.0)
        self.withdraw = Transaction.withdraw(session, 50.0, account)

        assert account == True
        assert account(Account.balance) == 50.0

    def test_withdraw__amount_null(self):
        account = Account.create_account(session, 50.0)
        self.withdraw = Transaction.withdraw(session, 0, account)

        assert account == True
        assert account(Account.balance) == 50.0

    def test_withdraw_amount_negatif(self):
        account = Account.create_account(session, 50.0)
        self.withdraw = Transaction.withdraw(session, -50.0, account)

        assert account == True
        assert account(Account.balance) == 50.0

    def test_withdraw_balance_null(self):
        account = Account.create_account(session, 0.0)
        self.withdraw = Transaction.withdraw(session, 50.0, account)

        assert account == True
        assert account(Account.balance) == 0.0

    def test_withdraw_balance_negatif(self):
        account = Account.create_account(session, 50.0)
        self.withdraw = Transaction.withdraw(session, 100.0, account)

        assert account == True
        assert account(Account.balance) == 50.0

    def test_withdraw_balance_negatif_debt(self):
        account = Account.create_account(session, 50.0)
        self.withdraw = Transaction.withdraw(session, -100.0, account)

        assert account == True
        assert account(Account.balance) == 50.0

class TestTransfer:

    def test_transfer(self):
        account_source = Account.create_account(session, 1000.0)
        account_target = Account.create_account(session, 0.0)
        self.transfer = Transaction.transfer(session, -100.0, account_source, account_target)

        assert account_source == True
        assert account_target == True
        assert account_source(Account.balance) == 0.0 and account_target(Account.balance) == 1000
    
