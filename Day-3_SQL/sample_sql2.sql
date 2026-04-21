create database lk_db;

show databases;

use lk_db;

create table user (
	user_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100) unique,
    created_at timestamp default current_timestamp
);

-- inserting record
insert into user (first_name, last_name, email)
values
("john","cena","john@gmail.com"),
("bob","marley","bob@gmail.com");


insert into user (first_name, last_name, email)
values
("alice","wonderland","alice@gmail.com"),
("michael","jackson","michael@gmail.com"),
("sachin","tendulkar","sachin@gmail.com"),
("bruce","wayne","bruce@gmail.com"),
("tony","stark","tony@gmail.com"),
("clark","kent","clark@gmail.com"),
("peter","parker","peter@gmail.com"),
("steve","jobs","steve@gmail.com");

-- fetch record
select * from user;

-- fetch record based on user id
select * from user where user_id=3;

-- using like operator
select * from user where first_name LIKE "p%";

-- fetch the email of user id 2
select email from user where user_id=2;

-- show the record in descending order
select * from user order by user_id DESC;

-- get the data between a range
select * from user where user_id between 3 and 5;

-- using IN operator
select * from user where user_id IN (2,3,10,11);

-- LIMIT and OFFSET
select * from user LIMIT 2;

select * from user LIMIT 2 OFFSET 2;

-- updating the record
update user set first_name="mathew" where user_id=3;

-- delete the user
delete from user where user_id = 3;

-- aggregation func
select count(*) as total_records from user;

-- join operation
create table adress (
	adr_id int primary key auto_increment,
    adress varchar(200) not null,
    user_id int not null,
	foreign key(user_id) references user(user_id)
	  on delete cascade
	  on update cascade
);

insert into user (first_name, last_name, email)
values
("test","user","test@gmail.com");


insert into adress (adress, user_id)
values ("begumpet, hyderabad", 12);

select * from adress;

-- join user and address
select u.first_name, u.last_name, ua.adress
from user u
join
adress ua
on
u.user_id = ua.user_id;






