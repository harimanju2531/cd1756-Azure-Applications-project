import pyodbc

# Replace with YOUR actual values
server = 'cmsserverharitha.database.windows.net'  # Full server name
database = 'cms'
username = 'cmsadmin'
password = 'CMS4dmin'  # Your actual password
driver = '{ODBC Driver 17 for SQL Server}'

print(f"Attempting to connect to: {server}")
print(f"Database: {database}")
print(f"Username: {username}")
print("-" * 50)

try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};Connection Timeout=30'
    )
    print("✅ SUCCESS! Connected to Azure SQL Database!")
    conn.close()
except Exception as e:
    print(f"❌ CONNECTION FAILED!")
    print(f"Error: {e}")