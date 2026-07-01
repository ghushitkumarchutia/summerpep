-- 1. CREATE PARENT TABLE: courses
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,                            -- Unique identifier for each course
    course_code VARCHAR(10) UNIQUE NOT NULL,                 -- Unique code (e.g., 'CSE101')
    course_name VARCHAR(100) NOT NULL,                       -- Course title
    credits INT CHECK (credits BETWEEN 1 AND 5) NOT NULL     -- Number of course credits (1 to 5)
);

-- 2. CREATE CHILD JUNCTION TABLE: enrollments
-- This table references both 'students' and 'courses' using FOREIGN KEYS.
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,                        -- Unique identifier for each enrollment record
    
    student_id INT NOT NULL,                                 -- Foreign Key Column
    course_id INT NOT NULL,                                  -- Foreign Key Column
    
    enrollment_date DATE DEFAULT CURRENT_DATE NOT NULL,      -- Date of enrollment
    grade VARCHAR(2) CHECK (grade IN ('O', 'A+', 'A', 'B+', 'B', 'F')), -- Grade achieved
    
    -- Defining the Foreign Key constraints explicitly
    CONSTRAINT fk_student 
        FOREIGN KEY (student_id) 
        REFERENCES students(student_id) 
        ON DELETE CASCADE,                                   -- If a student is deleted, delete their enrollments
        
    CONSTRAINT fk_course 
        FOREIGN KEY (course_id) 
        REFERENCES courses(course_id) 
        ON DELETE CASCADE,                                   -- If a course is deleted, delete its enrollments
        
    -- Constraint to ensure a student cannot enroll in the same course twice
    CONSTRAINT unique_student_course 
        UNIQUE (student_id, course_id)
);
