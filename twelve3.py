"""This program sorts the letters in the given string in descending order of frequency"""
from collections import Counter
s = raw_input("Enter a list of words: ")

def getKey(item):
    return item[1]

def sort(s):
    return sorted(Counter(s).items(), key = getKey, reverse=True)

print sort(s)
