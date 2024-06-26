use lab1

// Insert document
db.lab1.insertMany([
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

// Find documents where age is greater than 25 and gender is "male"
db.lab1.find({
	$and: [
		{ age : { $gt: 25 }},
		{ gender : 'male' }
	]
})

// Find documents where age is greater than 30 or gender is "female"
db.lab1.find({
	$or: [
		{ age : { $gt: 30 }},
		{ gender : 'female' }
	]
})

// Insert document
db.lab1.insertOne({
	name : "John",
	age : 35,
	gender : "male"
})

// Query document
db.lab1.find({
	age : { $gt: 30 }
})

// Update document
db.lab1.updateOne({ name : "John" },{ $set: { age : 40 }})

// Delete document
db.lab1.deleteOne({ name : "John" })

// Projection
db.lab1.find({},{ name : 1, age : 1 })

// RIP DB
db.lab1.drop()
