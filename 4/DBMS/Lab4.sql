create database Customer;
use Customer;

create table Customers(
	ID int primary key,
	Name varchar(20) not null,
	Age int not null,
	Address varchar(20) not null,
	Salary decimal(10,2) not null
);

insert into Customers values(
	1,'Avinash',24,'Manglore',20000
),(
	2,'Bhavish',24,'Manglore',30000
),(
	3,'Chetan',24,'Manglore',35000
),(
	4,'Krithi',24,'Manglore',50000
),(
	5,'Ramya',24,'Manglore',40000
);
select * from Customers;

-- create triggers and use delimiter as '|'
delimiter |

-- trigger for insert
create trigger after_insert_salary_difference after insert on Customers for each row begin
	set @my_sal_diff=
	concat('Salary inserted is ',new.Salary);
end; |

-- trigger for update
create trigger after_update_salary_difference after update on Customers for each row begin
	declare old_salary decimal(10, 2);
	declare new_salary decimal(10, 2);
	set old_salary = old.Salary;
	set new_salary = new.Salary;
	set @my_sal_diff =
	concat('Salary difference after update is ',new.Salary - old.Salary);
end; |

-- trigger for delete
create trigger after_delete_salary_difference after delete on Customers for each row begin
	set @my_sal_diff=
	concat('Salary deleted is ',old.Salary);
end; |
delimiter ;

-- check triggers for insert
insert into Customers values(
	6,'Shankar',35,'Bangalore',50000
);
select @my_sal_diff as Sal_diff;

-- check triggers for update
update Customers set Salary=55000 where ID=6;
select @my_sal_diff as Sal_diff;

-- check triggers for delete
delete from Customers where ID=6;
select @my_sal_diff as Sal_diff;

-- drop database to remove duplication
drop database Customer;
