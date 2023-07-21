import mysql.connector


class Connection(mysql.connector.MySQLConnection):
    """Connection to MySQL server."""

    def connect(host="localhost", user=None, password=None):
        if password and username:
            connection = mysql.connector.connect(host=host,
                                                 user=user,
                                                 passwd=password,
                                                 database="sentimental")
            return connection
        else:
            print(
                'Must include MySQL Database username and password in database_connector.Connection.connect() method.')
            return False


class Database:
    """Base database object."""

    def __init__(self, name='sentimental'):
        self.name = name
        self.connection = Connection.connect()

    def get_all(self, table_name, column='*', dictionary=True):
        cursor = self.connection.cursor(dictionary=dictionary)
        cursor.execute(f"SELECT {column} FROM {table_name}")
        return cursor
