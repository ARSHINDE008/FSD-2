# Setup Instructions for Student Management API

## Quick Start Guide

Follow these steps to set up and run the Student Management API on your local machine.

---

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify: `python --version`

2. **MySQL Server 5.7 or higher**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - Or use: `choco install mysql` (Windows) or `brew install mysql` (macOS)
   - Verify: `mysql --version`

3. **Postman** (for API testing)
   - Download from: https://www.postman.com/downloads/

---

## Step-by-Step Setup

### Step 1: Extract the Project Files

```bash
# Extract the zip file
Experiment-13-Complete.zip
```

The folder structure should look like:
```
Experiment-13/
├── app.py
├── requirements.txt
├── README.md
├── run.py
├── setup_db.py
├── test_api.py
├── Experiment-13.postman_collection.json
├── .env.example
└── SCREENSHOTS/
```

### Step 2: Create MySQL Database

Open MySQL command line or MySQL Workbench:

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS student_management;

-- Show created database
SHOW DATABASES;
```

Or use the setup script (see Step 5).

### Step 3: Configure Python Environment

#### Option A: Using Virtual Environment (Recommended)

```bash
# Navigate to the project directory
cd path/to/Experiment-13

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Install Dependencies Globally

```bash
pip install -r requirements.txt
```

### Step 4: Configure Database Credentials (Optional)

If your MySQL credentials differ from defaults, set environment variables:

#### On Windows Command Prompt:
```cmd
set MYSQL_HOST=localhost
set MYSQL_USER=root
set MYSQL_PASSWORD=your_password
set MYSQL_DB=student_management
set MYSQL_PORT=3306
```

#### On Windows PowerShell:
```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "your_password"
$env:MYSQL_DB = "student_management"
$env:MYSQL_PORT = "3306"
```

#### On macOS/Linux:
```bash
export MYSQL_HOST=localhost
export MYSQL_USER=root
export MYSQL_PASSWORD=your_password
export MYSQL_DB=student_management
export MYSQL_PORT=3306
```

### Step 5: Run Application

#### Option A: Using run.py (Recommended)
```bash
python run.py
```

#### Option B: Using app.py directly
```bash
python app.py
```

#### Option C: Using setup_db.py (Initialize DB first)
```bash
# Initialize database
python setup_db.py

# Then start the app
python app.py
```

---

## Expected Server Output

When the server starts successfully, you should see:

```
✓ Database tables initialized successfully
 * Running on http://0.0.0.0:5000
 * Serving Flask app 'app'
 * Debug mode: on
 * WARNING: This is a development server. Do not use it in a production deployment.
```

---

## Testing the API

### Option 1: Using Postman Collection

1. **Open Postman**
2. **Import Collection:**
   - File → Import → Select `Experiment-13.postman_collection.json`
3. **Set Base URL** (if not already set):
   - In "Variables" tab, set `base_url` to `http://localhost:5000`
4. **Run Requests:**
   - Start with "1. Server Status"
   - Then run the requests in order

### Option 2: Using Test Script

```bash
python test_api.py
```

This runs comprehensive tests on all endpoints and provides a summary.

### Option 3: Using cURL Commands

```bash
# Server Status
curl -X GET http://localhost:5000/

# Create Student
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"uid":"23BIS70001","name":"Arshinder Singh","email":"arshinder@example.com","age":20,"course":"B.Tech CSE"}'

# Get All Students
curl -X GET http://localhost:5000/students

# Get Student by ID
curl -X GET http://localhost:5000/students/1

# Update Student
curl -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"age":21,"course":"B.Tech IT"}'

# Delete Student
curl -X DELETE http://localhost:5000/students/1
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:** Install requirements
```bash
pip install -r requirements.txt
```

### Issue: "Access denied for user 'root'@'localhost'"

**Solution 1:** Update MySQL password
```bash
# Set environment variable with correct password
set MYSQL_PASSWORD=your_correct_password
```

**Solution 2:** Edit app.py and update connection string manually

### Issue: "Database 'student_management' doesn't exist"

**Solution:** Create the database
```sql
CREATE DATABASE student_management;
```

Or run the setup script:
```bash
python setup_db.py
```

### Issue: "Port 5000 already in use"

**Solution 1:** Stop the process using port 5000
```bash
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -i :5000
kill -9 <PID>
```

**Solution 2:** Change the port in app.py
```python
app.run(port=5001)  # Change to different port
```

### Issue: "No module named 'pymysql'"

**Solution:** Install PyMySQL
```bash
pip install PyMySQL
```

### Issue: "Can't connect to MySQL server"

**Solution:**
1. Ensure MySQL server is running
2. Check MySQL credentials
3. Verify MySQL host and port
4. Check firewall settings

---

## Running the Application

### Development Mode

```bash
python run.py
```

Server will:
- Run on `http://0.0.0.0:5000`
- Enable debug mode
- Auto-reload on file changes

### Production Mode

Edit `app.py` and change:
```python
app.run(debug=False)  # Disable debug in production
```

---

## API Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Check server status |
| POST | /students | Create new student |
| GET | /students | Get all students |
| GET | /students/{id} | Get student by ID |
| PUT | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |
| GET | /students/search/uid/{uid} | Search by UID |
| GET | /students/filter/course/{course} | Filter by course |

---

## Database Information

**Database Name:** `student_management`

**Table Name:** `student`

**Fields:**
- id (INT, Primary Key, Auto-increment)
- uid (VARCHAR(20), Unique)
- name (VARCHAR(100))
- email (VARCHAR(100), Unique, Optional)
- age (INT)
- course (VARCHAR(100), Optional)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

---

## Files in Project

| File | Purpose |
|------|---------|
| `app.py` | Main Flask application with all routes |
| `requirements.txt` | Python dependencies |
| `README.md` | Full project documentation |
| `run.py` | Simplified startup script |
| `setup_db.py` | Database initialization script |
| `test_api.py` | Comprehensive API test suite |
| `Experiment-13.postman_collection.json` | Postman collection for testing |
| `.env.example` | Environment variables template |
| `SCREENSHOTS/` | Directory for test screenshots |

---

## Next Steps

1. ✅ Start the server with: `python run.py`
2. ✅ Import Postman collection: `Experiment-13.postman_collection.json`
3. ✅ Run API tests: `python test_api.py`
4. ✅ Take screenshots of Postman tests
5. ✅ Check database table: `SELECT * FROM student;`
6. ✅ Document results in README.md

---

## For More Information

- See **README.md** for complete API documentation
- See **Experiment-13.postman_collection.json** for pre-configured API tests
- Run **test_api.py** for comprehensive test results

---

## Support

If you encounter any issues:

1. Check the **Troubleshooting** section above
2. Verify all prerequisites are installed
3. Check error messages carefully
4. Ensure MySQL server is running
5. Verify database and environment variables

---

**Happy Testing! 🚀**
