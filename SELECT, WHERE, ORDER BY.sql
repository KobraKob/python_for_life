
--SQL SELECT
select * from employees;

--DISTINCT
select distinct last_name from employees;

--
select first_name, city from employees;

--WHERE 
select first_name from employees
where department = 'IT';

select * from employees
where employee_id = 18;

select * from employees
where salary <= 60000;

--SQL ORDER BY
--The ORDER BY keyword is used to sort the result-set in ascending or descending order.
select first_name, last_name, salary from employees
order by salary desc ;






