import pymssql
from pydantic import BaseModel

conn = pymssql.connect(
    server='localhost:1434',
    user='mikolaj.kalitka',
    password='Test1234',
    database='test',
    as_dict=True
)
cursor = conn.cursor()

STARTING_SQL_QUERY = """
drop table if exists Osoba;
drop table if exists Jednostka;

create table Jednostka( ID int not null primary key identity, Nazwa varchar(20) );

set IDENTITY_INSERT Jednostka ON;

begin
  insert into Jednostka(ID, Nazwa) values( 1, 'Wrocław' );
  insert into Jednostka(ID, Nazwa) values( 2, 'Poznań' );
  insert into Jednostka(ID, Nazwa) values( 3, 'Kraków' );
  insert into Jednostka(ID, Nazwa) values( 4, 'Warszawa' );
end;

set IDENTITY_INSERT Jednostka OFF;

create table Osoba( ID int not null primary key identity, ID_Jednostka int references Jednostka(ID), Imie varchar(30), Nazwisko varchar(50), Pensja int)

set IDENTITY_INSERT Osoba ON;

begin
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 1, 1, 'Jan', 'Kowalski', 1000 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 2, 3, 'Ewa', 'Solska', 1200 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 3, 2, 'Bożydar', 'Nowak', 1500 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 4, 4, 'Adam', 'Adamski', 1700 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 5, 4, 'Zygmunt', 'Riposta', 1240 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 6, 2, 'Alicja', 'Gleba', 1600 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 7, 1, 'Tania', 'Borówka', 1560 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 8, 1, 'Natasza', 'Lizacka', 2500 );
  insert into Osoba(ID,ID_Jednostka,Imie,Nazwisko,Pensja) values( 9, 3, 'Stan', 'Taczkowski', 1900 );
end;

set IDENTITY_INSERT Osoba OFF;
"""

cursor.execute(STARTING_SQL_QUERY)
conn.commit()


# add j1 to the database
class Jednostka(BaseModel):
    id: int
    nazwa: str

    def __str__(self) -> str:
        return f"ID: {self.id}, Nazwa: {self.nazwa}"

j1 = Jednostka(id=5, nazwa='Londyn')

INSERT_JEDNOSTKA_SQL_QUERY = """
set IDENTITY_INSERT Jednostka ON;
insert into Jednostka(ID, Nazwa) values( %s, %s );
set IDENTITY_INSERT Jednostka OFF;
"""

cursor.execute(INSERT_JEDNOSTKA_SQL_QUERY, (j1.id, j1.nazwa))
conn.commit()

# select all Jednostka
SELECT_JEDNOSTKA_SQL_QUERY = "select * from Jednostka as j order by j.Nazwa"

cursor.execute(SELECT_JEDNOSTKA_SQL_QUERY)
records = cursor.fetchall()
for r in records:
    j = Jednostka(id=r['ID'], nazwa=r['Nazwa'])
    print(j)

# close
cursor.close()
conn.close()
