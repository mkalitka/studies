DROP TRIGGER IF EXISTS trg_UpdateModifiedDate
GO

CREATE TRIGGER trg_UpdateModifiedDate
ON SalesLT.Customer
AFTER UPDATE
AS
BEGIN
    UPDATE SalesLT.Customer
    SET ModifiedDate = GETDATE()
    FROM SalesLT.Customer AS c
    INNER JOIN inserted AS i
    ON c.CustomerID = i.CustomerID;
END
GO

BEGIN TRANSACTION
  SELECT TOP 1 CustomerID, FirstName, LastName, ModifiedDate
  FROM SalesLT.Customer

  UPDATE SalesLT.Customer
  SET FirstName = 'UpdatedName'
  WHERE CustomerID = 1

  SELECT CustomerID, FirstName, LastName, ModifiedDate
  FROM SalesLT.Customer
  WHERE CustomerID = 1
ROLLBACK TRANSACTION
GO
