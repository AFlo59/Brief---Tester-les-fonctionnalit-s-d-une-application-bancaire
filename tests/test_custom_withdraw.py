import pytest
from database.Custom import model as models


def test_withdraw_simple(session, account_factory):
    initial_balance = 100.0
    account = account_factory(initial_balance=initial_balance)
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = 50.0

    transaction = models.Transaction()
    transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance - withdrawal_amount
    assert transaction.type == "Withdraw"
    assert len(account.transactions) == initial_transaction_count + 1

def test_withdraw_negative_amount(session, account_factory):
    initial_balance = 100.0
    account = account_factory(initial_balance=initial_balance)
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = -50.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count

def test_withdraw_null_amount(session, account_factory):
    initial_balance = 100.0
    account = account_factory(initial_balance=initial_balance)
    initial_transaction_count = len(account.transactions)
    withdrawal_amount = 0.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance == initial_balance
    assert len(account.transactions) == initial_transaction_count