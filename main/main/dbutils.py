from pymongo import MongoClient
from django.conf import settings


def get_db_handle_username_password(db_name, host, port, username, password):
    client = MongoClient(
        host=host, port=int(port), username=username, password=password
    )
    db_handle = client["db_name"]
    return db_handle, client


def get_db_handle_connx_string(db_name, connx_string):
    client = MongoClient(connx_string)
    db_handle = client[db_name]
    return db_handle, client


def get_db_handle():
    return get_db_handle_connx_string(settings.MONGODB_NAME, settings.MONGODB_CONNX_STR)
