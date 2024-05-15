from model import Base, Account, Transaction

def insert_data(session):
    try:
        account1 = Account(id=1,balance=100)
        account2 = Account(id=2,balance=50)
        account3 = Account(id=3,balance=0)

        session.add(account1)
        session.add(account2)
        session.add(account3)
        
        session.commit()
        print("Données insérées avec succès.")
    except Exception as e:
        session.rollback()
        print("Erreur lors de l'insertion des données:", e)