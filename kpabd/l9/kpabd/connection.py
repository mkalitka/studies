import pymssql

class Connection:
    def __init__(self):
        self.conn = pymssql.connect(
            server='localhost:1434',
            user='mikolaj.kalitka',
            password='Test1234',
            database='test',
            as_dict=True
        )
        self.cursor = self.conn.cursor()
        # self.cursor.execute("""
        #     CREATE TABLE parts (
        #         id INT PRIMARY KEY,
        #         oem VARCHAR(255),
        #         manufacturer VARCHAR(255),
        #         number INT,
        #         description VARCHAR(255)
        #     );
        #
        #     CREATE TABLE tires (
        #         id INT PRIMARY KEY,
        #         oem VARCHAR(255),
        #         manufacturer VARCHAR(255),
        #         number VARCHAR(255),
        #         description VARCHAR(255),
        #         speed INT,
        #         rating VARCHAR(255)
        #     );
        #
        #     CREATE TABLE newtires (
        #         id INT PRIMARY KEY,
        #         oem VARCHAR(255),
        #         manufacturer VARCHAR(255),
        #         number VARCHAR(255),
        #         description VARCHAR(255),
        #         speed INT,
        #         rating VARCHAR(255),
        #         onstock INT
        #     );
        #
        #     CREATE TABLE usedtires (
        #         id INT PRIMARY KEY,
        #         oem VARCHAR(255),
        #         manufacturer VARCHAR(255),
        #         number VARCHAR(255),
        #         description VARCHAR(255),
        #         speed INT,
        #         rating VARCHAR(255),
        #         production_year INT,
        #         consumption_level VARCHAR(255)
        #     );
        #
        #     CREATE TABLE refurbishedtires (
        #         id INT PRIMARY KEY,
        #         oem VARCHAR(255),
        #         manufacturer VARCHAR(255),
        #         number VARCHAR(255),
        #         description VARCHAR(255),
        #         speed INT,
        #         rating VARCHAR(255),
        #         production_year INT,
        #         consumption_level VARCHAR(255),
        #         consumption_level_after_fixing VARCHAR(255)
        #     );
        # """)
        # self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()


manager = Connection()
