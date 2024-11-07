use MoviesDB
db.createCollection('Movies')

db.Movies.insertMany([{
	title: 'Inception',
	director: 'Christopher Nolan',
	genre: 'Science Fiction',
	year: 2010,
	ratings: {
		imdb: 8.8,
		rottenTomatoes: 87
	}
},{
	title: 'The Matrix',
	director: 'Wachowskis',
	genre: 'Science Fiction',
	year: 1999,
	ratings: {
		imdb: 8.7,
		rottenTomatoes: 87
	}
},{
	title: 'The Godfather',
	director: 'Francis Ford Coppola',
	genre: 'Crime',
	year: 1972,
	ratings: {
		imdb: 9.2,
		rottenTomatoes: 97
	}
}])

db.Movies.find({},{
	title: 1,
	director: 1,
	year: 1,
	_id: 0
}).limit(5)

db.dropDatabase()
