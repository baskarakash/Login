# FastAPI CRUD Application

## Overview

This FastAPI application demonstrates CRUD (Create, Read, Update, Delete) operations for managing employee records. It includes endpoints for registering, retrieving, updating, and deleting employee information. The application uses SQLAlchemy for database interactions and Pydantic for data validation.

## Project Components

### 1. FastAPI Application (`app/main.py`)

**Purpose**: Serve the API endpoints for employee management.

**Techniques and Tools**:
- **FastAPI**: The web framework used for creating the API.
- **SQLAlchemy**: ORM used for interacting with the PostgreSQL database.
- **Pydantic**: Library used for data validation and serialization.

**Endpoints**:
- **`/register_employee`**: Register a new employee.
- **`/get_employee/{employee_id}`**: Retrieve details of an employee by ID.
- **`/delete_employee/{employee_id}`**: Delete an employee by ID.
- **`/update_employee/{employee_id}`**: Update details of an existing employee.

### 2. Database Models (`app/models/auth_models.py`)

**Purpose**: Define the database schema and interact with the PostgreSQL database.

**Model**:
- **`EmpsModel`**: Represents the employee data structure in the database.

### 3. Schema Definitions (`app/routes/schema.py`)

**Purpose**: Define Pydantic models for data validation and serialization.

**Models**:
- **`UserRegistration`**: Schema for user registration (not used in the current implementation).
- **`EmpRegistration`**: Schema for employee data used in CRUD operations.

### 4. Routes (`app/routes/employee_routes.py`)

**Purpose**: Implement the CRUD operations for managing employee records.

**Endpoints**:
- **`/register_employee`**: Registers a new employee.
- **`/get_employee/{employee_id}`**: Retrieves an employee’s details.
- **`/delete_employee/{employee_id}`**: Deletes an employee.
- **`/update_employee/{employee_id}`**: Updates an employee’s information.

### 5. Settings (`app/settings.py`)

**Purpose**: Configure database settings and provide a function to get a database session.

**Configuration**:
- **Database URL**: Connection string for PostgreSQL.
- **`get_db` function**: Provides a database session for dependency injection.

## How It Works

### 1. Setup

1. **Database Configuration**:
   - Ensure PostgreSQL is running and accessible.
   - Update the `.env` file with your PostgreSQL credentials.

2. **Run Migrations**:
   - Ensure database schema is up-to-date with the latest migrations.

### 2. API Endpoints

1. **Register Employee**:
   - **POST** `/register_employee`
   - **Request Body**: JSON object with `employeename`, `employeeid`, `employeeage`, and `employeesalary`.
   - **Response**: Confirmation message.

2. **Get Employee**:
   - **GET** `/get_employee/{employee_id}`
   - **Response**: Employee details in JSON format.

3. **Delete Employee**:
   - **DELETE** `/delete_employee/{employee_id}`
   - **Response**: Confirmation message.

4. **Update Employee**:
   - **PUT** `/update_employee/{employee_id}`
   - **Request Body**: JSON object with `employeename`, `employeeage`, and `employeesalary`.
   - **Response**: Confirmation message.


