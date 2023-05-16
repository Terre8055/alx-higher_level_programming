-- Script: table_rows.sql
-- Description: Lists all rows of the table first_table from the hbtn_0c_0 database

-- Specify the database and table names
SET @database_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Retrieve all rows from the table
SELECT *
FROM `@database_name`.`@table_name`;

