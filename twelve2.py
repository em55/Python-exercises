"""This program sorts the given words in descending order of length"""
words = raw_input("Enter a list of words: ").split()

def sort(words):
    return sorted(zip([len(w) for w in words], words), reverse=True)

print sort(words)

