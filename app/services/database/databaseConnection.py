"""
autor: Martin Pommerening
"""

class DatabaseConnection:

    def __init__(self, url, username, password, dbname):
        __url = url
        __username = username
        __userpassword = password
        __dbName = dbname

    @staticmethod
    def connect():
        return object
        print("try to connect to given url")