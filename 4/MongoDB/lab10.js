db.Catalog.aggregate([
	{
		$search: {
			index : 'default', {
				query : 'your_search_query_here',
				description : 'your_description'
			}
		}
	},{
		$project: {
			_id : 0,
			productName : 1,
			description : 1,
			score : { $meta: 'searchScore' }
		}
	}
])
