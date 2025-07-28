// PROGRAM 3
// a. Execute query selectors (comparison selectors,logical selectors ) and list out the results on any
//    collection

use companyDB

// Create the Employees Collection and Insert Documents
db.Employees.insertMany([
	{
		name : "Alice",
		age : 30,
		department : "HR",
		salary : 50000,
		joinDate : new Date("2015-01-15")
	},{
		name : "Bob",
		age : 24,
		department : "Engineering",
		salary : 70000,
		joinDate : new Date("2019-03-10")
	},{
		name : "Charlie",
		age : 29,
		department : "Engineering",
		salary : 75000,
		joinDate : new Date("2017-06-23")
	},{
		name : "David",
		age : 35,
		department : "Marketing",
		salary : 60000,
		joinDate : new Date("2014-11-01")
	},{
		name : "Eve",
		age : 28,
		department : "Finance",
		salary : 80000,
		joinDate : new Date("2018-08-19")
	}
])

// $eq
db.Employees.find({
	department : { $eq: "Engineering" }
}).pretty()

// $ne
db.Employees.find({
	department : { $ne: "HR" }
}).pretty()

// $gt
db.Employees.find({
	age : { $gt: 30 }
}).pretty()

// $lt
db.Employees.find({
	salary : { $lt: 70000 }
}).pretty()

// $gte
db.Employees.find({
	joinDate : { $gte: new Date("2018-01-01") }
}).pretty()

// $lte
db.Employees.find({
	age : { $lte: 28 }
}).pretty()

// $and
db.Employees.find({
	$and: [
		{
			department : "Engineering"
		},{
			salary : { $gt: 70000 }
		}
	]
}).pretty()

// $or
db.Employees.find({
	$or: [
		{
			department : "HR"
		},{
			salary : { $lt: 60000 }
		}
	]
}).pretty()

// $not
db.Employees.find({
	department : { $not: { $eq: "Engineering" } }
}).pretty()

// $nor
db.Employees.find({
	$nor : [
		{
			department : "HR"
		},{
			salary : { $gt: 75000 }
		}
	]
}).pretty()

db.dropDatabase()
