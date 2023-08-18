-- Joins

-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- 1)    write a query in SQL to display the first name, last name, department number, and department name for each employee

select _employees.first_name, _employees.last_name, _employees.department_id, _department.department_name 
from _employees 
join _department on _employees.department_id = _department.department_id
order by department_name;


-- 2)    write a query in SQL to display the first and last name, department, city, and state province for each employee

select _employees.first_name, _employees.last_name, _department.department_name, _locations.city, _locations.state_province 
from _employees 
join _department on _employees.department_id = _department.department_id
join _locations on _department.location_id = _locations.location_id
order by department_name;

-- 3)    write a query in SQL to display the first name, last name, department number, and department name, for all 
-- employees for departments 80 or 40

select _employees.first_name, _employees.last_name, _employees.department_id, _department.department_name 
from _employees 
join _department on _employees.department_id = _department.department_id
where _employees.department_id in ('40', '80');

-- 4)    write a query in SQL to display all departments including those where does not have any employee

select department_id, department_name from _department;

-- 5)    write a query in SQL to display the first name of all employees including the first name of their manager
select employees1.first_name as employee_first_name, employees2.first_name as manager_first_name
from _employees as employees1
join _employees as employees2 
on employees1.manager_id = employees2.employee_id;

-- 6)    write a query in SQL to display the job title, full name (first and last name ) of the employee, 
-- and the difference between the maximum salary for the job and the salary of the employee

select _jobs.job_title,
(_employees.first_name,_employees.last_name) as full_name,
(_jobs.max_salary - _employees.salary) as diff_salary
from _employees
join _jobs on _employees.job_id = _jobs.job_id
group by full_name;

--  7)   write a query in SQL to display the job title and the average salary of employees

select _jobs.job_title, round(AVG(_employees.salary), 0) as average_salary
from _employees
join _jobs on _employees.job_id = _jobs.job_id
group by _jobs.job_title
order by average_salary;

-- 8)    write a query in SQL to display the full name (first and last name), 
-- and salary of those employees who work in any department located in London

select _employees.first_name, _employees.last_name, _employees.salary, _locations.city
from _employees 
join _department on _employees.department_id = _department.department_id
join _locations on _department.location_id = _locations.location_id
where city = 'London';

-- 9)  write a query in SQL to display the department name and the number of employees in each department

select count(_employees.last_name) as number_of_employees,_department.department_name
from _employees
join _department on _employees.department_id = _department.department_id
group by department_name
order by number_of_employees;