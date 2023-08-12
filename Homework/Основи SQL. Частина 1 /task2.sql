-- Select queries

-- Use the sample SQLite database hr.db

-- SQLite database hr.db link:

-- As a solution to HW, create a file named: task2.sql with all SQL queries:


--    1)  write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;

select first_name as First_Name, last_name as Last_Name from _employees;

--    2) write a query to get the unique department ID from the employee table

select distinct department_id from _employees order by department_id;

--    3) write a query to get all employee details from the employee table ordered by first name, descending

select * from _employees order by first_name DESC;

--    4) write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)

select first_name, last_name, salary, (salary * 0.12) as PF from _employees;

--    5) write a query to get the maximum and minimum salary from the employees table

select max (salary), min (salary) from _employees;

--    6) write a query to get a monthly salary (round 2 decimal places) of each and every employee

select first_name, last_name, salary, round ((salary / 12.0),2) as monthly_salary from _employees order by last_name;