create database Company5;
use Company5;

-- create Employee table with records
create table Employee(
	E_id int,
	E_name varchar(255),
	Age int,
	Salary decimal(10,2)
);

insert into Employee values(
	1,'Shankar',30,50000.00
),(
	2,'Rahul',25,45000.00
),(
	3,'Muskaan',35,62000.00
),(
	4,'Mathew',28,52000.00
),(
	5,'Raj',32,58000.00
);

select * from Employee;

delimiter |

create procedure fetch_employee_data() begin
	-- Declare variables to store cursor values
	declare emp_id int;
	declare emp_name varchar(255);
	declare emp_age int;
	declare emp_salary decimal(10,2);

	-- Declare a cursor for the Employee table
	declare emp_cursor cursor for select E_id,E_name,Age,Salary from Employee;

	-- Declare a cursor for the Employee table
	declare continue handler for not found set @finished=1;

	-- Open the cursor
	open emp_cursor;

	-- Initialize a variable to control cursor loop
	set @finished=0;

	-- Loop through the cursor results
	cursor_loop: loop
		-- Fetch the next row from the cursor into variables
		fetch emp_cursor into emp_id,emp_name,emp_age,emp_salary;

		-- Check if no more rows to fetch
		if @finished=1 then
			leave cursor_loop;
		end if;

		-- Output or process each row
		select concat(
			'Employee ID : ',emp_id,
			' | Name : ',emp_name,
			' | Age : ',emp_age,
			' | Salary : ',emp_salary
		) as employee_info;
	end loop;

	-- Close the cursor
	close emp_cursor;
end |

delimiter ;
call fetch_employee_data();
drop database Company5;
