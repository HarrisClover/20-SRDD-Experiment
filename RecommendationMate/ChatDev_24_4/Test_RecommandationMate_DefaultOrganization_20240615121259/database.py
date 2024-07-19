'''
This is the database file that contains the Database class. 
The Database class is responsible for connecting to the database, executing queries, and returning results.
'''
import sqlite3
class Database:
    def __init__(self, db_name='movies.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
    def fetch_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    def close(self):
        self.conn.close()