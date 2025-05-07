from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Text, Table, UniqueConstraint, func
from sqlalchemy.orm import relationship
from database import Base

# Association Table for M-M: Appointment <-> Treatment
appointment_treatment_table = Table(
    "Appointment_Treatments",
    Base.metadata,
    Column("AppointmentID", Integer, ForeignKey("Appointments.AppointmentID", ondelete="CASCADE"), primary_key=True),
    Column("TreatmentID", Integer, ForeignKey("Treatments.TreatmentID", ondelete="CASCADE"), primary_key=True)
)

class Patient(Base):
    __tablename__ = "Patients"

    PatientID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(100), nullable=False)
    DateOfBirth = Column(Date, nullable=False)
    PhoneNumber = Column(String(15), unique=True, nullable=False)
    Email = Column(String(100), unique=True)

    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    appointments = relationship("Appointment", back_populates="patient")

class Doctor(Base):
    __tablename__ = "Doctors"

    DoctorID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(100), nullable=False)
    Specialty = Column(String(100), nullable=False)
    PhoneNumber = Column(String(15), unique=True)
    Email = Column(String(100), unique=True)

    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    appointments = relationship("Appointment", back_populates="doctor")

class Treatment(Base):
    __tablename__ = "Treatments"

    TreatmentID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100), nullable=False)
    Description = Column(Text)

    appointments = relationship("Appointment", secondary=appointment_treatment_table, back_populates="treatments")

class Appointment(Base):
    __tablename__ = "Appointments"

    AppointmentID = Column(Integer, primary_key=True, index=True)
    PatientID = Column(Integer, ForeignKey("Patients.PatientID", ondelete="CASCADE"), nullable=False)
    DoctorID = Column(Integer, ForeignKey("Doctors.DoctorID", ondelete="SET NULL"), nullable=True)
    AppointmentDate = Column(DateTime, nullable=False)
    Reason = Column(String(255))

    CreatedAt = Column(DateTime, server_default=func.now())
    UpdatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now())

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    treatments = relationship("Treatment", secondary=appointment_treatment_table, back_populates="appointments")
