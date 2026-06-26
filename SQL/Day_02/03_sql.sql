SELECT * FROM lpu_students WHERE branch = 'Computer Science';

SELECT * FROM lpu_students WHERE age BETWEEN 19 AND 21;

SELECT * FROM lpu_students WHERE branch = 'Computer Science' OR branch = 'Information Technology';

SELECT * FROM lpu_students WHERE first_name LIKE 'S%';

SELECT DISTINCT branch FROM lpu_students;

SELECT first_name, cgpa FROM lpu_students;

SELECT * FROM lpu_students ORDER BY cgpa DESC;