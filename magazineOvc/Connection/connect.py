from peewee import *

def connect():
    mysql_db = MySQLDatabase(
        'OvcD1234_hranenie',
        user ='OvcD1234_adMount',
        password='111111',
        host='10.11.13.118',
        port=3306)
    return mysql_db

if __name__ == "__main__":
    connect().connect()