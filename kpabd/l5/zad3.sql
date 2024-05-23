SET STATISTICS TIME ON
GO

SET SHOWPLAN_ALL ON;
GO

-- Wyswietlanie indeksów klastrowanych
SELECT TableName = t.name, ClusteredIndexName = i.name, ColumnName = c.Name
FROM sys.tables t
INNER JOIN sys.indexes i ON t.object_id = i.object_id
INNER JOIN sys.index_columns ic ON i.index_id = ic.index_id AND i.object_id = ic.object_id
INNER JOIN sys.columns c ON ic.column_id = c.column_id AND ic.object_id = c.object_id
WHERE i.index_id = 1
AND EXISTS (
    SELECT * 
    FROM sys.columns c2 
    WHERE ic.object_id = c2.object_id AND c2.is_identity = 1
)
GO

DROP INDEX Ksiazka_PK ON Ksiazka;

-- Zmiana indeksu klastrowanego
CREATE CLUSTERED INDEX ClusteredIX_Ksiazka ON Ksiazka (Ksiazka_ID, Rok_Wydania DESC, Tytul ASC);

-- Optymalizacja sortowania na podstawie rok wydania i tytul, jeśli tabela jest używana głównie do odczytu danych
SELECT TOP 10 Rok_Wydania, Tytul FROM Ksiazka;

DROP INDEX ClusteredIX_Ksiazka ON Ksiazka;
GO

-- Tworzenie indeksu pokrywającego
-- Indeksy pokrywające mogą uprościć plany wykonania generowane przez optymalizator zapytań. Zapewniając wszystkie niezbędne dane w indeksie,
-- silnik bazy danych nie musi wykonywać dodatkowych sprzężeń lub wyszukiwań, które mogą komplikować plany wykonania i obniżać wydajność
CREATE NONCLUSTERED INDEX NonClusteredIX_Egzemplarz ON Egzemplarz (Ksiazka_ID, Sygnatura);

SELECT TOP 10 Sygnatura, Ksiazka_ID FROM Egzemplarz;

DROP INDEX NonClusteredIX_Egzemplarz ON Egzemplarz;
GO

-- Tworzenie indeksów dla optymalizacji zapytania typu JOIN
CREATE NONCLUSTERED INDEX IX_Egzemplarz_Ksiazka_ID ON Egzemplarz (Ksiazka_ID);
CREATE NONCLUSTERED INDEX IX_Ksiazka_ID ON Ksiazka (Ksiazka_ID);

-- Zapytanie optymalizowane pod kątem odczytu danych, gdy odpowiedź może zostać udzielona wyłącznie przy użyciu danych zawartych w indeksie
SELECT TOP 10 * FROM Ksiazka JOIN Egzemplarz ON Ksiazka.Ksiazka_ID = Egzemplarz.Ksiazka_ID;
GO

-- Usuwanie indeksów po zakończeniu testu
DROP INDEX IX_Egzemplarz_Ksiazka_ID ON Egzemplarz;
DROP INDEX IX_Ksiazka_ID ON Ksiazka;
GO

SET STATISTICS TIME OFF
GO

SET SHOWPLAN_ALL OFF;
GO

