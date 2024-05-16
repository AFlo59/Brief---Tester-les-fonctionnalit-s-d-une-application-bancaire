import pytest
from database.Custom import model as models

def test_get_balance_initial(session, account_factory):
    account = account_factory()
    initial_balance = account.balance

    assert account.balance != None
    assert initial_balance == account.get_balance()

def test_get_balance_after_deposit(session, account_factory):
    account = account_factory()
    initial_balance = account.balance
    deposit_amount = 100

    transaction = models.Transaction()
    transaction.deposit(session, account, deposit_amount)

    assert account.balance != None
    assert account.get_balance() != initial_balance
    assert account.get_balance() == initial_balance + deposit_amount

def test_get_balance_after_withdrawal(session, account_factory):
    account = account_factory(100)
    initial_balance = account.balance
    withdrawal_amount = 100

    transaction = models.Transaction()
    transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance != None
    assert account.get_balance() != initial_balance
    assert account.get_balance() == initial_balance - withdrawal_amount

def test_get_balance_after_failed_withdrawal(session, account_factory):
    account = account_factory()
    initial_balance = account.balance
    withdrawal_amount = 100

    with pytest.raises(ValueError):
        transaction = models.Transaction()
        transaction.withdraw(session, account, withdrawal_amount)

    assert account.balance != None
    assert account.get_balance() == initial_balance

def test_get_balance_after_transfer(session, account_factory):
    account_source = account_factory(1000)
    account_source_initial_balance = account_source.balance

    account_target = account_factory()
    account_target_initial_balance = account_target.balance

    transfer_amount = 750

    transaction = models.Transaction()
    transaction.transfer(session, account_source, account_target, transfer_amount)

    assert account_source.balance != None
    assert account_source_initial_balance > transfer_amount
    assert account_source.get_balance() == account_source_initial_balance - transfer_amount
    assert account_target.get_balance() == account_target_initial_balance + transfer_amount
