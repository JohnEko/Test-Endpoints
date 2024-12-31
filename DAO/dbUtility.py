import os
import psycopg2

USER =os.getenv("sqluser")
PASSWORD=os.getenv("dbpass")

def get_connections(dbuser:str, host:str, port:str, dbname:str, password:str):
    """
    Make connection to db
    set the port 
    set db instance name
    set user and db password
    """
    if not (host, port, dbuser, dbname, password):
        raise ValueError("Check your parameter decleared")
    try:
       
        conn =  psycopg2.connect(f"postgresql://{dbuser}:{password}@{host}/{dbname}")
    
        return conn
    except Exception as e:
        raise f"The connection is dose not exist: {e}"


def query_db(query):
    conn = get_connections(
        host="localhost",
        port=5432,
        dbuser=USER,
        password=PASSWORD,
        dbname="study"
    )

    try:
        curs = conn.cursor()
        curs.execute(query)
        records = curs.fetchall()
        curs.close()

    finally:
        conn.close()
    
    return records

records = query_db(query="select * from study limit 10")
