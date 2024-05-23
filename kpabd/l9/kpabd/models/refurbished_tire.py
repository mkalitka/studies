from ..connection import manager
from .used_tire import UsedTire
from pydantic import BaseModel

class RefurbishedTire(UsedTire):
    consumption_level_after_fixing: str


    def __str__(self):
        return f"ID: {self.id}, OEM: {self.oem}, Manufacturer: {self.manufacturer}, Number: {self.number}, Description: {self.description}, Speed: {self.speed}, Rating: {self.rating}, Production Year: {self.production_year}, Consumption Level: {self.consumption_level}, Consumption Level After Fixing: {self.consumption_level_after_fixing}"


def insert(refurbished_tire):
    INSERT_REFURBISHEDTIRE_QUERY = """
        INSERT INTO refurbishedtires (id, oem, manufacturer, number, description, speed, rating, production_year, consumption_level, consumption_level_after_fixing)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    manager.cursor.execute(INSERT_REFURBISHEDTIRE_QUERY, (refurbished_tire.id, refurbished_tire.oem, refurbished_tire.manufacturer, refurbished_tire.number, refurbished_tire.description, refurbished_tire.speed, refurbished_tire.rating, refurbished_tire.production_year, refurbished_tire.consumption_level, refurbished_tire.consumption_level_after_fixing))
    manager.conn.commit()


def find(id):
    FIND_REFURBISHEDTIRE_QUERY = """
        SELECT * FROM refurbishedtires WHERE id = %s;
    """
    manager.cursor.execute(FIND_REFURBISHEDTIRE_QUERY, (id,))
    record = manager.cursor.fetchone()
    manager.conn.commit()
    return RefurbishedTire(id=record["id"], oem=record["oem"], manufacturer=record["manufacturer"], number=record["number"], description=record["description"], speed=record["speed"], rating=record["rating"], production_year=record["production_year"], consumption_level=record["consumption_level"], consumption_level_after_fixing=record["consumption_level_after_fixing"])


def find_all():
    FIND_ALL_REFURBISHEDTIRES_QUERY = """
        SELECT * FROM refurbishedtires;
    """
    manager.cursor.execute(FIND_ALL_REFURBISHEDTIRES_QUERY)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    refurbished_tires = []
    for r in records:
        refurbished_tires.append(RefurbishedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"], consumption_level_after_fixing=r["consumption_level_after_fixing"]))
    return refurbished_tires


def update(id, oem, manufacturer, number, description, speed, rating, production_year, consumption_level, consumption_level_after_fixing):
    UPDATE_REFURBISHEDTIRE_QUERY = """
        UPDATE refurbishedtires
        SET oem = %s, manufacturer = %s, number = %s, description = %s, speed = %s, rating = %s, production_year = %s, consumption_level = %s, consumption_level_after_fixing = %s
        WHERE id = %s;
    """
    manager.cursor.execute(UPDATE_REFURBISHEDTIRE_QUERY, (oem, manufacturer, number, description, speed, rating, production_year, consumption_level, consumption_level_after_fixing, id))
    manager.conn.commit()


def delete(id):
    DELETE_REFURBISHEDTIRE_QUERY = """
        DELETE FROM refurbishedtires WHERE id = %s;
    """
    manager.cursor.execute(DELETE_REFURBISHEDTIRE_QUERY, (id,))
    manager.conn.commit()


def find_filter(filter_query):
    FIND_FILTER_REFURBISHEDTIRE_QUERY = """
        SELECT * FROM refurbishedtires WHERE %s;
    """
    manager.cursor.execute(FIND_FILTER_REFURBISHEDTIRE_QUERY % filter_query)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    refurbished_tires = []
    for r in records:
        refurbished_tires.append(RefurbishedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"], consumption_level_after_fixing=r["consumption_level_after_fixing"]))
    return refurbished_tires


def find_all_sorted(column_name, order):
    FIND_ALL_SORTED_REFURBISHEDTIRES_QUERY = """
        SELECT * FROM refurbishedtires ORDER BY %s %s;
    """
    manager.cursor.execute(FIND_ALL_SORTED_REFURBISHEDTIRES_QUERY % (column_name, order))
    records = manager.cursor.fetchall()
    manager.conn.commit()
    refurbished_tires = []
    for r in records:
        refurbished_tires.append(RefurbishedTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], production_year=r["production_year"], consumption_level=r["consumption_level"], consumption_level_after_fixing=r["consumption_level_after_fixing"]))
    return refurbished_tires
