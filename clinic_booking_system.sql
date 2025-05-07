-- ============================================
-- Clinic Booking System Database Schema
-- Created: 2025-04-18
-- Description:
--   - Manages patients, doctors, appointments, and treatments.
--   - Includes views for analytics and a stored procedure for doctor appointments.
-- Author: [Davis Ongeri]
-- ============================================

-- ----------------------------------------
-- DROP existing tables to avoid conflicts
-- ----------------------------------------
DROP TABLE IF EXISTS Appointment_Treatments;
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Treatments;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Doctors;

-- ----------------------
-- TABLE: Patients
-- ----------------------
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,
    DateOfBirth DATE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE NOT NULL CHECK (PhoneNumber REGEXP '^[0-9]{10,15}$'),
    Email VARCHAR(100) UNIQUE,
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ----------------------
-- TABLE: Doctors
-- ----------------------
CREATE TABLE Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Specialty VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE,
    Email VARCHAR(100) UNIQUE,
    AvailabilityHours VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ----------------------
-- TABLE: Treatments
-- ----------------------
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description TEXT
);

-- ----------------------
-- TABLE: Appointments
-- ----------------------
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT,
    AppointmentDate DATETIME NOT NULL,
    Reason VARCHAR(255),
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID) ON DELETE SET NULL
);

-- -------------------------------
-- TABLE: Appointment_Treatments
-- -------------------------------
CREATE TABLE Appointment_Treatments (
    AppointmentID INT,
    TreatmentID INT,
    PRIMARY KEY (AppointmentID, TreatmentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE
);

-- ----------------------
-- Sample Data
-- ----------------------

-- Patients
INSERT INTO Patients (FullName, Gender, DateOfBirth, PhoneNumber, Email, Address) VALUES
('John Doe', 'Male', '1990-05-12', '0712345678', 'johndoe@example.com', 'Nairobi'),
('Jane Smith', 'Female', '1985-09-20', '0723456789', 'janesmith@example.com', 'Mombasa'),
('Michael Otieno', 'Male', '2000-01-01', '0734567890', 'michael.o@example.com', 'Kisumu');

-- Doctors
INSERT INTO Doctors (FullName, Specialty, PhoneNumber, Email, AvailabilityHours) VALUES
('Dr. Alex Mutua', 'General Practitioner', '0745678901', 'alexmutua@clinic.com', 'Mon-Fri 9AM-5PM'),
('Dr. Sarah Mwangi', 'Dermatologist', '0756789012', 'sarahmwangi@clinic.com', 'Tue-Sat 10AM-4PM');

-- Treatments
INSERT INTO Treatments (Name, Description) VALUES
('Physical Therapy', 'Treatment to restore mobility and strength.'),
('Medication', 'Prescription drugs to relieve symptoms.'),
('Minor Surgery', 'Small surgical procedure under local anesthesia.');

-- Appointments
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Reason, Status) VALUES
(1, 1, '2025-04-20 10:00:00', 'Routine Checkup', 'Scheduled'),
(2, 2, '2025-04-21 14:30:00', 'Skin rash', 'Completed'),
(3, 1, '2025-04-22 09:00:00', 'Joint pain', 'Scheduled');

-- Appointment_Treatments
INSERT INTO Appointment_Treatments (AppointmentID, TreatmentID) VALUES
(1, 2),
(2, 2),
(3, 1),
(3, 2);

-- ----------------------
-- VIEWS
-- ----------------------

-- View 1: Upcoming appointments with patient and doctor names
CREATE VIEW UpcomingAppointments AS
SELECT 
    a.AppointmentID,
    p.FullName AS Patient,
    d.FullName AS Doctor,
    a.AppointmentDate,
    a.Reason,
    a.Status
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID
WHERE a.AppointmentDate >= NOW()
ORDER BY a.AppointmentDate;

-- View 2: Treatments per appointment
CREATE VIEW AppointmentTreatmentDetails AS
SELECT 
    a.AppointmentID,
    p.FullName AS Patient,
    t.Name AS Treatment,
    a.AppointmentDate
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Appointment_Treatments at ON a.AppointmentID = at.AppointmentID
JOIN Treatments t ON at.TreatmentID = t.TreatmentID
ORDER BY a.AppointmentDate;

-- ----------------------
-- STORED PROCEDURE
-- ----------------------

-- Procedure to get all appointments for a given doctor
DELIMITER //
CREATE PROCEDURE GetDoctorAppointments(IN doc_id INT)
BEGIN
    -- Validate doctor exists
    IF NOT EXISTS (SELECT 1 FROM Doctors WHERE DoctorID = doc_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Doctor not found';
    END IF;

    -- Retrieve appointments for the doctor
    SELECT 
        a.AppointmentID,
        p.FullName AS PatientName,
        a.AppointmentDate,
        a.Reason,
        a.Status
    FROM Appointments a
    JOIN Patients p ON a.PatientID = p.PatientID
    WHERE a.DoctorID = doc_id
    ORDER BY a.AppointmentDate;
END //
DELIMITER ;

-- ----------------------
-- Example Queries
-- ----------------------

-- 1. See all appointments for Dr. Alex Mutua
-- (DoctorID = 1)
-- CALL GetDoctorAppointments(1);

-- 2. View all upcoming appointments
-- SELECT * FROM UpcomingAppointments;

-- 3. List all treatments done during each appointment
-- SELECT * FROM AppointmentTreatmentDetails;
