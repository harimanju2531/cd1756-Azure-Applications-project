import pyodbc
import urllib

server = 'cmsserverharitha.database.windows.net'
database = 'cmsserverharitha123'
username = 'cmsadmin'
password = 'cms@12345'

# URL encode the password
encoded_password = urllib.parse.quote_plus(password)

# Build connection string properly
conn_str = (
    f"Driver={{ODBC Driver 17 for SQL Server}};"
    f"Server=tcp:{server},1433;"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

print("Testing connection with fixed format...")
print(f"Server: {server}")
print(f"Database: {database}")
print(f"Username: {username}")
print("-" * 50)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ SUCCESS! Connected to Azure SQL Database!")
    
    # Test a simple query
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    version = cursor.fetchone()
    print(f"SQL Server Version: {version[0][:50]}...")
    
    conn.close()
except Exception as e:
    print(f"❌ Connection failed!")
    print(f"Error: {e}")
    
    # Try alternative connection string with encoded password
    print("\nTrying alternative format with encoded password...")
    try:
        alt_conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=tcp:{server},1433;DATABASE={database};UID={username};PWD={encoded_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
        conn = pyodbc.connect(alt_conn_str)
        print("✅ SUCCESS with encoded password!")
        conn.close()
    except Exception as e2:
        print(f"❌ Still failed: {e2}")