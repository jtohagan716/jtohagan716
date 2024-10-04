import cx_Oracle

# Database connection details
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="orclpdb")
username = "your_username"
password = "your_password"

def connect_to_db():
    """Establish a connection to the Oracle database."""
    try:
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
        print("Database connection established.")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Error connecting to the database: {e}")
        return None
 
