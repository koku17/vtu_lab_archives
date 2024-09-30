use lab8

db.student.insertMany([{
	_id : 1,
	name : 'xyz',
	branch : 'AIML',
	usn : 37,
	age : 19
},{
	_id : 2,
	name : 'sam',
	branch : 'CSE',
	usn : 49,
	age : 20
},{
	_id : 3,
	name : 'jack',
	branch : 'MECH',
	usn : 48,
	age : 21
},{
	_id : 4,
	name : 'viola',
	branch : 'AIML',
	usn : 60,
	age : 22
},{
	_id : 5,
	name : 'pqr',
	branch : 'AIML',
	usn : 50,
	age : 25,
	grades : [24,34,45,67]
},{
	_id : 6,
	name : 'uv',
	course : 'cs',
	age : 50
}])

db.student.createIndex({
	name : 1
})

db.student.createIndex({
	branch : 1
},{
	age : -1
})

db.student.createIndex({
	usn : 1
},{
	unique : true
})

db.student.createIndex({
	course : 1
},{
	sparse : true
})

db.dropDatabase()
