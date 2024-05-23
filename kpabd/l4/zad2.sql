-- Savepoints in DBMS
-- Savepoints are markers set within a transaction in a DBMS, allowing you to partially
-- roll back a transaction to a certain point without affecting the preceding operations.
-- They are useful for error recovery in complex transactions. When a transaction is divided
-- into smaller segments, savepoints can be used to ensure that only the failed segment is undone
-- while retaining the successful parts.

USE AdventureWorksLT;

CREATE OR ALTER PROCEDURE usp_UpdateCustomerOrder
    @CustomerID INT,
    @NewPhone NVARCHAR(15),
    @OrderDate DATE,
    @TotalDue DECIMAL(10, 2)
AS
BEGIN
    BEGIN TRANSACTION;
    
    SAVE TRANSACTION CustomerUpdateSavepoint;

    BEGIN TRY
        UPDATE SalesLT.Customer
        SET Phone = @NewPhone
        WHERE CustomerID = @CustomerID;
        
        -- Simulate potential failure
        IF @NewPhone IS NULL
            THROW 51000, 'Phone number cannot be NULL', 1;

        INSERT INTO SalesLT.SalesOrderHeader (CustomerID, OrderDate, TotalDue)
        VALUES (@CustomerID, @OrderDate, @TotalDue);
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION CustomerUpdateSavepoint;
        PRINT 'Rolled back to CustomerUpdateSavepoint. Only customer update was undone.';
        
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        THROW;
    END CATCH;
END;
GO

EXEC usp_UpdateCustomerOrder 
    @CustomerID = 1, 
    @NewPhone = NULL,
    @OrderDate = '2023-10-01', 
    @TotalDue = 100.00;
GO
