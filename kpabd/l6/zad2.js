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
]

copies = [
    {"_id": 101, "signature": "A001", "book_id": 1},
    {"_id": 102, "signature": "A002", "book_id": 1},
    {"_id": 103, "signature": "B001", "book_id": 2}
]

readers = [
    {
        "_id": 201,
        "pesel": "12345678901",
        "last_name": "Kowalski",
        "city": "Warsaw",
        "birth_date": "1985-06-15",
        "last_borrowing": "2024-12-01"
    },
    {
        "_id": 202,
        "pesel": "98765432109",
        "last_name": "Nowak",
        "city": "Krakow",
        "birth_date": "1990-08-20",
        "last_borrowing": "2024-11-20"
    }
]

borrowings = [
    {"_id": 301, "reader_id": 201, "copy_id": 101, "borrow_date": "2024-12-01", "days": 2},
    {"_id": 302, "reader_id": 202, "copy_id": 102, "borrow_date": "2024-11-25", "days": 4},
    {"_id": 303, "reader_id": 202, "copy_id": 103, "borrow_date": "2024-11-15", "days": 10},
    {"_id": 304, "reader_id": 201, "copy_id": 103, "borrow_date": "2024-12-02", "days": 7}
]

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

console.log(db.books.find().pretty())
console.log(db.copies.find().pretty())
console.log(db.readers.find().pretty())
console.log(db.borrowings.find().pretty())
