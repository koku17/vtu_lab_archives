// PROGRAM 3
// b. Execute query selectors (Geospatial selectors, Bitwise selectors ) and list out the results on any
//    collection

use geoDatabase

db.Places.insertMany([
	{
		name : "Central Park",
		location : {
			type : "Point",
			coordinates : [ -73.9654,40.7829 ]
		}
	},{
		name : "Times Square",
		location : {
			type : "Point",
			coordinates : [ -73.9851,40.7580 ]
		}
	},{
		name : "Brooklyn Bridge",
		location : {
			type : "Point",
			coordinates : [ -73.9969,40.7061 ]
		}
	},{
		name : "Empire State Building",
		location : {
			type : "Point",
			coordinates : [ -73.9857,40.7488 ]
		}
	},{
		name : "Statue of Liberty",
		location : {
			type : "Point",
			coordinates : [ -74.0445,40.6892 ]
		}
	}
])

// Create a geospatial index
db.Places.createIndex({
	location : "2dsphere"
})

// Find places near a specific coordinate, for example : near Times Square.
db.Places.find({
	location : {
		$near: {
			$geometry: {
				type : "Point",
				coordinates : [ -73.9851,40.7580 ]
			},
			$maxDistance: 5000 // distance in meters
		}
	}
}).pretty()

// $geoWithin
db.Places.find({
	location: {
		$geoWithin: {
			$geometry: {
				type: "Polygon",
				coordinates: [
					[
						[-70.016, 35.715],
						[-74.014, 40.717],
						[-73.990, 40.730],
						[-73.990, 40.715],
						[-70.016, 35.715]
					]
				]
			}
		}
	}
}).pretty()

db.dropDatabase()

// Bitwise Selectors
use techDB

db.Devices.insertMany([
	{
		name : "Device A",
		status : 5 // Binary : 0101
	},{
		name : "Device B",
		status : 3 // Binary : 0011
	},{
		name : "Device C",
		status : 12 // Binary : 1100
	},{
		name : "Device D",
		status : 10 // Binary : 1010
	},{
		name : "Device E",
		status : 7 // Binary : 0111
	}
])

// $bitsAllSet
// Find devices where the binary status has both the 1st and 3rd bits set
db.Devices.find({
	status : { $bitsAllSet: [ 0,2 ] }
}).pretty()

// $bitsAnySet
// Find devices where the binary status has at least the 2nd bit set
db.Devices.find({
	status : { $bitsAnySet: [ 1 ] }
}).pretty()

// $bitsAllClear
// Find devices where the binary status has both the 2nd and 4th bits clear
db.Devices.find({
	status : { $bitsAllClear: [ 1,3 ] }
}).pretty()

// $bitsAnyClear
// Find devices where the binary status has at least the 1st bit clear
db.Devices.find({
	status : { $bitsAnyClear: [ 0 ] }
}).pretty()

db.dropDatabase()
