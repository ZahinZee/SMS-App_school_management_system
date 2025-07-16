from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields from the Student model
        read_only_fields = ('id', 'created_at', 'updated_at')  # Make these fields read-only

        def validate_stu_id(self, value):
            if not value.isalnum():
                raise serializers.ValidationError("Student ID must be alphanumeric.")
            return value

        def validate_grade(self, value):
            if value < 1 or value > 12:
                raise serializers.ValidationError("Grade Level Must Be Between 1 and 12.")
            return value