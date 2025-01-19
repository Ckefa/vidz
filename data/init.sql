CREATE DATABASE vidz;

USE vidz;

CREATE TABLE user (
  id VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO user VALUES ("0001", "admin");

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Admin1234';

GRANT ALL PRIVILEGES ON vidz.* TO 'admin'@'localhost';

FLUSH PRIVILEGES;

