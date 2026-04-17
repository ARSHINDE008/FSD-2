"""
Database Initialization Script
This script creates the MySQL database and initializes the student table
"""

import mysql.connector
from mysql.connector import Error
import os

def create_database():
    """Create MySQL database and initialize tables"""
    
    # Configuration
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'student_management')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            port=MYSQL_PORT
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")
            print(f"✓ Database '{MYSQL_DB}' created successfully")
            
            # Switch to the database
            cursor.execute(f"USE {MYSQL_DB};")
            
            # Create student table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                uid VARCHAR(20) UNIQUE NOT NULL,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE,
                age INT NOT NULL,
                course VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                KEY idx_uid (uid)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
            """
            
            cursor.execute(create_table_query)
            print("✓ Table 'student' created successfully")
            
            cursor.close()
            connection.close()
            print("✓ Database initialization completed successfully!")
            
    except Error as e:
        print(f"✗ Error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Student Management API - Database Setup")
    print("=" * 50)
    create_database()
    print("=" * 50)
