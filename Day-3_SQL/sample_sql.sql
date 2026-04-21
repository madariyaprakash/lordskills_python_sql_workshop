use test_db;

create table students (
	student_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(100) unique,
    phone varchar(15),
    dob date,
    gender enum('male','female','other'),
    created_at timestamp default current_timestamp
);



create database user_db;

use user_db;

-- create user table
create table user (
	user_id int primary key auto_increment,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(150) unique,
    created_at timestamp default current_timestamp
);

-- insert record into user table
insert into user (first_name, last_name, email) values ('prakash','madariya','prakash01@gmail.com');

-- show all the records of user table
select * from user;



-- add few more records
insert into user (first_name, last_name, email) values ('john','cena','john@gmail.com');
INSERT INTO user (first_name, last_name, email) VALUES ('alice','smith','alice.smith@gmail.com');
INSERT INTO user (first_name, last_name, email) VALUES ('robert','brown','robert.brown@yahoo.com');
INSERT INTO user (first_name, last_name, email) VALUES ('maria','garcia','maria.garcia@hotmail.com');
INSERT INTO user (first_name, last_name, email) VALUES ('david','lee','david.lee@gmail.com');
INSERT INTO user (first_name, last_name, email) VALUES ('sophia','johnson','sophia.johnson@outlook.com');
INSERT INTO user (first_name, last_name, email) VALUES ('michael','williams','michael.williams@gmail.com');
INSERT INTO user (first_name, last_name, email) VALUES ('emma','martin','emma.martin@yahoo.com');
INSERT INTO user (first_name, last_name, email) VALUES ('daniel','thomas','daniel.thomas@gmail.com');


-- fetch the record where id is 6
select * from user where user_id = 6;

-- fetch the user email whose id is 5
select email from user where user_id = 5;

-- fetch the records where usernames are starting with 'd'
select * from user where first_name like 'd%' and first_name like '%d';

-- fetch record which is in the list of ids
select * from user where user_id in (1,2,4);

-- fetch record which is between some numbers
select * from user where user_id between 1 and 5;

-- change the order in descending
select * from user order by user_id asc;

-- update the firstname of prakash to pradeep 
update user set first_name="pradeep" where user_id=1;

-- Aggregate function
-- #################################
select count(*) as gmail_count from user where email like "%@gmail.com";

-- group by email domain @gmail.com and other
select substring_index(email, "@", -1) as domain, count(*) as user_count from user group by domain;
-- consist(str, delimiter, count) - positive-before occurance, negative - after occurance

-- having clause
select substring_index(email, "@", -1) as domain, count(*) as user_count from user group by domain having count(*)>6;



-- indexing =====================================
create index idx_email on user(email);

CREATE INDEX idx_user_id ON user_address(user_id);

SELECT * FROM user WHERE email = 'john@gmail.com';

-- SELECT u.first_name, ua.address
-- FROM user u
-- JOIN user_address ua ON u.user_id = ua.user_id;



-- view is virtual table which act as main table which fetches the latest data everytime we query it. Basically, it's another table where you can create a new records modifying the existing record"
create view gmail_users as
select user_id, first_name, last_name, email
from user
where email like "%@gmail.com";

-- another example - create view of full name based on their id
create view full_name_user as
select user_id, concat(first_name, ' ', last_name) as full_name from user;

-- create address table for user
create table user_address (
  address_id int primary key auto_increment,
  address varchar(200) not null,
  user_id int not null,
  foreign key(user_id) references user(user_id)
  on delete cascade
  on update cascade
);

-- add a new record to user and user_address
insert into user(first_name, last_name, email) values ("mani","kumari","mani@gmail.com");

-- insert address for the corresponding user
insert into user_address(address,user_id) values ("begumpet, hyderabad, telangana", 17);

-- add address to other users as well 
INSERT INTO user_address (address, user_id) VALUES 
('Hyderabad, India', 1),
('New York, USA', 6),
('Los Angeles, USA', 7),
('Chicago, USA', 8),
('San Francisco, USA', 9),
('Boston, USA', 10),
('Dallas, USA', 11),
('Miami, USA', 12),
('Delhi, India', 16);


-- fetch all the user address
select * from user_address;

delete from user_address where address_id between 10 and 20;

-- joing the table user and user_address
select * from user u
right join
user_address ua
on u.user_id = ua.user_id;




