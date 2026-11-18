from rest_framework import serializers

class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Department name is required."})
    code = serializers.CharField(max_length=20, required=True, error_messages={"blank": "Department code is required."})
    hod = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Head of Department (HOD) is required."})
    description = serializers.CharField(max_length=255, required=False, allow_blank=True, default="")


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Student name is required."})
    roll_number = serializers.CharField(max_length=30, required=True, error_messages={"blank": "Roll number is required."})
    email = serializers.EmailField(required=True, error_messages={"blank": "Valid email is required."})
    phone = serializers.CharField(max_length=20, required=True, error_messages={"blank": "Phone number is required."})
    department = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Department is required."})
    year = serializers.CharField(max_length=50, required=True, error_messages={"blank": "Year/Semester is required."})


class StaffSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Staff member name is required."})
    employee_id = serializers.CharField(max_length=30, required=True, error_messages={"blank": "Employee ID is required."})
    email = serializers.EmailField(required=True, error_messages={"blank": "Valid email is required."})
    phone = serializers.CharField(max_length=20, required=True, error_messages={"blank": "Phone number is required."})
    department = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Department is required."})
    designation = serializers.CharField(max_length=100, required=True, error_messages={"blank": "Designation is required."})
