-- 1. INSERT DATA INTO THE PARENT TABLE (courses)
INSERT INTO courses (course_code, course_name, credits) 
VALUES
('CSE101', 'Introduction to Computer Science', 4),
('MTH201', 'Discrete Mathematics', 3),
('ECE102', 'Basic Electronics', 4),
('PHY101', 'Engineering Physics', 4),
('ENG101', 'English Communication', 2);

-- 2. INSERT DATA INTO THE JUNCTION TABLE (enrollments)
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
VALUES
(1, 1, '2023-08-15', 'A+'), -- Alex Michael Smith in CSE101
(1, 2, '2023-08-15', 'A'),  -- Alex Michael Smith in MTH201
(2, 2, '2023-08-16', 'O'),  -- Sarah Johnson Williams in MTH201
(2, 5, '2023-08-16', 'B+'), -- Sarah Johnson Williams in ENG101
(3, 3, '2023-08-15', 'B'),  -- James Brown Jones in ECE102
(4, 4, '2023-08-17', 'A'),  -- Emily Davis Garcia in PHY101
(5, 3, '2023-08-15', 'F'),  -- Robert Wilson Miller in ECE102
(6, 1, '2023-08-15', 'O'),  -- Linda Moore Rodriguez in CSE101
(7, 5, '2023-08-18', 'A'),  -- William Taylor Martinez in ENG101
(8, 3, '2023-08-15', 'B+'), -- Elizabeth Anderson Hernandez in ECE102
(9, 2, '2023-08-16', 'A'),  -- David Thomas Lopez in MTH201
(10, 3, '2023-08-15', 'O'); -- Barbara Jackson Gonzalez in ECE102

-- 3. JOIN QUERY: VIEW ENROLLED STUDENTS WITH COURSE DETAILS
-- This returns the student's name, their course, and the grade they received.
SELECT 
    s.student_id,
    s.student_name,
    c.course_code,
    c.course_name,
    e.grade
FROM enrollments e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id
ORDER BY s.student_name;

-- 4. JOIN QUERY: COUNT STUDENTS ENROLLED IN EACH COURSE
SELECT 
    c.course_code,
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_code, c.course_name
ORDER BY total_students DESC;

-- 5. DEMONSTRATING ON DELETE CASCADE
-- If you delete a student, Postgres automatically deletes their enrollments!
-- For example, let's delete Alex Michael Smith (student_id = 1):
-- DELETE FROM students WHERE student_id = 1;
-- If you then check the enrollments table, Alex Michael Smith's records (student_id = 1) will be gone automatically.

