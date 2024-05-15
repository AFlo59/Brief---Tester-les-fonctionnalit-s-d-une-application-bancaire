import pytest
from database.Custom.model import *


def test_deposit(account_factory, deposit_factory):
    account = account_factory(0)
    deposit = deposit_factory(50, account)

    account.deposit(deposit)
    assert account.get_balance() == 50

def test_deposit_amount_null(account_factory, deposit_factory):
    account = account_factory(50)
    deposit = deposit_factory(0, account)

    account.deposit(deposit)
    assert account.get_balance() == 50

def test_deposit_amount_negatif(account_factory, deposit_factory):
    account = account_factory(50)
    deposit = deposit_factory(-50, account)

    account.deposit(deposit)
    assert account.get_balance() == 50

def test_withdraw(account_factory, withdraw_factory):
    account = account_factory(100)
    withdraw = withdraw_factory(50, account)

    account.withdraw(withdraw)
    assert account.get_balance() == 50

def test_withdraw__amount_null(account_factory, withdraw_factory):
    account = account_factory(100)
    withdraw = withdraw_factory(0, account)

    account.withdraw(withdraw)
    assert account.get_balance() == 100

def test_withdraw_amount_negatif(account_factory, withdraw_factory):
    account = account_factory(100)
    withdraw = withdraw_factory(-50, account)

    account.withdraw(withdraw)
    assert account.get_balance() == 100

def test_transfer(account_factory, transfer_factory):
    account_source = account_factory(1000)
    account_target = account_factory(0.0)
    transfer = transfer_factory(1000, account_source, account_target)

    transfer.transfer(transfer)
    assert account_source.get_balance() == 0.0 and account_target.get_balance() == 1000
    


