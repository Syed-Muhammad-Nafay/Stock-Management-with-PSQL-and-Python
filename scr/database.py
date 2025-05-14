import psycopg2
from database_config import DB_CONFIG

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print('Connection failed❌')
        return None
