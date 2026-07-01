-- CREATE THE STUDENTS TABLE
CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,                          -- Auto-incrementing unique identifier for each student
    student_name VARCHAR(50) NOT NULL,                      -- Full name of the student (cannot be null)
    age INT CHECK (age BETWEEN 18 AND 60),                  -- Age constraint ensuring students are between 18 and 60 years old
    branch VARCHAR(50) NOT NULL,                            -- Academic branch or department (e.g., Computer Science)
    semester INT CHECK (semester BETWEEN 1 AND 8) NOT NULL, -- Current semester (must be between 1 and 8)
    cgpa DECIMAL(3,2) CHECK (cgpa BETWEEN 0 AND 10),        -- Cumulative Grade Point Average (scale of 0.00 to 10.00)
    city VARCHAR(50) NOT NULL,                              -- City of residence
    admission_date DATE NOT NULL                            -- Date when the student was admitted (fixed syntax: removed trailing comma)
);
