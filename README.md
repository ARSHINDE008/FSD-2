# Student Management API - Experiment 13

## Overview
A complete full-stack web application for managing student records with CRUD operations, input validation, and MySQL database integration. This project demonstrates best practices in API design, database management, and data validation.

**Student Name:** [Your Name]  
**Roll Number:** [Your Roll Number]  
**Class:** [Your Class]

---

## Project Structure

```
Experiment-13/
├── app.py                                  # Main Flask application
├── requirements.txt                        # Python dependencies
├── README.md                               # Project documentation
└── SCREENSHOTS/                            # Testing screenshots
    ├── 1_server_status.png
    ├── 2_create_student.png
    ├── 3_get_all_students.png
    ├── 4_get_student_by_id.png
    ├── 5_update_student.png
    ├── 6_delete_student.png
    ├── 7_search_by_uid.png
    ├── 8_filter_by_course.png
    └── 9_database_table.png
```

---

## Features

### ✅ CRUD Operations
- **CREATE**: Add new students with validation
- **READ**: Retrieve all students or specific students with pagination
- **UPDATE**: Modify existing student records (partial update supported)
- **DELETE**: Remove student records

### ✅ Data Validation
- **UID**: Unique identifier (required, 1-20 chars)
- **Name**: Student name (required, 2-100 chars)
- **Email**: Valid email format (optional, unique)
- **Age**: Between 5-120 years (required)
- **Course**: Course name (optional, 2-100 chars)

### ✅ Advanced Features
- Search students by UID
- Filter students by course
- Pagination support (page, per_page)
- Timestamp tracking (created_at, updated_at)
- Comprehensive error handling
- MySQL database with proper indexing

---

## Prerequisites

- **Python 3.8+**
- **MySQL 5.7+**
- **Postman** (for API testing)

---

## Setup Instructions

### 1. Create MySQL Database

Open MySQL command line or MySQL Workbench and run:

```sql
CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;
```

### 2. Install Python Dependencies

```bash
# Navigate to project directory
cd Experiment-13

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database Connection (Optional)

Default credentials: root user with no password
To use different credentials, set environment variables:

```bash
# On Windows Command Prompt:
set MYSQL_HOST=localhost
set MYSQL_USER=root
set MYSQL_PASSWORD=your_password
set MYSQL_DB=student_management
set MYSQL_PORT=3306

# On Windows PowerShell:
$env:MYSQL_HOST = "localhost"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your_password"

# On macOS/Linux:
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DB=student_management
```

### 4. Run the Application

```bash
python app.py
```

Expected output:
```
✓ Database tables initialized successfully
 * Running on http://0.0.0.0:5000
 * Serving Flask app 'app'
 * Debug mode: on
```

---

## API Endpoints

### Base URL
```
http://localhost:5000
```

### 1. **Health Check / Home**
```
GET /
```

**Response (200 OK):**
```json
{
    "message": "Student Management API",
    "status": "running",
    "version": "1.0.0"
}
```

---

### 2. **Create Student**
```
POST /students
Content-Type: application/json
```

**Request Body:**
```json
{
    "uid": "23BIS70001",
    "name": "Arshinder Singh",
    "email": "arshinder@example.com",
    "age": 20,
    "course": "B.Tech CSE"
}
```

**Response (201 Created):**
```json
{
    "message": "Student created successfully",
    "student": {
        "id": 1,
        "uid": "23BIS70001",
        "name": "Arshinder Singh",
        "email": "arshinder@example.com",
        "age": 20,
        "course": "B.Tech CSE",
        "created_at": "2024-01-15T10:30:00",
        "updated_at": "2024-01-15T10:30:00"
    }
}
```

**Error Response (400 Bad Request):**
```json
{
    "error": "Validation failed",
    "details": {
        "age": ["Must be between 5 and 120."]
    }
}
```

---

### 3. **Get All Students**
```
GET /students?page=1&per_page=10
```

**Response (200 OK):**
```json
{
    "message": "Students retrieved successfully",
    "total": 5,
    "page": 1,
    "per_page": 10,
    "total_pages": 1,
    "students": [
        {
            "id": 1,
            "uid": "23BIS70001",
            "name": "Arshinder Singh",
            "email": "arshinder@example.com",
            "age": 20,
            "course": "B.Tech CSE",
            "created_at": "2024-01-15T10:30:00",
            "updated_at": "2024-01-15T10:30:00"
        }
    ]
}
```

---

### 4. **Get Student by ID**
```
GET /students/{id}
```

**Response (200 OK):**
```json
{
    "message": "Student retrieved successfully",
    "student": {
        "id": 1,
        "uid": "23BIS70001",
        "name": "Arshinder Singh",
        "email": "arshinder@example.com",
        "age": 20,
        "course": "B.Tech CSE",
        "created_at": "2024-01-15T10:30:00",
        "updated_at": "2024-01-15T10:30:00"
    }
}
```

**Error Response (404 Not Found):**
```json
{
    "error": "Student not found"
}
```

---

### 5. **Update Student**
```
PUT /students/{id}
Content-Type: application/json
```

**Request Body (partial update allowed):**
```json
{
    "name": "Arshinder Singh Updated",
    "age": 21,
    "course": "B.Tech IT"
}
```

**Response (200 OK):**
```json
{
    "message": "Student updated successfully",
    "student": {
        "id": 1,
        "uid": "23BIS70001",
        "name": "Arshinder Singh Updated",
        "email": "arshinder@example.com",
        "age": 21,
        "course": "B.Tech IT",
        "created_at": "2024-01-15T10:30:00",
        "updated_at": "2024-01-15T10:35:00"
    }
}
```

---

### 6. **Delete Student**
```
DELETE /students/{id}
```

**Response (200 OK):**
```json
{
    "message": "Student deleted successfully",
    "deleted_student": {
        "id": 1,
        "uid": "23BIS70001",
        "name": "Arshinder Singh",
        "email": "arshinder@example.com",
        "age": 20,
        "course": "B.Tech CSE",
        "created_at": "2024-01-15T10:30:00",
        "updated_at": "2024-01-15T10:35:00"
    }
}
```

---

### 7. **Search Student by UID**
```
GET /students/search/uid/{uid}
```

**Response (200 OK):**
```json
{
    "message": "Student found",
    "student": { /* student object */ }
}
```

---

### 8. **Filter Students by Course**
```
GET /students/filter/course/{course}
```

**Response (200 OK):**
```json
{
    "message": "Students retrieved successfully",
    "count": 3,
    "students": [ /* array of student objects */ ]
}
```

---

## Validation Rules

| Field | Type | Required | Rules | Example |
|-------|------|----------|-------|---------|
| uid | String | Yes | 1-20 characters, unique | "23BIS70001" |
| name | String | Yes | 2-100 characters | "Arshinder Singh" |
| email | Email | No | Valid email format, unique | "arshinder@example.com" |
| age | Integer | Yes | 5-120 years | 20 |
| course | String | No | 2-100 characters | "B.Tech CSE" |

---

## HTTP Status Codes

| Code | Meaning | Scenario |
|------|---------|----------|
| 200 | OK | Successful GET, PUT, DELETE |
| 201 | Created | Successful POST |
| 400 | Bad Request | Validation error or duplicate unique field |
| 404 | Not Found | Student ID doesn't exist |
| 500 | Server Error | Database or server error |

---

## Error Handling

### 1. Validation Error
```json
{
    "error": "Validation failed",
    "details": {
        "name": ["Shorter than minimum length 2."],
        "age": ["Must be between 5 and 120."]
    }
}
```

### 2. Duplicate UID
```json
{
    "error": "Student with this UID already exists"
}
```

### 3. Not Found
```json
{
    "error": "Student not found"
}
```

### 4. Server Error
```json
{
    "error": "Server error: [error details]"
}
```

---

## Testing with Postman

### 1. Import Collection (Optional)
- File: `Experiment-13.postman_collection.json`
- Actions: File → Import → Select the JSON file

### 2. Manual Testing Steps

**Step 1: Server Status**
```
GET http://localhost:5000/
```

**Step 2: Create Multiple Students**
```
POST http://localhost:5000/students
Content-Type: application/json

{
    "uid": "23BIS70001",
    "name": "Arshinder Singh",
    "email": "arshinder@google.com",
    "age": 20,
    "course": "B.Tech CSE"
}
```

**Step 3: Get All Students**
```
GET http://localhost:5000/students
```

**Step 4: Get Specific Student**
```
GET http://localhost:5000/students/1
```

**Step 5: Update Student**
```
PUT http://localhost:5000/students/1
Content-Type: application/json

{
    "age": 21,
    "course": "B.Tech IT"
}
```

**Step 6: Search by UID**
```
GET http://localhost:5000/students/search/uid/23BIS70001
```

**Step 7: Filter by Course**
```
GET http://localhost:5000/students/filter/course/B.Tech CSE
```

**Step 8: Delete Student**
```
DELETE http://localhost:5000/students/1
```

---

## Database Schema

### Student Table Structure

```sql
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uid VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT NOT NULL,
    course VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    KEY idx_uid (uid)
);
```

### Field Descriptions

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique student identifier |
| uid | VARCHAR(20) | UNIQUE, NOT NULL | University ID (roll number) |
| name | VARCHAR(100) | NOT NULL | Student's full name |
| email | VARCHAR(100) | UNIQUE, NULL | Student's email address |
| age | INT | NOT NULL | Student's age |
| course | VARCHAR(100) | NULL | Enrolled course/program |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP | Last update timestamp |

---

## Technologies Used

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.8+ | Programming language |
| Flask | 2.3.3 | Web framework |
| Flask-SQLAlchemy | 3.0.5 | ORM |
| SQLAlchemy | 2.0.23 | Database abstraction |
| Marshmallow | 3.20.1 | Validation library |
| PyMySQL | 1.1.0 | MySQL driver |
| MySQL | 5.7+ | Database |

---

## Troubleshooting

### Problem: "Access denied for user 'root'@'localhost'"
**Solution:** 
- Update MySQL credentials in app.py
- Or set environment variables with correct password

### Problem: "Database 'student_management' doesn't exist"
**Solution:** Create database using SQL:
```sql
CREATE DATABASE student_management;
```

### Problem: "Port 5000 already in use"
**Solution:** 
- Change port in app.py: `app.run(port=5001)`
- Or stop the process using port 5000

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Install requirements:
```bash
pip install -r requirements.txt
```

### Problem: Connection timeout
**Solution:** 
- Ensure MySQL server is running
- Check MySQL host and port configuration
- Verify firewall settings

---

## Learning Outcomes

1. ✅ RESTful API design principles and best practices
2. ✅ CRUD operations implementation using Flask
3. ✅ MySQL database design and integration
4. ✅ Input validation using Marshmallow
5. ✅ Error handling and HTTP status codes
6. ✅ API testing with Postman
7. ✅ SQLAlchemy ORM usage
8. ✅ Database relationships and indexing

---

## Files Description

1. **app.py** - Main Flask application containing:
   - Database configuration
   - Student model definition
   - Marshmallow validation schema
   - All CRUD endpoint implementations
   - Error handling

2. **requirements.txt** - Python dependencies:
   - Flask and extensions
   - Database drivers
   - Validation libraries

3. **README.md** - Complete documentation

---

## Future Enhancements

- [ ] User authentication (JWT tokens)
- [ ] Role-based access control
- [ ] Advanced filtering and sorting
- [ ] Swagger/OpenAPI documentation
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] API rate limiting
- [ ] Logging system
- [ ] Deployment to production

---

## Credits

**Developer:** [Your Name]  
**Roll Number:** [Your Roll Number]  
**Institution:** [Your College Name]  
**Date:** January 2024

---

## Contact & Support

For questions or issues, please contact: [email@example.com]

---

## License

This project is for educational purposes only.

---

**Happy Learning! 🚀**
