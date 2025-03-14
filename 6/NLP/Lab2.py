from collections import Counter
import pandas as pd

sentences = [
	"The quick brown fox jumps over the lazy dog",
	"A journey of a thousand miles begins with a single step",
	"To be or not to be that is the question",
	"All that glitters is not gold",
	"An apple a day keeps the doctor away"
]

def tokenize (sentence):
	return sentence.lower ().split ()

def generate_ngrams (tokens, n):
	return [tuple (tokens[i:i + n]) for i in range (len (tokens) - n + 1)]

unigrams = []
bigrams = []
trigrams = []

for sentence in sentences:
	tokens = tokenize (sentence)
	unigrams.extend (generate_ngrams (tokens, 1))
	bigrams.extend (generate_ngrams (tokens, 2))
	trigrams.extend (generate_ngrams (tokens, 3))

unigram_counts = Counter (unigrams)
bigram_counts = Counter (bigrams)
trigram_counts = Counter (trigrams)

def calculate_ngram_probabilities (ngram_counts, lower_order_counts = None):
	probabilities = {}
	for ngram, count in ngram_counts.items ():
		if lower_order_counts:
			prefix = ngram[:-1]
			prefix_count = lower_order_counts[prefix] if prefix in lower_order_counts else 1
			probabilities[ngram] = count / prefix_count
		else:
			probabilities[ngram] = count / sum (ngram_counts.values ())
	return probabilities

unigram_probs = calculate_ngram_probabilities (unigram_counts)
bigram_probs = calculate_ngram_probabilities (bigram_counts, unigram_counts)
trigram_probs = calculate_ngram_probabilities (trigram_counts, bigram_counts)

df_unigrams = pd.DataFrame (unigram_probs.items (), columns = ["Unigram", "Probability"])
df_bigrams = pd.DataFrame (bigram_probs.items (), columns = ["Bigram", "Probability"])
df_trigrams = pd.DataFrame (trigram_probs.items (), columns = ["Trigram", "Probability"])

print (
	"Unigram Probabilities :", df_unigrams.to_string (index = False),
	"\nBigram Probabilities :", df_bigrams.to_string (index = False),
	"\nTrigram Probabilities :", df_trigrams.to_string (index = False),
	sep = "\n"
)
