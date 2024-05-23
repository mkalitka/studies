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
drop table if exists [Order];

create table [Order]
(
	[ID] int primary key identity,
	[Customer] varchar(100),
	[Address] varchar(150),
	[Status] varchar(100)
);
"""

cursor.execute(STARTING_SQL_QUERY)
conn.commit()

class Order(BaseModel):
    customer: str
    address: str
    status: str

    def __str__(self) -> str:
        return f"Order: {self.customer}, {self.address}, {self.status}"

o = Order(customer='IBM', address='USA', status='In Travel')

INSERT_ORDER_SQL_QUERY = """
    insert into [Order] ([Customer], [Address], [Status])
    values (%s, %s, %s)
"""

cursor.execute(INSERT_ORDER_SQL_QUERY, (o.customer, o.address, o.status))
conn.commit()

SELECT_ORDER_SQL_QUERY = """
    select * from [Order]
"""

cursor.execute(SELECT_ORDER_SQL_QUERY)
records = cursor.fetchall()
for r in records:
    o = Order(customer=r['Customer'], address=r['Address'], status=r['Status'])
    print(o)
