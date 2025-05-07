from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from models import Patient, Doctor, Treatment, Appointment, appointment_treatment_table
from schemas import PatientCreate, DoctorCreate, TreatmentCreate, AppointmentCreate, PatientUpdate, DoctorUpdate, TreatmentUpdate, AppointmentUpdate

# Patient CRUD Operations

def create_patient(db: Session, patient: PatientCreate):
    """Create a new patient record in the database."""
    db_patient = Patient(
        FullName=patient.FullName,
        DateOfBirth=patient.DateOfBirth,
        PhoneNumber=patient.PhoneNumber,
        Email=patient.Email,
        Gender=patient.Gender,
        CreatedAt=datetime.utcnow(),
        UpdatedAt=datetime.utcnow()
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    """Fetch a single patient by ID."""
    db_patient = db.query(Patient).filter(Patient.PatientID == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    """Fetch all patients, with optional pagination."""
    return db.query(Patient).offset(skip).limit(limit).all()

def update_patient(db: Session, patient_id: int, patient: PatientUpdate):
    """Update an existing patient's details by ID."""
    db_patient = db.query(Patient).filter(Patient.PatientID == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    # Update the fields provided in the request body
    for var, value in vars(patient).items():
        setattr(db_patient, var, value) if value else None
    
    # Set the UpdatedAt timestamp to current time
    db_patient.UpdatedAt = datetime.utcnow()
    
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    """Delete a patient record by ID."""
    db_patient = db.query(Patient).filter(Patient.PatientID == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(db_patient)
    db.commit()
    return {"message": "Patient deleted successfully"}

# Doctor CRUD Operations

def create_doctor(db: Session, doctor: DoctorCreate):
    """Create a new doctor record in the database."""
    db_doctor = Doctor(
        FullName=doctor.FullName,
        Specialty=doctor.Specialty,
        PhoneNumber=doctor.PhoneNumber,
        Email=doctor.Email,
        CreatedAt=datetime.utcnow(),
        UpdatedAt=datetime.utcnow()
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    """Fetch a single doctor by ID."""
    db_doctor = db.query(Doctor).filter(Doctor.DoctorID == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    """Fetch all doctors, with optional pagination."""
    return db.query(Doctor).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor_id: int, doctor: DoctorUpdate):
    """Update an existing doctor's details by ID."""
    db_doctor = db.query(Doctor).filter(Doctor.DoctorID == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    # Update the fields provided in the request body
    for var, value in vars(doctor).items():
        setattr(db_doctor, var, value) if value else None
    
    # Set the UpdatedAt timestamp to current time
    db_doctor.UpdatedAt = datetime.utcnow()
    
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    """Delete a doctor record by ID."""
    db_doctor = db.query(Doctor).filter(Doctor.DoctorID == doctor_id).first()
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    db.delete(db_doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}

# Treatment CRUD Operations

def create_treatment(db: Session, treatment: TreatmentCreate):
    """Create a new treatment record in the database."""
    db_treatment = Treatment(
        Name=treatment.Name,
        Description=treatment.Description
    )
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def get_treatment(db: Session, treatment_id: int):
    """Fetch a single treatment by ID."""
    db_treatment = db.query(Treatment).filter(Treatment.TreatmentID == treatment_id).first()
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return db_treatment

def get_treatments(db: Session, skip: int = 0, limit: int = 100):
    """Fetch all treatments, with optional pagination."""
    return db.query(Treatment).offset(skip).limit(limit).all()

def update_treatment(db: Session, treatment_id: int, treatment: TreatmentUpdate):
    """Update an existing treatment record by ID."""
    db_treatment = db.query(Treatment).filter(Treatment.TreatmentID == treatment_id).first()
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    
    # Update the fields provided in the request body
    for var, value in vars(treatment).items():
        setattr(db_treatment, var, value) if value else None
    
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def delete_treatment(db: Session, treatment_id: int):
    """Delete a treatment record by ID."""
    db_treatment = db.query(Treatment).filter(Treatment.TreatmentID == treatment_id).first()
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    
    db.delete(db_treatment)
    db.commit()
    return {"message": "Treatment deleted successfully"}

# Appointment CRUD Operations

def create_appointment(db: Session, appointment: AppointmentCreate):
    """Create a new appointment record in the database."""
    db_appointment = Appointment(
        PatientID=appointment.PatientID,
        DoctorID=appointment.DoctorID,
        AppointmentDate=appointment.AppointmentDate,
        Reason=appointment.Reason,
        CreatedAt=datetime.utcnow(),
        UpdatedAt=datetime.utcnow()
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointment(db: Session, appointment_id: int):
    """Fetch a single appointment by ID."""
    db_appointment = db.query(Appointment).filter(Appointment.AppointmentID == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    """Fetch all appointments, with optional pagination."""
    return db.query(Appointment).offset(skip).limit(limit).all()

def update_appointment(db: Session, appointment_id: int, appointment: AppointmentUpdate):
    """Update an existing appointment record by ID."""
    db_appointment = db.query(Appointment).filter(Appointment.AppointmentID == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    # Update the fields provided in the request body
    for var, value in vars(appointment).items():
        setattr(db_appointment, var, value) if value else None
    
    # Set the UpdatedAt timestamp to current time
    db_appointment.UpdatedAt = datetime.utcnow()
    
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    """Delete an appointment record by ID."""
    db_appointment = db.query(Appointment).filter(Appointment.AppointmentID == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    db.delete(db_appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}

# Link Treatments to Appointment

def link_treatment_to_appointment(db: Session, appointment_id: int, treatment_ids: list):
    """Link treatments to an appointment, given an appointment ID and list of treatment IDs."""
    if not db.query(Appointment).filter_by(AppointmentID=appointment_id).first():
        raise HTTPException(status_code=404, detail="Appointment not found")

    # Ensure that the treatment IDs exist in the database
    valid_ids = db.query(Treatment.TreatmentID).filter(Treatment.TreatmentID.in_(treatment_ids)).all()
    valid_ids = [t[0] for t in valid_ids]
    
    # Insert the treatments into the junction table
    for treatment_id in valid_ids:
        db.execute(
            appointment_treatment_table.insert().values(AppointmentID=appointment_id, TreatmentID=treatment_id)
        )
    db.commit()

def get_appointment_treatments(db: Session, appointment_id: int):
    """Fetch all treatments associated with an appointment by ID."""
    return db.query(Treatment).join(appointment_treatment_table).filter(
        appointment_treatment_table.c.AppointmentID == appointment_id
    ).all()
