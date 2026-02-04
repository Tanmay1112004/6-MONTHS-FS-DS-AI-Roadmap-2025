# 🔌 Python MySQL Connector

A modern, production-ready Python interface for MySQL. This utility simplifies database interactions by abstracting connection logic, ensuring security via environment variables, and optimizing performance through connection pooling.

## ✨ Features

* **⚡ Connection Pooling:** Reuses active connections to minimize overhead and latency.
* **🔐 Secure Credentials:** Native support for `.env` files to keep your secrets out of source control.
* **🛠️ CRUD Templates:** Pre-built patterns for Create, Read, Update, and Delete operations.
* **🐍 Pythonic API:** Leverages **Context Managers** (`with` statements) for automatic resource cleanup.
* **📝 Type Safety:** Full type hinting for a better developer experience (IDE autocomplete).

---

## ⚙️ Configuration & Setup

### 1. Requirements

* **Python:** 3.8 or higher
* **MySQL:** Server 5.7+ or 8.0+

### 2. Installation

Install the necessary dependencies via pip:

```bash
pip install mysql-connector-python python-dotenv

```

### 3. Environment Variables

Create a `.env` file in your project root. Use the provided template:

```bash
# Rename .env.example to .env and fill in your details
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=your_secure_password
DB_NAME=app_db
POOL_SIZE=5

```

---

## 🚀 Usage Example

The connector is designed to be clean and readable. Here is how you can perform a safe, parameterized query:

```python
from db_connector import MySQLConnector

# 1. Initialize the connector
db = MySQLConnector(
    host="localhost",
    user="admin",
    password="secure_password",
    database="app_db",
    pool_size=5
)

# 2. Execute queries using a Context Manager
# This ensures the connection returns to the pool automatically
user_id = 42

with db.connection() as conn:
    query = "SELECT * FROM users WHERE id = %s"
    results = conn.execute_query(query, (user_id,))
    
    for user in results:
        print(f"Found User: {user['name']}")

```

---

## 📦 File Structure

| File | Purpose |
| --- | --- |
| `db_connector.py` | Core logic for the MySQL connection and pool management. |
| `.env.example` | Template for environment configuration. |
| `requirements.txt` | Project dependencies (`mysql-connector`, `dotenv`, `pytest`). |

---

## 🤝 Contributing & Support

If you're interested in improving the CRUD templates or adding support for other database engines, feel free to fork this repo!

**Author:** Tanmay Kahirsagar

**Links:** [LinkedIn](https://www.google.com/search?q=https://linkedin.com/in/tanmay-kahirsagar) | [GitHub](https://www.google.com/search?q=https://github.com/tanmay-kahirsagar)

---
