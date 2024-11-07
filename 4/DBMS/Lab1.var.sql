-- Create a user and grant all permissions to the user.
create user 'test'@'localhost' identified by 'test';
grant all privileges on *.* to 'test'@'localhost';
flush privileges;
show grants for 'test'@'localhost';

-- Insert the any three records in the employee table contains attributes
-- Empno,Ename,Job,Manager_No,Sal,Commission and use rollback, Check the result.
create database Employee;
use Employee;

-- Create Table
create table Employee(
	Empno int,Ename varchar(20),Job varchar(20),Manager_No int,Salary Decimal(10,2),Commission int
);

-- Get table info
desc Employee;

-- Insert data into table
insert into Employee values(
	100,'Abhishek','Manager',10,25000,70
),(
	101,'Bharat','Analyst',20,20000,60
),(
	102,'Charan','Trainee',30,15000,50
);
select * from Employee;
commit;

-- insert after commit
insert into Employee values(
	103,'Ganesh','Trainee',40,15000,50
);
select * from Employee;

-- disable autocommit
set autocommit=0;
insert into Employee values(
	103,'Noob','Trainee',40,15000,50
);
select * from Employee;

-- check rollaback
rollback;
select * from Employee;

-- Add primary key constraint and not null constraint to the employee table
alter table Employee add primary key(Empno), modify Ename varchar(20) NOT NULL;
desc Employee;

-- Insert null values to the employee table and verify the result
insert into Employee values(
	104,'Karan','Trainee',40,NULL,50
);
select * from Employee;

drop database Employee;
drop user 'test'@'localhost';
