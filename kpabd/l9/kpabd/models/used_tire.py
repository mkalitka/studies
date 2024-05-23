from ..connection import manager
from .tire import Tire

class UsedTire(Tire):
    production_year: int
    consumption_level: str


    def __str__(self):
        return f"ID: {self.id}, OEM: {self.oem}, Manufacturer: {self.manufacturer}, Number: {self.number}, Description: {self.description}, Speed: {self.speed}, Rating: {self.rating}, Production Year: {self.production_year}, Consumption Level: {self.consumption_level}"


def insert(used_tire):
    INSERT_USEDTIRE_QUERY = """
        INSERT INTO usedtires (id, oem, manufacturer, number, description, speed, rating, production_year, consumption_level)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    manager.cursor.execute(INSERT_USEDTIRE_QUERY, (used_tire.id, used_tire.oem, used_tire.manufacturer, used_tire.number, used_tire.description, used_tire.speed, used_tire.rating, used_tire.production_year, used_tire.consumption_level))
    manager.conn.commit()


def find(id):
    FIND_USEDTIRE_QUERY = """
        SELECT * FROM usedtires WHERE id = %s;
    """
    manager.cursor.execute(FIND_USEDTIRE_QUERY, (id,))
    record = manager.cursor.fetchone()
    manager.conn.commit()
    return UsedTire(id=record["id"], oem=record["oem"], manufacturer=record["manufacturer"], number=record["number"], description=record["description"], speed=record["speed"], rating=record["rating"], production_year=record["production_year"], consumption_level=record["consumption_level"])


def find_all():
    FIND_ALL_USEDTIRES_QUERY = """
        SELECT * FROM usedtires;
    """
    manager.cursor.execute(FIND_ALL_USEDTIRES_QUERY)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    used_tires = []
    for r in records:
        used_tires.append(UsedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"]))
    return used_tires


def update(id, oem, manufacturer, number, description, speed, rating, production_year, consumption_level):
    UPDATE_USEDTIRE_QUERY = """
        UPDATE usedtires
        SET oem = %s, manufacturer = %s, number = %s, description = %s, speed = %s, rating = %s, production_year = %s, consumption_level = %s
        WHERE id = %s;
    """
    manager.cursor.execute(UPDATE_USEDTIRE_QUERY, (oem, manufacturer, number, description, speed, rating, production_year, consumption_level, id))
    manager.conn.commit()


def delete(id):
    DELETE_USEDTIRE_QUERY = """
        DELETE FROM usedtires WHERE id = %s;
    """
    manager.cursor.execute(DELETE_USEDTIRE_QUERY, (id,))
    manager.conn.commit()


def find_filter(filter_query):
    FIND_FILTER_USEDTIRE_QUERY = """
        SELECT * FROM usedtires WHERE %s;
    """
    manager.cursor.execute(FIND_FILTER_USEDTIRE_QUERY % filter_query)
    records = manager.cursor.fetchall()
    used_tires = []
    for r in records:
        used_tires.append(UsedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"]))
    return used_tires


def find_all_sorted(column_name, order):
    FIND_ALL_SORTED_USEDTIRES_QUERY = """
        SELECT * FROM usedtires ORDER BY %s %s;
    """
    manager.cursor.execute(FIND_ALL_SORTED_USEDTIRES_QUERY % (column_name, order))
    records = manager.cursor.fetchall()
    manager.conn.commit()
    used_tires = []
    for r in records:
        used_tires.append(UsedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"]))
    return used_tires
