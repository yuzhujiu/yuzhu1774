--唯一索引
create table index_test(
id int auto_increment,
name varchar(30),
primary key(id),
unique (name)
);

create table index_test(
id int primary key auto_increment,
name varchar(30) unique,
);

--class 表添加name字段普通索引
create index nameIndex on class(name);


--查看索引三法
desc class;
show create table class;
show index from class;

--删除索引
drop index name on index_test


