# Create User and grant all permissions
create user 'tester'@'localhost' identified by 'tester';
grant all privileges on *.* to 'tester'@'localhost';
flush privileges;
show grants for 'tester'@'localhost';

# Create db
create database employee;
use employee;
show databases;

# Create Table
create table Employee(
	Empno int,Ename varchar(20),Job varchar(20),Manager_No int,Salary Decimal(10,2),Commission int
);

# Get table info
desc Employee;

# Insert data into table
insert into Employee values(
	100,'Abhishek','Manager',10,25000,70
);

insert into Employee values(
	101,'Bharat','Analyst',20,20000,60
);

insert into Employee values(
	102,'Charan','Trainee',30,15000,50
);

select * from Employee;

commit;

insert into Employee values(
	103,'Ganesh','Trainee',40,15000,50
);

select * from Employee;

set autocommit=0;

insert into Employee values(
	103,'Noob','Trainee',40,15000,50
);

select * from Employee;
rollback;
select * from Employee;

# Primary Key
alter table Employee add primary key(Empno), modify Ename varchar(20) NOT NULL;
desc Employee;

insert into Employee values(
	104,'Karan','Trainee',40,NULL,50
);

select * from Employee;

drop database employee;
