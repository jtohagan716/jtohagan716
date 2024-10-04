 import pandas as pd
from db_connection import connect_to_db

def fetch_data():
    """Fetch data from the database."""
    connection = connect_to_db()
    if connection:
        try:
            query = """
            SELECT employee_id, first_name, last_name, department_id, salary
            FROM employees
            WHERE salary > 50000
            ORDER BY salary DESC
            """
            df = pd.read_sql(query, con=connection)
            print("Data fetched successfully.")
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            connection.close()
    return None

