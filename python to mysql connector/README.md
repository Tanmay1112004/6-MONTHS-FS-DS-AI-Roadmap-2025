# 🔌 Python MySQL Connector

### Production-Ready, Secure & Pooled Database Interface

> A lightweight, Pythonic abstraction layer for MySQL with connection pooling, environment-based configuration, and clean resource management.

---

## 📌 Overview

This utility provides a structured, production-friendly way to interact with MySQL databases using:

* ⚡ **Connection Pooling** for performance
* 🔐 **Environment Variable Security**
* 🐍 **Context Manager-based API**
* 🧩 Clean CRUD patterns
* 📝 Type-hinted implementation

Designed for backend systems, APIs, microservices, and data-driven applications.

---

## 🏗 Architecture Overview

![demo](https://github.com/Tanmay1112004/6-MONTHS-FS-DS-AI-Roadmap-2025/blob/main/python%20to%20mysql%20connector/screenshots/Screenshot%202025-08-14%20184655.png)

![Image](https://www.researchgate.net/publication/352803770/figure/fig4/AS%3A1080215497383960%401634554852448/Schematic-diagram-of-MySQL-connection-pool.jpg)

![Image](https://miro.medium.com/1%2AnU2n5j4EuBrApI1DWBp1TQ.png)

![Image](https://media.licdn.com/dms/image/v2/D4D12AQHn_FaaW2dRWQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1683063399889?e=2147483647\&t=IzWq9CCKo_14s8BEs0T2zm4N35z43vIluJju-HxQDK8\&v=beta)

![Image](https://user-images.githubusercontent.com/44774033/68544061-6b9b3180-0402-11ea-8cc7-1794eead69d4.png)

### Execution Flow

```
Application Layer
      ↓
MySQLConnector Class
      ↓
Connection Pool Manager
      ↓
MySQL Server
```

Connections are reused efficiently instead of being created per request.

---

## ✨ Core Features

### ⚡ Connection Pooling

* Reuses active connections
* Reduces latency
* Prevents resource exhaustion
* Configurable pool size

---

### 🔐 Secure Credential Management

* Native `.env` integration
* Keeps secrets out of version control
* Production-friendly configuration

---

### 🐍 Pythonic Context Management

Uses `with` statements for automatic cleanup:

```python
with db.connection() as conn:
    results = conn.execute_query(query, params)
```

No manual connection closing.
No accidental leaks.

---

### 🛠 CRUD-Ready Design

Pre-structured patterns for:

* INSERT
* SELECT
* UPDATE
* DELETE

Supports parameterized queries to prevent SQL injection.

---

### 📝 Type Hints & Clean API

* IDE-friendly
* Better maintainability
* Stronger developer experience

---

## ⚙️ Setup & Installation

### 1️⃣ Requirements

* Python 3.8+
* MySQL 5.7+ / 8.0+

---

### 2️⃣ Install Dependencies

```bash
pip install mysql-connector-python python-dotenv
```

---

### 3️⃣ Configure Environment

Create `.env`:

```bash
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=your_secure_password
DB_NAME=app_db
POOL_SIZE=5
```

Or rename:

```
.env.example → .env
```

---

## 🚀 Usage Example

```python
from db_connector import MySQLConnector

db = MySQLConnector(
    host="localhost",
    user="admin",
    password="secure_password",
    database="app_db",
    pool_size=5
)

user_id = 42

with db.connection() as conn:
    query = "SELECT * FROM users WHERE id = %s"
    results = conn.execute_query(query, (user_id,))
    
    for user in results:
        print(f"Found User: {user['name']}")
```

---

## 📦 Project Structure

```
python-mysql-connector/
│
├── db_connector.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🧠 Why This Project Matters

This project demonstrates:

✔ Backend architecture awareness
✔ Resource management discipline
✔ Secure configuration practices
✔ Clean abstraction layer design
✔ Production-readiness mindset

This is the kind of utility used in:

* REST APIs
* Microservices
* Data pipelines
* SaaS backends

---

## 🔮 Future Enhancements

* Async support (asyncio + aiomysql)
* Logging & query profiling
* Retry logic for transient failures
* Transaction management utilities
* Support for PostgreSQL
* Dockerized test environment
* CI/CD integration with pytest

---

## 🧪 Testing

Planned support:

```bash
pytest
```

Unit tests will validate:

* Pool creation
* Connection reuse
* Query execution
* Error handling

---

## 👨‍💻 Author

**Tanmay Kshirsagar**

🔗 LinkedIn: [https://linkedin.com/in/tanmay-kshirsagar](https://linkedin.com/in/tanmay-kshirsagar)
💻 GitHub: [https://github.com/Tanmay1112004](https://github.com/Tanmay1112004)

---
