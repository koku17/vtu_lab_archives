from collections import Counter
import numpy as np
def naive_bayes(docs, labels):
    vocab = set()
    word_counts = {'comedy': Counter(), 'action': Counter()}
    class_counts = {'comedy': 0, 'action': 0}
    for doc, label in zip(docs, labels):
        words = doc.split(',')
        vocab.update(words)
        word_counts[label].update(words)
        class_counts[label] += 1
    vocab_size = len(vocab)
    total_docs = sum(class_counts.values())
    class_probs = {cls: np.log(class_counts[cls] / total_docs) for cls in class_counts}
    return word_counts, class_probs, vocab, vocab_size, class_counts
def predict_naive_bayes(word_counts, class_probs, vocab, vocab_size, class_counts, doc, smoothing=1):
    scores = {}
    words = doc.split(',')
    for cls in class_probs:
        log_prob = class_probs[cls]
        total_words_in_class = sum(word_counts[cls].values())
        for word in words:
            word_freq = word_counts[cls][word]
            word_likelihood = np.log((word_freq + smoothing) / (total_words_in_class + smoothing * vocab_size))
            log_prob += word_likelihood
        scores[cls] = log_prob
    return max(scores, key=scores.get)
docs = [
    'fun, couple, love, love',
    'fast, furious, shoot',
    'couple, fly, fast, fun, fun',
    'fly, fast, shoot, love'
]
labels = ['comedy', 'action', 'comedy', 'action']
word_counts, class_probs, vocab, vocab_size, class_counts = naive_bayes(docs, labels)
doc_D = 'fast, couple, shoot, fly'
predicted_class = predict_naive_bayes(word_counts, class_probs, vocab, vocab_size, class_counts, doc_D)
print(f'The most likely class for document D is {predicted_class}')
