# Enterprise Linux Web Database Administration Project

A complete hands-on Linux administration project using **Amazon Linux 2023 or Fedora**, **Apache HTTP Server**, **PHP**, **MariaDB/MySQL**, **Bash scripting**, **Cron**, networking utilities, permissions, services, logs, database administration, monitoring, backup, and troubleshooting.

This project is designed for students who want to practice Linux commands in a realistic environment and build a project that can be added to their **GitHub portfolio and resume**.

---

# 1. Project Title

## Enterprise Linux Web Server and Database Administration Project

**Repository**

```text
https://github.com/atulkamble/linux-lamp-project
```

Alternative repository name:

```text
linux-lamp-student-portal
```

---

# 2. Project Overview

In this project, we will deploy a complete database-driven web application on an Amazon Linux 2023 or Fedora-based Linux system.

The application will be a simple:

## Student Management Portal

The application will allow users to:

* Add student records
* View student records
* Update student information
* Delete student records
* Store data inside MariaDB/MySQL
* Access the application using a browser

The main focus of the project is not PHP development.

The main objective is to understand how Linux components work together:

```text
Linux
+
Apache
+
PHP
+
MariaDB/MySQL
+
Networking
+
Users
+
Permissions
+
Services
+
Processes
+
Logs
+
Bash
+
Cron
+
Backup
+
Troubleshooting
```

---

# 3. Project Objectives

After completing this project, students should be able to:

* Understand Linux system architecture
* Connect to a Linux server using SSH
* Work with files and directories
* Create Linux users and groups
* Configure Linux permissions
* Install packages using DNF
* Manage RPM packages
* Install and configure Apache HTTP Server
* Install PHP
* Install MariaDB/MySQL
* Manage Linux services using systemd
* Create databases and tables
* Create database users
* Configure database privileges
* Connect PHP with MariaDB/MySQL
* Build a basic database-driven application
* Perform CRUD operations
* Understand TCP ports
* Troubleshoot network connectivity
* Monitor Linux processes
* Analyze Linux and Apache logs
* Use Bash scripting
* Automate tasks using Cron
* Backup website data
* Backup MariaDB/MySQL databases
* Restore a database
* Monitor disk and memory usage
* Troubleshoot Apache and MariaDB failures
* Push the complete project to GitHub
* Explain the project during interviews

---

# 4. Technologies Used

| Technology                 | Purpose                 |
| -------------------------- | ----------------------- |
| Amazon Linux 2023 / Fedora | Operating System        |
| AWS EC2 / Local VM         | Linux Server            |
| SSH                        | Remote Server Access    |
| Apache HTTP Server         | Web Server              |
| PHP                        | Server-side Application |
| MariaDB / MySQL            | Database                |
| SQL                        | Database Operations     |
| Bash                       | Automation              |
| Cron                       | Task Scheduling         |
| systemd                    | Service Management      |
| Git                        | Version Control         |
| GitHub                     | Project Repository      |
| curl                       | HTTP Testing            |
| ss                         | Port Monitoring         |
| ip                         | Network Configuration   |
| journalctl                 | System Logs             |

---

# 5. Project Architecture

## Basic Architecture

```text
                         INTERNET
                             |
                             |
                             v
                   +-------------------+
                   | AWS Security Group|
                   |                   |
                   | SSH  : 22         |
                   | HTTP : 80         |
                   +---------+---------+
                             |
                             |
                             v
              +-------------------------------+
              |       Amazon Linux 2023       |
              |            / Fedora           |
              |                               |
              |  +-------------------------+  |
              |  | Apache HTTP Server      |  |
              |  | Port 80                 |  |
              |  +------------+------------+  |
              |               |               |
              |               v               |
              |  +-------------------------+  |
              |  | PHP Application         |  |
              |  | Student Portal          |  |
              |  +------------+------------+  |
              |               |               |
              |               | mysqli        |
              |               v               |
              |  +-------------------------+  |
              |  | MariaDB / MySQL         |  |
              |  | Port 3306               |  |
              |  |                         |  |
              |  | Database:               |  |
              |  | student_portal          |  |
              |  +-------------------------+  |
              |                               |
              | Bash Scripts                  |
              | Cron Jobs                     |
              | Logs                          |
              | Backups                       |
              +-------------------------------+
```

---

# 6. Application Request Flow

When a user opens the website:

```text
Browser
   |
   | HTTP Request
   |
   v
Apache HTTP Server
   |
   v
PHP Application
   |
   | mysqli
   |
   v
MariaDB / MySQL
   |
   v
student_portal Database
   |
   v
Students Table
   |
   v
PHP generates HTML
   |
   v
Apache
   |
   v
Browser
```

---

# 7. Project Directory Structure

Create the following project structure:

```text
linux-lamp-project/
│
├── README.md
│
├── website/
│   ├── index.php
│   ├── students.php
│   ├── add.php
│   ├── edit.php
│   ├── delete.php
│   ├── db.php
│   └── style.css
│
├── database/
│   ├── database.sql
│   └── sample-data.sql
│
├── scripts/
│   ├── install_lamp.sh
│   ├── health_check.sh
│   ├── backup_website.sh
│   ├── backup_database.sh
│   ├── system_report.sh
│   └── cleanup_logs.sh
│
├── docs/
│   ├── linux-commands.md
│   ├── mysql-commands.md
│   ├── troubleshooting.md
│   └── resume-points.md
│
├── backups/
│
├── logs/
│
└── screenshots/
```

Clone the repository (already contains this layout):

```bash
git clone https://github.com/atulkamble/linux-lamp-project.git

cd linux-lamp-project
```

Or create it from scratch:

```bash
mkdir linux-lamp-project

cd linux-lamp-project

mkdir website
mkdir database
mkdir scripts
mkdir docs
mkdir backups
mkdir logs
mkdir screenshots
```

Check:

```bash
ls
```

If `tree` is installed:

```bash
tree
```

---

# 8. Lab Requirements

Students can perform this project using:

## Option 1 — AWS EC2

Recommended:

```text
Operating System: Amazon Linux 2023
Instance Type: t2.micro / t3.micro
Storage: 8-10 GB
```

Security Group:

| Protocol | Port | Source    |
| -------- | ---: | --------- |
| SSH      |   22 | Your IP   |
| HTTP     |   80 | 0.0.0.0/0 |
| HTTPS    |  443 | Optional  |

Do not expose MySQL port `3306` publicly when the database and application are running on the same server.

## Option 2 — Fedora VM

Students can use:

* VirtualBox
* VMware
* Hyper-V
* Local Fedora installation

---

# 9. Connect to Amazon Linux Using SSH

Example:

```bash
ssh -i key.pem ec2-user@PUBLIC-IP
```

Example:

```bash
ssh -i linux-project.pem ec2-user@54.10.20.30
```

Verify current user:

```bash
whoami
```

Expected:

```text
ec2-user
```

---

# 10. Basic Linux System Information

Practice:

```bash
hostname
```

```bash
hostnamectl
```

```bash
uname
```

```bash
uname -a
```

```bash
cat /etc/os-release
```

```bash
whoami
```

```bash
id
```

```bash
pwd
```

```bash
date
```

```bash
uptime
```

```bash
arch
```

```bash
lscpu
```

```bash
free -h
```

```bash
df -h
```

These commands help understand:

* Linux distribution
* Kernel
* CPU architecture
* Memory
* Storage
* Hostname
* Logged-in user

---

# 11. File and Directory Commands

Check current directory:

```bash
pwd
```

List files:

```bash
ls
```

Detailed listing:

```bash
ls -l
```

Hidden files:

```bash
ls -la
```

Create directory:

```bash
mkdir demo
```

Create nested directories:

```bash
mkdir -p demo/test/app
```

Change directory:

```bash
cd demo
```

Return:

```bash
cd ..
```

Create file:

```bash
touch test.txt
```

Copy:

```bash
cp test.txt test-copy.txt
```

Move:

```bash
mv test-copy.txt newfile.txt
```

Delete:

```bash
rm newfile.txt
```

Delete directory:

```bash
rm -rf demo
```

---

# 12. File Viewing Commands

Create:

```bash
echo "Linux Project" > test.txt
```

Display:

```bash
cat test.txt
```

First lines:

```bash
head test.txt
```

Last lines:

```bash
tail test.txt
```

Read larger file:

```bash
less /etc/passwd
```

Search:

```bash
grep root /etc/passwd
```

---

# 13. Linux Users and Groups

Create a web administration user:

```bash
sudo useradd webadmin
```

Set password:

```bash
sudo passwd webadmin
```

Create group:

```bash
sudo groupadd webteam
```

Add user:

```bash
sudo usermod -aG webteam webadmin
```

Verify:

```bash
id webadmin
```

```bash
groups webadmin
```

Check users:

```bash
cat /etc/passwd
```

Check groups:

```bash
cat /etc/group
```

---

# 14. Linux Permissions

Linux permissions:

```text
r = Read
w = Write
x = Execute
```

Check:

```bash
ls -l
```

Example:

```text
-rwxr-xr--
```

Permission calculation:

```text
r = 4
w = 2
x = 1
```

Examples:

```text
7 = rwx
6 = rw-
5 = r-x
4 = r--
```

Change permission:

```bash
chmod 755 script.sh
```

Change owner:

```bash
sudo chown webadmin file.txt
```

Change owner and group:

```bash
sudo chown webadmin:webteam file.txt
```

---

# 15. Package Management

Amazon Linux 2023 and Fedora use `dnf`.

Update metadata/packages:

```bash
sudo dnf update -y
```

Search:

```bash
dnf search httpd
```

Package information:

```bash
dnf info httpd
```

Install:

```bash
sudo dnf install httpd -y
```

List RPM packages:

```bash
rpm -qa
```

Search package:

```bash
rpm -qa | grep httpd
```

Find package files:

```bash
rpm -ql httpd
```

---

# 16. Install Apache HTTP Server

Install:

```bash
sudo dnf install httpd -y
```

Check version:

```bash
httpd -v
```

Start:

```bash
sudo systemctl start httpd
```

Enable:

```bash
sudo systemctl enable httpd
```

Or:

```bash
sudo systemctl enable --now httpd
```

Status:

```bash
systemctl status httpd
```

---

# 17. systemctl Commands

Students should practice:

```bash
sudo systemctl start httpd
```

```bash
sudo systemctl stop httpd
```

```bash
sudo systemctl restart httpd
```

```bash
sudo systemctl reload httpd
```

```bash
sudo systemctl enable httpd
```

```bash
sudo systemctl disable httpd
```

```bash
systemctl status httpd
```

```bash
systemctl is-active httpd
```

```bash
systemctl is-enabled httpd
```

---

# 18. Test Apache

From Linux:

```bash
curl http://localhost
```

Check headers:

```bash
curl -I http://localhost
```

Check port:

```bash
sudo ss -lntp | grep :80
```

Expected:

```text
LISTEN ... :80
```

Open:

```text
http://PUBLIC-IP
```

---

# 19. Install PHP

## Amazon Linux 2023

```bash
sudo dnf install php php-fpm php-mysqli php-json -y
```

## Fedora

```bash
sudo dnf install php php-fpm php-mysqlnd -y
```

Check:

```bash
php -v
```

Check PHP modules:

```bash
php -m
```

Check MySQL module:

```bash
php -m | grep -i mysqli
```

Restart Apache:

```bash
sudo systemctl restart httpd
```

---

# 20. Test PHP

Create:

```bash
sudo vi /var/www/html/info.php
```

Add:

```php
<?php

phpinfo();

?>
```

Open:

```text
http://PUBLIC-IP/info.php
```

After testing, remove it because `phpinfo()` exposes system information:

```bash
sudo rm /var/www/html/info.php
```

---

# 21. Install MariaDB/MySQL

## Amazon Linux 2023

```bash
sudo dnf install mariadb105-server -y
```

## Fedora

```bash
sudo dnf install mariadb-server -y
```

Start:

```bash
sudo systemctl start mariadb
```

Enable:

```bash
sudo systemctl enable mariadb
```

Or:

```bash
sudo systemctl enable --now mariadb
```

Check:

```bash
systemctl status mariadb
```

Version:

```bash
mysql --version
```

---

# 22. Check Database Port

MariaDB/MySQL generally listens on:

```text
3306
```

Check:

```bash
sudo ss -lntp | grep 3306
```

Check process:

```bash
ps -ef | grep maria
```

```bash
pgrep -a mariadbd
```

---

# 23. Secure MariaDB

Run:

```bash
sudo mysql_secure_installation
```

Follow the prompts.

Topics covered:

* Root authentication
* Anonymous accounts
* Test databases
* Remote root access
* Security hardening

---

# 24. Login to MariaDB

```bash
sudo mysql
```

Or:

```bash
mysql -u root -p
```

Check:

```sql
SHOW DATABASES;
```

Exit:

```sql
exit;
```

---

# 25. Create Student Portal Database

Login:

```bash
sudo mysql
```

Create database:

```sql
CREATE DATABASE student_portal;
```

Verify:

```sql
SHOW DATABASES;
```

Select:

```sql
USE student_portal;
```

---

# 26. Create Students Table

Create:

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Check tables:

```sql
SHOW TABLES;
```

Describe:

```sql
DESCRIBE students;
```

---

# 27. Create Database Application User

Do not use the database root account inside the website.

Create:

```sql
CREATE USER 'webapp'@'localhost'
IDENTIFIED BY 'Student@12345';
```

Grant only required permissions:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE
ON student_portal.*
TO 'webapp'@'localhost';
```

Verify:

```sql
SHOW GRANTS FOR 'webapp'@'localhost';
```

Apply:

```sql
FLUSH PRIVILEGES;
```

---

# 28. Insert Sample Records

Select:

```sql
USE student_portal;
```

Insert:

```sql
INSERT INTO students
(name,email,course,city)
VALUES
('Rahul Sharma','rahul@example.com','Linux','Pune');
```

```sql
INSERT INTO students
(name,email,course,city)
VALUES
('Priya Patil','priya@example.com','AWS','Mumbai');
```

```sql
INSERT INTO students
(name,email,course,city)
VALUES
('Amit Kumar','amit@example.com','DevOps','Delhi');
```

View:

```sql
SELECT * FROM students;
```

---

# 29. SQL Commands Practice

## SELECT

```sql
SELECT * FROM students;
```

Specific columns:

```sql
SELECT name,email FROM students;
```

Filter:

```sql
SELECT * FROM students
WHERE city='Pune';
```

Sort:

```sql
SELECT * FROM students
ORDER BY name;
```

Count:

```sql
SELECT COUNT(*) FROM students;
```

---

# 30. INSERT

```sql
INSERT INTO students
(name,email,course,city)
VALUES
('Neha','neha@example.com','Azure','Pune');
```

---

# 31. UPDATE

```sql
UPDATE students
SET course='Linux + DevOps'
WHERE id=1;
```

---

# 32. DELETE

```sql
DELETE FROM students
WHERE id=1;
```

---

# 33. Create Database SQL File

Create:

```bash
vi database/database.sql
```

Add:

```sql
CREATE DATABASE IF NOT EXISTS student_portal;

USE student_portal;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Load:

```bash
sudo mysql < database/database.sql
```

---

# 34. Create Sample Data File

Create:

```bash
vi database/sample-data.sql
```

Add:

```sql
USE student_portal;

INSERT INTO students
(name,email,course,city)
VALUES
('Rahul Sharma','rahul@example.com','Linux','Pune'),
('Priya Patil','priya@example.com','AWS','Mumbai'),
('Amit Kumar','amit@example.com','DevOps','Delhi');
```

Load:

```bash
sudo mysql < database/sample-data.sql
```

---

# 35. Configure PHP Database Connectivity

Create:

```bash
vi website/db.php
```

Add:

```php
<?php

$host = "localhost";
$user = "webapp";
$password = "Student@12345";
$database = "student_portal";

$conn = new mysqli(
    $host,
    $user,
    $password,
    $database
);

if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}

?>
```

For real production systems, do not store passwords directly in application source code.

Use:

* Environment variables
* AWS Secrets Manager
* Parameter Store
* Vault
* Other secret-management systems

The hardcoded password is used here only for basic lab understanding.

---

# 36. Test Database Connectivity

Create:

```bash
sudo vi /var/www/html/db-test.php
```

Add:

```php
<?php

$conn = new mysqli(
    "localhost",
    "webapp",
    "Student@12345",
    "student_portal"
);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

echo "Database connection successful!";

?>
```

Test:

```bash
curl http://localhost/db-test.php
```

Expected:

```text
Database connection successful!
```

---

# 37. Create Application Home Page

Create:

```bash
vi website/index.php
```

Add:

```php
<?php

require 'db.php';

$result = $conn->query(
    "SELECT COUNT(*) AS total FROM students"
);

$data = $result->fetch_assoc();

?>

<!DOCTYPE html>

<html>

<head>

    <title>Linux Student Portal</title>

    <link rel="stylesheet" href="style.css">

</head>

<body>

<div class="container">

    <h1>Enterprise Linux Student Portal</h1>

    <p>
        Apache + PHP + MariaDB/MySQL
    </p>

    <div class="card">

        <h2>Linux Server</h2>

        <p>
            Hostname:
            <?php echo htmlspecialchars(gethostname()); ?>
        </p>

        <p>
            PHP Version:
            <?php echo htmlspecialchars(PHP_VERSION); ?>
        </p>

    </div>

    <div class="card">

        <h2>Database</h2>

        <p>
            Total Students:
            <?php echo htmlspecialchars($data['total']); ?>
        </p>

    </div>

    <a class="button" href="students.php">
        View Students
    </a>

    <a class="button" href="add.php">
        Add Student
    </a>

</div>

</body>

</html>
```

---

# 38. Create Students Page

Create:

```bash
vi website/students.php
```

Add:

```php
<?php

require 'db.php';

$result = $conn->query(
    "SELECT * FROM students ORDER BY id DESC"
);

?>

<!DOCTYPE html>

<html>

<head>

<title>Students</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<div class="container">

<h1>Student Records</h1>

<a class="button" href="index.php">
Home
</a>

<a class="button" href="add.php">
Add Student
</a>

<br><br>

<table>

<tr>

<th>ID</th>
<th>Name</th>
<th>Email</th>
<th>Course</th>
<th>City</th>
<th>Created</th>
<th>Actions</th>

</tr>

<?php while($row = $result->fetch_assoc()) { ?>

<tr>

<td>
<?php echo htmlspecialchars($row['id']); ?>
</td>

<td>
<?php echo htmlspecialchars($row['name']); ?>
</td>

<td>
<?php echo htmlspecialchars($row['email']); ?>
</td>

<td>
<?php echo htmlspecialchars($row['course']); ?>
</td>

<td>
<?php echo htmlspecialchars($row['city']); ?>
</td>

<td>
<?php echo htmlspecialchars($row['created_at']); ?>
</td>

<td>

<a href="edit.php?id=<?php echo $row['id']; ?>">
Edit
</a>

<form
method="POST"
action="delete.php"
style="display:inline">

<input
type="hidden"
name="id"
value="<?php echo $row['id']; ?>">

<button type="submit">
Delete
</button>

</form>

</td>

</tr>

<?php } ?>

</table>

</div>

</body>

</html>
```

---

# 39. Create Add Student Page

Create:

```bash
vi website/add.php
```

Add:

```php
<?php

require 'db.php';

$message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $name = trim($_POST["name"]);
    $email = trim($_POST["email"]);
    $course = trim($_POST["course"]);
    $city = trim($_POST["city"]);

    $stmt = $conn->prepare(
        "INSERT INTO students
        (name,email,course,city)
        VALUES (?, ?, ?, ?)"
    );

    $stmt->bind_param(
        "ssss",
        $name,
        $email,
        $course,
        $city
    );

    if ($stmt->execute()) {

        header("Location: students.php");

        exit;

    } else {

        $message = "Unable to add student.";

    }

}

?>

<!DOCTYPE html>

<html>

<head>

<title>Add Student</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<div class="container">

<h1>Add Student</h1>

<p>
<?php echo htmlspecialchars($message); ?>
</p>

<form method="POST">

<label>Name</label>

<input
type="text"
name="name"
required>

<label>Email</label>

<input
type="email"
name="email"
required>

<label>Course</label>

<input
type="text"
name="course"
required>

<label>City</label>

<input
type="text"
name="city">

<button type="submit">
Add Student
</button>

</form>

<br>

<a href="students.php">
Back
</a>

</div>

</body>

</html>
```

---

# 40. Create Edit Page

Create:

```bash
vi website/edit.php
```

Add:

```php
<?php

require 'db.php';

$id = intval($_GET["id"] ?? 0);

$stmt = $conn->prepare(
    "SELECT * FROM students WHERE id=?"
);

$stmt->bind_param("i", $id);

$stmt->execute();

$result = $stmt->get_result();

$student = $result->fetch_assoc();

if (!$student) {

    exit("Student not found.");

}

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $name = trim($_POST["name"]);
    $email = trim($_POST["email"]);
    $course = trim($_POST["course"]);
    $city = trim($_POST["city"]);

    $stmt = $conn->prepare(
        "UPDATE students
        SET name=?, email=?, course=?, city=?
        WHERE id=?"
    );

    $stmt->bind_param(
        "ssssi",
        $name,
        $email,
        $course,
        $city,
        $id
    );

    $stmt->execute();

    header("Location: students.php");

    exit;

}

?>

<!DOCTYPE html>

<html>

<head>

<title>Edit Student</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<div class="container">

<h1>Edit Student</h1>

<form method="POST">

<label>Name</label>

<input
type="text"
name="name"
value="<?php echo htmlspecialchars($student['name']); ?>"
required>

<label>Email</label>

<input
type="email"
name="email"
value="<?php echo htmlspecialchars($student['email']); ?>"
required>

<label>Course</label>

<input
type="text"
name="course"
value="<?php echo htmlspecialchars($student['course']); ?>"
required>

<label>City</label>

<input
type="text"
name="city"
value="<?php echo htmlspecialchars($student['city']); ?>">

<button type="submit">
Update Student
</button>

</form>

</div>

</body>

</html>
```

---

# 41. Create Delete Page

Create:

```bash
vi website/delete.php
```

Add:

```php
<?php

require 'db.php';

if ($_SERVER["REQUEST_METHOD"] !== "POST") {

    http_response_code(405);

    exit("Method not allowed.");

}

$id = intval($_POST["id"] ?? 0);

$stmt = $conn->prepare(
    "DELETE FROM students WHERE id=?"
);

$stmt->bind_param("i", $id);

$stmt->execute();

header("Location: students.php");

exit;

?>
```

---

# 42. Create CSS

Create:

```bash
vi website/style.css
```

Add:

```css
body {
    font-family: Arial, sans-serif;
    background: #f5f6fa;
    margin: 0;
    padding: 0;
}

.container {
    width: 85%;
    margin: 40px auto;
}

h1 {
    color: #222;
}

.card {
    background: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
}

table {
    width: 100%;
    border-collapse: collapse;
    background: white;
}

th,
td {
    padding: 12px;
    border: 1px solid #ddd;
}

th {
    background: #222;
    color: white;
}

input {
    width: 100%;
    padding: 10px;
    margin: 8px 0 18px;
    box-sizing: border-box;
}

button,
.button {
    padding: 10px 16px;
    border: none;
    text-decoration: none;
    cursor: pointer;
}

.button {
    display: inline-block;
    background: #222;
    color: white;
    margin-right: 10px;
}
```

---

# 43. Deploy Website

Copy:

```bash
sudo cp -r website/* /var/www/html/
```

Check:

```bash
ls -lah /var/www/html/
```

Set ownership:

```bash
sudo chown -R root:apache /var/www/html
```

Directory permissions:

```bash
sudo find /var/www/html -type d -exec chmod 755 {} \;
```

File permissions:

```bash
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

Restart:

```bash
sudo systemctl restart httpd
```

Test:

```bash
curl http://localhost
```

Open:

```text
http://PUBLIC-IP
```

---

# 44. Networking Commands

Check interfaces:

```bash
ip addr
```

Short version:

```bash
ip a
```

Routing:

```bash
ip route
```

IP:

```bash
hostname -I
```

Test connectivity:

```bash
ping -c 4 8.8.8.8
```

DNS:

```bash
ping -c 4 google.com
```

HTTP:

```bash
curl http://localhost
```

Headers:

```bash
curl -I http://localhost
```

Ports:

```bash
ss -tulpn
```

Apache:

```bash
sudo ss -lntp | grep :80
```

Database:

```bash
sudo ss -lntp | grep :3306
```

---

# 45. DNS Commands

Install utilities if necessary:

```bash
sudo dnf install bind-utils -y
```

Use:

```bash
nslookup google.com
```

```bash
dig google.com
```

```bash
host google.com
```

---

# 46. Test Database Connectivity from CLI

```bash
mysql \
-u webapp \
-p \
-h localhost \
student_portal
```

Enter:

```text
Student@12345
```

Then:

```sql
SHOW TABLES;
```

```sql
SELECT * FROM students;
```

---

# 47. Test Port 3306

Install Netcat if necessary.

Then:

```bash
nc -zv localhost 3306
```

This helps understand:

```text
Application
     |
     v
TCP Port
     |
     v
Database Service
```

---

# 48. Process Management

Display processes:

```bash
ps
```

All:

```bash
ps aux
```

Apache:

```bash
ps aux | grep httpd
```

MariaDB:

```bash
ps aux | grep maria
```

Find PID:

```bash
pgrep httpd
```

```bash
pgrep -a mariadbd
```

Interactive monitoring:

```bash
top
```

Kill a process:

```bash
kill PID
```

Force:

```bash
kill -9 PID
```

Normally services should be restarted using `systemctl` rather than killing their processes manually.

---

# 49. Apache Logs

Access log:

```bash
sudo tail /var/log/httpd/access_log
```

Live:

```bash
sudo tail -f /var/log/httpd/access_log
```

Error log:

```bash
sudo tail -f /var/log/httpd/error_log
```

Last 50 lines:

```bash
sudo tail -50 /var/log/httpd/error_log
```

---

# 50. systemd Logs

Apache:

```bash
sudo journalctl -u httpd
```

Latest 50:

```bash
sudo journalctl -u httpd -n 50
```

Live:

```bash
sudo journalctl -u httpd -f
```

MariaDB:

```bash
sudo journalctl -u mariadb
```

Live:

```bash
sudo journalctl -u mariadb -f
```

---

# 51. Disk Monitoring

```bash
df -h
```

Database size:

```bash
sudo du -sh /var/lib/mysql
```

Website:

```bash
du -sh /var/www/html
```

Logs:

```bash
sudo du -sh /var/log/*
```

Disks:

```bash
lsblk
```

Mounts:

```bash
mount
```

---

# 52. Memory Monitoring

```bash
free -h
```

Processes:

```bash
top
```

Uptime/load:

```bash
uptime
```

---

# 53. Linux Search Commands

Find Apache configuration:

```bash
sudo find /etc -name "httpd.conf"
```

Find PHP:

```bash
sudo find /etc -name "php.ini"
```

Find MariaDB files:

```bash
sudo find /etc -iname "*maria*"
```

Search Apache configuration:

```bash
grep -n "DocumentRoot" /etc/httpd/conf/httpd.conf
```

Search PHP:

```bash
grep "memory_limit" /etc/php.ini
```

---

# 54. Important Linux Locations

```text
/etc/
Linux configuration files

/home/
User home directories

/var/
Variable application data

/var/www/html/
Apache website files

/var/log/
System logs

/var/log/httpd/
Apache logs

/etc/httpd/
Apache configuration

/etc/php.ini
PHP configuration

/var/lib/mysql/
MariaDB data

/etc/my.cnf
MariaDB/MySQL configuration

/etc/systemd/
Systemd configuration

/tmp/
Temporary files

/opt/
Optional applications/backups
```

---

# 55. Create Website Backup Script

Create:

```bash
vi scripts/backup_website.sh
```

Add:

```bash
#!/bin/bash

SOURCE="/var/www/html"

BACKUP_DIR="/opt/backups/website"

DATE=$(date +%Y-%m-%d_%H-%M-%S)

mkdir -p "$BACKUP_DIR"

tar -czf \
"$BACKUP_DIR/website_$DATE.tar.gz" \
"$SOURCE"

if [ $? -eq 0 ]
then
    echo "Website backup successful."
else
    echo "Website backup failed."
fi
```

Permission:

```bash
chmod +x scripts/backup_website.sh
```

Run:

```bash
sudo ./scripts/backup_website.sh
```

Check:

```bash
ls -lh /opt/backups/website
```

---

# 56. Create Database Backup Script

Create:

```bash
vi scripts/backup_database.sh
```

Add:

```bash
#!/bin/bash

DATABASE="student_portal"

BACKUP_DIR="/opt/backups/database"

DATE=$(date +%Y-%m-%d_%H-%M-%S)

mkdir -p "$BACKUP_DIR"

mysqldump "$DATABASE" \
> "$BACKUP_DIR/student_portal_$DATE.sql"

if [ $? -eq 0 ]
then
    echo "Database backup successful."
else
    echo "Database backup failed."
fi
```

Make executable:

```bash
chmod +x scripts/backup_database.sh
```

Run with an appropriately authenticated database account:

```bash
sudo ./scripts/backup_database.sh
```

Check:

```bash
ls -lh /opt/backups/database
```

---

# 57. Database Restore

Check backups:

```bash
ls -lh /opt/backups/database/
```

Restore example:

```bash
mysql student_portal \
< /opt/backups/database/student_portal_2026-01-01_02-00-00.sql
```

Verify:

```bash
mysql -e "SELECT * FROM student_portal.students;"
```

---

# 58. Health Check Script

Create:

```bash
vi scripts/health_check.sh
```

Add:

```bash
#!/bin/bash

echo "======================================"

echo " Enterprise Linux Application Health"

echo "======================================"

echo

echo "Hostname:"
hostname

echo

echo "Operating System:"
cat /etc/os-release | grep PRETTY_NAME

echo

echo "Apache Status:"

if systemctl is-active --quiet httpd
then
    echo "RUNNING"
else
    echo "DOWN"
fi

echo

echo "MariaDB Status:"

if systemctl is-active --quiet mariadb
then
    echo "RUNNING"
else
    echo "DOWN"
fi

echo

echo "HTTP Test:"

if curl -s http://localhost > /dev/null
then
    echo "Website Accessible"
else
    echo "Website Failed"
fi

echo

echo "Port 80:"

if ss -lnt | grep -q ':80'
then
    echo "LISTENING"
else
    echo "NOT LISTENING"
fi

echo

echo "Port 3306:"

if ss -lnt | grep -q ':3306'
then
    echo "LISTENING"
else
    echo "NOT LISTENING"
fi

echo

echo "Memory:"

free -h

echo

echo "Disk:"

df -h /

echo

echo "System Uptime:"

uptime

echo

echo "======================================"
```

Make executable:

```bash
chmod +x scripts/health_check.sh
```

Run:

```bash
./scripts/health_check.sh
```

---

# 59. Create System Report Script

Create:

```bash
vi scripts/system_report.sh
```

Add:

```bash
#!/bin/bash

echo "===== SYSTEM REPORT ====="

echo

echo "Date:"
date

echo

echo "Hostname:"
hostname

echo

echo "Kernel:"
uname -r

echo

echo "OS:"
cat /etc/os-release | grep PRETTY_NAME

echo

echo "Uptime:"
uptime

echo

echo "Memory:"
free -h

echo

echo "Disk:"
df -h

echo

echo "IP:"
hostname -I

echo

echo "Apache:"
systemctl is-active httpd

echo

echo "MariaDB:"
systemctl is-active mariadb

echo

echo "Listening Ports:"
ss -lnt

echo

echo "========================="
```

Run:

```bash
chmod +x scripts/system_report.sh
```

```bash
./scripts/system_report.sh
```

---

# 60. Cron Installation

Install:

```bash
sudo dnf install cronie -y
```

Enable:

```bash
sudo systemctl enable --now crond
```

Status:

```bash
systemctl status crond
```

---

# 61. Schedule Website Backup

Edit root cron:

```bash
sudo crontab -e
```

Add:

```cron
0 1 * * * /home/ec2-user/linux-lamp-project/scripts/backup_website.sh >> /var/log/website-backup.log 2>&1
```

Runs:

```text
Every day at 1:00 AM
```

---

# 62. Schedule Database Backup

Add:

```cron
0 2 * * * /home/ec2-user/linux-lamp-project/scripts/backup_database.sh >> /var/log/database-backup.log 2>&1
```

Runs:

```text
Every day at 2:00 AM
```

Check:

```bash
sudo crontab -l
```

---

# 63. Cron Format

```text
* * * * * command
| | | | |
| | | | +---- Day of Week
| | | +------ Month
| | +-------- Day of Month
| +---------- Hour
+------------ Minute
```

Example:

```cron
30 6 * * * command
```

Means:

```text
Every day at 6:30 AM
```

---

# 64. Compression Commands

Create TAR archive:

```bash
tar -cvf website.tar /var/www/html
```

Compressed:

```bash
tar -czvf website.tar.gz /var/www/html
```

Extract:

```bash
tar -xzvf website.tar.gz
```

Gzip:

```bash
gzip file.txt
```

Decompress:

```bash
gunzip file.txt.gz
```

---

# 65. Firewall — Fedora

Check:

```bash
sudo firewall-cmd --state
```

Allow HTTP:

```bash
sudo firewall-cmd \
--permanent \
--add-service=http
```

Allow HTTPS:

```bash
sudo firewall-cmd \
--permanent \
--add-service=https
```

Reload:

```bash
sudo firewall-cmd --reload
```

Check:

```bash
sudo firewall-cmd --list-all
```

On AWS, also configure the EC2 Security Group.

---

# 66. Security Best Practices

Students should understand the following:

* Do not expose port 3306 publicly.
* Do not use database root from PHP.
* Use a dedicated database user.
* Grant minimum permissions.
* Restrict SSH to trusted IP addresses.
* Do not run the website as root.
* Use proper filesystem permissions.
* Use prepared SQL statements.
* Escape HTML output.
* Do not commit passwords into GitHub.
* Use environment variables or a secrets manager in production.
* Keep the OS updated.
* Monitor logs.
* Backup regularly.
* Test backup restoration.
* Remove unnecessary packages/services.
* Use HTTPS for production applications.

---

# 67. Apache Troubleshooting

Check:

```bash
systemctl status httpd
```

Logs:

```bash
sudo journalctl -xeu httpd
```

Configuration:

```bash
sudo apachectl configtest
```

Expected:

```text
Syntax OK
```

Check port:

```bash
sudo ss -lntp | grep :80
```

Check website:

```bash
curl http://localhost
```

---

# 68. MariaDB Troubleshooting

Check:

```bash
systemctl status mariadb
```

Logs:

```bash
sudo journalctl -xeu mariadb
```

Port:

```bash
sudo ss -lntp | grep :3306
```

Test login:

```bash
mysql -u webapp -p student_portal
```

---

# 69. Troubleshooting — Access Denied

Error:

```text
Access denied for user
```

Login as administrator:

```bash
sudo mysql
```

Check accounts:

```sql
SELECT User,Host
FROM mysql.user;
```

Check grants:

```sql
SHOW GRANTS FOR 'webapp'@'localhost';
```

---

# 70. Troubleshooting — Connection Refused

Check database service:

```bash
systemctl status mariadb
```

Check port:

```bash
ss -lntp | grep 3306
```

Logs:

```bash
sudo journalctl -u mariadb -n 50
```

Start:

```bash
sudo systemctl start mariadb
```

---

# 71. Troubleshooting — Website Doesn't Open

Follow:

```text
Browser
   |
   v
Security Group
   |
   v
Port 80
   |
   v
Apache
   |
   v
PHP
   |
   v
Application
```

Commands:

```bash
ping SERVER-IP
```

```bash
curl http://localhost
```

```bash
systemctl status httpd
```

```bash
ss -lntp | grep :80
```

```bash
sudo journalctl -u httpd
```

```bash
sudo tail -50 /var/log/httpd/error_log
```

---

# 72. Troubleshooting — Website Works but Database Doesn't

Use this sequence:

```text
Check MariaDB service
        |
        v
Check port 3306
        |
        v
Test MySQL CLI
        |
        v
Check database
        |
        v
Check DB user
        |
        v
Check privileges
        |
        v
Check PHP mysqli
        |
        v
Check Apache logs
```

Commands:

```bash
systemctl status mariadb
```

```bash
ss -lntp | grep 3306
```

```bash
mysql -u webapp -p student_portal
```

```bash
php -m | grep mysqli
```

```bash
tail /var/log/httpd/error_log
```

---

# 73. Troubleshooting — Port 80 Already Used

Check:

```bash
sudo ss -lntp | grep :80
```

Alternative:

```bash
sudo lsof -i :80
```

If Nginx is using port 80:

```bash
sudo systemctl stop nginx
```

Restart Apache:

```bash
sudo systemctl restart httpd
```

---

# 74. Troubleshooting — Permission Denied

Check:

```bash
ls -ld /var/www/html
```

```bash
ls -l /var/www/html
```

Fix ownership:

```bash
sudo chown -R root:apache /var/www/html
```

Fix directories:

```bash
sudo find /var/www/html -type d -exec chmod 755 {} \;
```

Fix files:

```bash
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

---

# 75. Optional Advanced Architecture

After completing the single-server project, separate the web and database servers.

```text
                        INTERNET
                            |
                            v
                    +---------------+
                    | Web Security  |
                    | Group         |
                    | 80 / 443      |
                    +-------+-------+
                            |
                            v
                   +----------------+
                   | EC2 Web Server |
                   |                |
                   | Apache         |
                   | PHP            |
                   | 10.0.1.10      |
                   +-------+--------+
                           |
                           | TCP 3306
                           |
                           v
                   +----------------+
                   | DB Server      |
                   |                |
                   | MariaDB        |
                   | 10.0.2.10      |
                   +----------------+
```

---

# 76. Two-Server Security Group Design

## Web Server

```text
SSH 22
Source: Administrator IP

HTTP 80
Source: Internet

HTTPS 443
Source: Internet
```

## Database Server

```text
MySQL 3306
Source:
Web Server Security Group only
```

Do not use:

```text
3306
0.0.0.0/0
```

---

# 77. Remote Database Connectivity

From web server:

```bash
nc -zv 10.0.2.10 3306
```

Connect:

```bash
mysql \
-h 10.0.2.10 \
-u webapp \
-p \
student_portal
```

PHP:

```php
$host = "10.0.2.10";
```

Students now practice:

* Private IP addressing
* TCP ports
* Security groups
* Network connectivity
* Remote database authentication

---

# 78. Git Configuration

Install:

```bash
sudo dnf install git -y
```

Verify:

```bash
git --version
```

Configure:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

---

# 79. Initialize Git Repository

Inside project:

```bash
git init
```

Check:

```bash
git status
```

Add:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial Linux web database project"
```

---

# 80. Recommended .gitignore

Create:

```bash
vi .gitignore
```

Add:

```gitignore
*.log
*.sql.gz
backups/*
.env
.env.*
config.local.php
```

Do not upload real secrets.

---

# 81. Push to GitHub

Repository:

```text
linux-lamp-project
```

Then:

```bash
git branch -M main
```

```bash
git remote add origin \
https://github.com/atulkamble/linux-lamp-project.git
```

```bash
git push -u origin main
```

---

# 82. Useful Linux Commands Practiced

## File Management

```text
pwd
ls
cd
mkdir
touch
cp
mv
rm
cat
less
head
tail
find
grep
```

## User Management

```text
whoami
id
useradd
usermod
passwd
groupadd
groups
```

## Permissions

```text
chmod
chown
chgrp
```

## System Information

```text
hostname
hostnamectl
uname
uptime
date
lscpu
free
df
```

## Packages

```text
dnf
rpm
```

## Processes

```text
ps
top
pgrep
kill
pkill
```

## Services

```text
systemctl
journalctl
```

## Networking

```text
ip
ping
curl
wget
ss
nc
dig
nslookup
host
```

## Storage

```text
df
du
lsblk
mount
```

## Compression

```text
tar
gzip
gunzip
```

## Automation

```text
bash
crontab
```

## Database

```text
mysql
mysqldump
```

---

# 83. SQL Commands Practiced

```text
CREATE DATABASE
CREATE TABLE
CREATE USER
GRANT
SHOW DATABASES
SHOW TABLES
SHOW GRANTS
DESCRIBE
SELECT
INSERT
UPDATE
DELETE
WHERE
ORDER BY
COUNT
```

---

# 84. Complete Project Workflow

```text
01. Launch Linux Server
        |
        v
02. Connect using SSH
        |
        v
03. Explore Linux OS
        |
        v
04. Practice files/directories
        |
        v
05. Create users/groups
        |
        v
06. Configure permissions
        |
        v
07. Install Apache
        |
        v
08. Manage httpd service
        |
        v
09. Install PHP
        |
        v
10. Install MariaDB
        |
        v
11. Secure database
        |
        v
12. Create database
        |
        v
13. Create students table
        |
        v
14. Create webapp DB user
        |
        v
15. Configure least privilege
        |
        v
16. Create PHP application
        |
        v
17. Connect PHP to MariaDB
        |
        v
18. Perform CRUD
        |
        v
19. Deploy under /var/www/html
        |
        v
20. Configure ownership/permissions
        |
        v
21. Test HTTP connectivity
        |
        v
22. Test database connectivity
        |
        v
23. Analyze logs
        |
        v
24. Monitor processes
        |
        v
25. Monitor disk/memory
        |
        v
26. Create Bash scripts
        |
        v
27. Backup website
        |
        v
28. Backup database
        |
        v
29. Configure Cron
        |
        v
30. Test database restore
        |
        v
31. Practice failure scenarios
        |
        v
32. Troubleshoot
        |
        v
33. Push project to GitHub
```

---

# 85. Student Practice Tasks

Students should intentionally break and repair the environment.

## Task 1

Stop Apache:

```bash
sudo systemctl stop httpd
```

Try:

```bash
curl http://localhost
```

Find the problem and fix it.

---

## Task 2

Stop MariaDB:

```bash
sudo systemctl stop mariadb
```

Open the application.

Observe the database failure.

Troubleshoot and fix.

---

## Task 3

Change permissions:

```bash
sudo chmod 000 /var/www/html/index.php
```

Try opening the website.

Investigate logs.

Restore:

```bash
sudo chmod 644 /var/www/html/index.php
```

---

## Task 4

Check which service owns port 80:

```bash
sudo ss -lntp | grep :80
```

---

## Task 5

Find Apache configuration:

```bash
sudo find /etc -name httpd.conf
```

---

## Task 6

Find the five largest directories:

```bash
sudo du -sh /* 2>/dev/null | sort -h | tail
```

---

## Task 7

Find failed services:

```bash
systemctl --failed
```

---

## Task 8

Generate HTTP requests:

```bash
for i in {1..20}
do
    curl -s http://localhost > /dev/null
done
```

Then:

```bash
sudo tail /var/log/httpd/access_log
```

---

## Task 9

Perform database backup.

Then intentionally delete a record:

```sql
DELETE FROM students;
```

Restore database from backup.

---

## Task 10

Configure automated backup using Cron.

Confirm:

```bash
sudo crontab -l
```

---

# 86. Interview Questions from This Project

Students should be able to answer:

### Linux

1. What is Amazon Linux?
2. What is Fedora?
3. What is a Linux distribution?
4. What is a kernel?
5. What does `/etc/os-release` contain?
6. Difference between `root` and normal users?
7. What is `sudo`?
8. What is the purpose of `/var`?
9. What is `/etc`?
10. What is `/var/log`?

### Permissions

11. What does `chmod 755` mean?
12. Difference between `chmod` and `chown`?
13. What are owner, group, and others?
14. What do read, write, and execute permissions mean?

### Packages

15. What is DNF?
16. What is RPM?
17. Difference between DNF and RPM?

### systemd

18. What is systemd?
19. What is `systemctl`?
20. Difference between `start` and `enable`?
21. How do you check whether a service is active?

### Apache

22. What is Apache?
23. What is the default Apache HTTP port?
24. What is `/var/www/html`?
25. Where are Apache logs stored?
26. How do you troubleshoot Apache?

### Database

27. What is MariaDB?
28. Difference between MySQL and MariaDB?
29. What port does MySQL use?
30. What is a database user?
31. What is the purpose of `GRANT`?
32. Why should an application avoid using root?
33. What is least privilege?
34. What is `mysqldump`?

### Networking

35. Difference between `ip addr` and `ip route`?
36. What does `ss` do?
37. What is port 80?
38. What is port 3306?
39. What is `curl`?
40. What is `nc`?

### Logs

41. What is `journalctl`?
42. How do you view Apache error logs?
43. Difference between an access log and error log?

### Automation

44. What is Bash?
45. What is Cron?
46. Explain `0 2 * * *`.
47. How would you automate database backups?

### Troubleshooting

48. Website isn't opening. What do you check?
49. Apache is running but website isn't reachable externally. Why?
50. Website loads but cannot connect to the database. What do you check?

---

# 87. Resume Project Description

After completing the lab, students can add:

## Enterprise Linux Web & Database Administration Project

* Deployed and administered an Apache web server on Amazon Linux 2023/Fedora.
* Installed and configured PHP and MariaDB/MySQL for a database-driven web application.
* Developed and deployed a Student Management Portal supporting CRUD operations.
* Created relational database tables, database users, and least-privilege permissions.
* Configured Linux users, groups, ownership, and filesystem permissions.
* Managed Linux services using `systemctl` and investigated failures with `journalctl`.
* Performed Linux networking and port troubleshooting using `ip`, `ss`, `ping`, `curl`, `nc`, `dig`, and `nslookup`.
* Monitored Linux processes, memory, disk utilization, services, and TCP ports.
* Developed Bash scripts for health monitoring, system reporting, website backup, and database backup.
* Scheduled automated backup operations using Cron.
* Performed MariaDB/MySQL backup and restore operations using `mysqldump`.
* Investigated Apache access/error logs and database service logs.
* Used Git and GitHub for source-code and documentation management.
* Practiced real-world Linux troubleshooting involving services, ports, permissions, networking, web servers, databases, and logs.

---

# 88. Skills Demonstrated

After completion, students can demonstrate:

```text
Linux Administration
Amazon Linux 2023
Fedora
AWS EC2
SSH
Linux Filesystem
Linux Users
Linux Groups
Linux Permissions
DNF
RPM
systemd
systemctl
Apache HTTP Server
PHP
MariaDB
MySQL
SQL
CRUD
Linux Networking
TCP/IP
Ports
DNS
curl
Netcat
Linux Processes
Logs
journalctl
Disk Management
Memory Monitoring
Bash Scripting
Cron
Backup
Restore
Troubleshooting
Git
GitHub
```

---

# 89. Final Architecture Summary

```text
                     USER / BROWSER
                           |
                           |
                         HTTP
                        PORT 80
                           |
                           v
                +---------------------+
                |   AWS EC2 / Linux   |
                | Amazon Linux/Fedora |
                +----------+----------+
                           |
                           v
                +---------------------+
                | Apache HTTP Server  |
                |      httpd          |
                +----------+----------+
                           |
                           v
                +---------------------+
                | PHP Application     |
                | Student Portal      |
                +----------+----------+
                           |
                        mysqli
                           |
                           v
                +---------------------+
                | MariaDB / MySQL     |
                | Port 3306           |
                | student_portal      |
                +----------+----------+
                           |
                           v
                    +-------------+
                    | students    |
                    | table       |
                    +-------------+

Linux Administration surrounding the application:

Users + Groups
      |
Permissions
      |
systemd
      |
Processes
      |
Networking
      |
Logs
      |
Bash Scripts
      |
Cron
      |
Backups
      |
Monitoring
      |
Troubleshooting
```

---

# 90. Learning Outcome

By completing this project, students gain practical experience administering a Linux-based application environment rather than only memorizing commands.

Students practice commands in context:

```text
COMMAND
   +
REAL SERVICE
   +
REAL APPLICATION
   +
REAL DATABASE
   +
REAL FAILURE
   +
TROUBLESHOOTING
```

This project can serve as a strong beginner-to-intermediate portfolio project for:

* Linux Administrator
* Linux Support Engineer
* AWS Cloud Engineer
* Cloud Support Engineer
* DevOps Engineer
* Junior DevOps Engineer
* System Administrator
* Infrastructure Engineer
* Technical Support Engineer

---

# 91. Recommended Next-Level Enhancements

After completing the base project, students can extend it with:

1. HTTPS using SSL/TLS
2. Apache Virtual Hosts
3. Custom domain
4. AWS Route 53
5. Separate database server
6. Amazon RDS
7. AWS Application Load Balancer
8. Auto Scaling
9. CloudWatch monitoring
10. SELinux practice
11. `firewalld`
12. Logrotate
13. Database replication
14. Environment variables
15. AWS Secrets Manager
16. GitHub Actions
17. Jenkins CI/CD
18. Docker
19. Terraform
20. Ansible

A useful progression is:

```text
Linux
  ↓
Apache
  ↓
PHP
  ↓
MariaDB
  ↓
Bash
  ↓
Git
  ↓
Docker
  ↓
CI/CD
  ↓
Terraform
  ↓
AWS Architecture
```

---

# 92. Conclusion

This project provides an end-to-end practical environment for learning Linux administration.

Instead of practicing isolated commands such as:

```bash
systemctl
chmod
chown
ps
ss
curl
journalctl
df
free
mysqldump
crontab
```

students use them together to deploy, operate, monitor, secure, automate, backup, and troubleshoot a real database-driven web application.

The completed project demonstrates practical knowledge of:

```text
Linux System Administration
+
Web Server Administration
+
Database Administration
+
Networking
+
Security
+
Automation
+
Monitoring
+
Troubleshooting
+
Git/GitHub
```

That makes the project suitable for both **hands-on Linux training and a student GitHub/resume portfolio**.

---

# 93. More Info

**GitHub Repository**

```text
https://github.com/atulkamble/linux-lamp-project
```

Clone it:

```bash
git clone https://github.com/atulkamble/linux-lamp-project.git
```

Report issues or suggest improvements via GitHub Issues on the repository above.

**Author**: Atul Kamble

**License**: [MIT](LICENSE)
