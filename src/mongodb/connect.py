"""mongodb.connect.py module"""
import pymongo


def connect() -> pymongo.MongoClient:
    """
    Connect to mongoDB.

    Returns
    -------
    MongoClient
        The pymongo client for mongoDB
    """
    conn_str = "mongodb://localhost:27017"
    # set a 5-second connection timeout
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    return client
