use ProgBooksDB

db.createCollection("ProgrammingBooks")

db.ProgrammingBooks.insertMany([
	{
		title : "Clean Code",
		author : "Robert C. Martin",
		category : "Software Development",
		year : 2008
	},{
		title : "JavaScript : The Good Parts",
		author : "Douglas Crockford",
		category : "JavaScript",
		year : 2008
	},{
		title : "Design Patterns",
		author : "Erich Gamma",
		category : "Software Design",
		year : 1994
	},{
		title : "Introduction to Algorithms",
		author : "Thomas H. Cormen",
		category : "Algorithms",
		year : 2009
	},{
		title : "Python Crash Course",
		author : "Eric Matthes",
		category : "Python",
		year : 2015
	}
]);

// WHERE clause equivalent
db.ProgrammingBooks.find({
	year : 2008
}).pretty()

// Using the $and Operator
db.ProgrammingBooks.find({
	$and: [
		{
			category : "Software Development"
		},{
			year : 2008
		}
	]
}).pretty()








// Using the $or Operator
db.ProgrammingBooks.find({
	$or: [
		{
			category : "JavaScript"
		},{
			year : 2015
		}
	]
}).pretty()

// Combining $and and $or Operators
db.ProgrammingBooks.find({
	$or: [
		{
			$and: [
				{
					category : "Software Development"
				},{
					year : { $gt: 2007 }
				}
			]
		},{
			category : "Python"
		}
	]
}).pretty()

db.dropDatabase()
