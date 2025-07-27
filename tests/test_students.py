import sys
import os
from fastapi.testclient import TestClient
from pyexpat.errors import messages

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)


def test_get_all_students():
    response=client.get("/api/student/get_all_students")
    assert  response.status_code == 200
    data=response.json()
    assert "message" in data

def test_get_students_by_name():
    response = client.get("/api/student/get_students_by_name/Ranjiv Singh")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_get_students_by_id():
    response = client.get("/api/student/get_students_by_id/1")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_insert_student():
    response = client.post("/api/student/insert_student_record",json={
    "student_name":"rahul4 patil",
    "student_email":"rahul4@gmail.com"
})
    assert response.status_code == 201
    data = response.json()
    assert "message" in data
