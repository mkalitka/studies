from ..connection import manager
from .part import Part

class Tire(Part):
    speed: int
    rating: str


    def __str__(self):
        return f"ID: {self.id}, OEM: {self.oem}, Manufacturer: {self.manufacturer}, Number: {self.number}, Description: {self.description}, Speed: {self.speed}, Rating: {self.rating}"


def insert(tire):
    INSERT_TIRE_QUERY = """
        INSERT INTO tires (id, oem, manufacturer, number, description, speed, rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    manager.cursor.execute(INSERT_TIRE_QUERY, (tire.id, tire.oem, tire.manufacturer, tire.number, tire.description, tire.speed, tire.rating))
    manager.conn.commit()


def find(id):
    FIND_TIRE_QUERY = """
        SELECT * FROM tires
        WHERE id = %s;
    """
    manager.cursor.execute(FIND_TIRE_QUERY, (id,))
    record = manager.cursor.fetchone()
    manager.conn.commit()
    return Tire(id=record["id"], oem=record["oem"], manufacturer=record["manufacturer"], number=record["number"], description=record["description"], speed=record["speed"], rating=record["rating"])


def find_all():
    FIND_ALL_TIRES_QUERY = """
        SELECT * FROM tires;
    """
    manager.cursor.execute(FIND_ALL_TIRES_QUERY)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    tires = []
    for r in records:
        tires.append(Tire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"]))
    return tires


def update(id, oem, manufacturer, number, description, speed, rating):
    UPDATE_TIRE_QUERY = """
        UPDATE tires
        SET oem = %s, manufacturer = %s, number = %s, description = %s, speed = %s, rating = %s
        WHERE id = %s;
    """
    manager.cursor.execute(UPDATE_TIRE_QUERY, (oem, manufacturer, number, description, speed, rating, id))
    manager.conn.commit()


def delete(id):
    DELETE_TIRE_QUERY = """
        DELETE FROM tires WHERE id = %s;
    """
    manager.cursor.execute(DELETE_TIRE_QUERY, (id,))
    manager.conn.commit()


def find_filter(filter_query):
    FIND_FILTER_TIRE_QUERY = """
        SELECT * FROM tires WHERE %s;
    """
    manager.cursor.execute(FIND_FILTER_TIRE_QUERY % filter_query)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    tires = []
    for r in records:
        tires.append(Tire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"]))
    return tires


def find_all_sorted(column_name, order):
    FIND_ALL_SORTED_TIRES_QUERY = """
        SELECT * FROM tires ORDER BY %s %s;
    """
    manager.cursor.execute(FIND_ALL_SORTED_TIRES_QUERY % (column_name, order))
    records = manager.cursor.fetchall()
    manager.conn.commit()
    tires = []
    for r in records:
        tires.append(Tire(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"], speed=r["speed"], rating=r["rating"]))
    return tires
