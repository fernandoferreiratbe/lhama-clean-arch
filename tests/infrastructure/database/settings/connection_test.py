""" Database Connection Test Module"""
from sqlalchemy import Engine

from src.infrastructure.database.settings.connection import DatabaseConnectionHandler


def test_given_valid_parameters_when_create_connection_object_should_return_engine(
        database_connection_parameters
):  # pylint: disable=W0613
    """ Given valid parameters should return valida engine object"""
    database_connection_handle = DatabaseConnectionHandler()
    engine = database_connection_handle.get_engine()

    assert isinstance(engine, Engine)
