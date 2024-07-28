""" Configuration Test Module should offer resources  to unit test execution """
import os
import pytest


@pytest.fixture
def database_connection_parameters():
    """ Function should offer necessary env var to unit test """
    os.environ["DB_DIALECT"] = "mysql+pymysql"
    os.environ["DB_USER_NAME"] = "username"
    os.environ["DB_USER_PWD"] = "userpass"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_NAME"] = "clean_database"
