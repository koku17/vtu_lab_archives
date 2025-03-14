use lab7
db.listing_url.insertMany([{
	_id : 1,
	name : 'prestige',
	listing_url : 'http\\apartment\\details',
	address : 'bangalore',
	host_picture_url : 'http\\apartment\\images'
},{
	_id : 2,
	name : 'prestige',
	listing_url : 'http\\apartment\\details',
	address : 'mysore',
	host_picture_url : 'http\\apartment\\images'
},{
	_id : 3,
	name : 'resort',
	listing_url : 'http\\resorts\\details',
	address : 'mysore',
	host_picture_url : 'http\\resort\\images'
},{
	_id : 4,
	name : 'resort',
	listing_url : 'http\\resort\\details',
	address : 'bangalore',
	host_picture_url : 'http\\resort\\images'
}])

db.listing_url.find({},{
	name : 1,
	listing_url : 1,
	address : 1,
	host_picture_url : 1,
	_id : 0
})

db.listingsAndReviews.find({},{
	listing_url : 1,
	name : 1,
	address : 1,
	host_picture_url : 1
})

db.dropDatabase()
