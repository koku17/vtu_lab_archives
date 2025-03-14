use ProgBooksDB
db.createCollection('ProgrammingBooks')

db.ProgrammingBooks.insertOne({
	title: 'The Pragmatic Programmer: Your Journey to Mastery',
	author: 'David Thomas, Andrew Hunt',
	category: 'Software Development',
	year: 1999
})

db.ProgrammingBooks.insertMany([{
    title: 'Clean Code: A Handbook of Agile Software Craftsmanship',
    author: 'Robert C. Martin',
    category: 'Software Development',
    year: 2008
},{
    title: 'JavaScript: The Good Parts',
    author: 'Douglas Crockford',
    category: 'JavaScript',
    year: 2008
},{
    title: 'Design Patterns: Elements of Reusable Object-Oriented Software',
    author: 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides',
    category: 'Software Design',
    year: 1994
},{
    title: 'Introduction to Algorithms',
    author: 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein',
    category: 'Algorithms',
    year: 1990
},{
    title: 'Python Crash Course: A Hands-On, Project-Based Introduction to Programming',
    author: 'Eric Matthes',
    category: 'Python',
    year: 2015
}])

db.ProgrammingBooks.find({ year: 2008 }).pretty()

db.ProgrammingBooks.find({
	$and: [{
		category: 'Software Development'
	},{
		year: 2008
	}]
}).pretty()

db.ProgrammingBooks.find({
	$or: [{
		category: 'JavaScript'
	},{
		year: 2015
	}]
}).pretty()

db.ProgrammingBooks.find({
	$or: [{
		$and: [{
			category: 'Software Development'
		},{
			year: { $gt: 2007 }
		}]
	},{
		category: 'Python'
	}]
}).pretty()

db.dropDatabase()
