-- CREATE THE TABLE
CREATE TABLE lpu_students(
    student_id SERIAL PRIMARY KEY, -- Primary key
    first_name VARCHAR(50) NOT NULL, -- Not null
    middle_name VARCHAR(50), -- Nullable
    last_name VARCHAR(50) NOT NULL, -- Not null
    Reg_id INT UNIQUE NOT NULL, -- Unique and not null
    branch VARCHAR(50), -- Nullable
    batch INT NOT NULL, -- Not null
    cgpa DECIMAL(3,2) CHECK (cgpa BETWEEN 0 AND 10), -- Check constraint
    age INT CHECK (age BETWEEN 18 AND 60), -- Check constraint
    city VARCHAR(50) -- Nullable
);

