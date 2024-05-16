import pytest
from database.Custom import model as models


def test_deposit_simple(session, account_factory):
    account = account_factory(100)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    deposit_amount = 50.0

    transaction = models.Transaction()
    transaction.deposit(session, account, deposit_amount)

    assert account.balance == initial_balance + deposit_amount
    assert transaction.type == "Deposit"
    assert len(account.transactions) == initial_transaction_count + 1

def test_deposit_negative_amount(session, account_factory):
    account = account_factory(100)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    deposit_amount = -50.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.deposit(session, account, deposit_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count

def test_deposit_null_amount(session, account_factory):
    account = account_factory(100)
    initial_balance = account.balance
    initial_transaction_count = len(account.transactions)
    deposit_amount = 0.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.deposit(session, account, deposit_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count