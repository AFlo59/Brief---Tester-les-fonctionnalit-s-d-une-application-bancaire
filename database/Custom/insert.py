from model import Base, Account, Transaction

def insert_data(session):
    try:
        # account1 = Account()
        # account1.create_account(session, initial_balance=100)
        # account2 = Account()
        # account2.create_account(session, initial_balance=50)
        # account3 = Account()
        # account3.create_account(session)
        # account4 = Account()
        # account4.create_account(session, initial_balance=199.99)

        # session.add(account4)
        # session.add(account1)
        # session.add(account2)
        # session.add(account3)
        
        session.commit()
        print("Données insérées avec succès.")
    except Exception as e:
        session.rollback()
        print("Erreur lors de l'insertion des données:", e)