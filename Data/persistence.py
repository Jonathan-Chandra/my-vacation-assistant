import sqlite3
from sqlite3 import Error
import sql_scripts

DATABASE_NAME='database.sqlite3'

def create_connection(database_name: str):
  """
  Creates a database connection to the SQLite database passed
  :param database_name: database name
  :return: connection object or none
  """
  connection = None
  try:
    connection = sqlite3.connect(database_name)
    return connection
  except Error as e:
    print(e)

  return connection

  def create_table(connection, sql_script):
    """
    Creates a sql table within the connected database passed
    :param connection: connection object
    :param sql_script: sql script that contains the table creation
    :return: none
    """
    try:
      cursor = connection.cursor()
      cursor.execute(sql_script)
    except Error as e:
      print(e)

def main():
  return 0

if __name__ == '__main__':
  main()
  