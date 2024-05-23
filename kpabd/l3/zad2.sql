-- Static Cursor: A static cursor returns a result set that is fixed at the time the cursor is opened.
-- Changes made to the data in the database after the cursor is opened are not visible through the cursor.

-- Dynamic Cursor: A dynamic cursor reflects all changes made to the rows in its result set as you scroll around the cursor. 
-- The data values, order, and membership of the rows can change on each fetch.

-- Keyset Cursor: A keyset cursor is a hybrid of static and dynamic cursors. 
-- It behaves like a dynamic cursor in that it detects changes to the membership and order of its result set when scrolling through the cursor. 
-- However, it behaves like a static cursor in that it does not detect changes to the values in the rows of its result set.

SET NOCOUNT ON

DROP TABLE IF EXISTS numbers
GO
CREATE TABLE numbers ( prim_key INT PRIMARY KEY, nr INT )
GO
DECLARE @a INT
SET @a = 1
WHILE ( @a <= 60 )
BEGIN
  INSERT numbers VALUES ( @a, @a )
  SET @a = @a + 1
END
GO

DECLARE @x INT
SET @x = 10

-- DECLARE c CURSOR STATIC FOR SELECT nr FROM numbers WHERE nr <= @x
-- DECLARE c CURSOR DYNAMIC FOR SELECT nr FROM numbers WHERE nr <= @x
DECLARE c CURSOR KEYSET FOR SELECT nr FROM numbers WHERE nr <= @x

SET @x = 20

OPEN c

DECLARE @aux INT, @counter INT
SET @counter = 2

PRINT 'Next numbers from the cursor:'
FETCH NEXT FROM c INTO @aux
WHILE ( @@fetch_status = 0 )
BEGIN
  PRINT @aux
  PRINT 'number: ' + CAST(@aux AS VARCHAR)
  PRINT 'counter: ' + CAST(@counter AS VARCHAR)
  DELETE FROM numbers WHERE nr = @counter
  FETCH NEXT FROM c INTO @aux
  SET @counter = @counter + 2
END
CLOSE c
DEALLOCATE c
PRINT 'End of the cursor, status: ' + CAST(@@fetch_status AS VARCHAR)

SELECT * FROM numbers WHERE nr <= 10
