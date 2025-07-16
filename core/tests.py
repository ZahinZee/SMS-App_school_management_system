from django.test import TestCase
from .models import Student
from .serializers import StudentSerializer
from datetime import date # Importing date for date fields

# Create your tests here.

class StudentSerializerTest(TestCase):
    def test(self):
        student_data = {
            'stu_id': 'ST001',
            'name': 'John Doe',
            'email': 'john.doe@school.com',
            'phone': '1234567890',
            'grade': 10,
            'enrollment_date': date.today(),  # Using today's date for enrollment
            'is_active': True
        }
            
        serializer = StudentSerializer(data=student_data)
        self.assertTrue(serializer.is_valid(), "Serializer should be valid with correct data")

