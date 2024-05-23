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

create table Osoba
(
	ID int primary key identity,
	Imie varchar(30) not null,
	Nazwisko varchar(50) not null,
	UlicaDom varchar(100),
	MiastoDom varchar(100),
	UlicaPraca varchar(100),
	MiastoPraca varchar(100)
)
"""

cursor.execute(STARTING_SQL_QUERY)
conn.commit()


class Adres(BaseModel):
    ulica: str
    miasto: str

    def __str__(self) -> str:
        return f"Ulica: {self.ulica}, miasto: {self.miasto}"

class Osoba(BaseModel):
    imie: str
    nazwisko: str
    ulicadom: str
    miastodom: str
    ulicapraca: str
    miastopraca: str

    def __str__(self) -> str:
        return f"Imie: {self.imie}, nazwisko: {self.nazwisko}, adres dom: ({Adres(ulica=self.ulicadom, miasto=self.miastodom)}), adres praca: ({Adres(ulica=self.ulicapraca, miasto=self.miastopraca)})"

domowyAdres = Adres(ulica="Grabiszyńska", miasto="Wrocław")
sluzbowyAdres = Adres(ulica="Szczytnicka", miasto="Wrocław")
osoba = Osoba(imie="Jan", nazwisko="Kowalski", ulicadom=domowyAdres.ulica, miastodom=domowyAdres.miasto, ulicapraca=sluzbowyAdres.ulica, miastopraca=sluzbowyAdres.miasto)


INSERT_OSOBA_SQL_QUERY = """
    insert into Osoba (Imie, Nazwisko, UlicaDom, MiastoDom, UlicaPraca, MiastoPraca)
    values (%s, %s, %s, %s, %s, %s)
"""


cursor.execute(INSERT_OSOBA_SQL_QUERY, (osoba.imie, osoba.nazwisko, osoba.ulicadom, osoba.miastodom, osoba.ulicapraca, osoba.miastopraca))
conn.commit()


SELECT_OSOBA_SQL_QUERY = """
    select * from Osoba
"""

cursor.execute(SELECT_OSOBA_SQL_QUERY)
records = cursor.fetchall()
for r in records:
    o = Osoba(imie=r['Imie'], nazwisko=r['Nazwisko'], ulicadom=r['UlicaDom'], miastodom=r['MiastoDom'], ulicapraca=r['UlicaPraca'], miastopraca=r['MiastoPraca'])
    print(o)
