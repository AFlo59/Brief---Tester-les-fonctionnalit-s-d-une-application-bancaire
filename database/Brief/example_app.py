from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship


from bank import Account
from init_db import Base, engine, Session
 

def main():
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
	
if __name__ == "**main**":
	main()