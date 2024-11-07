use companyDB

db.Employees.insertMany([{
	name: 'Alice',
	age: 30,
	department: 'HR',
	salary: 50000,
	joinDate: new Date('2015-01-15')
},{
	name: 'Bob',
	age: 24,
	department: 'Engineering',
	salary: 70000,
	joinDate: new Date('2019-03-10')
},{
	name: 'Charlie',
	age: 29,
	department: 'Engineering',
	salary: 75000,
	joinDate: new Date('2017-06-23')
},{
	name: 'David',
	age: 35,
	department: 'Marketing',
	salary: 60000,
	joinDate: new Date('2014-11-01')
},{
	name: 'Eve',
	age: 28,
	department: 'Finance',
	salary: 80000,
	joinDate: new Date('2018-08-19')
}])

db.Employees.find({
	$and: [{
		department: 'Engineering'
	},{
		salary: { $gt: 70000 }
	}]
}).pretty()

db.Employees.find({
	$or: [{
		department: 'HR'
	},{
		salary: { $lt: 60000 }
	}]
}).pretty()

db.Employees.find({
	department: {
		$not: { $eq: 'Engineering' }
	}
}).pretty()

db.Employees.find({
	$nor: [{
		department: 'HR'
	},{
		salary: { $gt: 75000 }
	}]
}).pretty()

db.dropDatabase()
