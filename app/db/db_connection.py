import random
import psycopg2
import json
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, credentials):
        self._dbuser = credentials['db_user']
        self._dbpass = credentials['db_pass']
        self._dbhost = credentials['db_host']
        self._dbport = credentials['db_port']
        self._dbname = credentials['db_name']

    def connect(self):
        try:
            connection = psycopg2.connect(user=self._dbuser,
                                          password=self._dbpass,
                                          host=self._dbhost,
                                          port=self._dbport,
                                          database=self._dbname)
            cursor = connection.cursor()
            return cursor, connection
        except (Exception, psycopg2.Error) as error:
            print("Failed to establish Connection", error)