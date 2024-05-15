from model import Base, Account, Transaction

def update_data(session):
    try:
        account1 = session.query(Account).filter(Account.id == 1).first()
        account2 = session.query(Account).filter(Account.id == 2).first()
        if account1:
            transaction = Transaction()
            transaction.transfer(session, amount=50, account_source=account1, account_target=account2)
        
        session.commit()
        print("Données modifiés avec succès.")
    except Exception as e:
        session.rollback()
        print("Erreur lors de la modification des données:", e)