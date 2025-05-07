from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

# ----------------------------------------
# Shared config class for Pydantic models
# Enables compatibility with SQLAlchemy ORM models
# ----------------------------------------
class ConfigORM:
    from_attributes = True  # Replaces deprecated orm_mode = True (Pydantic v2+)

# ----------------------------------------
# Patient Schemas
# ----------------------------------------

# Patient Schema Base class (for data validation)
class PatientBase(BaseModel):
    FullName: str  # Patient's full name
    DateOfBirth: date  # Patient's date of birth
    PhoneNumber: str  # Patient's phone number
    Email: Optional[str]  # Patient's email (optional)
    Gender: str  # Patient's gender (added)

# Patient Create Schema (inherits from PatientBase)
class PatientCreate(PatientBase):
    pass

# Patient Update Schema (inherits from PatientBase)
class PatientUpdate(PatientBase):
    FullName: Optional[str]  # Allow partial update
    DateOfBirth: Optional[date]
    PhoneNumber: Optional[str]
    Email: Optional[str]
    Gender: Optional[str]

# Patient Schema (includes PatientID, CreatedAt, and UpdatedAt for returning data)
class Patient(PatientBase):
    PatientID: int  # Patient ID (for database lookup)
    CreatedAt: datetime  # When the patient was created
    UpdatedAt: datetime  # When the patient was last updated
    
    class Config(ConfigORM):  # Uses shared config
        pass

# ----------------------------------------
# Doctor Schemas
# ----------------------------------------

# Doctor Schema Base class (for data validation)
class DoctorBase(BaseModel):
    FullName: str  # Doctor's full name
    Specialty: str  # Doctor's specialty
    PhoneNumber: Optional[str]  # Doctor's phone number (optional)
    Email: Optional[str]  # Doctor's email (optional)

# Doctor Create Schema (inherits from DoctorBase)
class DoctorCreate(DoctorBase):
    pass

# Doctor Update Schema (inherits from DoctorBase)
class DoctorUpdate(DoctorBase):
    FullName: Optional[str]
    Specialty: Optional[str]
    PhoneNumber: Optional[str]
    Email: Optional[str]

# Doctor Schema (includes DoctorID, CreatedAt, and UpdatedAt for returning data)
class Doctor(DoctorBase):
    DoctorID: int  # Doctor ID (for database lookup)
    CreatedAt: datetime  # When the doctor was created
    UpdatedAt: datetime  # When the doctor was last updated
    
    class Config(ConfigORM):  # Uses shared config
        pass

# ----------------------------------------
# Treatment Schemas
# ----------------------------------------

# Treatment Schema Base class (for data validation)
class TreatmentBase(BaseModel):
    Name: str  # Name of the treatment
    Description: Optional[str]  # Description of the treatment (optional)

# Treatment Create Schema (inherits from TreatmentBase)
class TreatmentCreate(TreatmentBase):
    pass

# Treatment Update Schema (inherits from TreatmentBase)
class TreatmentUpdate(TreatmentBase):
    Name: Optional[str]
    Description: Optional[str]

# Treatment Schema (includes TreatmentID for returning data)
class Treatment(TreatmentBase):
    TreatmentID: int  # Treatment ID (for database lookup)
    
    class Config(ConfigORM):  # Uses shared config
        pass

# ----------------------------------------
# Appointment Schemas
# ----------------------------------------

# Appointment Schema Base class (for data validation)
class AppointmentBase(BaseModel):
    PatientID: int  # Linked Patient ID
    DoctorID: Optional[int]  # Linked Doctor ID (optional, can be null)
    AppointmentDate: datetime  # Date and time of appointment
    Reason: Optional[str]  # Reason for appointment (optional)

# Appointment Create Schema (inherits from AppointmentBase)
class AppointmentCreate(AppointmentBase):
    pass

# Appointment Update Schema (inherits from AppointmentBase)
class AppointmentUpdate(AppointmentBase):
    PatientID: Optional[int]  # Allow partial update
    DoctorID: Optional[int]
    AppointmentDate: Optional[datetime]
    Reason: Optional[str]

# Appointment Schema (includes AppointmentID, CreatedAt, and UpdatedAt for returning data)
class Appointment(AppointmentBase):
    AppointmentID: int  # Appointment ID (for database lookup)
    CreatedAt: datetime  # When the appointment was created
    UpdatedAt: datetime  # When the appointment was last updated
    treatments: List[Treatment] = []  # List of treatments linked to this appointment (was capitalized before, now lowercase to match relationship key)

    class Config(ConfigORM):  # Uses shared config
        pass

# ----------------------------------------
# Custom Response Schemas
# ----------------------------------------

# Upcoming Appointment Schema for viewing upcoming appointments (with Patient and Doctor names)
class UpcomingAppointment(BaseModel):
    AppointmentID: int  # Appointment ID
    Patient: str  # Full name of the patient
    Doctor: str  # Full name of the doctor
    AppointmentDate: datetime  # Date and time of appointment
    Reason: Optional[str]  # Reason for appointment (optional)
    
    class Config(ConfigORM):  # Uses shared config
        pass

# Appointment Treatment Detail Schema for viewing treatments linked to an appointment
class AppointmentTreatmentDetail(BaseModel):
    AppointmentID: int  # Appointment ID
    Patient: str  # Full name of the patient
    Treatment: str  # Name of the treatment
    AppointmentDate: datetime  # Date and time of appointment

    class Config(ConfigORM):  # Uses shared config
        pass
