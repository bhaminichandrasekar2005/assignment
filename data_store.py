"""
In-memory data storage for College Management System.
Stores data in Python memory structures without using SQLite or any external database.
"""

class InMemoryStore:
    def __init__(self):
        self._departments = [
            {
                "id": 1,
                "name": "Computer Science & Engineering",
                "code": "CSE",
                "hod": "Dr. Alan Turing",
                "description": "Software systems, algorithms, and artificial intelligence."
            },
            {
                "id": 2,
                "name": "Electronics & Communication",
                "code": "ECE",
                "hod": "Dr. Claude Shannon",
                "description": "Embedded systems, signal processing, and communication networks."
            },
            {
                "id": 3,
                "name": "Mechanical Engineering",
                "code": "ME",
                "hod": "Dr. Nikola Tesla",
                "description": "Thermodynamics, mechanical design, robotics, and automation."
            },
            {
                "id": 4,
                "name": "Business Administration",
                "code": "BBA",
                "hod": "Prof. Peter Drucker",
                "description": "Management, financial analysis, marketing, and leadership."
            }
        ]

        self._students = [
            {
                "id": 1,
                "name": "Aarav Sharma",
                "roll_number": "CSE-2024-01",
                "email": "aarav.sharma@example.edu",
                "phone": "+1 555-0101",
                "department": "Computer Science & Engineering",
                "year": "3rd Year"
            },
            {
                "id": 2,
                "name": "Emily Watson",
                "roll_number": "ECE-2024-15",
                "email": "emily.watson@example.edu",
                "phone": "+1 555-0102",
                "department": "Electronics & Communication",
                "year": "2nd Year"
            },
            {
                "id": 3,
                "name": "Liam Brown",
                "roll_number": "ME-2023-42",
                "email": "liam.brown@example.edu",
                "phone": "+1 555-0103",
                "department": "Mechanical Engineering",
                "year": "4th Year"
            },
            {
                "id": 4,
                "name": "Sophia Patel",
                "roll_number": "BBA-2025-08",
                "email": "sophia.patel@example.edu",
                "phone": "+1 555-0104",
                "department": "Business Administration",
                "year": "1st Year"
            }
        ]

        self._staff = [
            {
                "id": 1,
                "name": "Dr. Margaret Hamilton",
                "employee_id": "EMP-101",
                "email": "m.hamilton@example.edu",
                "phone": "+1 555-0201",
                "department": "Computer Science & Engineering",
                "designation": "Professor & HOD"
            },
            {
                "id": 2,
                "name": "Dr. Richard Feynman",
                "employee_id": "EMP-102",
                "email": "r.feynman@example.edu",
                "phone": "+1 555-0202",
                "department": "Electronics & Communication",
                "designation": "Senior Professor"
            },
            {
                "id": 3,
                "name": "Prof. Ada Lovelace",
                "employee_id": "EMP-103",
                "email": "a.lovelace@example.edu",
                "phone": "+1 555-0203",
                "department": "Computer Science & Engineering",
                "designation": "Associate Professor"
            },
            {
                "id": 4,
                "name": "Prof. Henry Gantt",
                "employee_id": "EMP-104",
                "email": "h.gantt@example.edu",
                "phone": "+1 555-0204",
                "department": "Business Administration",
                "designation": "Assistant Professor"
            }
        ]

        # Tracking next primary key IDs
        self._next_dept_id = 5
        self._next_student_id = 5
        self._next_staff_id = 5

    # ---------------- Department Operations ----------------
    def get_departments(self):
        return list(self._departments)

    def get_department_by_id(self, dept_id):
        for dept in self._departments:
            if dept["id"] == dept_id:
                return dept
        return None

    def add_department(self, data):
        new_dept = {
            "id": self._next_dept_id,
            "name": data.get("name", "").strip(),
            "code": data.get("code", "").strip().upper(),
            "hod": data.get("hod", "").strip(),
            "description": data.get("description", "").strip(),
        }
        self._next_dept_id += 1
        self._departments.append(new_dept)
        return new_dept

    def update_department(self, dept_id, data):
        dept = self.get_department_by_id(dept_id)
        if not dept:
            return None
        dept["name"] = data.get("name", dept["name"]).strip()
        dept["code"] = data.get("code", dept["code"]).strip().upper()
        dept["hod"] = data.get("hod", dept["hod"]).strip()
        dept["description"] = data.get("description", dept["description"]).strip()
        return dept

    def delete_department(self, dept_id):
        dept = self.get_department_by_id(dept_id)
        if dept:
            self._departments.remove(dept)
            return True
        return False

    # ---------------- Student Operations ----------------
    def get_students(self):
        return list(self._students)

    def get_student_by_id(self, student_id):
        for student in self._students:
            if student["id"] == student_id:
                return student
        return None

    def add_student(self, data):
        new_student = {
            "id": self._next_student_id,
            "name": data.get("name", "").strip(),
            "roll_number": data.get("roll_number", "").strip().upper(),
            "email": data.get("email", "").strip().lower(),
            "phone": data.get("phone", "").strip(),
            "department": data.get("department", "").strip(),
            "year": data.get("year", "").strip(),
        }
        self._next_student_id += 1
        self._students.append(new_student)
        return new_student

    def update_student(self, student_id, data):
        student = self.get_student_by_id(student_id)
        if not student:
            return None
        student["name"] = data.get("name", student["name"]).strip()
        student["roll_number"] = data.get("roll_number", student["roll_number"]).strip().upper()
        student["email"] = data.get("email", student["email"]).strip().lower()
        student["phone"] = data.get("phone", student["phone"]).strip()
        student["department"] = data.get("department", student["department"]).strip()
        student["year"] = data.get("year", student["year"]).strip()
        return student

    def delete_student(self, student_id):
        student = self.get_student_by_id(student_id)
        if student:
            self._students.remove(student)
            return True
        return False

    # ---------------- Staff Operations ----------------
    def get_staff(self):
        return list(self._staff)

    def get_staff_by_id(self, staff_id):
        for s in self._staff:
            if s["id"] == staff_id:
                return s
        return None

    def add_staff(self, data):
        new_staff = {
            "id": self._next_staff_id,
            "name": data.get("name", "").strip(),
            "employee_id": data.get("employee_id", "").strip().upper(),
            "email": data.get("email", "").strip().lower(),
            "phone": data.get("phone", "").strip(),
            "department": data.get("department", "").strip(),
            "designation": data.get("designation", "").strip(),
        }
        self._next_staff_id += 1
        self._staff.append(new_staff)
        return new_staff

    def update_staff(self, staff_id, data):
        s = self.get_staff_by_id(staff_id)
        if not s:
            return None
        s["name"] = data.get("name", s["name"]).strip()
        s["employee_id"] = data.get("employee_id", s["employee_id"]).strip().upper()
        s["email"] = data.get("email", s["email"]).strip().lower()
        s["phone"] = data.get("phone", s["phone"]).strip()
        s["department"] = data.get("department", s["department"]).strip()
        s["designation"] = data.get("designation", s["designation"]).strip()
        return s

    def delete_staff(self, staff_id):
        s = self.get_staff_by_id(staff_id)
        if s:
            self._staff.remove(s)
            return True
        return False

    # ---------------- Dashboard Stats ----------------
    def get_dashboard_stats(self):
        # Calculate department-wise counts
        dept_counts = {}
        for dept in self._departments:
            dept_counts[dept["name"]] = 0
        for student in self._students:
            dept_name = student.get("department")
            if dept_name in dept_counts:
                dept_counts[dept_name] += 1

        return {
            "total_students": len(self._students),
            "total_staff": len(self._staff),
            "total_departments": len(self._departments),
            "department_breakdown": [
                {"department": k, "student_count": v}
                for k, v in dept_counts.items()
            ],
            "recent_students": self._students[-5:][::-1],
            "recent_staff": self._staff[-5:][::-1]
        }


# Singleton instance shared across requests
store = InMemoryStore()
