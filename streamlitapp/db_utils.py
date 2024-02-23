import psycopg2
from sqlalchemy import create_engine

class Database():

    def __init__(self):
        db_params = {
            "dbname": "AIA",
            "user": "alexis",
            "password": "",
            "host": "localhost",
            "port": "5432",  # Default PostgreSQL port
        }
        self.connection = psycopg2.connect(**db_params)
        self.engine = create_engine(
            f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['dbname']}"
        )

    def insert(self,insert_query):
        cursor = self.connection.cursor()

        cursor.execute(insert_query)
        self.connection.commit()
        cursor.close()

    def execute(self,query):
        cursor = self.connection.cursor()

        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def close(self):
        self.connection.close()
