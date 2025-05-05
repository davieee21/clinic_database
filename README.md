````markdown
# Clinic Booking System API 🚑💻

## Project Overview 📝

The **Clinic Booking System API** helps manage patients, doctors, appointments, and treatments for a clinic. The API allows users to create, read, update, and delete records for each of these entities. It also supports linking treatments to appointments.

## Technologies Used ⚙️

- **FastAPI** - A modern web framework for building APIs with Python 3.7+.
- **MySQL** - A relational database for storing clinic data.
- **SQLAlchemy** - ORM for seamless database interactions.
- **Pydantic** - Data validation and serialization library.
- **Uvicorn** - ASGI server for serving FastAPI applications.

## Getting Started 🚀

### Prerequisites ⚡

- Python 3.7 or higher
- MySQL server (local or remote)
- Virtual environment (optional but recommended)

### Installation 🛠️

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/clinic-booking-system-api.git
   cd clinic-booking-system-api
````

2. Create a virtual environment (optional):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up MySQL and update the `DATABASE_URL` in the `.env` file with your MySQL connection details.

5. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

6. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API documentation.

## API Endpoints 🔗

### Patients 🏥

* **GET** `/patients/` - Retrieve all patients.
* **GET** `/patients/{patient_id}/` - Retrieve a patient by ID.
* **POST** `/patients/` - Create a new patient.
* **PUT** `/patients/{patient_id}/` - Update a patient's details.
* **DELETE** `/patients/{patient_id}/` - Delete a patient.

### Doctors 🩺

* **GET** `/doctors/` - Retrieve all doctors.
* **GET** `/doctors/{doctor_id}/` - Retrieve a doctor by ID.
* **POST** `/doctors/` - Create a new doctor.
* **PUT** `/doctors/{doctor_id}/` - Update a doctor's details.
* **DELETE** `/doctors/{doctor_id}/` - Delete a doctor.

### Treatments 💊

* **GET** `/treatments/` - Retrieve all treatments.
* **GET** `/treatments/{treatment_id}/` - Retrieve a treatment by ID.
* **POST** `/treatments/` - Create a new treatment.
* **PUT** `/treatments/{treatment_id}/` - Update a treatment's details.
* **DELETE** `/treatments/{treatment_id}/` - Delete a treatment.

### Appointments 📅

* **GET** `/appointments/` - Retrieve all appointments.
* **GET** `/appointments/{appointment_id}/` - Retrieve an appointment by ID.
* **POST** `/appointments/` - Create a new appointment.
* **PUT** `/appointments/{appointment_id}/` - Update an appointment's details.
* **DELETE** `/appointments/{appointment_id}/` - Delete an appointment.

### Appointment Treatments 🧑‍⚕️💉

* **POST** `/appointments/{appointment_id}/treatments/` - Link treatments to an appointment.

## Sample Queries 📝

### 1. Create a New Patient

```bash
POST /patients/
{
  "FullName": "John Doe",
  "Gender": "Male",
  "DateOfBirth": "1990-05-12",
  "PhoneNumber": "0712345678",
  "Email": "johndoe@example.com",
  "Address": "Nairobi"
}
```

### 2. Get All Appointments

```bash
GET /appointments/
```

### 3. Update a Doctor's Information

```bash
PUT /doctors/1/
{
  "FullName": "Dr. Alex Mutua",
  "Specialty": "Dermatologist",
  "PhoneNumber": "0745678901",
  "Email": "alexmutua@clinic.com",
  "AvailabilityHours": "Mon-Fri 9AM-5PM"
}
```

### 4. Delete a Patient

```bash
DELETE /patients/3/
```

## Project Structure 📂

```
clinic-booking-system-api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── main.py
│   ├── database.py
│   └── config.py
│
├── .env
├── requirements.txt
└── README.md
```

* **models.py** - Database models.
* **schemas.py** - Pydantic models (schemas) for request/response validation.
* **crud.py** - CRUD operations for interacting with the database.
* **main.py** - FastAPI app entry point.
* **database.py** - Database connection logic.
* **config.py** - Configuration settings.

## License 📝

MIT License

## Author 👨‍💻

Davis Ongeri - [Your GitHub Profile](https://github.com/davieee21)

```
```

