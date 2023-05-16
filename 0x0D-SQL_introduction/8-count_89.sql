-- Script: count_records.sql
-- Description: Displays the number of records with id = 89 in the first_table of the hbtn_0c_0 database

-- Specify the database and table names
SET @database_name = 'hbtn_0c_0';
SET @table_name = 'first_table';

-- Specify the id value to count
SET @id = 89;

-- Count the number of records with id = 89
SELECT COUNT(*) AS record_count
FROM `@database_name`.`@table_name`
WHERE id = @id;

