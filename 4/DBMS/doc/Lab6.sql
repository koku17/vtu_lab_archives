create database Rollcall;
use Rollcall;

create table N_Rollcall(
	Student_id int primary key,
	Student_name varchar(255),
	Birth_date date
);

create table O_Rollcall(
	Student_id int primary key,
	Student_name varchar(255),
	Birth_date date
);

insert into O_Rollcall values(
	1,'Amit','1995-08-15'
),(
	3,'Chinmay','1992-12-10'
);

select * from O_Rollcall;

insert into N_Rollcall values(
	1,'Amit','1995-08-15'
),(
	2,'Nishmitha','1998-03-22'
),(
	3,'Chinmay','1992-12-10'
),(
	4,'Devang','2000-05-18'
),(
	5,'Manish','1997-09-03'
);

delimiter |

create procedure merge_rollcall_data() begin
	declare done int default false;
	declare n_id int;
	declare n_name varchar(255);
	declare n_birth_date varchar(255);

	declare n_cursor cursor for select Student_id,Student_name,Birth_date from N_Rollcall;
	declare continue handler for not found set done=true;
	open n_cursor;

	cursor_loop: loop
		fetch n_cursor into n_id,n_name,n_birth_date;
		if done then
			leave cursor_loop;
		end if;




		if not exists(
			select 1 from O_Rollcall where Student_id=n_id
		)then
			insert into O_Rollcall values(
				n_id,n_name,n_birth_date
			);
		end if;
	end loop;

	close n_cursor;
end |

delimiter ;

call merge_rollcall_data();

select * from O_Rollcall;
drop database Rollcall;
