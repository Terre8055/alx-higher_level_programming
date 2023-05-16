-- Script: table_description.sql
-- Description: Prints the full description of the table first_table from the hbtn_0c_0 database

-- Specify the database and table names
SET @database_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Retrieve the table description
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM information_schema.columns
WHERE TABLE_SCHEMA = @database_name
  AND TABLE_NAME = @table_name;

