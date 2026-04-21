import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "Prakash@000",   # <-- Change this
    "database": "student_result_db"
}

def get_connection():
    """Returns a MySQL connection. Raises Error on failure."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        raise Exception(f"Database connection failed: {str(e)}")
