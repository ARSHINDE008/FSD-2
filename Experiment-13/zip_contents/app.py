from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Update MySQL credentials below
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/chandigarh_university_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ===============================
# Student Model
# ===============================
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "age": self.age
        }

# ===============================
# Validation Schema
# ===============================
class StudentSchema(Schema):
    uid = fields.String(required=True, validate=validate.Length(min=1, max=20))
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    age = fields.Integer(required=True, validate=lambda n: n > 0)

student_schema = StudentSchema()

# Create tables
with app.app_context():
    db.create_all()

# ===============================
# CRUD Routes
# ===============================

# Create
@app.route('/students', methods=['POST'])
def create_student():
    try:
        data = request.get_json()
        validated_data = student_schema.load(data)
        
        # Check if uid already exists
        if Student.query.filter_by(uid=validated_data['uid']).first():
            return jsonify({"error": "Student with this UID already exists"}), 400
            
        new_student = Student(**validated_data)
        db.session.add(new_student)
        db.session.commit()
        return jsonify(new_student.to_dict()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Read All
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students]), 200

# Read One
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student:
        return jsonify(student.to_dict()), 200
    return jsonify({"error": "Student not found"}), 404

# Update
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
        
    try:
        data = request.get_json()
        # allow partial update
        if 'uid' in data:
            # Check uniqueness
            existing = Student.query.filter_by(uid=data['uid']).first()
            if existing and existing.id != id:
                return jsonify({"error": "UID already in use"}), 400
            student.uid = data['uid']
        if 'name' in data:
            student.name = data['name']
        if 'age' in data:
            student.age = data['age']
            
        db.session.commit()
        return jsonify(student.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# Delete
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
        
    try:
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
