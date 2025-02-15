create database Employee;
use Employee;

create table Employees(
	Empno int,
	Ename varchar(20),
	Job varchar(20),
	MGR int,
	Sal decimal(10,2)
);

-- Add a column commission with domain to the Employee table
alter table Employees add(Commission int);
desc Employees;

-- Insert any five records into the table
insert into Employees values(
        100,'Abhishek','Manager',10,25000,100
),(
        101,'Bharat','Analyst',20,20000,50
),(
        102,'Charan','Trainee',30,15000,75
);
select * from Employees;

-- Update the column details of job
update Employees set Job='Trainee' where Empno=101;
select * from Employees;

-- Rename the column of Employ table using alter command
alter table Employees rename column MGR to Manager_No;
select * from Employees;

-- Delete the employee whose Empno is 105
delete from Employees where Empno=105;
select * from Employees;

drop database Employee;
