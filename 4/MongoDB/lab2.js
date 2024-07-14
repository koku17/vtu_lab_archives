use lab2

// Insert document
db.lab2.insertMany([
	{
		name : 'Ananth',
		age : 32,
		gender : 'male'
	},{
		name : 'Adithi',
		age : 35,
		gender : 'female'
	},{
		name : 'Ananya',
		age : 27,
		gender : 'female'
	},{
		name : 'Aditya',
		age : 30,
		gender : 'male'
	},{
		name : 'Bharat',
		age : 25,
		gender : 'male'
	},{
		name : 'Rahul',
		age : 28,
		gender : 'male'
	},{
		name : 'Revathi',
		age : 25,
		gender : 'female'
	}
])

// Select certain fields and ignore some fields
db.lab2.find({}, { name: 1, age: 1, _id: 0 })

// Display the first 5 documents
db.lab2.find().limit(5)

// RIP DB
db.lab2.drop()
