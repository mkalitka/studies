from pydantic import BaseModel

class Osoba(BaseModel):
    imie: str
    nazwisko: str

os = Osoba(imie="Jan", nazwisko="Kowalski")

p1 = os.model_copy()
p2 = os.model_copy()

if p1 == p2:
    print("Ta sama osoba")
else:
    print("Różne osoby")

p1.imie = "John"

p3 = os.model_copy()

if p1 == p3:
    print("Ta sama osoba")
else:
    print("Różne osoby")
