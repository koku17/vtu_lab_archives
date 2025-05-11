import nltk
from nltk.corpus import wordnet

nltk.download ('wordnet')
nltk.download ('omw-1.4')

def get_synonyms_antonyms (word):
	synonyms = set ()
	antonyms = set ()
	for syn in wordnet.synsets (word):
		for lemma in syn.lemmas ():
			synonyms.add (lemma.name ())
			if lemma.antonyms ():
				for ant in lemma.antonyms ():
					antonyms.add (ant.name ())
	return synonyms, antonyms

word = "active"
synonyms, antonyms = get_synonyms_antonyms (word)

print (
	f"Synonyms of '{word}':",
	", ".join (sorted (synonyms)),
	f"\nAntonyms of '{word}':",
	", ".join (sorted (antonyms)), sep = '\n'
)
