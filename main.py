from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import crud
import schemas
import database  # Import your database module

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = database.Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- Patient Routes -----------------

@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db=db, patient=patient)

@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db=db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@app.get("/patients/", response_model=list[schemas.Patient])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_patients(db=db, skip=skip, limit=limit)

# PUT - Update Patient
@app.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db=db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.update_patient(db=db, patient_id=patient_id, patient=patient)

# DELETE - Delete Patient
@app.delete("/patients/{patient_id}", response_model=schemas.Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud.get_patient(db=db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud.delete_patient(db=db, patient_id=patient_id)

# ----------------- Doctor Routes -----------------

@app.post("/doctors/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db=db, doctor=doctor)

@app.get("/doctors/{doctor_id}", response_model=schemas.Doctor)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db=db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return db_doctor

@app.get("/doctors/", response_model=list[schemas.Doctor])
def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_doctors(db=db, skip=skip, limit=limit)

# PUT - Update Doctor
@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db=db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return crud.update_doctor(db=db, doctor_id=doctor_id, doctor=doctor)

# DELETE - Delete Doctor
@app.delete("/doctors/{doctor_id}", response_model=schemas.Doctor)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud.get_doctor(db=db, doctor_id=doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return crud.delete_doctor(db=db, doctor_id=doctor_id)

# ----------------- Treatment Routes -----------------

@app.post("/treatments/", response_model=schemas.Treatment)
def create_treatment(treatment: schemas.TreatmentCreate, db: Session = Depends(get_db)):
    return crud.create_treatment(db=db, treatment=treatment)

@app.get("/treatments/{treatment_id}", response_model=schemas.Treatment)
def get_treatment(treatment_id: int, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment(db=db, treatment_id=treatment_id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return db_treatment

@app.get("/treatments/", response_model=list[schemas.Treatment])
def get_treatments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_treatments(db=db, skip=skip, limit=limit)

# PUT - Update Treatment
@app.put("/treatments/{treatment_id}", response_model=schemas.Treatment)
def update_treatment(treatment_id: int, treatment: schemas.TreatmentCreate, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment(db=db, treatment_id=treatment_id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return crud.update_treatment(db=db, treatment_id=treatment_id, treatment=treatment)

# DELETE - Delete Treatment
@app.delete("/treatments/{treatment_id}", response_model=schemas.Treatment)
def delete_treatment(treatment_id: int, db: Session = Depends(get_db)):
    db_treatment = crud.get_treatment(db=db, treatment_id=treatment_id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return crud.delete_treatment(db=db, treatment_id=treatment_id)

# ----------------- Appointment Routes -----------------

@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment)

@app.get("/appointments/{appointment_id}", response_model=schemas.Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db=db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment

@app.get("/appointments/", response_model=list[schemas.Appointment])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_appointments(db=db, skip=skip, limit=limit)

# PUT - Update Appointment
@app.put("/appointments/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db=db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return crud.update_appointment(db=db, appointment_id=appointment_id, appointment=appointment)

# DELETE - Delete Appointment
@app.delete("/appointments/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db=db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return crud.delete_appointment(db=db, appointment_id=appointment_id)

# ----------------- Link Treatments to Appointment -----------------

@app.post("/appointments/{appointment_id}/treatments/")
def link_treatment_to_appointment(appointment_id: int, treatment_ids: list[int], db: Session = Depends(get_db)):
    crud.link_treatment_to_appointment(db=db, appointment_id=appointment_id, treatment_ids=treatment_ids)
    return {"message": "Treatments linked successfully"}

# ----------------- Root Endpoint -----------------

@app.get("/")
def root():
    return {"message": "Welcome to the Clinic Booking System API!"}
