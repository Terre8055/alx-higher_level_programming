-- Script: create_second_table.sql
-- Description: Creates the second_table in the hbtn_0c_0 database and adds multiple rows

-- Specify the database name
SET @database_name = 'hbtn_0c_0';

-- Create the second_table if it doesn't exist
CREATE TABLE IF NOT EXISTS `@database_name`.`second_table` (
  id INT,
  name VARCHAR(256),
  score INT
);

-- Insert rows into the second_table
INSERT INTO `@database_name`.`second_table` (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);

