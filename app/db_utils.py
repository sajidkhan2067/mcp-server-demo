import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", "5432")),
    )

def execute_query(sql_query):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            if sql_query.strip().lower().startswith("select"):
                return [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
            conn.commit()
            return {"status": "success"}
    finally:
        conn.close()
