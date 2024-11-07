// PROGRAM 2
// a. Develop a MongoDB query to select certain fields and ignore some fields of the documents from any
//    collection

use MoviesDB
db.Movies.insertMany([
	{
		title : "Inception",
		director : "Christopher Nolan",
		genre : "Science Fiction",
		year : 2010,
		ratings : {
			imdb : 8.8,
			rottenTomatoes : 87
		}
	},{
		title : "The Matrix",
		director : "Wachowskis",
		genre : "Science Fiction",
		year : 1999,
		ratings : {
			imdb : 8.7,
			rottenTomatoes : 87
		}
	},{
		title : "The Godfather",
		director : "Francis Ford Coppola",
		genre : "Crime",
		year : 1972,
		ratings : {
			imdb : 9.2,
			rottenTomatoes : 97
		}
	}
]);

// To select only the title and director fields from the Movies collection
db.Movies.find({},{
	title : 1,
	director : 1,
	_id : 0
})

// To exclude the ratings field from the results :
db.Movies.find({},{
	ratings : 0
})

// Combining Filter and Projection
db.Movies.find({
	director : "Christopher Nolan"
},{
	title : 1,
	year : 1,
	_id : 0
})

db.dropDatabase()
