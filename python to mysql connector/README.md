# Python MySQL Connector 🔌

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![MySQL Version](https://img.shields.io/badge/mysql-5.7%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A modern Python interface for MySQL with:
- Connection pooling
- Secure credential management
- CRUD operation templates
- Context manager support
- Comprehensive error handling

## Features ✨

- **Connection Pooling**: Efficiently manage database connections
- **Environment Variables**: Secure credential configuration
- **CRUD Operations**: Ready-to-use templates for common operations
- **Type Hints**: Full Python type support
- **Context Managers**: Automatic connection handling



Requirements
Python 3.8+

MySQL Server 5.7+

mysql-connector-python

Usage Example 🚀

from db_connector import MySQLConnector

# Initialize connector
db = MySQLConnector(
    host="localhost",
    user="admin",
    password="secure_password",
    database="app_db",
    pool_size=5
)

# Execute query
with db.connection() as conn:
    results = conn.execute_query("SELECT * FROM users WHERE id = %s", (user_id,))

Configuration ⚙️
Rename .env.example to .env

Set your MySQL credentials:

DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=secure_password
DB_NAME=app_db
POOL_SIZE=5

requirements.txt:
mysql-connector-python==8.0.33
python-dotenv==1.0.0
pytest==7.4.0

.env.example:
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database
POOL_SIZE=5


