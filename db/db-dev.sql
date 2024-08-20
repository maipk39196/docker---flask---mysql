CREATE DATABASE db-dev;
USE db-dev;

CREATE TABLE users (
    uid int not null AUTO_INCREMENT,
    name varchar(100) not null,
    age int (100) not null,
    PRIMARY KEY (uid)
);
INSERT INTO users (uid, name, age) VALUES
(121, 'Alice', 18),
(122, 'Bob', 17),
(123, 'Cindy', 25),
(124, 'Dan', 21);


INSERT INTO users(name, age)
VALUES("Dunk", "22"), ("Just_test","18");

