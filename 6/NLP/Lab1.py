import re, nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# NLTK data
nltk.download ('punkt_tab')
nltk.download ('stopwords')

def preprocess_text (text):
	# Original
	print ("Original :\n", text, sep = "")

	# Tokenization
	tokens = word_tokenize (text)
	print ("\nTokenization :\n", tokens, sep = "")
	
	# Filtration
	filtered_tokens = [word for word in tokens if word.isalpha ()]
	print ("\nFiltration :\n", filtered_tokens, sep = "")
	
	# Script Validation
	valid_tokens = [word for word in filtered_tokens if re.match (r'^[a-zA-Z]+$', word)]
	print ("\nScript Validation :\n", valid_tokens, sep = "")
	
	# Stop Word Removal
	stop_words = set (stopwords.words ('english'))
	meaningful_words = [word.lower () for word in valid_tokens if word.lower () not in stop_words]
	print ("\nStop Word Removal :\n", meaningful_words, sep = "")
	
	# Stemming
	stemmer = PorterStemmer ()
	stemmed_words = [stemmer.stem (word) for word in meaningful_words]
	print ("\nStemming :\n", meaningful_words, "\n", sep = "")

# Example usage
statements = [
	'Hello! This is an example sentence to demonstrate txt processing in NLP, :) 123',
	'Python is amazing! こんにちは (Hello in Japanese), नमस्ते (Hello in Hindi), Привет (Hello in Russian). NLP is fun! 123'

]

for text in statements:
	preprocess_text (text)
