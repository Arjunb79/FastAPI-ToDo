from scripts.constants.db_connect import db_connect


def create_collection():
    try:
        db = db_connect()
        collection = db["todo"]
        return collection
    except Exception as e:
        print(e)
