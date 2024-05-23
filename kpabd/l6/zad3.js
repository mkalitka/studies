db.books.drop();
db.copies.drop();
db.readers.drop();
db.borrowings.drop();

db.createCollection("books", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "isbn", "title", "author", "year_published", "price", "borrowed_last_month"],
            properties: {
                _id: {
                    bsonType: "int",
                },
                isbn: {
                    bsonType: "string",
                },
                title: {
                    bsonType: "string",
                },
                author: {
                    bsonType: "object",
                    required: ["first_name", "last_name"],
                    properties: {
                        first_name: {
                            bsonType: "string",
                        },
                        last_name: {
                            bsonType: "string",
                        }
                    }
                },
                year_published: {
                    bsonType: "int",
                },
                price: {
                    bsonType: "double",
                },
                borrowed_last_month: {
                    bsonType: "bool",
                }
            }
        }
    }
});

db.createCollection("copies", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "signature", "book_id"],
            properties: {
                _id: {
                    bsonType: "int",
                },
                signature: {
                    bsonType: "string",
                },
                book_id: {
                    bsonType: "int",
                }
            }
        }
    }
});

db.createCollection("readers", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "pesel", "last_name", "city", "birth_date", "last_borrowing"],
            properties: {
                _id: {
                    bsonType: "int",
                },
                pesel: {
                    bsonType: "string",
                },
                last_name: {
                    bsonType: "string",
                },
                city: {
                    bsonType: "string",
                },
                birth_date: {
                    bsonType: "date",
                },
                last_borrowing: {
                    bsonType: "date",
                }
            }
        }
    }
});

db.createCollection("borrowings", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "reader_id", "copy_id", "borrow_date", "days"],
            properties: {
                _id: {
                    bsonType: "int",
                },
                reader_id: {
                    bsonType: "int",
                },
                copy_id: {
                    bsonType: "int",
                },
                borrow_date: {
                    bsonType: "date",
                },
                days: {
                    bsonType: "int",
                }
            }
        }
    }
});

books = [
    {
        "_id": 1,
        "isbn": "978-3-16-148410-0",
        "title": "MongoDB Basics",
        "author": {"first_name": "John", "last_name": "Doe"},
        "year_published": 2020,
        "price": 29.99,
        "borrowed_last_month": false
    },
    {
        "_id": 2,
        "isbn": "978-1-4028-9462-6",
        "title": "Advanced NoSQL",
        "author": {"first_name": "Jane", "last_name": "Smith"},
        "year_published": 2019,
        "price": 39.99,
        "borrowed_last_month": true
    }
];

copies = [
    {"_id": 101, "signature": "A001", "book_id": 1},
    {"_id": 102, "signature": "A002", "book_id": 1},
    {"_id": 103, "signature": "B001", "book_id": 2}
];

readers = [
    {
        "_id": 201,
        "pesel": "12345678901",
        "last_name": "Kowalski",
        "city": "Warsaw",
        "birth_date": new Date("1985-06-15"),
        "last_borrowing": new Date("2024-12-01")
    },
    {
        "_id": 202,
        "pesel": "98765432109",
        "last_name": "Nowak",
        "city": "Krakow",
        "birth_date": new Date("1990-08-20"),
        "last_borrowing": new Date("2024-11-20")
    }
];

borrowings = [
    {"_id": 301, "reader_id": 201, "copy_id": 101, "borrow_date": new Date("2024-12-01"), "days": 2},
    {"_id": 302, "reader_id": 202, "copy_id": 102, "borrow_date": new Date("2024-11-25"), "days": 4},
    {"_id": 303, "reader_id": 202, "copy_id": 103, "borrow_date": new Date("2024-11-15"), "days": 10},
    {"_id": 304, "reader_id": 201, "copy_id": 103, "borrow_date": new Date("2024-12-02"), "days": 7}
];

if (db.books.countDocuments() === 0) {
    db.books.insertMany(books);
}

if (db.copies.countDocuments() === 0) {
    db.copies.insertMany(copies);
}

if (db.readers.countDocuments() === 0) {
    db.readers.insertMany(readers);
}

if (db.borrowings.countDocuments() === 0) {
    db.borrowings.insertMany(borrowings);
}
