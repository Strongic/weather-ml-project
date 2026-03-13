import sqlite3
import pandas as pd

class Database:
    
    def __init__(self, db_path = "data/stations.db"):
        self.db_path = db_path
    
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def query(self, sql, params=None):
        conn = self.connect()

        if params:
            df = pd.read_sql_query(sql, conn, params=params)
        else:
            df = pd.read_sql_query(sql, conn)
        
        conn.close()

        return df

    def get_us_stations(self):
        
        sql = "SELECT * FROM stations WHERE country='US'"
        return self.query(sql)

 