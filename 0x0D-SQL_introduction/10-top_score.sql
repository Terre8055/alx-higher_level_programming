-- Script: list_second_table_records.sql
-- Description: Lists all records from the second_table in the hbtn_0c_0 database

-- Specify the database name
SET @database_name = 'hbtn_0c_0';

-- List all records from the second_table
SELECT score, name
FROM `@database_name`.`second_table`
ORDER BY score DESC;

