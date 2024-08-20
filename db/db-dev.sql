CREATE DATABASE db-dev;
USE db-dev;

CREATE TABLE users (
    uid int not null AUTO_INCREMENT,
    name varchar(100) not null,
    age int (100) not null,
    PRIMARY KEY (uid)
);

INSERT INTO USERS(name, age)
VALUES("Dunk", "22"), ("Just_test","18");