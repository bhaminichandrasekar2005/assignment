from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_store import store
from .serializers import DepartmentSerializer, StudentSerializer, StaffSerializer

# ---------------- Dashboard View ----------------
class DashboardStatsView(APIView):
    """
    Returns counts for total students, total staff, total departments,
    and recent activity for the dashboard.
    """
    def get(self, request):
        stats = store.get_dashboard_stats()
        return Response(stats, status=status.HTTP_200_OK)


# ---------------- Department Views ----------------
class DepartmentListCreateView(APIView):
    """
    GET: List all departments.
    POST: Create a new department.
    """
    def get(self, request):
        departments = store.get_departments()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            created_dept = store.add_department(serializer.validated_data)
            return Response(created_dept, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetailView(APIView):
    """
    GET: Retrieve department by ID.
    PUT: Update department by ID.
    DELETE: Remove department by ID.
    """
    def get(self, request, pk):
        dept = store.get_department_by_id(pk)
        if not dept:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        dept = store.get_department_by_id(pk)
        if not dept:
            return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            updated_dept = store.update_department(pk, serializer.validated_data)
            return Response(updated_dept, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        success = store.delete_department(pk)
        if success:
            return Response({"message": "Department deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND)


# ---------------- Student Views ----------------
class StudentListCreateView(APIView):
    """
    GET: List all students.
    POST: Create a new student.
    """
    def get(self, request):
        students = store.get_students()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            created_student = store.add_student(serializer.validated_data)
            return Response(created_student, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    """
    GET: Retrieve student by ID.
    PUT: Update student by ID.
    DELETE: Remove student by ID.
    """
    def get(self, request, pk):
        student = store.get_student_by_id(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        student = store.get_student_by_id(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            updated_student = store.update_student(pk, serializer.validated_data)
            return Response(updated_student, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        success = store.delete_student(pk)
        if success:
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


# ---------------- Staff Views ----------------
class StaffListCreateView(APIView):
    """
    GET: List all staff members.
    POST: Create a new staff member.
    """
    def get(self, request):
        staff = store.get_staff()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            created_staff = store.add_staff(serializer.validated_data)
            return Response(created_staff, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetailView(APIView):
    """
    GET: Retrieve staff by ID.
    PUT: Update staff by ID.
    DELETE: Remove staff by ID.
    """
    def get(self, request, pk):
        staff = store.get_staff_by_id(pk)
        if not staff:
            return Response({"error": "Staff member not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        staff = store.get_staff_by_id(pk)
        if not staff:
            return Response({"error": "Staff member not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            updated_staff = store.update_staff(pk, serializer.validated_data)
            return Response(updated_staff, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        success = store.delete_staff(pk)
        if success:
            return Response({"message": "Staff member deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Staff member not found"}, status=status.HTTP_404_NOT_FOUND)
