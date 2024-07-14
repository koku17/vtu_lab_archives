// Unique index
db.collection.createIndex(
	{ username : 1 },
	{ unique : true }
)

// Sparse index
db.collection.createIndex(
	{ city : 1 },
	{ sparse : true }
)

// Compound index
db.collection.createIndex({
	age : 1,
	city : -1
})

// Multikey index
db.collection.createIndex({ tags : 1})

// Using index
db.collection.find({ username : "john" }).hint({ username : 1 })

// Explain query execution plan
db.collection.find({
	age : { $gt: 30 }
}).explain()
