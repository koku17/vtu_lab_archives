// PROGRAM 1
// b. Execute the Commands of MongoDB and operations in MongoDB

use ProgBooksDB
db.createCollection("ProgrammingBooks")

// insert a new document into the ProgrammingBooks collection :
db.ProgrammingBooks.insertOne({
	title : "The Pragmatic Programmer : Your Journey to Mastery",
	author : "David Thomas,Andrew Hunt",
	category : "Software Development",
	year : 1999
})

db.ProgrammingBooks.insertMany([
	{
		title : "Clean Code : A Handbook of Agile Software Craftsmanship",
		author : "Robert C. Martin",
		category : "Software Development",
		year : 2008
	},{
		title : "JavaScript : The Good Parts",
		author : "Douglas Crockford",
		category : "JavaScript",
		year : 2008
	},{
		title : "Design Patterns : Elements of Reusable Object-Oriented Software",
		author : "Erich Gamma,Richard Helm,Ralph Johnson,John Vlissides",
		category : "Software Design",
		year : 1994
	},{
		title : "Introduction to Algorithms",
		author : "Thomas H. Cormen,Charles E. Leiserson,Ronald L. Rivest,Clifford Stein",
		category : "Algorithms",
		year : 1990

	},{
		title : "Python Crash Course : A Hands-On,Project-Based Introduction to Programming",
		author : "Eric Matthes",
		category : "Python",
		year : 2015

	}
])

// Find All Documents
db.ProgrammingBooks.find().pretty()

// Find Documents Matching a Condition
db.ProgrammingBooks.find({
	year : { $gt: 2000 }
}).pretty()


// Update a Single Document
db.ProgrammingBooks.updateOne(
	{
		title : "Clean Code : A Handbook of Agile Software Craftsmanship"
	},{
		$set: { author : "Robert C. Martin (Uncle Bob)" }
})

// Verify by displaying books published in year 2008
db.ProgrammingBooks.find({
	year : { $eq: 2008 }
}).pretty()

// Another way to verify
db.ProgrammingBooks.find({
	author : { $regex: "Robert*" }
}).pretty()

// Update Multiple Documents
db.ProgrammingBooks.updateMany({
	year : { $lt: 2010 }
},{
	$set: { category : "Classic Programming Books" }
})

// Delete a Single Document
db.ProgrammingBooks.deleteOne({
	title : "JavaScript : The Good Parts"
})

// Verify to see document is deleted
db.ProgrammingBooks.find({
	title : "JavaScript : The Good Parts"
}).pretty()

db.dropDatabase()
