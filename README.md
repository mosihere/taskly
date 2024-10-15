# Task Management System API

## Overview

The **Taskly** API provides endpoints to manage tasks and users. Users can perform CRUD operations on tasks, and admins have additional privileges to manage users. Authentication is based on **mobile phone numbers and passwords**.

This project demonstrates:
- A custom user model with phone number authentication.
- Task management with CRUD operations.
- Filtering capabilities on task title and creation date.
- Admin-specific privileges like managing users.
- JWT-based token authentication.

## Features

- **Task Management**: Create, read, update, and delete tasks.
- **User Management**: Admins can view and manage all users.
- **Authentication**: Secure token-based authentication using **JWT**.
- **Filtering**: Filter tasks by title and creation date.
- **API Documentation**: Interactive API documentation with **Swagger UI** and static documentation with **Redoc**.

## Technologies Used

- **Django**: Python web framework.
- **Django Rest Framework (DRF)**: For building REST APIs.
- **Djoser**: Handling User Endpoints and Serializers + Views
- **JWT**: For secure authentication.
- **drf-yasg**: For generating interactive API documentation.
- **sqlite**: Default Database.

## Requirements

- Python 3.8+
- Django 3.2+
- Django Rest Framework
- Django Rest Framework SimpleJWT
- drf-yasg (for Swagger and Redoc)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mosihere/taskly.git
```

### 2. Create a Virtual Environment

```bash
cd taskly
python3 -m venv venv
source venv/bin/activate  # For Unix-based systems
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
Your API will be available at: http://127.0.0.1:8000/

### 6. Create a Superuser (Admin)
To access admin-specific features, create a superuser:
```bash
python manage.py createsuperuser
```

### 7. Access the API Documentation

- **Swagger UI**: Interactive API testing at `http://127.0.0.1:8000/swagger/`
- **Redoc**: Static API documentation at `http://127.0.0.1:8000/redoc/`

## Endpoints

### Authentication

- **Login**: `/api/auth/token/login/`
- **Get JWT (Jason Web Token)**: `/api/auth/jwt/create/`

## Important Note

In case you use Browsable Api, After registering and obtaining your JWT from the specified endpoint, ensure that you store it in the browser header. You can use the **ModHeader** extension to manage your headers as follows:

```bash
Authorization: JWT <your_json_web_token>
```
Hint: Simpler to use Swagger Interactive API.
<br>
Also in case you use Postman, Curl or whatever, don't forget to set the JWT in header aswell.
### Task Management

- **GET** `/api/tasks/`: List all tasks (filtered by title or creation date).
- **POST** `/api/tasks/`: Create a new task.
- **GET** `/api/tasks/{id}/`: Retrieve a single task.
- **PUT** `/api/tasks/{id}/`: Update a task.
- **PATCH** `/api/tasks/{id}/`: Partial Update a task.
- **DELETE** `/api/tasks/{id}/`: Delete a task.

### User Management (Admin Only)

- **GET** `/api/auth/users/`: List all users (admin only).
- **GET** `/api/auth/users/{id}/`: Retrieve details of a single user.
- **DELETE** `/api/auth/users/{id}/`: Delete a user (admin only).

### Filtering
Tasks can be filtered by:

* Title: Use the `?title=` query parameter.
* Creation Date: Use the `?created_at=` query parameter.
<br>

example
`GET /api/tasks/?title=meeting&created_at=2024-10-13`


### Testing
Unit tests have been written to ensure that all endpoints function correctly. To run the tests, use the following command:

```bash
python manage.py test
```

### Final Notes:
#### For Simplicity there is no .env file and environment variables<br>

We Don't implement some auth/users/< something > endpoints
<br>
they are exists by default because of using Djoser
<br>

#### Main and necessary endpoints to Manage Users are:
* Create User + Get List of Users By Admins: `/api/auth/users/`
* Create JWT for User, this endpoint let you Get your JWT: `/api/auth/jwt/create/`
* Refresh the Token: `/api/auth/jwt/refresh/`
* CRUD operations (Admin Only): `/api/auth/users/<id>/`
* CRUD (User): `/api/auth/users/me/`
