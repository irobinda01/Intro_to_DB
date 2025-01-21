import mysql.connector
from mysql.connector import errorcode

# Database name
DB_NAME = "alx_book_store"

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",        # Change this if your server is not localhost
            user="root",             # Replace with your MySQL username
            password="your_password" # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # SQL command to create the database
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print(f"Database '{DB_NAME}' created successfully!")
    except mysql.connector.Error as err:
        # Handle specific errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close the connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()
