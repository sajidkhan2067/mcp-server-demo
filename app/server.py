import os
import psycopg2
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Postgres Server")

def run_query(sql: str):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "password"),
        dbname=os.getenv("DB_NAME", "mydb"),
        port=int(os.getenv("DB_PORT", "5432")),
    )
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
            conn.commit()
            return {"status": "success"}
    finally:
        conn.close()

@mcp.tool()
def sql_query(query: str) -> object:
    """Run a SQL query on the Postgres database and return the result."""
    try:
        return run_query(query)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()  # <-- THIS is the entry point for MCP server
