create table users(                                     loginid varchar(30) primary key,
password varchar(30),
etype varchar(20));   


create table master(
empid int primary key,
ename varchar(30) not null,
desig varchar(30) not null,
bsalary float,
address varchar(50),
pin varchar(10),
city varchar(20),
loginid varchar(30));


alter table master add constraint fk010 foreign key fk010(loginid) references users(loginid);

create table attendence(
empid int,
adate varchar(15),
intime varchar(20),
outtime varchar(20));
alter table attendence add constraint fk011 foreign key fk011(empid) references master(empid);


select * from user_constraints;