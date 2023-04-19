import random
import psycopg2
import json
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class TweetWriter:
    def __init__(self, db_connection: DatabaseConnection):
        self._db_connection = db_connection

    def write_tweets(self, *params):
        try:
            cursor, connection = self._db_connection.connect()
            tweet_query = """ INSERT INTO Tweet_Data (user_id,tweet_id, tweet_text,sentiment,comp,Emoticon,created_at) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            tweet_to_insert = (params)
            cursor.execute(tweet_query, tweet_to_insert)
            connection.commit()
            print("Record inserted successfully into table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Tweet_Data table", error)