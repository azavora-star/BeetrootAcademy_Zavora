-- Task 1

-- Create a table

-- Create a table of your choice inside the sample SQLite database, rename it, and add a new column. Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

-- As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this task




CREATE TABLE test.sql_basics_p1
(
)
;

ALTER TABLE IF EXISTS test.sql_basics_p1
    OWNER to beetroot_test;
        
    
ALTER TABLE IF EXISTS test.sql_basics_p1
    ADD COLUMN bbg_ticker "char";

COMMENT ON COLUMN test.sql_basics_p1.bbg_ticker
    IS 'bloomberg data identifier ';    
    
ALTER TABLE IF EXISTS test.sql_basics
    OWNER to beetroot_test;
    
    
INSERT INTO test.sql_basics(
	isin, com_descrip, bbg, ric)
	VALUES ('US0378331005','Apple Inc.','AAPL US Equity','AAPL.O');  
	
delete from test.sql_basics where isin = 'isin'	  