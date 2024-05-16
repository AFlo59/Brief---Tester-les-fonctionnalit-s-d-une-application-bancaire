import pytest
from database.Custom import model as models


def test_transfer_normal(session, account_factory):
    initial_balance_source = 100.0
    initial_balance_target = 50.0
    account_source = account_factory(initial_balance=initial_balance_source)
    account_target = account_factory(initial_balance=initial_balance_target)
    initial_transaction_count_source = len(account_source.transactions)
    initial_transaction_count_target = len(account_target.transactions)
    transfer_amount = 50.0

    transaction = models.Transaction()
    withdrawal, deposit = transaction.transfer(session, account_source, account_target, transfer_amount)

    assert account_source.balance == initial_balance_source - transfer_amount
    assert account_target.balance == initial_balance_target + transfer_amount
    assert withdrawal.type == "Withdraw"
    assert deposit.type == "Deposit"
    assert len(account_source.transactions) == initial_transaction_count_source + 1
    assert len(account_target.transactions) == initial_transaction_count_target + 1

def test_transfer_insufficient_funds(session, account_factory):
    initial_balance_source = 100.0
    initial_balance_target = 50.0
    account_source = account_factory(initial_balance=initial_balance_source)
    account_target = account_factory(initial_balance=initial_balance_target)
    initial_transaction_count_source = len(account_source.transactions)
    initial_transaction_count_target = len(account_target.transactions)
    transfer_amount = 200.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.transfer(session, account_source, account_target, transfer_amount)

    assert account_source.balance == initial_balance_source
    assert account_target.balance == initial_balance_target
    assert len(account_source.transactions) == initial_transaction_count_source
    assert len(account_target.transactions) == initial_transaction_count_target

def test_transfer_negative_amount(session, account_factory):
    initial_balance_source = 100.0
    initial_balance_target = 50.0
    account_source = account_factory(initial_balance=initial_balance_source)
    account_target = account_factory(initial_balance=initial_balance_target)
    initial_transaction_count_source = len(account_source.transactions)
    initial_transaction_count_target = len(account_target.transactions)
    transfer_amount = -50.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.transfer(session, account_source, account_target, transfer_amount)

    assert account_source.balance == initial_balance_source
    assert account_target.balance == initial_balance_target
    assert len(account_source.transactions) == initial_transaction_count_source
    assert len(account_target.transactions) == initial_transaction_count_target

def test_transfer_zero_amount(session, account_factory):
    initial_balance_source = 100.0
    initial_balance_target = 50.0
    account_source = account_factory(initial_balance=initial_balance_source)
    account_target = account_factory(initial_balance=initial_balance_target)
    initial_transaction_count_source = len(account_source.transactions)
    initial_transaction_count_target = len(account_target.transactions)
    transfer_amount = 0.0

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.transfer(session, account_source, account_target, transfer_amount)

    assert account_source.balance == initial_balance_source
    assert account_target.balance == initial_balance_target
    assert len(account_source.transactions) == initial_transaction_count_source
    assert len(account_target.transactions) == initial_transaction_count_target


