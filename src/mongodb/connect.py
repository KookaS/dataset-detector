import pymongo


def connect() -> pymongo.MongoClient:
    try:
        # Replace the uri string with your MongoDB deployment's connection string.
        conn_str = "mongodb://localhost:27017"
        # set a 5-second connection timeout
        client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        return client
    except Exception:
        raise