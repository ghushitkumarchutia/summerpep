INSERT INTO department (department_code, department_name) VALUES
('HR', 'Human Resources'),
('DEV', 'Software Development');

INSERT INTO employee (employee_number, employee_name, date_of_birth, date_of_joining, designation, salary, manager_employee_number, department_code) VALUES
(101, 'Alice Smith', '1985-04-12', '2010-06-01', 'Engineering Manager', 95000, NULL, 'DEV'),
(102, 'Bob Johnson', '1992-08-25', '2015-03-15', 'Software Engineer', 75000, 101, 'DEV'),
(103, 'Charlie Brown', '1995-11-30', '2020-01-10', 'HR Specialist', 60000, NULL, 'HR');

INSERT INTO project (project_id, project_name) VALUES
('AI_AGENT', 'Autonomous Coding Assistant'),
('WEB_PORTAL', 'Company Intranet Website');

INSERT INTO employee_projects (employee_number, project_id, start_date, end_date) VALUES
(101, 'AI_AGENT', '2026-01-01', NULL),
(102, 'AI_AGENT', '2026-02-15', NULL),
(102, 'WEB_PORTAL', '2026-03-01', '2026-06-30');