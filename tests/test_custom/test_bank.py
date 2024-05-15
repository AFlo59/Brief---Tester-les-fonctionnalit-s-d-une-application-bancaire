import pytest
from database.Custom.model import Base, Account, Transaction
from unittest.mock import patch
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

class TestDeposit:
    
    def test_deposit(account_factory, my_session):
        with my_session:
            account = account_factory()
            account.deposit(50.0)
            # Checks
            # 1. Verify that current balance is updated
            assert account.balance == 50.0
            # 2. Verify a new transaction has been correctly added with 'deposit' type
            assert my_session.query(Transaction).count() == 1
            assert (my_session
                    .query(Transaction)
                    .filter(Transaction.transaction_id == 1)
                    .one()
                    ).type == "Deposit"
            # 3. Verify the new transaction's timestamp has been correctly added
            assert (my_session
                .query(Transaction)
                .filter(Transaction.transaction_id == 1)
                .one()
                ).timestamp
            # 4. Verify session.commit has been called.
            assert my_session.commit.call_count == 2
            # my_session.commit.assert_any_call()
        # The non-commented is better as `session.commit` is also called within account_factory
        

#     def test_deposit_amount_null(self, session):
#         account = Account.create_account(session, 50.0)
#         self.deposit = Transaction.deposit(session, 0, account)

#         assert Account.balance == 50.0

#     def test_deposit_amount_negatif(self, session):
#         account = Account.create_account(session, 50.0)
#         self.deposit = Transaction.deposit(session, -50.0, account)

#         assert Account.balance == 50.0

# class TestWithdraw:
#     def test_withdraw(self, session):
#         account = Account.create_account(session, 100.0)
#         self.withdraw = Transaction.withdraw(session, 50.0, account)

#         assert account == True
#         assert account(Account.balance) == 50.0

#     def test_withdraw__amount_null(self, session):
#         account = Account.create_account(session, 50.0)
#         self.withdraw = Transaction.withdraw(session, 0, account)

#         assert account == True
#         assert account(Account.balance) == 50.0

#     def test_withdraw_amount_negatif(self, session):
#         account = Account.create_account(session, 50.0)
#         self.withdraw = Transaction.withdraw(session, -50.0, account)

#         assert account == True
#         assert account(Account.balance) == 50.0

#     def test_withdraw_balance_null(self, session):
#         account = Account.create_account(session, 0.0)
#         self.withdraw = Transaction.withdraw(session, 50.0, account)

#         assert account == True
#         assert account(Account.balance) == 0.0

#     def test_withdraw_balance_negatif(self, session):
#         account = Account.create_account(session, 50.0)
#         self.withdraw = Transaction.withdraw(session, 100.0, account)

#         assert account == True
#         assert account(Account.balance) == 50.0

#     def test_withdraw_balance_negatif_debt(self, session):
#         account = Account.create_account(session, 50.0)
#         self.withdraw = Transaction.withdraw(session, -100.0, account)

#         assert account == True
#         assert account(Account.balance) == 50.0

# class TestTransfer:

#     def test_transfer(self, session):
#         account_source = Account.create_account(session, 1000.0)
#         account_target = Account.create_account(session, 0.0)
#         self.transfer = Transaction.transfer(session, 1000.0, account_source, account_target)

#         assert account_source == True
#         assert account_target == True
#         assert account_source(Account.balance) == 0.0 and account_target(Account.balance) == 1000.0

#     def test_transfer(self, session):
#         account_source = Account.create_account(session, 1000.0)
#         account_target = Account.create_account(session, 0.0)
#         self.transfer = Transaction.transfer(session, 1000.0, account_source, account_target)

#         assert account_source == True
#         assert account_target == True
#         assert account_source(Account.balance) == 0.0 and account_target(Account.balance) == 1000.0
    
