# Experiment 13 – Connect Backend with Database and Perform CRUD Operations

## 🎯 Objective

Create a backend server in Python (Flask), connect it to a MySQL database, implement CRUD API endpoints for Students, validate inputs using Marshmallow, and test via Postman.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python + Flask | Backend server |
| Flask-SQLAlchemy | ORM for MySQL |
| Marshmallow | Input validation |
| PyMySQL | MySQL driver |
| MySQL | Database |
| Postman | API testing |

---

## 📁 Folder Structure

```
experiment-13/
├── app.py              # Main Flask application with all CRUD routes
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## ⚙️ Setup Instructions

### 1. Create MySQL Database

Open your MySQL client and run:

```sql
CREATE DATABASE chandigarh_university_db;
```

The `student` table is created automatically when the server starts.

### 2. Update Database Credentials

In `app.py`, update the connection string if your MySQL credentials differ:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/chandigarh_university_db'
```

Replace `root` (username) and `root123` (password) with your actual credentials.

### 3. Install Dependencies

```bash
pip install flask flask_sqlalchemy marshmallow pymysql
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python app.py
```

Server runs on: `http://localhost:8000`

---

## 🗃️ Database Table: `student`

| Column | Type | Constraints |
|--------|------|-------------|
| id     | INT  | Primary Key, Auto Increment |
| uid    | VARCHAR(20) | Unique, Not Null |
| name   | VARCHAR(100) | Not Null |
| age    | INT  | Not Null |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/students` | Create a new student |
| `GET` | `/students` | Get all students |
| `GET` | `/students/<id>` | Get a student by ID |
| `PUT` | `/students/<id>` | Update a student by ID |
| `DELETE` | `/students/<id>` | Delete a student by ID |

---

## 📋 Request & Response Examples

### ➕ Create Student — `POST /students`

**Request Body:**
```json
{
  "uid": "21BCS1001",
  "name": "Rahul Sharma",
  "age": 20
}
```

**Response (201):**
```json
{
  "id": 1,
  "uid": "21BCS1001",
  "name": "Rahul Sharma",
  "age": 20
}
```

---

### 📋 Get All Students — `GET /students`

**Response (200):**
```json
[
  {
    "id": 1,
    "uid": "21BCS1001",
    "name": "Rahul Sharma",
    "age": 20
  }
]
```

---

### 🔍 Get Student by ID — `GET /students/1`

**Response (200):**
```json
{
  "id": 1,
  "uid": "21BCS1001",
  "name": "Rahul Sharma",
  "age": 20
}
```

**Response (404):**
```json
{
  "error": "Student not found"
}
```

---

### ✏️ Update Student — `PUT /students/1`

**Request Body (partial update supported):**
```json
{
  "name": "Rahul Kumar",
  "age": 21
}
```

**Response (200):**
```json
{
  "id": 1,
  "uid": "21BCS1001",
  "name": "Rahul Kumar",
  "age": 21
}
```

---

### 🗑️ Delete Student — `DELETE /students/1`

**Response (200):**
```json
{
  "message": "Student deleted successfully"
}
```

---

## ✅ Validation Rules

Input is validated using **Marshmallow** before any database operation:

| Field | Rules |
|-------|-------|
| `uid` | Required, max 20 characters |
| `name` | Required, max 100 characters |
| `age` | Required, must be a positive integer |

**Validation Error Response (400):**
```json
{
  "uid": ["Missing data for required field."],
  "age": ["Not a valid integer."]
}
```

---

## 🧪 Testing with Postman

1. Open Postman
2. Set the base URL to `http://localhost:8000`
3. Use the endpoints from the table above
4. Set `Content-Type: application/json` in Headers for POST/PUT requests
5. Add the JSON body for POST/PUT requests

---

## 📸 Screenshots

Add screenshots of:
- Postman requests/responses for all 5 CRUD operations
- MySQL database table showing the stored data

Place them in a `screenshots/` folder.
