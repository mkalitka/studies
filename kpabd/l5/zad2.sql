DROP TABLE IF EXISTS Wypozyczenie;
DROP TABLE IF EXISTS Egzemplarz;
DROP TABLE IF EXISTS Ksiazka;
DROP TABLE IF EXISTS Czytelnik;
GO

DROP PROCEDURE IF EXISTS P1;
DROP PROCEDURE IF EXISTS P2;
DROP PROCEDURE IF EXISTS P3;
GO

CREATE TABLE Czytelnik (
    Czytelnik_ID INT IDENTITY(1,1) PRIMARY KEY,  -- Dodano IDENTITY
    PESEL VARCHAR(11) NOT NULL,
    Nazwisko VARCHAR(255),
    Miasto VARCHAR(255),
    Data_Urodzenia DATE
);

CREATE TABLE Ksiazka (
    Ksiazka_ID INT IDENTITY(1,1) PRIMARY KEY,  -- Dodano IDENTITY
    ISBN VARCHAR(20),
    Tytul VARCHAR(255),
    Autor VARCHAR(255),
    Rok_Wydania INT,
    Cena DECIMAL(10, 2)
);

CREATE TABLE Egzemplarz (
    Egzemplarz_ID INT IDENTITY(1,1) PRIMARY KEY,  -- Dodano IDENTITY
    Ksiazka_ID INT FOREIGN KEY REFERENCES Ksiazka(Ksiazka_ID),
    Sygnatura VARCHAR(20)
);

CREATE TABLE Wypozyczenie (
    Wypozyczenie_ID INT IDENTITY(1,1) PRIMARY KEY,  -- Dodano IDENTITY
    Czytelnik_ID INT FOREIGN KEY REFERENCES Czytelnik(Czytelnik_ID),
    Egzemplarz_ID INT FOREIGN KEY REFERENCES Egzemplarz(Egzemplarz_ID),
    Data DATE,
    Liczba_Dni INT
);

GO

-- all join
CREATE PROCEDURE P1 AS
BEGIN
    SELECT DISTINCT c.PESEL, c.Nazwisko
    FROM Egzemplarz e
    JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
    JOIN Wypozyczenie w ON e.Egzemplarz_ID = w.Egzemplarz_ID
    JOIN Czytelnik c ON c.Czytelnik_ID = w.Czytelnik_ID;
END;
GO

-- 1 subquery
CREATE PROCEDURE P2 AS
BEGIN
    SELECT c.PESEL, c.Nazwisko
    FROM Czytelnik c
    WHERE c.Czytelnik_ID IN (
        SELECT w.Czytelnik_ID FROM Wypozyczenie w
        JOIN Egzemplarz e ON e.Egzemplarz_ID = w.Egzemplarz_ID
        JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
    );
END;
GO

-- 2 subqueries
CREATE PROCEDURE P3 AS
BEGIN
    SELECT DISTINCT c.PESEL, c.Nazwisko
    FROM Czytelnik c
    WHERE c.Czytelnik_ID IN (
        SELECT DISTINCT w.Czytelnik_ID
        FROM Wypozyczenie w
        WHERE w.Egzemplarz_ID IN (
            SELECT e.Egzemplarz_ID
            FROM Egzemplarz e
            JOIN Ksiazka k ON e.Ksiazka_ID = k.Ksiazka_ID
        )
    );
END;
GO

-- execution plans
SET SHOWPLAN_ALL ON;
GO

EXEC P1;
EXEC P2;
EXEC P3;
GO

SET SHOWPLAN_ALL OFF;
GO

SET IDENTITY_INSERT Ksiazka ON
INSERT INTO Ksiazka (Ksiazka_ID, ISBN, Tytul, Autor, Rok_Wydania, Cena) VALUES
(1, '978-83-246-1234-5', 'Database Administration Guide', 'Helen Feddema', 2006, 69),
(2, '978-83-246-5678-9', 'Programming SQL Server', 'Robert Vieira', 2007, 97),
(3, '978-83-246-6543-2', 'SQL Server Essentials', 'Eric L. Brown', 2007, 57),
(4, '978-83-246-9876-5', 'PHP & MySQL Web Development', 'Włodzimierz Gajda', 2010, 79),
(5, '978-83-246-1111-3', 'Access 2007 PL', 'Andrew Unsworth', 2009, 39),
(6, '978-83-246-7890-0', 'Clean Code', 'Robert C. Martin', 2010, 67);
SET IDENTITY_INSERT Ksiazka OFF
GO

SET IDENTITY_INSERT Egzemplarz ON
INSERT INTO Egzemplarz (Egzemplarz_ID, Ksiazka_ID, Sygnatura) VALUES
(1, 5, 'S0001'),
(2, 5, 'S0002'),
(3, 1, 'S0003'),
(4, 1, 'S0004'),
(5, 1, 'S0005'),
(6, 2, 'S0006'),
(7, 3, 'S0007'),
(8, 3, 'S0008'),
(9, 3, 'S0009'),
(10, 3, 'S0010'),
(11, 6, 'S0011'),
(12, 6, 'S0012'),
(13, 4, 'S0013'),
(14, 4, 'S0014'),
(15, 4, 'S0015');
SET IDENTITY_INSERT Egzemplarz OFF
GO

SET IDENTITY_INSERT Czytelnik ON
INSERT INTO Czytelnik (CZYTELNIK_ID, PESEL, NAZWISKO, MIASTO, DATA_URODZENIA) VALUES
(1, '44050812345', 'Jankowski', 'Kraków', '1985-05-08'),
(2, '49091223456', 'Bąk', 'Gdańsk', '1990-09-12'),
(3, '53041534567', 'Mazur', 'Poznań', '1995-04-15');
SET IDENTITY_INSERT Czytelnik OFF;
GO

SET IDENTITY_INSERT Wypozyczenie ON;
INSERT INTO Wypozyczenie (Wypozyczenie_ID, Czytelnik_ID, Egzemplarz_ID, Data, Liczba_Dni) VALUES
(1, 1, 3, '2023-04-01', 10),
(2, 1, 4, '2023-05-15', 14),
(3, 1, 5, '2023-06-05', 30),
(4, 2, 7, '2023-07-01', 5),
(5, 3, 8, '2023-07-02', 20),
(6, 3, 12, '2023-08-01', 18),
(7, 3, 13, '2023-08-10', 10),
(8, 1, 9, '2023-09-01', 7),
(9, 2, 11, '2023-09-10', 12),
(10, 2, 10, '2023-10-01', 14),
(11, 3, 6, '2023-10-15', 15),
(12, 1, 14, '2023-11-01', 6),
(13, 2, 5, '2023-11-05', 9);
SET IDENTITY_INSERT Wypozyczenie OFF;
GO

DECLARE @StartTime1 DATETIME, @EndTime1 DATETIME;
DECLARE @StartTime2 DATETIME, @EndTime2 DATETIME;
DECLARE @StartTime3 DATETIME, @EndTime3 DATETIME;

SET @StartTime1 = GETDATE();
EXEC P1;
SET @EndTime1 = GETDATE();

SET @StartTime2 = GETDATE();
EXEC P2;
SET @EndTime2 = GETDATE();

SET @StartTime3 = GETDATE();
EXEC P3;
SET @EndTime3 = GETDATE();

DECLARE @Runtime1 INT, @Runtime2 INT, @Runtime3 INT;
SET @Runtime1 = DATEDIFF(ms, @StartTime1, @EndTime1);
SET @Runtime2 = DATEDIFF(ms, @StartTime2, @EndTime2);
SET @Runtime3 = DATEDIFF(ms, @StartTime3, @EndTime3);

PRINT 'Time P1: ' + CAST(@Runtime1 AS VARCHAR) + ' ms';
PRINT 'Time P2: ' + CAST(@Runtime2 AS VARCHAR) + ' ms';
PRINT 'Time P3: ' + CAST(@Runtime3 AS VARCHAR) + ' ms';
GO
