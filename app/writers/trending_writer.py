import random
import psycopg2
import json
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class TrendingWriter:
    def __init__(self, db_connection: DatabaseConnection):
        self._db_connection = db_connection

    def write_trends(self, *params):
        try:
            cursor, connection = self._db_connection.connect()
            trending_query = """ INSERT INTO Trending_Data (trend_name, url, tweet_volume) VALUES (%s,%s,%s)"""
            trend_to_insert = (params)
            cursor.execute(trending_query, trend_to_insert)
            connection.commit()
            print("Record inserted successfully into table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Trending_Data table", error)
