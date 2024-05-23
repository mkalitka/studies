-- Dirty read occurs when a transaction reads uncommitted changes made by another transaction

-- Transaction 1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN TRANSACTION;

UPDATE SalesLT.Customer
SET CompanyName = 'Temporary Name'
WHERE CustomerID = 1;

-- Transaction 2
BEGIN TRANSACTION;



-- Back to Transaction 1
SELECT CompanyName 
FROM SalesLT.Customer
WHERE CustomerID = 1;

ROLLBACK TRANSACTION; -- T1 rolls back its changes



-- Non repeatable read occurs when a transaction reads the same data twice but gets different results
-- because another transaction has modified the data in between the reads.

-- Transaction 1
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRANSACTION;

SELECT CompanyName
FROM SalesLT.Customer
WHERE CustomerID = 1;

-- Transaction 2
BEGIN TRANSACTION;

UPDATE SalesLT.Customer
SET CompanyName = 'Updated Name'
WHERE CustomerID = 1;

COMMIT TRANSACTION;

-- Back to Transaction 1
SELECT CompanyName 
FROM SalesLT.Customer
WHERE CustomerID = 1; -- Now reads 'Updated Name'

ROLLBACK TRANSACTION; -- T1 rolls back



-- A phantom read occurs when a transaction retrieves a set of rows twice but gets a different set of rows
-- because another transaction has inserted or deleted rows in the meantime.

-- Transaction 1
BEGIN TRANSACTION;

SELECT * 
FROM SalesLT.Customer
WHERE CompanyName LIKE 'A%'; -- Returns 5 rows

-- Transaction 2
BEGIN TRANSACTION;

INSERT INTO SalesLT.Customer (FirstName, CompanyName, Phone, EmailAddress)
VALUES ('xyz', 'Apex Ltd', '123-456-7890', 'contact@apex.com');

COMMIT TRANSACTION;

-- Back to Transaction 1
SELECT * 
FROM SalesLT.Customer
WHERE CompanyName LIKE 'A%'; -- Now returns 6 rows

ROLLBACK TRANSACTION; -- T1 rolls back
