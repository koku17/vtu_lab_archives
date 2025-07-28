// PROGRAM 6
// Execute Aggregation Pipeline and its operations (pipeline must contain $match, $group, $sort, $project,
// $skip etc. students encourage to execute several queries to demonstrate various aggregation operators)

use restaurantDB

// Insert sample documents into the restaurants collection
db.restaurants.insertMany([
	{
		name : "Biryani House",
		cuisine : "Indian",
		location : "Jayanagar",
		reviews : [{
			user : "Aarav",
			rating : 5,
			comment : "Amazing biryani!"
		},{
			user : "Bhavana",
			rating : 4,
			comment : "Great place!"
		}]
	},{
		name : "Burger Joint",
		cuisine : "American",
		location : "Koramangala",
		reviews : [{
			user : "Chirag",
			rating : 3,
			comment : "Average burger"
		},{
			user : "Devika",
			rating : 4,
			comment : "Good value"
		}]
	},{
		name : "Pasta House",
		cuisine : "Italian",
		location : "Rajajinagar",
		reviews : [{
			user : "Esha",
			rating : 5,
			comment : "Delicious pasta!"
		},{
			user : "Farhan",
			rating : 4,
			comment : "Nice ambiance"
		}]
	},{
		name : "Curry Palace",
		cuisine : "Indian",
		location : "Jayanagar",
		reviews : [
		{
			user : "Gaurav",
			rating : 4,
			comment : "Spicy and tasty!"
		},{
			user : "Harini",
			rating : 5,
			comment : "Best curry in town!"
		}]
	},{
		name : "Taco Stand",
		cuisine : "Mexican",
		location : "Jayanagar",
		reviews : [
		{
			user : "Ishaan",
			rating : 5,
			comment : "Fantastic tacos!"
		},{
			user : "Jaya",
			rating : 4,
			comment : "Very authentic"
		}]

	}
])

// Run the aggregation pipeline query to display reviews summary
db.restaurants.aggregate([
	{
		$match: { location : "Jayanagar" }
	},{
		$unwind: "$reviews"
	},{
		$group: {
			_id : "$name",
			averageRating : { $avg: "$reviews.rating" },
			totalReviews : { $sum: 1 }
		}
	},{
		$sort: { averageRating : -1 }
	},{
		$project: {
			_id : 0,
			restaurant : "$_id",
			averageRating : 1,
			totalReviews : 1
		}
	},{
		$skip: 1
	}
]).pretty()

db.dropDatabase()
