-- Script: insert_row.sql
-- Description: Inserts a new row into the first_table in the hbtn_0c_0 database

-- Specify the database and table names
SET @database_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Specify the values for the new row
SET @id = 89;
SET @name = 'Best School';

-- Insert the new row into the table
INSERT INTO `@database_name`.`@table_name` (id, name)
VALUES (@id, '@name');

