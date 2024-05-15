from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)