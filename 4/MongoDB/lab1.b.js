use ProgBooksDB
db.createCollection('ProgrammingBooks')

db.ProgrammingBooks.insertOne({
	title: 'The Pragmatic Programmer: Your Journey to Mastery',
	author: 'David Thomas, Andrew Hunt',
	category: 'Software Development',
	year: 1999
})

db.ProgrammingBooks.insertMany({
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
})

db.ProgrammingBooks.find().pretty()
db.ProgrammingBooks.find({ year: { $gt: 2000 }}).pretty()

db.ProgrammingBooks.updateOne({
	title: 'Clean Code: A Handbook of Agile Software Craftsmanship'
},{
	$set: { author: 'Robert C. Martin (Uncle Bob)' }
})

db.ProgrammingBooks.find({ year: { $eq: 2008 }}).pretty()
db.ProgrammingBooks.find({ author: { $regex: 'Robert*' }}).pretty()

db.ProgrammingBooks.updateMany({
	year: { $lt: 2010 }
},{
	$set: { category: 'Classic Programming Books' }
})

db.ProgrammingBooks.find({ year: { $lt: 2010 }}).pretty()
db.ProgrammingBooks.deleteOne({ title: 'JavaScript: The Good Parts' })
db.ProgrammingBooks.find({ title: 'JavaScript: The Good Parts' }).pretty()
db.ProgrammingBooks.deleteMany({ year: { $lt: 1995 }})
db.ProgrammingBooks.deleteMany({})
db.ProgrammingBooks.find().pretty()

db.ProgrammingBooks.find({},{
	title: 1,
	author: 1
})

db.ProgrammingBooks.find({},{ year: 0 })
db.dropDatabase()
