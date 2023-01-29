--部门表
CREATE TABLE dept (
id int PRIMARY KEY auto_increment,
dname varchar(50) not null
);

--员工表
CREATE TABLE person (
id int PRIMARY KEY AUTO_INCREMENT,
name varchar(32) NOT NULL,
age tinyint unsigned,
salary decimal(8,2),
dept_id int comment "关系字段"
);

insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');

insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);

insert into person values
(7,"Tonny",30,18500,8);

--为person表添加一个外键
alter table person add
constraint dept_fk
foreign key (dept_id)
references dept(id);

--删除外键
alter table person drop foreign key dept_fk;


--级联动作演示
alter table person add
foreign key (dept_id)
references dept(id);

alter table person
drop foreign key person_ibfk_1;

--主表改从表随着改
alter table person add
foreign key (dept_id)
references dept(id)
on delete cascade on update cascade;

--主表变，从表变成null
alter table person add
foreign key (dept_id)
references dept(id)
on delete set null on update set null;

--多对多关系表达
CREATE TABLE athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  age tinyint NOT NULL,
  country varchar(30) NOT NULL
);

CREATE TABLE sports (
  id int primary key AUTO_INCREMENT,
  sport varchar(30) NOT NULL
);

CREATE TABLE athlete_sports (
   id int primary key auto_increment,
   athlete_id int NOT NULL,
   sports_id int NOT NULL,
   FOREIGN KEY (athlete_id) REFERENCES athlete (id),
   FOREIGN KEY (sports_id) REFERENCES sports (id)
);

--在关系表中增加一个名次字段
alter table athlete_sports add ranking int;























