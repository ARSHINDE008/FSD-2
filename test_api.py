"""
API Test Script - Student Management API
Tests all CRUD endpoints with comprehensive test cases
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"
TEST_RESULTS = []

def print_header(title):
    """Print test section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def print_success(message):
    """Print success message"""
    print(f"✓ {message}")

def print_error(message):
    """Print error message"""
    print(f"✗ {message}")

def print_result(method, endpoint, status_code, success):
    """Print and store test result"""
    status_text = "PASS" if success else "FAIL"
    color = "✓" if success else "✗"
    print(f"  {color} {method:6} {endpoint:40} [{status_code}] {status_text}")
    TEST_RESULTS.append({
        "method": method,
        "endpoint": endpoint,
        "status_code": status_code,
        "status": status_text
    })

def test_server_status():
    """Test 1: Server Status"""
    print_header("TEST 1: Server Status Check")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"\nRequest: GET {BASE_URL}/")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("GET", "/", response.status_code, success)
        
        if success:
            print_success("Server is running successfully")
        else:
            print_error("Server status check failed")
        
        return success
    except Exception as e:
        print_error(f"Connection error: {e}")
        return False

def test_create_students():
    """Test 2: Create Students"""
    print_header("TEST 2: Create Students")
    
    students_data = [
        {
            "uid": "23BIS70001",
            "name": "Arshinder Singh",
            "email": "arshinder@example.com",
            "age": 20,
            "course": "B.Tech CSE"
        },
        {
            "uid": "23BIS70002",
            "name": "Priya Sharma",
            "email": "priya@example.com",
            "age": 19,
            "course": "B.Tech CSE"
        },
        {
            "uid": "23BIS70003",
            "name": "Rahul Kumar",
            "email": "rahul@example.com",
            "age": 21,
            "course": "B.Tech IT"
        }
    ]
    
    created_ids = []
    
    for idx, student in enumerate(students_data, 1):
        try:
            print(f"\nCreating Student {idx}:")
            print(f"  Payload: {json.dumps(student, indent=2)}")
            
            response = requests.post(
                f"{BASE_URL}/students",
                json=student,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"  Response Status: {response.status_code}")
            
            if response.status_code == 201:
                data = response.json()
                print(f"  Response: {json.dumps(data, indent=2)}")
                created_ids.append(data["student"]["id"])
                print_result("POST", "/students", response.status_code, True)
                print_success(f"Student created with ID: {data['student']['id']}")
            else:
                print(f"  Response: {response.text}")
                print_result("POST", "/students", response.status_code, False)
                print_error(f"Failed to create student: {response.text}")
        
        except Exception as e:
            print_error(f"Request error: {e}")
            print_result("POST", "/students", 500, False)
    
    return created_ids

def test_get_all_students():
    """Test 3: Get All Students"""
    print_header("TEST 3: Get All Students")
    
    try:
        response = requests.get(f"{BASE_URL}/students")
        print(f"\nRequest: GET {BASE_URL}/students")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("GET", "/students", response.status_code, success)
        
        if success:
            data = response.json()
            print_success(f"Retrieved {data.get('count', len(data.get('students', [])))} students")
        else:
            print_error("Failed to retrieve students")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("GET", "/students", 500, False)
        return False

def test_get_student_by_id(student_id):
    """Test 4: Get Student by ID"""
    print_header(f"TEST 4: Get Student by ID (ID={student_id})")
    
    try:
        response = requests.get(f"{BASE_URL}/students/{student_id}")
        print(f"\nRequest: GET {BASE_URL}/students/{student_id}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("GET", f"/students/{student_id}", response.status_code, success)
        
        if success:
            print_success(f"Student retrieved successfully")
        else:
            print_error("Failed to retrieve student")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("GET", f"/students/{student_id}", 500, False)
        return False

def test_update_student(student_id):
    """Test 5: Update Student"""
    print_header(f"TEST 5: Update Student (ID={student_id})")
    
    update_data = {
        "name": "Arshinder Singh Updated",
        "age": 21,
        "course": "B.Tech IT"
    }
    
    try:
        print(f"\nRequest: PUT {BASE_URL}/students/{student_id}")
        print(f"Payload: {json.dumps(update_data, indent=2)}")
        
        response = requests.put(
            f"{BASE_URL}/students/{student_id}",
            json=update_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("PUT", f"/students/{student_id}", response.status_code, success)
        
        if success:
            print_success("Student updated successfully")
        else:
            print_error("Failed to update student")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("PUT", f"/students/{student_id}", 500, False)
        return False

def test_search_by_uid(uid):
    """Test 6: Search by UID"""
    print_header(f"TEST 6: Search by UID ({uid})")
    
    try:
        response = requests.get(f"{BASE_URL}/students/search/uid/{uid}")
        print(f"\nRequest: GET {BASE_URL}/students/search/uid/{uid}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("GET", f"/students/search/uid/{uid}", response.status_code, success)
        
        if success:
            print_success("Student found by UID")
        else:
            print_error("Failed to search student by UID")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("GET", f"/students/search/uid/{uid}", 500, False)
        return False

def test_filter_by_course(course):
    """Test 7: Filter by Course"""
    print_header(f"TEST 7: Filter by Course ({course})")
    
    try:
        response = requests.get(f"{BASE_URL}/students/filter/course/{course}")
        print(f"\nRequest: GET {BASE_URL}/students/filter/course/{course}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("GET", f"/students/filter/course/{course}", response.status_code, success)
        
        if success:
            data = response.json()
            print_success(f"Found {data.get('count', 0)} students in {course}")
        else:
            print_error("Failed to filter students by course")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("GET", f"/students/filter/course/{course}", 500, False)
        return False

def test_delete_student(student_id):
    """Test 8: Delete Student"""
    print_header(f"TEST 8: Delete Student (ID={student_id})")
    
    try:
        print(f"\nRequest: DELETE {BASE_URL}/students/{student_id}")
        
        response = requests.delete(f"{BASE_URL}/students/{student_id}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
        
        success = response.status_code == 200
        print_result("DELETE", f"/students/{student_id}", response.status_code, success)
        
        if success:
            print_success("Student deleted successfully")
        else:
            print_error("Failed to delete student")
        
        return success
    except Exception as e:
        print_error(f"Request error: {e}")
        print_result("DELETE", f"/students/{student_id}", 500, False)
        return False

def print_test_summary():
    """Print test summary"""
    print_header("TEST SUMMARY")
    
    print("\nTest Results:")
    print("-" * 70)
    print(f"{'Method':<8} {'Endpoint':<40} {'Status':<10} {'Result':<6}")
    print("-" * 70)
    
    for result in TEST_RESULTS:
        print(f"{result['method']:<8} {result['endpoint']:<40} {result['status_code']:<10} {result['status']:<6}")
    
    print("-" * 70)
    
    passed = len([r for r in TEST_RESULTS if r['status'] == 'PASS'])
    total = len(TEST_RESULTS)
    
    print(f"\nTotal Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    print("\n" + "=" * 70)

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 10 + "STUDENT MANAGEMENT API - TEST SUITE" + " " * 24 + "║")
    print("║" + " " * 20 + "Testing All CRUD Endpoints" + " " * 23 + "║")
    print("╚" + "=" * 68 + "╝")
    
    print(f"\n► Testing Server: {BASE_URL}")
    print(f"► Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run tests
    if not test_server_status():
        print_error("\n⚠️  Server is not running. Please start the server first.")
        print("Run: python app.py")
        return
    
    student_ids = test_create_students()
    
    test_get_all_students()
    
    if student_ids:
        test_get_student_by_id(student_ids[0])
        test_update_student(student_ids[0])
        test_search_by_uid("23BIS70001")
        test_filter_by_course("B.Tech CSE")
        test_delete_student(student_ids[2])
    
    print_test_summary()
    print(f"\n► Test Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
    except Exception as e:
        print(f"\n\n✗ Unexpected error: {e}")
