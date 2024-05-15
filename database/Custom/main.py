from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Account, Transaction

def create_database(engine):
    try:
        Base.metadata.create_all(engine)
        print("Base de données créée avec succès.")
    except Exception as e:
        print("Erreur lors de la création de la base de données:", e)

def insert_data(session):
    try:
        account1 = Account(balance=100)
        account2 = Account(balance=50)
        account3 = Account(balance=0)

        session.add(account1)
        session.add(account2)
        session.add(account3)
        
        session.commit()
        print("Données insérées avec succès.")
    except Exception as e:
        session.rollback()
        print("Erreur lors de l'insertion des données:", e)

def main():
    try:
        engine = create_engine('sqlite:///Bank.db')
        create_database(engine)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        
        insert_data(session)

        account1 = session.query(Account).first()
        if account1:
            account1.create_account(session, initial_balance=200)
            transaction = Transaction()
            transaction.deposit(session, amount=50, account=account1)
        
        session.close()
    except Exception as e:
        print("Une erreur s'est produite:", e)

if __name__ == "__main__":
    main()