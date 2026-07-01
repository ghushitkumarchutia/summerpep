SELECT 
    e.employee_name AS Employee,
    e.designation AS Designation,
    m.employee_name AS Manager,
    d.department_name AS Department,
    p.project_name AS Project,
    ep.start_date AS "Project Start Date"
FROM employee e
LEFT JOIN employee m ON e.manager_employee_number = m.employee_number
LEFT JOIN department d ON e.department_code = d.department_code
LEFT JOIN employee_projects ep ON e.employee_number = ep.employee_number
LEFT JOIN project p ON ep.project_id = p.project_id
ORDER BY Employee;