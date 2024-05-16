import pytest
from database.Custom import model as models


def test_withdraw_normal(session, account_factory):
    account = account_factory(100.0)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = 50.0

    transaction = models.Transaction()
    transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance - withdrawal_amount
    assert transaction.type == "Withdraw"
    assert len(account.transactions) == initial_transaction_count + 1

def test_withdraw_insufficient_funds(session, account_factory):
    account = account_factory(100.0)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = 500.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count == 0

def test_withdraw_negative_amount(session, account_factory):
    account = account_factory(100.0)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = -50.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count == 0

def test_withdraw_zero_amount(session, account_factory):
    account = account_factory(100.0)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = 0.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count == 0