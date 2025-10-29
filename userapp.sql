CREATE DATABASE IF NOT EXISTS user_app;
USE user_app;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, email, password) VALUES
('Akshaya', 'akshaya@example.com', 'pass123'),
('Ravi', 'ravi@example.com', 'ravi@456'),
('Priya', 'priya@example.com', 'priya@789'),
('Manoj', 'manoj@example.com', 'manoj@111'),
('Divya', 'divya@example.com', 'divya@222'),
('Arun', 'arun@example.com', 'arun@333'),
('Sneha', 'sneha@example.com', 'sneha@444'),
('Kiran', 'kiran@example.com', 'kiran@555'),
('Vikram', 'vikram@example.com', 'vikram@666'),
('Meena', 'meena@example.com', 'meena@777');

SELECT * FROM users;