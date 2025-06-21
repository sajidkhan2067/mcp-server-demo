from mcp.client import MCPClient

def main():
    # Create client with your auth token
    client = MCPClient(
        proxy_url="http://localhost:6277",
        auth_token="54f7ec6d1e1cb746c83ef51cc3383e4c3e598d7079cd2c34f01251202d385455"
    )
    
    # Execute SQL query
    result = client.tool_call(
        tool="sql_query",
        arguments={"query": "SELECT * FROM employees'"}
    )
    
    print("Query result:")
    print(result)

if __name__ == "__main__":
    main()