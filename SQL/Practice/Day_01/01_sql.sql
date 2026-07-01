CREATE TABLE department(
    department_code VARCHAR(50),
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE project(
    project_id VARCHAR(50),
    project_name VARCHAR(100) NOT NULL
);

CREATE TABLE employee(
    employee_number INT,
    employee_name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    date_of_joining DATE NOT NULL,
    designation VARCHAR(100),
    salary INT CHECK (salary > 0),
    manager_employee_number INT,
    department_code VARCHAR(50)
);

CREATE TABLE employee_projects(
    employee_number INT,
    project_id VARCHAR(50),
    start_date DATE NOT NULL,
    end_date DATE
);

ALTER TABLE department
    ADD CONSTRAINT department_pk PRIMARY KEY (department_code);

ALTER TABLE project
    ADD CONSTRAINT project_pk PRIMARY KEY (project_id);

ALTER TABLE employee
    ADD CONSTRAINT employee_pk PRIMARY KEY (employee_number);

ALTER TABLE employee_projects
    ADD CONSTRAINT employee_project_pk PRIMARY KEY (employee_number, project_id);

ALTER TABLE employee
    ADD CONSTRAINT employee_fk1 
    FOREIGN KEY (department_code) 
    REFERENCES department(department_code) 
    ON DELETE SET NULL;

ALTER TABLE employee
    ADD CONSTRAINT employee_fk2 
    FOREIGN KEY (manager_employee_number) 
    REFERENCES employee(employee_number) 
    ON DELETE SET NULL;

ALTER TABLE employee_projects
    ADD CONSTRAINT employee_projects_fk1 
    FOREIGN KEY (employee_number) 
    REFERENCES employee(employee_number) 
    ON DELETE CASCADE;

ALTER TABLE employee_projects
    ADD CONSTRAINT employee_projects_fk2 
    FOREIGN KEY (project_id) 
    REFERENCES project(project_id) 
    ON DELETE CASCADE;