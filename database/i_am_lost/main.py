from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Account, Transaction

def create_database(engine):
    try:
        Base.metadata.create_all(engine)
        print("Base de données créée avec succès.")
    except Exception as e:
        print("Erreur lors de la création de la base de données:", e)

def insert_data(engine):
    try:

        Session = sessionmaker(bind=engine)
        session = Session()  

        account1 = Account(balance=100)
        account2 = Account(balance=50)
        account3 = Account()
        session.add(account3)
        session.add(account1)
        session.add(account2)


        session.commit()
        session.close()

        print("Données insérées avec succès.")
    except Exception as e:
        print("Erreur lors de l'insertion des données:", e)

def main():
    try:

        engine = create_engine('sqlite:///Bank.db')
        create_database(engine)
        

        insert_data(engine)
        
    except Exception as e:
        print("Une erreur s'est produite:", e)

if __name__ == "__main__":
    main()
