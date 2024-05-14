import os
from dotenv import load_dotenv
import sqlite3


load_dotenv()

def connect_to_database():
    return sqlite3.connect('Bank.db')