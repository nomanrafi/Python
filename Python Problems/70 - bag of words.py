# Write a function that accepts a list of strings, performs Bag of Words, and converts it to numerical vectors.

# https://en.wikipedia.org/wiki/Bag-of-words_model

def bow(sentences):
    vocab = []
    for i in sentences:
        vocab.extend(i.split()) 
    vocab = list(set(vocab))
