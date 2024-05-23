console.log(
  db.borrowings.find().sort({ borrow_date: 1 }).limit(2)
)

console.log(
  db.borrowings.find({
    "days": { $lt: 9 }
  })
)
