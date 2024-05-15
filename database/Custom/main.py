from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Account, Transaction

from insert import insert_data
from update import update_data

def create_database(engine):
    try:
        Base.metadata.create_all(engine)
        print("Base de données créée avec succès.")
    except Exception as e:
        print("Erreur lors de la création de la base de données:", e)


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