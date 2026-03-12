import os
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-random-secret-key-here-change-this'

    # Blob Storage Settings
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images12345'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'iU1jhn5Dcyy+wT9wfzmK3eHENqIrhc+og+HirecdJdqj2s1QSz0dMCwc+Rl6GE8ft1SomiuDC2Lt+ASt4afqrw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or 'DefaultEndpointsProtocol=https;AccountName=images12345;AccountKey=iU1jhn5Dcyy+wT9wfzmK3eHENqIrhc+og+HirecdJdqj2s1QSz0dMCwc+Rl6GE8ft1SomiuDC2Lt+ASt4afqrw==;EndpointSuffix=core.windows.net'

    # SQL Database Settings - FIXED VERSION
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cmsserverharitha.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cmsserverharitha123'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'cms@12345'
    
    # FIXED: URL-encode the password to handle the @ symbol
    import urllib.parse
    encoded_password = urllib.parse.quote_plus(SQL_PASSWORD)
    
    # FIXED: Correct connection string format for Azure SQL with special characters
    params = urllib.parse.quote_plus(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server=tcp:{SQL_SERVER},1433;"
        f"Database={SQL_DATABASE};"
        f"Uid={SQL_USER_NAME};"
        f"Pwd={SQL_PASSWORD};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=no;"
        f"Connection Timeout=30;"
    )
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MS Authentication Settings
    CLIENT_ID = os.environ.get('CLIENT_ID') or 'your-client-id-from-phase-4'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'your-client-secret-from-phase-4'
    
    # For multi-tenant app (allows personal Microsoft accounts)
    AUTHORITY = "https://login.microsoftonline.com/common"
    
    # This must match the redirect URI path in your app registration
    REDIRECT_PATH = "/getAToken"
    
    # Microsoft Graph API scopes
    SCOPE = ["User.Read"]
    
    # Session type for token cache
    SESSION_TYPE = "filesystem"