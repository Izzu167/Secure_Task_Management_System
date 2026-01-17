# Secure_Task_Management_System
A secure, scalable solution for managing tasks in an organization.

---

## How to Run

1. **Navigate to the project directory:**
   ```bash
   cd C:\Users\YourName\Path\To\SecureWebProject

2. **Run the application:**
   ```bash
   venv\Scripts\activate (For activated)
   python manage.py runserver

3. Access the application: Open your browser and navigate to http://127.0.0.1:8000/home/.

## Default Credentials

The application seeds a default Administrator account on startup:

- Email: admin
- Password: 1234

## Features

- Role-Based Access Control (RBAC): Admin vs User Non-admin Roles.
- Authorization Checks: Authorization is verified on each endpoint.
- Audit Logs: Admins can see who tried to log in.
- Security: Secure login flow, Password, Session Management & CSRF Protection.
