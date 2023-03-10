-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa.states;
CREATE TABLE IF NOT EXISTS states (
    id INT SERIAL DEFAULT VALUE primary key,
    name VARCHAR(256)
); 