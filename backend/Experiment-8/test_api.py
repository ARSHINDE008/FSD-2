import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    print("--- Starting API Tests ---")

    # 1. Test Home Route
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Home Route: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Server is not running? {e}")
        return

    # 2. Test Create Student (POST)
    new_student = {"name": "Arshinder", "age": 22}
    response = requests.post(f"{BASE_URL}/students", json=new_student)
    print(f"Create Student: {response.status_code} - {response.json()}")
    student_id = response.json().get("id")

    # 3. Test Get All Students (GET)
    response = requests.get(f"{BASE_URL}/students")
    print(f"Get All Students: {response.status_code} - Found {len(response.json())} students")

    # 4. Test Get One Student (GET)
    response = requests.get(f"{BASE_URL}/students/{student_id}")
    print(f"Get Student {student_id}: {response.status_code} - {response.json()}")

    # 5. Test Update Student (PUT)
    updated_data = {"name": "Arshinder Updated", "age": 23}
    response = requests.put(f"{BASE_URL}/students/{student_id}", json=updated_data)
    print(f"Update Student {student_id}: {response.status_code} - {response.json()}")

    # 6. Test Delete Student (DELETE)
    response = requests.delete(f"{BASE_URL}/students/{student_id}")
    print(f"Delete Student {student_id}: {response.status_code} - {response.json()}")

    # 7. Verify Deletion
    response = requests.get(f"{BASE_URL}/students/{student_id}")
    print(f"Verify Deletion: {response.status_code} (Expect 404)")

    print("--- API Tests Completed ---")

if __name__ == "__main__":
    test_api()
