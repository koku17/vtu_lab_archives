import nltk
from nltk import CFG

grammar = CFG.fromstring ("""
	S -> NP VP
	NP -> Det N | Det Adj N | PN
	VP -> V NP | V
	Det -> 'the' | 'a'
	N -> 'cat' | 'dog' | 'man' | 'park'
	Adj -> 'big' | 'small'
	V -> 'chased' | 'saw' | 'ate'
	PN -> 'John' | 'Mary'
""")

test_sentences = [
	'the cat chased the dog',
	'John saw the dog',
	'Mary ate',
	'the big dog saw a cat'
]

for sent in test_sentences:
	sentence = sent.split ()
	print (f"\n=== Parsing : {' '.join (sentence)} ===")

	print ('\n** Top-Down Parsing (Recursive Descent) **')
	rd_parser = nltk.RecursiveDescentParser (grammar)
	found_parse = False
	for tree in rd_parser.parse (sentence):
		found_parse = True
		print (tree)
		
	tree.pretty_print ()
	if not found_parse:
		print ('No valid parse tree found using Top-Down Parsing')

	print ('\n** Bottom-Up Parsing (Chart Parser) **')
	chart_parser = nltk.ChartParser (grammar)
	found_parse = False
	for tree in chart_parser.parse (sentence):
		found_parse = True
		print (tree)

	tree.pretty_print ()
	if not found_parse:
		print ('No valid parse tree found using Bottom-Up Parsing')
