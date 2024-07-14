db.catalog.find({ $text: { $search: "keyword" }})

db.collection.find({ $text: { $search: "keyword -excludedWord" }})
