# 🏥 Clinic Booking System API

A full-featured CRUD API for managing a clinic’s bookings, patients, doctors, appointments, and treatments. Built with **FastAPI** and **MySQL**, this project demonstrates backend API development using modern Python tools and relational database integration.

---

## 🚀 Features

- Full CRUD operations for:
  - Patients
  - Doctors
  - Appointments
  - Treatments
- Link multiple treatments to appointments (many-to-many)
- SQLAlchemy models & Pydantic schemas
- Modular project structure
- Connected to MySQL database (replaceable DB URI)
- Automatically generated Swagger docs via FastAPI

---

## ⚙️ Technologies Used

- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- Uvicorn (ASGI server)
- Alembic (optional: for migrations)

---

## 🧑‍💻 Getting Started

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
