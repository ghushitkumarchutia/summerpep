-- ADVANCED FILTERING
SELECT student_id, first_name FROM lpu_students WHERE age is NULL;

-- NOTE: Using '=' with NULL (age = NULL) will NOT return any rows.
-- In SQL, you must always use 'IS NULL' to find NULL values.
SELECT student_id, first_name FROM lpu_students WHERE age = NULL;

SELECT * FROM lpu_students WHERE age BETWEEN 18 AND 21;

SELECT * FROM lpu_students WHERE city IN ('Houston', 'Los Angeles', 'Chicago');

SELECT * FROM lpu_students WHERE branch IN ('Electrical Engineering', 'Mechanical Engineering');

SELECT * FROM lpu_students WHERE Reg_id IN (2023001, 2023004, 2023009);

-- NAME STARTS WITH R
SELECT * FROM lpu_students WHERE first_name LIKE 'R%';

-- NAME ENDS WITH n
SELECT * FROM lpu_students WHERE first_name LIKE '%n';

-- NAME HAS "ra" IN IT
SELECT * FROM lpu_students WHERE first_name LIKE '%ra%';

-- CITY START WITH D
SELECT * FROM lpu_students WHERE city LIKE 'D%';

-- BRANCH ENDS WITH e
SELECT * FROM lpu_students WHERE branch LIKE '%e';

-- NAMES WHO CONTAINS EXACTLY 4 CHARACTERS
SELECT * FROM lpu_students WHERE first_name LIKE '____';

-- SORT BY NAME
SELECT * FROM lpu_students ORDER BY first_name;

-- SORT BY CITY
SELECT * FROM lpu_students ORDER BY city;

-- SORT BY CGPA FROM HEIGHTEST TO LOWEST
SELECT * FROM lpu_students ORDER BY cgpa DESC;

-- SORT BY BRANCH THEN NAME
SELECT * FROM lpu_students ORDER BY branch, first_name;

-- SORT BY AGE FROM YOUNGEST TO OLDEST
SELECT * FROM lpu_students ORDER BY age ASC;