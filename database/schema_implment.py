import psycopg2
from database_config import DB_CONFIG
  
with open(r'C:\Users\HP\Documents\DATA_ANALYST\STOCK_MANAGER\database\schema.sql', 'r') as file:
    schema = file.read()
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(schema)
    conn.commit()
except Exception as e:
    print(f'{e}')
finally:
    cur.close()
    conn.close()