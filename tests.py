from rest_framework.test import APISimpleTestCase
from rest_framework import status

class CollegeApiTests(APISimpleTestCase):

    def test_dashboard_stats(self):
        response = self.client.get('/api/dashboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_students', response.data)
        self.assertIn('total_staff', response.data)
        self.assertIn('total_departments', response.data)
        self.assertTrue(response.data['total_students'] >= 4)

    def test_department_crud(self):
        # 1. List
        res = self.client.get('/api/departments/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 2. Create
        payload = {
            "name": "Civil Engineering",
            "code": "CE",
            "hod": "Dr. John Smeaton",
            "description": "Structures, surveying, and mechanics"
        }
        res_post = self.client.post('/api/departments/', payload, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)
        new_id = res_post.data['id']
        self.assertEqual(res_post.data['code'], 'CE')

        # 3. Retrieve
        res_get = self.client.get(f'/api/departments/{new_id}/')
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)
        self.assertEqual(res_get.data['name'], 'Civil Engineering')

        # 4. Update
        res_put = self.client.put(f'/api/departments/{new_id}/', {
            "name": "Civil & Structural Engineering",
            "code": "CSE-CIVIL",
            "hod": "Dr. John Smeaton",
            "description": "Updated description"
        }, format='json')
        self.assertEqual(res_put.status_code, status.HTTP_200_OK)
        self.assertEqual(res_put.data['name'], 'Civil & Structural Engineering')

        # 5. Delete
        res_del = self.client.delete(f'/api/departments/{new_id}/')
        self.assertEqual(res_del.status_code, status.HTTP_200_OK)

        # 6. Verify 404 after delete
        res_after = self.client.get(f'/api/departments/{new_id}/')
        self.assertEqual(res_after.status_code, status.HTTP_404_NOT_FOUND)

    def test_student_crud(self):
        # 1. Create student
        payload = {
            "name": "David Miller",
            "roll_number": "CSE-2024-99",
            "email": "david.miller@example.edu",
            "phone": "555-987-1234",
            "department": "Computer Science & Engineering",
            "year": "2nd Year"
        }
        res_post = self.client.post('/api/students/', payload, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)
        student_id = res_post.data['id']

        # 2. Get student
        res_get = self.client.get(f'/api/students/{student_id}/')
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)
        self.assertEqual(res_get.data['name'], "David Miller")

        # 3. Update student
        res_put = self.client.put(f'/api/students/{student_id}/', {
            "name": "David M. Miller",
            "roll_number": "CSE-2024-99",
            "email": "david.miller.new@example.edu",
            "phone": "555-987-1234",
            "department": "Computer Science & Engineering",
            "year": "3rd Year"
        }, format='json')
        self.assertEqual(res_put.status_code, status.HTTP_200_OK)
        self.assertEqual(res_put.data['year'], "3rd Year")

        # 4. Delete student
        res_del = self.client.delete(f'/api/students/{student_id}/')
        self.assertEqual(res_del.status_code, status.HTTP_200_OK)

    def test_staff_crud(self):
        # 1. Create staff
        payload = {
            "name": "Dr. Katherine Johnson",
            "employee_id": "EMP-900",
            "email": "katherine.j@example.edu",
            "phone": "555-432-8888",
            "department": "Mechanical Engineering",
            "designation": "Associate Professor"
        }
        res_post = self.client.post('/api/staff/', payload, format='json')
        self.assertEqual(res_post.status_code, status.HTTP_201_CREATED)
        staff_id = res_post.data['id']

        # 2. Retrieve
        res_get = self.client.get(f'/api/staff/{staff_id}/')
        self.assertEqual(res_get.status_code, status.HTTP_200_OK)

        # 3. Update
        res_put = self.client.put(f'/api/staff/{staff_id}/', {
            "name": "Dr. Katherine Johnson",
            "employee_id": "EMP-900",
            "email": "katherine.j@example.edu",
            "phone": "555-432-8888",
            "department": "Mechanical Engineering",
            "designation": "Professor"
        }, format='json')
        self.assertEqual(res_put.status_code, status.HTTP_200_OK)
        self.assertEqual(res_put.data['designation'], "Professor")

        # 4. Delete
        res_del = self.client.delete(f'/api/staff/{staff_id}/')
        self.assertEqual(res_del.status_code, status.HTTP_200_OK)
