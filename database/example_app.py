from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship


from bank import Account
from init_db import Base, engine, Session
 

def main():
	session = Session()

	account1 = Account(id=1,balance=100)
	session.add(account1)
	account2 = Account(id=2,balance=50)
	session.add(account2)
	session.commit()
	
	
	session.close()
	
if __name__ == "**main**":
	main()