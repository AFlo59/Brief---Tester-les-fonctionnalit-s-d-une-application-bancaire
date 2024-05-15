Readme - Bank Account Management Introduction

This project aims to develop a bank account management application using object-oriented programming principles. The application will handle common banking operations such as account creation, deposit, withdrawal, money transfer, and balance inquiry. The main objective is to test the functionalities of this application using pytest and set up a CI/CD pipeline using GitHub Actions. Core Features

The main features of the application include:

Account creation (create_account)
Money deposit (deposit)
Money withdrawal (withdraw)
Money transfer (transfer)
Balance inquiry (get_balance)

The code is structured into two main classes: Account and Transaction, implemented in the Python file bank.py using object-oriented programming. Database Initialization

The database is simulated using sqlalchemy. The database schema consists of two tables: Accounts and Transactions. The purpose of adding the database is to practice mocking to avoid polluting the production database with tests. Database manipulation is done using the mock-alchemy package. Testing with Pytest

Tests are conducted in the test_bank.py file using pytest. The different functionalities of the application are tested with various scenarios and parameters using @pytest.mark.parametrize. Some tests requiring a database connection are marked with @pytest.mark.database. Non-essential or temporary tests are skipped using @pytest.mark.skip, and tests expected to fail under certain conditions are identified with @pytest.mark.xfail. CI/CD Pipeline

A CI/CD pipeline is set up using GitHub Actions. The pipeline automatically runs tests with every change made to the repository. The main branch (main) is protected so that any pull request is automatically rejected if tests do not pass. Project Structure

bank.py: Contains the logic of the bank account management application.
init_db.py: Initializes the connection to the database and creates necessary tables.
example_app.py: Provides an example scenario using the defined operations.
test_bank.py: Test file to validate the functionalities of the application.
conftest.py: Contains various fixtures used in the tests.

Conclusion

This project provides a practical opportunity to develop and test a bank account management application using object-oriented programming concepts, pytest for testing, and GitHub Actions for continuous integration and continuous deployment.