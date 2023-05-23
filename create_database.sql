create database itracker;
use itracker;
create table word
( id int NOT NULL auto_increment,
    word varchar(255) NOT NULL,
    PRIMARY KEY (id) 
    );
insert into word (word) values ('grenouille'),('pomme')
,('banane'),('cerise'),('durian'),('oeuf');