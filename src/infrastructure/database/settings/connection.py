"""" Connection module should expose behaviors related to database connection """
import os

from sqlalchemy import create_engine, Engine


class DatabaseConnectionHandler:
    """"Database Connection Handler to manage connection"""

    def __init__(self) -> None:
        """ Create a valid connection string during instantiation object """
        database_dialect = os.getenv("DB_DIALECT")
        database_user_name = os.getenv("DB_USER_NAME")
        database_password = os.getenv("DB_USER_PWD")
        database_host = os.getenv("DB_HOST")
        database_port = os.getenv("DB_PORT")
        database_name = os.getenv("DB_NAME")
        self.__connection_string = (f"{database_dialect}://{database_user_name}:{database_password}@"
                                    f"{database_host}:{database_port}/{database_name}")
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self) -> Engine:
        """ Create a new engine object using constructed connection string"""
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self) -> Engine:
        """ Return valid engine object previously created """
        return self.__engine
