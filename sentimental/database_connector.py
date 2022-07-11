import mysql.connector


class Connection(mysql.connector.MySQLConnection):
    """Connection to MySQL server."""

    def connect(_host="localhost", _user='root', password=None):
        if password:
            connection = mysql.connector.connect(host=_host,
                                                 user=_user,
                                                 passwd=password,
                                                 database="sentimental")
            return connection
        else:
            print(
                'Must include MySQL Database password in database_connector.Connection.connect() function.')
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


if __name__ == '__main__':
    database = Database()
    data = database.get_all(table_name='sp500')
    [print(item) for item in data]
