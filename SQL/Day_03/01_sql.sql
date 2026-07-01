-- ALTER THE EXISTING TABLE (from Day 1) TO ADD NEW COLUMNS FOR DAY 3
ALTER TABLE students 
    ADD COLUMN gender VARCHAR(10) CHECK (gender IN ('Male', 'Female')),
    ADD COLUMN email VARCHAR(50) UNIQUE,                   -- Initially nullable to allow data updates
    ADD COLUMN phone_number VARCHAR(15) UNIQUE,            -- Initially nullable to allow data updates
    ADD COLUMN fees DECIMAL(10,2) CHECK (fees >= 0),
    ADD COLUMN attendance DECIMAL(5,2) CHECK (attendance BETWEEN 0 AND 100);

-- REMOVE THE OLD COLUMN THAT IS NOT PART OF THE DAY 3 SCHEMA
ALTER TABLE students 
    DROP COLUMN is_placed;
