# HRMS – Human Resource Management System (Django + MySQL)

A **basic yet production-structured HRMS application** built using Django and
Django REST Framework.  
The system manages employees, tracks attendance, and generates
department-wise reports using Django ORM.

This project follows **clean architecture**, **Django best practices**, and
is suitable for academic submissions, interviews, and further extension.

---

## 📌 Project Overview

The HRMS application provides:
- Employee management
- Attendance tracking with duplicate prevention
- Department-wise reporting
- REST APIs for backend operations
- Bootstrap-based responsive UI using Django templates

The project uses **MySQL with mysql-connector-python ONLY** (no mysqlclient).

---

## ✨ Features

- Employee CRUD (via REST API)
- Attendance marking (one record per employee per day)
- Employee detail with attendance history
- Department-wise employee count report
- Clean REST API responses (JSON-based status)
- Bootstrap 5 responsive UI
- Django Admin integration

---

## 🛠 Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Django (latest stable) |
| API          | Django REST Framework |
| Database     | MySQL |
| DB Connector | mysql-connector-python |
| Frontend    | Django Templates + Bootstrap 5 |
| Language     | Python 3.10+ |

---

## 📂 Project Structure

HRMS/
│
├── manage.py
├── requirements.txt
│
├── HRMS/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Employees/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── attendance
│   │   │   ├── attendance_mark.html
│   │   ├── employees
│   │   │   ├── employee_detail.html
│   │   │   ├── employee_list.html
│   │   ├── reports
│   │   │   ├── department_report.html
│   │     
│   └── static/
│           ├── css
│               ├── style.css
│         

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows

# Install the requirements.txt with pip
pip install -r requirements.txt

# Create a MySQL Database 
CREATE DATABASE hrms_db;
CREATE USER 'hrms_user'@'localhost' IDENTIFIED BY 'hrms_password';
GRANT ALL PRIVILEGES ON hrms_db.* TO 'hrms_user'@'localhost';
FLUSH PRIVILEGES;

# Update credentials in settings.py with your database details


# Run this Migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Server
python manage.py runserver

Visit : http://127.0.0.1:8000/

# Check the API's Using Postman or Other API server
API Endpoints
# Employees
POST /api/employees/
# Like this
    # {
    # "name": "John Doe",
    # "email": "john@example.com",
    # "address": "Bangalore",
    # "department": "IT",
    # "designation": "Developer",
    # "date_of_joining": "2023-06-01"
    # }
# You got this Output
    # {
    # "status": "success",
    # "message": "Employee created successfully",
    # "data": {
    #     "id": 1,
    #     "name": "John Doe",
    #     "email": "john@example.com",
    #     "department": "IT"
    # }
    # }


GET /api/employees/
GET /api/employees/<id>/

# Attendance
POST /api/attendance/mark/
GET /api/attendance/<employee_id>/

# Reports
GET /api/reports/department-count/


Final Notes

Uses Django ORM only

No mysqlclient

Attendance duplication prevented at DB + logic level

Clean separation of API and HTML views

This project is intentionally structured to be extended, not rewritten.


---

## FINAL MENTOR VERDICT

You now have:
- A **runnable HRMS**
- Correct MySQL setup (connector-only)
- REST APIs + UI
- Proper Django architecture
- No beginner mistakes left

If something breaks **now**, it’s not design — it’s execution.

If you want:
- Authentication
- Role-based access
- Payroll
- Leave management
- Docker
- Tests

THANKS YOU.
