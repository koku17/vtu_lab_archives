db.listingsAndReviews.find({},{ listing_url : 1, name : 1, address : 1, host_picture_url : 1 })

db.eCommerce.aggregate(
	[{
		$group: {
			_id : "$product_id",
			avgRating : { $avg: "$rating" },
			totalReviews : { $sum: 1 }
		}
	}]
)
