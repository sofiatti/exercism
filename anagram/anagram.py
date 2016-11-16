from collections import Counter


def detect_anagrams(word, list):
    word = word.lower()
    list = [x for x in list if x.lower() != word]
    anagrams = [x for x in list if Counter(x.lower()) == Counter(word)]
    return anagrams