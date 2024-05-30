create table Employee(
	E_id int PRIMARY KEY,
	E_name varchar(255),
	Age int,
	Salary decimal(10,2)
);

select count(E_name) as TotalEmployees from Employee;
select max(Age) as MaxAge from Employee;
select min(Age) as MinAge from Employee;
select E_name,Salary from Employee order by Salary asc;
select Salary,count(*) as EmployeeCount
from Employee group by Salary;
