from model import Transaction, Account

def update_data(session):
    try:
        account1 = session.query(Account).filter(Account.id == 1).first()
        account2 = session.query(Account).filter(Account.id == 2).first()
        if account1 and account2:
            transaction = Transaction(session=session)
            transaction.transfer(amount=50, account_source=account1, account_target=account2)

        account3 = session.query(Account).filter(Account.id == 3).first()
        if account3:
            transaction = Transaction(session=session)
            transaction.deposit(amount=99.99, account=account3)
        
        session.commit()
        print("Données modifiées avec succès.")
    except Exception as e:
        session.rollback()
        print("Erreur lors de la modification des données:", e)
