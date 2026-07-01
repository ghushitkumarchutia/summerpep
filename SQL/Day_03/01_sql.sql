-- CREATE THE STUDENTS TABLE WITH ADVANCED CONSTRAINTS
CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,                           -- Auto-incrementing unique ID
    student_name VARCHAR(50) NOT NULL,                       -- Full name of the student
    age INT CHECK (age BETWEEN 18 AND 60),                   -- Age must be between 18 and 60
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')), -- Gender check constraint
    branch VARCHAR(50) NOT NULL,                             -- Academic department/branch
    semester INT CHECK (semester BETWEEN 1 AND 8) NOT NULL,  -- Current semester (1 to 8)
    cgpa DECIMAL(3,2) CHECK (cgpa BETWEEN 0 AND 10),         -- CGPA on a scale of 0.00 to 10.00
    city VARCHAR(50) NOT NULL,                               -- Residential city
    email VARCHAR(50) UNIQUE NOT NULL,                       -- Unique student email address
    phone_number VARCHAR(15) UNIQUE NOT NULL,                -- Unique student phone number
    admission_date DATE NOT NULL,                            -- Admission date
    fees DECIMAL(10,2) CHECK (fees >= 0),                    -- Tuition fees (must be non-negative)
    attendance DECIMAL(5,2) CHECK (attendance BETWEEN 0 AND 100) -- Attendance percentage (fixed datatype precision)
);
