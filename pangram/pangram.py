import string


def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)
    for letter in alphabet:
        if letter in list(sentence.lower()):
            continue
        else:
            return False
    return True