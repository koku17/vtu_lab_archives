import os
from collections import Counter
import nltk
from nltk.tag import DefaultTagger, UnigramTagger
from nltk import ConditionalFreqDist
from nltk.corpus import brown, inaugural, reuters, udhr, PlaintextCorpusReader, treebank, words

for i in [ \
    'brown', 'inaugural', 'reuters', 'udhr', 'punkt', 'averaged_perceptron_tagger', \
    'universal_tagset', 'tagsets', 'treebank', 'words' \
]:
    nltk.download(i)

print (
    '\n=== Brown Corpus ===',
    '\nCategories : ', brown.categories (),
    '\nWords : ', brown.words (categories = 'news')[:10],
    '\nSents : ', brown.sents (categories = 'news')[:2],

    '\n\n=== Inaugural Corpus ===',
    '\nFile IDs : ', inaugural.fileids ()[:5],
    '\nWords : ', inaugural.words ('2009-Obama.txt')[:10],

    '\n\n=== Reuters Corpus ===',
    '\nCategories : ', reuters.categories ()[:5],
    '\nWords : ', reuters.words (categories = 'crude')[:10],
    '\nSents : ', reuters.sents (categories = 'crude')[:2],

    '\n\n=== Udhr Corpus ===',
    '\nLanguages : ', udhr.fileids ()[:5],
    '\nWords : ', udhr.words ('English-Latin1')[:10],
    sep = '\n'
)

corpus_root = 'my_corpus'
os.makedirs (corpus_root, exist_ok = True)
with open (os.path.join (corpus_root, 'sample.txt'), 'w') as f:
    f.write ('This is the custom corpus file. It can be used for testing.')
custom_corpus = PlaintextCorpusReader (corpus_root, '.*\.txt')

print (
    '\n\n=== Custom Corpus Words ===',
    '\nCustom Corpus Words :', custom_corpus.words (),
    sep = '\n'
)

word_category_pairs = [
    (word.lower (), cat)
    for cat in brown.categories ()
    for word in brown.words (categories = cat)
]

cfd = ConditionalFreqDist (word_category_pairs)

print (
    '\n\n=== CFD ===',
    "\nCFD Example (words 'news') : ", cfd['news'].most_common (3),
    '\nTagged Sents : ', treebank.tagged_sents ()[:2],
    '\nTagged Words : ', treebank.tagged_words ()[:10],
    sep = '\n'
)

tags = [tag for (word, tag) in treebank.tagged_words ()]
tag_freq = Counter (tags)
noun_tags = [tag for tag in tags if tag.startswith ('NN')]
noun_freq = Counter (noun_tags)

print (
    '\nMost Frequent POS Tags : ', tag_freq.most_common(5),
    '\nMost Frequent NOUN Tags : ', noun_freq.most_common(5),
    sep = '\n'
)

word_properties = {
    'cat': {'type': 'animal', 'sound': 'meow'},
    'car': {'type': 'vehicle', 'fuel': 'petrol'},
    'apple': {'type': 'fruit', 'color': 'red'}
}

print ('\nWord Properties :\n')
for word, props in word_properties.items ():
    print (f'{word.title ()} -> {props}')

default_tagger = DefaultTagger('NN')
train_data = treebank.tagged_sents()[:3000]
test_data = treebank.tagged_sents()[3000:]
unigram_tagger = UnigramTagger (train_data, backoff = default_tagger)

print (
    '\nDefault Tagger test : ', default_tagger.tag (['Hello', 'World']),
    '\nUnigramTagger Accuracy : ', unigram_tagger.evaluate (test_data),
    sep = '\n'
)

wordlist = set (words.words ())

def score_by_fewest_words (segmented_list):
    return [(words, len (words)) for words in segmented_list]

def segment_filtered (text, min_len = 2):
    results = []

    def helper (text, sentence):
        if not text:
            results.append (sentence)
            return
        for i in range (1, len(text) + 1):
            word = text[:i]
            if len (word) >= min_len and word in wordlist:
                helper (text[i:], sentence + [word])
    helper (text, [])
    return results

results = segment_filtered ('themanrantosave', min_len = 2)
scored = score_by_fewest_words (results)
scored.sort (key = lambda x: x[1])

print ('\nFiltered & Scored Segmentations : ')
for words, score in scored:
    print ('->', ' '.join (words), '|Word Count : ', score)
