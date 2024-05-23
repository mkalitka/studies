from ..connection import manager
from pydantic import BaseModel

class Part(BaseModel):
    id: int
    oem: str
    manufacturer: str
    number: int
    description: str


    def __str__(self):
        return f"ID: {self.id}, OEM: {self.oem}, Manufacturer: {self.manufacturer}, Number: {self.number}, Description: {self.description}"


def insert(part):
    INSERT_PART_QUERY = """
        INSERT INTO parts (id, oem, manufacturer, number, description)
        VALUES (%s, %s, %s, %s, %s);
    """
    manager.cursor.execute(INSERT_PART_QUERY, (part.id, part.oem, part.manufacturer, part.number, part.description))
    manager.conn.commit()


def find(id):
    FIND_PART_QUERY = """
        SELECT * FROM parts WHERE id = %s;
    """
    manager.cursor.execute(FIND_PART_QUERY, (id,))
    record = manager.cursor.fetchone()
    manager.conn.commit()
    return Part(id=record["id"], oem=record["oem"], manufacturer=record["manufacturer"], number=record["number"], description=record["description"])


def find_all():
    FIND_ALL_PARTS_QUERY = """
        SELECT * FROM parts;
    """
    manager.cursor.execute(FIND_ALL_PARTS_QUERY)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    parts = []
    for r in records:
        parts.append(Part(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"]))
    return parts


def update(id, oem, manufacturer, number, description):
    UPDATE_PART_QUERY = """
        UPDATE parts
        SET oem = %s, manufacturer = %s, number = %s, description = %s
        WHERE id = %s;
    """
    manager.cursor.execute(UPDATE_PART_QUERY, (oem, manufacturer, number, description, id))
    manager.conn.commit()


def delete(id):
    DELETE_PART_QUERY = """
        DELETE FROM parts WHERE id = %s;
    """
    manager.cursor.execute(DELETE_PART_QUERY, (id,))
    manager.conn.commit()


def find_filter(filter_query):
    FIND_FIlTER_PART_QUERY = """
        SELECT * FROM parts WHERE %s;
    """
    manager.cursor.execute(FIND_FIlTER_PART_QUERY % filter_query)
    records = manager.cursor.fetchall()
    manager.conn.commit()
    parts = []
    for r in records:
        parts.append(Part(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"]))
    return parts


def find_all_sorted(column_name, order):
    FIND_ALL_SORTED_PARTS_QUERY = """
        SELECT * FROM parts ORDER BY %s %s;
    """
    print(FIND_ALL_SORTED_PARTS_QUERY % (column_name, order))
    manager.cursor.execute(FIND_ALL_SORTED_PARTS_QUERY % (column_name, order))
    records = manager.cursor.fetchall()
    manager.conn.commit()
    parts = []
    for r in records:
        parts.append(Part(id=r["id"], oem=r["oem"], manufacturer=r["manufacturer"], number=r["number"], description=r["description"]))
    return parts
