create database Employee;
use Employee;

--  Create Employee table containing all Records E_id, E_name, Age, Salary
create table Employee(
	E_id int primary key,
	E_name varchar(255),
	Age int,
	Salary decimal(10,2)
);

insert into Employee values(
	1,'Akash',25,20000
),(
	2,'Arjun',30,30000
),(
	3,'Lokesh',27,40000
),(
	4,'Ganesh',22,15000
),(
	5,'Vinay',28,10000
);
select * from Employee;

-- Count number of employee names from Employee table
select count(E_name) as TotalEmployees from Employee;

-- Find the Maximum age from Employee table
select max(Age) as MaxAge from Employee;

-- Find the Minimum age from Employee table
select min(Age) as MinAge from Employee;

-- Find salaries of employee in Ascending Order
select E_name,Salary from Employee order by Salary asc;

-- Find grouped salaries of employees
select Salary,count(*) as EmployeeCount from Employee group by Salary;

drop database Employee;
