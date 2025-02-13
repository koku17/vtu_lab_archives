import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# NLTK data
nltk.download ('punkt_tab')
nltk.download ('stopwords')

def preprocess_text (text):
	# Tokenization
	tokens = word_tokenize (text)
	
	# Filtration
	filtered_tokens = [re.sub (r'[^a-zA-Z]', '', token) for token in tokens]
	filtered_tokens = [token for token in filtered_tokens if token]
	
	# Script Validation
	validated_tokens = [token for token in filtered_tokens if re.match (r'^[a-zA-Z]+$', token)]
	
	# Stop Word Removal
	stop_words = set (stopwords.words ('english'))
	filtered_tokens = [token.lower () for token in validated_tokens if token.lower () not in stop_words]
	
	# Stemming
	stemmer = PorterStemmer ()
	stemmed_tokens = [stemmer.stem (token) for token in filtered_tokens]
	
	return stemmed_tokens

# Example usage
text = 'Hello ! This is an example sentence to demonstrate txt processing in NLP, \U0001f642 123'
print ('Processed text : ', preprocess_text (text))
