"""
autor: Martin Pommerening
"""

#%%
import matplotlib.pyplot as plt
import databaseConnection

class DatabaseCreator:
    database = None

    def __init__(self, adress, username, userpassword, databaseName):
        con = databaseConnection.DatabaseConnection(adress, username, userpassword, databaseName).connect()
        print(adress, username, userpassword, databaseName)


    def createDatabase(self):
        print("try to create an new Database")

    def updateDatabase(self):
        if self.database is not {} and not None:
            print("update an existing Database")
        else:
            raise Exception

    def getDataFromDatabase(self):
        print("getting Data from Database")

    def deleteDatabase(self):
        print("delete Data from Database")
