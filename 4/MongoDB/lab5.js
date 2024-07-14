use lab5

// Insert document
db.lab5.insertMany([
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

// Aggregation operation Average
db.lab5.aggregate([{
	$group: {
		_id : null,
		avgAge : { $avg: "$age" }
	}
}])

// Aggregation operation Minimum
db.lab5.aggregate([{
	$group: {
		_id : null,
		minAge : { $min: "$age" }
	}
}])

// Aggregation operation Maximum
db.lab5.aggregate([{
	$group: {
		_id : null,
		maxAge : { $max: "$age" }
	}
}])

// Aggregation operation Push
db.lab5.aggregate([{
	$group: {
		_id : null,
		allNames : { $push: "$name" }
	}
}])

// Aggregation operation addToSet
db.lab5.aggregate([{
	$group: {
		_id : null,
		uniqueNames : { $addToSet: "$name" }
	}
}])

// RIP DB
db.lab5.drop()
