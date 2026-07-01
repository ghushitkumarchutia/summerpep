-- UPDATE THE NEWLY ADDED COLUMNS FOR THE EXISTING 10 STUDENTS
UPDATE students SET gender = 'Male', email = 'alex.smith@example.com', phone_number = '9876543211', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Alex Michael Smith';
UPDATE students SET gender = 'Female', email = 'sarah.williams@example.com', phone_number = '9876543212', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Sarah Johnson Williams';
UPDATE students SET gender = 'Male', email = 'james.jones@example.com', phone_number = '9876543213', fees = 50000.00, attendance = 85.00 WHERE student_name = 'James Brown Jones';
UPDATE students SET gender = 'Female', email = 'emily.garcia@example.com', phone_number = '9876543214', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Emily Davis Garcia';
UPDATE students SET gender = 'Male', email = 'robert.miller@example.com', phone_number = '9876543215', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Robert Wilson Miller';
UPDATE students SET gender = 'Female', email = 'linda.rodriguez@example.com', phone_number = '9876543216', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Linda Moore Rodriguez';
UPDATE students SET gender = 'Male', email = 'william.martinez@example.com', phone_number = '9876543217', fees = 50000.00, attendance = 85.00 WHERE student_name = 'William Taylor Martinez';
UPDATE students SET gender = 'Female', email = 'elizabeth.hernandez@example.com', phone_number = '9876543218', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Elizabeth Anderson Hernandez';
UPDATE students SET gender = 'Male', email = 'david.lopez@example.com', phone_number = '9876543219', fees = 50000.00, attendance = 85.00 WHERE student_name = 'David Thomas Lopez';
UPDATE students SET gender = 'Female', email = 'barbara.gonzalez@example.com', phone_number = '9876543220', fees = 50000.00, attendance = 85.00 WHERE student_name = 'Barbara Jackson Gonzalez';

-- NOW THAT ALL DATA IS POPULATED, ENFORCE NOT NULL CONSTRAINTS
ALTER TABLE students 
    ALTER COLUMN email SET NOT NULL,
    ALTER COLUMN phone_number SET NOT NULL;

