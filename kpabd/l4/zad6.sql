-- Locking hints allow you to override the default locking behavior of the SQL server
-- for a specific query. They provide granular control over how SQL Server acquires and
-- manages locks during query execution. Commond locking hints include
-- NOLOCK, READPAST, UPDLOCK, and XLOCK.


CREATE TABLE IF NOT EXISTS TestData (
    ID INT PRIMARY KEY,
    Value NVARCHAR(50)
);

INSERT INTO TestData (ID, Value)
VALUES (1, 'Value 1'), (2, 'Value 2'), (3, 'Value 3');
GO;



SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
-- Example without NOLOCK
SELECT * FROM TestData;
GO;
-- Check locks, expected behavior:
-- Shared locks (S) on rows in TestData are held until the transaction completes.
-- Range locks to prevent inserts/deletes in the queried range.
ROLLBACK TRANSACTION;
GO;



SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;
-- Example with NOLOCK
SELECT * FROM TestData WITH (NOLOCK);
GO;
-- Check locks, expected behavior:
-- No shared locks (S) are held on rows in TestData.
-- The query reads uncommitted data and allows other transactions to modify the rows.
ROLLBACK TRANSACTION;
GO;



-- Query to inspect the locks:
SELECT 
    request_session_id AS spid,
    resource_type AS ResourceType,
    resource_associated_entity_id AS EntityID,
    request_mode AS LockMode,
    request_status AS LockStatus
FROM sys.dm_tran_locks
WHERE request_session_id = SESSION_ID();
