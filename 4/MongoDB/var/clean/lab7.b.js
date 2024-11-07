use lab7

db.Ecommerce.insertMany([{
	_id : 1,
	productname : 'mobile',
	productid : 's1pro',
	ratings : 5,
	reviews : 'good'
},{
	_id : 2,
	productname : 'mobile',
	productid : 's1pro',
	ratings : 4,
	reviews : 'better'
},{
	_id : 3,
	productname : 'laptop',
	productid : 'l1pro',
	ratings : 5,
	reviews : 'good'
},{
	_id : 4,
	productname : 'laptop',
	productid : 'l1pro',
	ratings : 4,
	reviews : 'better'
},{
	_id : 5,
	productname : 'laptop',
	productid : 'l2pro',
	ratings : 8,
	reviews : 'best'
}])

db.Ecommerce.aggregate({
	$group: {
		_id : '$productid',
		avgrating : { $avg: '$ratings' },
		reviews_list: { $push:'$reviews' }
	}
})

db.eCommerce.aggregate([{
	$group: {
		_id : '$productid',
		avgRating : { $avg: '$ratings' },
		totalReviews : { $sum: 1 }
	}
}])

db.dropDatabase()
