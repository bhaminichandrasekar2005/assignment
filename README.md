# College Management System (React.js + Django REST Framework)

A clean, modern, beginner-friendly **College Management System** built with **React.js** on the frontend and **Django + Django REST Framework (DRF)** on the backend, using **in-memory data storage (Zero Database / No SQLite)**.

---

## 📁 Project Structure

```text
c:\projects\
├── collegeproject/              # Django Backend Project
│   ├── manage.py                # Django CLI entrypoint
│   ├── collegeproject/          # Project settings & URL configuration
│   │   ├── __init__.py
│   │   ├── settings.py          # CORS, DRF, and in-memory settings (DATABASES = {})
│   │   ├── urls.py              # Root routing (connects /api/)
│   │   ├── asgi.py
│   │   └── wsgi.py
│   └── api/                     # DRF REST API App
│       ├── __init__.py
│       ├── apps.py
│       ├── data_store.py        # Thread-safe in-memory data store with seed data
│       ├── serializers.py       # DRF serializers with field validations
│       ├── views.py             # Class-based views for CRUD & Dashboard stats
│       ├── urls.py              # Endpoints: /dashboard/, /students/, /staff/, /departments/
│       └── tests.py             # DRF unit tests (100% passing)
│
├── frontend/my-react-app/       # React.js Frontend Project (Vite + React Router + Axios)
│   ├── package.json             # React, Axios, React Router DOM
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── api/
│       │   └── axiosClient.js   # Centralized Axios instance (baseURL: http://127.0.0.1:8000/api)
│       ├── components/
│       │   ├── Layout.jsx       # Responsive layout with Sidebar and Navbar
│       │   ├── Sidebar.jsx      # Navigation sidebar with active route highlights
│       │   ├── Navbar.jsx       # Top bar with API connectivity status
│       │   ├── StatCard.jsx     # Modern metric display cards
│       │   ├── Modal.jsx        # Reusable modal for Add/Edit/Delete
│       │   ├── Toast.jsx        # Notification alert banners
│       │   └── Icons.jsx        # Lightweight, crisp SVG icons
│       ├── pages/
│       │   ├── Dashboard.jsx    # Overview KPI counters, dept distribution, recent items
│       │   ├── Students.jsx     # Students CRUD, search, dept filter, form validation
│       │   ├── Staff.jsx        # Staff CRUD, search, dept filter, form validation
│       │   └── Departments.jsx  # Departments CRUD, search, cards layout
│       ├── App.jsx              # React Router configuration
│       ├── main.jsx             # React DOM root render
│       └── index.css            # Clean, modern, responsive CSS design
│
└── venv/                        # Python Virtual Environment
```

---

## 🚀 Quick Execution Guide

### 1. Start the Django Backend Server

Open your first terminal window:

```powershell
cd c:\projects\collegeproject
..\venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```
> The Django REST API will be running at: `http://127.0.0.1:8000/api/`

---

### 2. Start the React Frontend Application

Open a second terminal window:

```powershell
cd c:\projects\frontend\my-react-app
npm run dev
```
> The React web app will open at: `http://localhost:5173/` (or port indicated in the terminal).

---

## 📡 REST API Endpoints Overview

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/dashboard/` | Total counts for students, staff, departments & recent items |
| `GET` | `/api/departments/` | List all departments |
| `POST` | `/api/departments/` | Add a new department |
| `GET` | `/api/departments/<id>/` | Retrieve department details |
| `PUT` | `/api/departments/<id>/` | Edit department details |
| `DELETE` | `/api/departments/<id>/` | Delete department |
| `GET` | `/api/students/` | List all students |
| `POST` | `/api/students/` | Add a new student |
| `GET` | `/api/students/<id>/` | Retrieve student details |
| `PUT` | `/api/students/<id>/` | Edit student details |
| `DELETE` | `/api/students/<id>/` | Delete student |
| `GET` | `/api/staff/` | List all staff members |
| `POST` | `/api/staff/` | Add a new staff member |
| `GET` | `/api/staff/<id>/` | Retrieve staff details |
| `PUT` | `/api/staff/<id>/` | Edit staff details |
| `DELETE` | `/api/staff/<id>/` | Delete staff member |

---

## 🧪 Running Automated Tests

To test backend CRUD operations and in-memory persistence:

```powershell
cd c:\projects\collegeproject
..\venv\Scripts\python.exe manage.py test api
```
All tests use Django's `APISimpleTestCase` with zero database dependencies.
