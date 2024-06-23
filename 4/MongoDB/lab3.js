use lab3
// Insert document
db.lab3.insertMany([
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
// Comparison selectors
db.lab3.find({ age : { $gt: 30 } })
// Logical selectors
db.lab3.find({$and: [{ age : { $gt: 25 } },{ gender : "male" }] })
// Geographical data
db.createCollection('places')
db.places.insertMany([
	{
		Name : "Central Park",
		Location : { type : "Point",coordinates : [ -73.97,40.77 ] },
		category : "Parks",
		flag : 6
	},{
		Name : "Sara D. Roosevelt Park",
		Location : { type : "Point",coordinates : [ -73.9928,40.193 ] },
		category : "Parks",
		flag : 7
	},{
		Name : "Polo Grounds",
		Location : { type : "Point",coordinates : [ -73.9928,40.7193 ] },
		category : "Stadiums",
		flag : 8
	}
])
db.places.createIndex({ Location : "2dsphere" })
// Geospatial selectors
db.places.find({
	Location : {
		$near: {
			$geometry: {
				type : "Point",
				coordinates : [-73.9667,40.78]
			}
		}
	}
})
// Bitwise selectors
db.places.find({ flag: { $bitsAllSet: 4 }})
// RIP DB
db.places.dropIndex({ Location : "2dsphere" })
db.dropDatabase()
