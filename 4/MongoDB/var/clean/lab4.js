use retailDB

db.Products.insertMany([
{
	name : "Laptop",
	brand : "BrandA",
	features : [{
		name : "Processor",
		value : "Intel i7"
	},{
		name : "RAM",
		value : "16GB"
	},{
		name : "Storage",
		value : "512GB SSD"
	}],
	reviews : [{
		user : "Alice",
		rating : 5,
		comment : "Excellent!"
	},{
		user : "Bob",
		rating : 4,
		comment : "Very good"
	},{
		user : "Charlie",
		rating : 3,
		comment : "Average"
	}]
},{
		name : "Smartphone",
		brand : "BrandB",
		features : [{
			name : "Processor",
			value : "Snapdragon 888"
		},{
			name : "RAM",
			value : "8GB"
		},{
			name : "Storage",
			value : "256GB"
		}],
		reviews : [{
			user : "Dave",
			rating : 4,
			comment : "Good phone"
		},{
			user : "Eve",
			rating : 2,
			comment : "Not satisfied"
		}]
	}
])



// The $ Projection Operator
db.Products.find({
	name : "Laptop",
	"reviews.user" : "Alice"
},{
	"reviews.$" : 1
}).pretty()

// The $elemMatch Projection Operator
db.Products.find({
	name : "Laptop"
},{
	reviews : {
		$elemMatch: {
			rating : { $gt: 4 }
		}
	}
}).pretty()

// The $slice Projection Operator
db.Products.find({
	name : "Smartphone"
},{
	reviews : { $slice: 1 }
}).pretty()

// Multiple Projection Operators
db.Products.find({
	name : "Laptop"
},{
	name : 1,
	features : { $slice: 2},
	reviews : {
		$elemMatch: { rating : 5 }
	}
}).pretty()

db.dropDatabase()
