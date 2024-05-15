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

def main():
    try:
        engine = create_engine('sqlite:///Bank.db')
        create_database(engine)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        
        insert_data(session)
        update_data(session)

        session.close()
    except Exception as e:
        print("Une erreur s'est produite:", e)

if __name__ == "__main__":
    main()