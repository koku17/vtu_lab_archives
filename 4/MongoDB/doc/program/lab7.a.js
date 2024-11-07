use vacationRentals

db.listingsAndReviews.insertMany([{
	listing_url: 'http://www.example.com/listing/123456',
	name: 'Beautiful Apartment',
	address: {
		street: '123 Main Street',
		suburb: 'Central',
		city: 'Metropolis',
		country: 'Wonderland'
	},
	host: {
		name: 'Alice',
		picture_url: 'http://www.example.com/images/host/host123.jpg'
	}
},{
	listing_url: 'http://www.example.com/listing/654321',
	name: 'Cozy Cottage',
	address: {
		street: '456 Another St',
		suburb: 'North',
		city: 'Smallville',
		country: 'Wonderland'
	},
	host: {
		name: 'Bob',
		picture_url: ''
	}
},{
	listing_url: 'http://www.example.com/listing/789012',
	name: 'Modern Condo',
	address: {
		street: '789 Side Road',
		suburb: 'East',
		city: 'Gotham',
		country: 'Wonderland'
	},
	host: {
		name: 'Charlie',
		picture_url: 'http://www.example.com/images/host/host789.jpg'
	}
}])

db.listingsAndReviews.find({
	'host.picture_url': {
		$exists: true,
		$ne: ''
	}
},{
	listing_url: 1,
	name: 1,
	address: 1,
	'host.picture_url': 1
}).pretty()

db.dropDatabase()
