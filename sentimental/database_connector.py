"""Database model."""

from mysql.connector import connect
from mysql.connector.connection import MySQLCursor


class Database:
    """Generic Database object."""

    def __init__(self, name: str, host: str):
        """Initialise Database."""
        self.name = name
        self.host = host


class MySQLDatabase(Database):
    """MySQLDatabase object."""

    def __init__(self, name: str, host: str, username: str, password: str) -> None:
        """Initialise MySQLDatabase."""
        super().__init__(name, host)
        self.connection = connect(host=host, user=username, passwd=password, database=name)

    def get_all(self, table_name: str, column: str = "*", dictionary: bool = True) -> MySQLCursor:
        """Get all entries from the specified column in a specified table."""
        cursor = self.connection.cursor(dictionary=dictionary)
        cursor.execute(f"SELECT {column} FROM {table_name}")
        return cursor
