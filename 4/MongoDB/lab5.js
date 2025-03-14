use salesDB

db.Sales.insertMany([{
	date: new Date('2024-01-01'),
	product: 'Laptop',
	price: 1200,
	quantity: 1,
	customer: 'Amar'
},{
	date: new Date('2024-01-02'),
	product: 'Laptop',
	price: 1200,
	quantity: 2,
	customer: 'Babu'
},{
	date: new Date('2024-01-03'),
	product: 'Mouse',
	price: 25,
	quantity: 5,
	customer: 'Chandra'
},{
	date: new Date('2024-01-04'),
	product: 'Keyboard',
	price: 45,
	quantity: 3,
	customer: 'Amar'
},{
	date: new Date('2024-01-05'),
	product: 'Monitor',
	price: 300,
	quantity: 1,
	customer: 'Babu'
},{
	date: new Date('2024-01-06'),
	product: 'Laptop',
	price: 1200,
	quantity: 1,
	customer: 'Deva'
}])

db.Sales.aggregate([{
	$group: {
		_id: '$product',
		averagePrice: { $avg: '$price' }
	}
}]).pretty()

db.Sales.aggregate([{
	$group: {
		_id: '$product',
		minPrice: { $min: '$price' }
    }
}]).pretty()


db.Sales.aggregate([{
	$group: {
		_id: '$product',
		maxPrice: { $max: '$price' }
    }
}]).pretty()

db.Sales.aggregate([{
	$group: {
		_id: '$customer',
		products: { $push: '$product' }
	}
}]).pretty()

db.Sales.aggregate([{
	$group: {
		_id: '$customer',
		uniqueProducts: { $addToSet: '$product' }
	}
}]).pretty()

db.Sales.aggregate([{
	$group: {
		_id: '$product',
		totalQuantity: { $sum: '$quantity' },
		totalSales: {
			$sum: {
				$multiply: ['$price','$quantity']
			}
		},
		customers: { $addToSet: '$customer' }
	}
}]).pretty()

db.dropDatabase()
