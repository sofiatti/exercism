from collections import defaultdict


def word_count(sentence):
    word_counts = defaultdict(int)
    for word in sentence.split():
        word_counts[word] += 1
    return word_counts