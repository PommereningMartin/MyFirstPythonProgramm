"""
autor: Martin Pommerening
"""
from services.database.databaseCreator import DatabaseCreator

def main():
    creator = DatabaseCreator("localhost:9090", "test", "testPw", "testDb")
    creator.createDatabase()
    creator.getDataFromDatabase()
    creator.updateDatabase()
    creator.deleteDatabase()


if __name__ == "__main__":
    main()