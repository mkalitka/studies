from ..connection import manager
from .tire import Tire

class NewTire(Tire):
    onstock: int


    def __str__(self):
        return f"ID: {self.id}, OEM: {self.oem}, Manufacturer: {self.manufacturer}, Number: {self.number}, Description: {self.description}, Speed: {self.speed}, Rating: {self.rating}, On Stock: {self.onstock}"


def insert(new_tire):
    INSERT_NEWTIRE_QUERY = """
        INSERT INTO newtires (id, oem, manufacturer, number, description, speed, rating, onstock)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    manager.cursor.execute(INSERT_NEWTIRE_QUERY, (new_tire.id, new_tire.oem, new_tire.manufacturer, new_tire.number, new_tire.description, new_tire.speed, new_tire.rating, new_tire.onstock))
    manager.conn.commit()


def find(id):
    FIND_NEWTIRE_QUERY = """
        SELECT * FROM newtires WHERE id = %s;
    """
    manager.cursor.execute(FIND_NEWTIRE_QUERY, (id,))
    record = manager.cursor.fetchone()
    manager.conn.commit()
    return NewTire(id=record["id"], oem=record["oem"], manufacturer=record["manufacturer"], number=record["number"], description=record["description"], speed=record["speed"], rating=record["rating"], onstock=record["onstock"])


def find_all():
    FIND_ALL_NEWTIRES_QUERY = """
        SELECT * FROM newtires;
    """
    manager.cursor.execute(FIND_ALL_NEWTIRES_QUERY)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    new_tires = []
    for r in records:
        new_tires.append(NewTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], onstock=r["onstock"]))
    return new_tires


def update(id, oem, manufacturer, number, description, speed, rating, onstock):
    UPDATE_NEWTIRE_QUERY = """
        UPDATE newtires
        SET oem = %s, manufacturer = %s, number = %s, description = %s, speed = %s, rating = %s, onstock = %s
        WHERE id = %s;
    """
    manager.cursor.execute(UPDATE_NEWTIRE_QUERY, (oem, manufacturer, number, description, speed, rating, onstock, id))
    manager.conn.commit()


def delete(id):
    DELETE_NEWTIRE_QUERY = """
        DELETE FROM newtires WHERE id = %s;
    """
    manager.cursor.execute(DELETE_NEWTIRE_QUERY, (id,))
    manager.conn.commit()


def find_filter(filter_query):
    FIND_FILTER_NEWTIRE_QUERY = """
        SELECT * FROM newtires WHERE %s;
    """
    manager.cursor.execute(FIND_FILTER_NEWTIRE_QUERY % filter_query)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    new_tires = []
    for r in records:
        new_tires.append(NewTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], onstock=r["onstock"]))
    return new_tires


def find_all_sorted(column_name, order):
    FIND_ALL_SORTED_NEWTIRES_QUERY = """
        SELECT * FROM newtires ORDER BY %s %s;
    """
    manager.cursor.execute(FIND_ALL_SORTED_NEWTIRES_QUERY % (column_name, order))
    records = manager.cursor.fetchall()
    manager.conn.commit()
    new_tires = []
    for r in records:
        new_tires.append(NewTire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"], onstock=r["onstock"]))
    return new_tires
