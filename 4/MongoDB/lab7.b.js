use ecommerce

db.products.insertMany([{
	product_id: 1,
	name: 'Laptop',
	category: 'Electronics',
	price: 1200,
	reviews: [{
		user: 'Alice',
		rating: 5,
		comment: 'Excellent!'
	},{
		user: 'Bob',
		rating: 4,
		comment: 'Very good'
	},{
		user: 'Charlie',
		rating: 3,
		comment: 'Average',
	}]
},{
	product_id: 2,
	name: 'Smartphone',
	category: 'Electronics',
	price: 800,
	reviews: [{
		user: 'Dave',
		rating: 4,
		comment: 'Good phone'
	},{
		user: 'Eve',
		rating: 2,
		comment: 'Not satisfied'
	},{
		user: 'Frank',
		rating: 5,
		comment: 'Amazing!',
	}]
},{
	product_id: 3,
	name: 'Headphones',
	category: 'Accessories',
	price: 150,
	reviews: [{
		user: 'Grace',
		rating: 5,
		comment: 'Great sound'
	},{
		user: 'Heidi',
		rating: 3,
		comment: 'Okay',
	}]
}])

db.products.aggregate([{
	$unwind: '$reviews'
},{
	$group: {
		_id: '$name',
		totalReviews: { $sum: 1 },
		averageRating: { $avg: '$reviews.rating' },
		comments: { $push: '$reviews.comment' }
	}
},{
	$project: {
		_id: 0,
		product: '$_id',
		totalReviews: 1,
		averageRating: 1,
		comments: 1
	}
}]).pretty()
