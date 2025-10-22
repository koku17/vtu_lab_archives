import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

nltk.download("punkt_tab", quiet=True)

corpus = [
    "deep learning is a subset of machine Learning.",
    "Word embeddings are a type of word representation.",
    "Neural networkd learn from data.",
]

tokenized_corpus = [
    [tok for tok in word_tokenize(sentence.lower()) if tok.isalpha()]
    for sentence in corpus
]

model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=50,
    window=5,
    min_count=1,
    workers=4,
    sg=1,
    epochs=100,
    seed=42,
)

print("Embedding for 'deep' :", model.wv.get_vector("deep"), sep="\n")
