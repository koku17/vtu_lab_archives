use lab9

db.catalog.insertMany([{
	_id: 1,
	subject: 'mongoDB',
	author: 'xyz',
	views: 50
},{
	_id: 2,
	subject: 'mongoDB',
	author: 'efg',
	views: 5 
},{
	_id: 3,
	subject: 'dbms',
	author: 'abc',
	views: 90 
},{
	_id: 4,
	subject: 'dbms',
	author: 'xyz',
	views: 100 
},{
	_id: 5,
	subject: 'ai and dbms',
	author: 'abc',
	views: 200
},{
	_id: 6,
	subject: 'machine learning',
	author: 'jkl',
	views: 80
},{
	_id: 7,
	subject: 'machine learning',
	author: 'efg',
	views: 10 
},{
	_id: 8,
	subject: 'operating system',
	author: 'xyz',
	views: 10
}])

db.catalog.createIndex({
		subject: 'text'
})

db.catalog.find({
	$text:{ $search: ' dbms ' }
})

db.dropDatabase()
