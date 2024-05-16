from mock_alchemy.mocking import UnifiedAlchemyMagicMock
import pytest

from database.Brief.bank import Account as BriefAccount

from database.Custom.model import Account as CustomAccount


@pytest.fixture
def my_brief_session():
    session = UnifiedAlchemyMagicMock()
    yield session
    session.rollback()

@pytest.fixture
def account_brief_factory(my_brief_session):
    def create_account(id, balance = 0):
        new_account = BriefAccount(
            session = my_brief_session,
            id = id,
            balance = balance
        )
        my_brief_session.add(new_account)
        my_brief_session.commit()
        return new_account
    return create_account

@pytest.fixture
def account_custom_factory(session):
    def create_account(initial_balance = 0):
        new_account = CustomAccount(
            balance = initial_balance
        )
        session.add(new_account)
        session.commit()
        return new_account
    return create_account