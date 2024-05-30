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
);

insert into Employee values(
        101,'Bharat','Analyst',20,20000
);

insert into Employee values(
        102,'Charan','Trainee',30,15000
);

select * from Employees;

update Employees set Job='Trainee' where empno=101;

alter table employees rename column mgr to manager_no;

select * from Employees;

delete from Employees where empno=105;

select * from Employees;
