import nltk
from nltk.corpus import brown, inaugural, reuters, udhr, treebank, words
from nltk.corpus import PlaintextCorpusReader
from nltk import ConditionalFreqDist, UnigramTagger, DefaultTagger
from collections import Counter
import os

for i in [ \
	'brown', 'inaugural', 'reuters', 'udhr', 'punkt', 'averaged_perceptron_tagger', \
	'universal_tagset', 'tagsets', 'treebank', 'words' \
] :
	nltk.download (i)

os.makedirs ('tmp', exist_ok = True)
with open ('tmp/sample.txt', 'w') as f:
	f.write ('This is a custom corpus. Testing custom data.')
custom = PlaintextCorpusReader ('tmp', '.*\.txt')

tags = [tag for _, tag in treebank.tagged_words ()]
noun_tags = [tag for tag in tags if tag.startswith ('NN')]

props = {'cat': {'type': 'animal'}, 'apple': {'type': 'fruit'}}

default_tagger = DefaultTagger ('NN')
unigram_tagger = UnigramTagger (treebank.tagged_sents ()[:3000], backoff=default_tagger)
wordlist = set (words.words ())

def segment (text, min_len = 2):
	results = []
	def backtrack (t, path = []):
		if not t:
			results.append (path)
			return
		for i in range (min_len, len (t) + 1):
			w = t[:i]
			if w in wordlist:
				backtrack (t[i:], path + [w])
	backtrack (text)
	return sorted ([(seg, len (seg)) for seg in results], key = lambda x: x[1])

segments = segment('themanrantosave')

print (
	'BROWN : ', brown.categories ()[ : 5], brown.words (categories = 'news')[:10],
	'INAUGURAL : ', inaugural.fileids ()[ : 2], inaugural.words ('2009-Obama.txt')[:10],
	'REUTERS : ', reuters.categories ()[ : 3], reuters.words (categories = 'crude')[:10],
	'UDHR : ', udhr.fileids ()[ : 2], udhr.words ('English-Latin1')[:10],

	'Custom Corpus Words : ', custom.words (),
	'Tagged Sents : ', treebank.tagged_sents ()[:1],
	'Tagged Words : ', treebank.tagged_words ()[:5],
	'Top NOUN Tags : ', Counter (noun_tags).most_common (3), sep = '\n'
)

for w, p in props.items ():
	print (f'{w} → {p}')

print (
	'UnigramTagger Accuracy : ', unigram_tagger.evaluate (treebank.tagged_sents()[3000:]),
	'Segmented Words : ', sep = '\n'
)

for s, sc in segments:
	print ('->', ''.join (s), '| Count : ', sc)
