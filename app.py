from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
import pymysql
import os
from datetime import datetime

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# ===============================
# Database Configuration
# ===============================
# MySQL Configuration
MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
MYSQL_DB = os.environ.get('MYSQL_DB', 'student_management')
MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)

# ===============================
# Student Model
# ===============================
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(20), unique=True, nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "course": self.course,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }

# ===============================
# Validation Schema
# ===============================
class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    uid = fields.String(required=True, validate=validate.Length(min=1, max=20))
    name = fields.String(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=False, allow_none=True)
    age = fields.Integer(required=True, validate=validate.Range(min=5, max=120))
    course = fields.String(required=False, allow_none=True, validate=validate.Length(min=2, max=100))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# Create tables
with app.app_context():
    try:
        db.create_all()
        print("✓ Database tables initialized successfully")
    except Exception as e:
        print(f"✗ Error creating tables: {e}")

# ===============================
# CRUD Routes
# ===============================

# Home/Health Check
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Student Management API",
        "status": "running",
        "version": "1.0.0"
    }), 200


# CREATE - POST /students
@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with validation."""
    try:
        data = request.get_json()
        
        # Validate input data
        try:
            validated_data = student_schema.load(data)
        except ValidationError as err:
            return jsonify({
                "error": "Validation failed",
                "details": err.messages
            }), 400
        
        # Check if uid already exists
        if Student.query.filter_by(uid=validated_data['uid']).first():
            return jsonify({"error": "Student with this UID already exists"}), 400
        
        # Check if email already exists (if provided)
        if validated_data.get('email') and Student.query.filter_by(email=validated_data['email']).first():
            return jsonify({"error": "Student with this email already exists"}), 400
            
        new_student = Student(**validated_data)
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify({
            "message": "Student created successfully",
            "student": new_student.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# READ ALL - GET /students
@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    try:
        # Get query parameters for filtering and pagination
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # Paginate results
        paginated = Student.query.paginate(page=page, per_page=per_page)
        
        return jsonify({
            "message": "Students retrieved successfully",
            "total": paginated.total,
            "page": page,
            "per_page": per_page,
            "total_pages": paginated.pages,
            "students": [student.to_dict() for student in paginated.items]
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# READ ONE - GET /students/<id>
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Retrieve a specific student by ID."""
    try:
        student = Student.query.get(student_id)
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        return jsonify({
            "message": "Student retrieved successfully",
            "student": student.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# UPDATE - PUT /students/<id>
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student."""
    try:
        student = Student.query.get(student_id)
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Validate and update fields
        if 'uid' in data:
            # Check uniqueness
            existing = Student.query.filter_by(uid=data['uid']).first()
            if existing and existing.id != student_id:
                return jsonify({"error": "UID already in use"}), 400
            student.uid = data['uid']
        
        if 'name' in data:
            if not isinstance(data['name'], str) or len(data['name']) < 2:
                return jsonify({"error": "Name must be at least 2 characters"}), 400
            student.name = data['name']
        
        if 'email' in data:
            if data['email']:
                existing = Student.query.filter_by(email=data['email']).first()
                if existing and existing.id != student_id:
                    return jsonify({"error": "Email already in use"}), 400
            student.email = data['email']
        
        if 'age' in data:
            try:
                age = int(data['age'])
                if age < 5 or age > 120:
                    return jsonify({"error": "Age must be between 5 and 120"}), 400
                student.age = age
            except (ValueError, TypeError):
                return jsonify({"error": "Age must be a valid integer"}), 400
        
        if 'course' in data:
            student.course = data['course']
        
        db.session.commit()
        
        return jsonify({
            "message": "Student updated successfully",
            "student": student.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# DELETE - DELETE /students/<id>
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student."""
    try:
        student = Student.query.get(student_id)
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        deleted_student = student.to_dict()
        db.session.delete(student)
        db.session.commit()
        
        return jsonify({
            "message": "Student deleted successfully",
            "deleted_student": deleted_student
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# Search by UID
@app.route('/students/search/uid/<uid>', methods=['GET'])
def search_by_uid(uid):
    """Search student by UID."""
    try:
        student = Student.query.filter_by(uid=uid).first()
        
        if not student:
            return jsonify({"error": "Student not found"}), 404
        
        return jsonify({
            "message": "Student found",
            "student": student.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


# Get students by course
@app.route('/students/filter/course/<course>', methods=['GET'])
def filter_by_course(course):
    """Get all students in a specific course."""
    try:
        students = Student.query.filter_by(course=course).all()
        
        if not students:
            return jsonify({"message": f"No students found in course: {course}", "students": []}), 200
        
        return jsonify({
            "message": "Students retrieved successfully",
            "count": len(students),
            "students": [student.to_dict() for student in students]
        }), 200
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
