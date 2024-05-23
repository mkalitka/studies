-- Query to inspect the locks
SELECT 
    request_session_id AS spid,
    resource_type AS ResourceType,
    resource_associated_entity_id AS EntityID,
    request_mode AS LockMode,
    request_status AS LockStatus
FROM sys.dm_tran_locks
WHERE request_session_id = SESSION_ID();

-- rodzaje blokad

USE Test;

drop table if exists liczby;
go
create table liczby ( liczba int );
go
insert liczby values ( 10 );
go

-- 1 --
-- repeatable read prevents non-repeatable reads (a row read once cannot be modified by
-- another transaction until the current transaction completes)
set transaction isolation level repeatable read;
begin transaction

-- w drugim po³¹czeniu robimy update: update liczby set liczba=4
-- ogl¹damy blokady: sp_lock

select * from liczby

-- ponownie w drugim po³¹czeniu robimy update: update liczby set liczba=4
-- ogl¹damy blokady: sp_lock

commit

-- 2 --
-- serializable ensures full isolation, including protection against phantom reads
-- (no new rows can be added within the range of rows read by the current transaction)
set transaction isolation level serializable;

insert liczby values ( 10 );

begin transaction

-- w drugim po³¹czeniu robimy insert: insert liczby values(151)
-- ogl¹damy blokady: sp_lock

select * from liczby

-- ponownie w drugim po³¹czeniu robimy insert: insert liczby values(151)
-- ogl¹damy blokady: sp_lock

commit

-- 3 --
-- snapshot provides a consistent view of the data as it was when the transaction started,
-- avoiding blocking by other transactions.
-- sprawdzamy opcjê Allow Snapshot Isolation
-- ALTER DATABASE AdventureWorksLT SET ALLOW_SNAPSHOT_ISOLATION ON
set transaction isolation level snapshot;
begin transaction

select * from liczby

-- ponownie w drugim po³¹czeniu robimy update: update liczby set liczba=6
-- ogl¹damy blokady: sp_lock

update liczby set liczba=7

select * from liczby

commit
