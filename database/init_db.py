from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship
from datetime import datetime

# init_db.py ###
Base = declarative_base()
engine = create_engine('sqlite:///Bank.db')
Session = scoped_session(sessionmaker(bind=engine))
# Base.metadata.create_all(engine)
######