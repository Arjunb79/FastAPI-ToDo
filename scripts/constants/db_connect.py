from pymongo import MongoClient

from scripts.config.application_config import uri


def db_connect():
    try:
        client = MongoClient(uri)
        database = client.ToDos
        dblist = client.list_database_names()
        if database in dblist:
            print("database exist")
        print("database created")
        return database
    except Exception as e:
        print(e)
