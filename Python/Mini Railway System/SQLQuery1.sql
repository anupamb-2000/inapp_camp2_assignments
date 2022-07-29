CREATE DATABASE railways_db

USE railways_db

CREATE TABLE trains(
train_no INT PRIMARY KEY,
train_name VARCHAR(25),
start_station VARCHAR(50),
end_station VARCHAR(50),
available_seats INT,
waiting_list INT
);

CREATE TABLE stations(
station_id INT PRIMARY KEY,
station_name VARCHAR(25)
);

CREATE TABLE stops(
train_no INT FOREIGN KEY(train_no) REFERENCES trains,
station_id INT FOREIGN KEY(station_id) REFERENCES stations
);

CREATE TABLE passengers(
id INT IDENTITY PRIMARY KEY,
name VARCHAR(25),
age INT,
gender VARCHAR(2),
start_station VARCHAR(25),
end_station VARCHAR(25),
seats INT,
train_no INT FOREIGN KEY(train_no) REFERENCES trains,
ticket_status VARCHAR(25)
);

INSERT INTO trains VALUES
(123, 'TVM_ALP', 'TVM', 'ALP', 5, 2),
(142, 'TVM_ERN', 'TVM', 'ERN', 5, 2),
(135, 'TVM_KZK', 'TVM', 'KZK', 5, 2)

INSERT INTO stations VALUES
(1, 'ALP'),
(2, 'ERN'),
(3, 'KZK'),
(4, 'TVM')

INSERT INTO stops VALUES
(123, 1),
(142, 1),
(142, 2),
(135, 1),
(135, 2),
(135, 3)

SELECT * FROM trains
SELECT * FROM stations
SELECT * FROM stops
SELECT * FROM passengers

CREATE VIEW destinations AS 
SELECT DISTINCT stations.station_name 
FROM stations
JOIN stops 
ON stations.station_id = stops.station_id

SELECT * FROM destinations
