use geoDatabase

db.Places.insertMany([{
	name: 'Central Park',
	location: {
		type: 'Point',
	coordinates: [-73.9654,40.7829]
	}
},{
	name: 'Times Square',
	location: {
		type: 'Point',
		coordinates: [-73.9851,40.7580]
	}
},{
	name: 'Brooklyn Bridge',
	location: {
		type: 'Point',
		coordinates: [-73.9969,40.7061]
	}
},{
	name: 'Empire State Building',
	location: {
		type: 'Point',
		coordinates: [-73.9857,40.7488]
	}
},{
	name: 'Statue of Liberty',
	location: {
		type: 'Point',
		coordinates: [-74.0445,40.6892]
	}
}])

db.Places.createIndex({ location: '2dsphere' })

db.Places.find({
	location: {
		$near: {
			$geometry: {
				type: 'Point',
				coordinates: [-73.9851, 40.7580]
			},
			$maxDistance: 5000
		}
	}
}).pretty()

db.Places.find({
	location: {
		$geoWithin: {
			$geometry: {
				type: 'Polygon',
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

use techDB

db.Devices.insertMany([{
	name: 'Device A',
	status: 5
},{
	name: 'Device B',
	status: 3
},{
	name: 'Device C',
	status: 12
},{
	name: 'Device D',
	status: 10
},{
	name: 'Device E',
	status: 7
}])

db.Devices.find({
	status: { $bitsAllSet: [1] }
}).pretty()

db.Devices.find({
	status: { $bitsAnySet: [1] }
}).pretty()

db.Devices.find({
	status: { $bitsAllClear: [1,3] }
}).pretty()

db.Devices.find({
	status: { $bitsAnyClear: [0] }
}).pretty()

db.dropDatabase()
