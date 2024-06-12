create database employee;
use employee;

create table Employees(
	Empno int,
	Ename varchar(20),
	Job varchar(20),
	MGR int,
	Sal decimal(10,2)
);

desc employees

alter table employees add(commission int);
insert into Employee values(
        100,'Abhishek','Manager',10,25000
),(
        101,'Bharat','Analyst',20,20000
),(
        102,'Charan','Trainee',30,15000
);

select * from Employees;

update Employees set Job='Trainee' where Empno=101;
alter table employees rename column MGR to Manager_No;

select * from Employees;

delete from Employees where Empno=105;
select * from Employees;
