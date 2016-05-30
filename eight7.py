"""This program counts the frequency of the specified letter with the count method"""

word = raw_input("Enter a word: ")
letter = raw_input("Enter a letter: ")
print word.count(letter, 0, len(word))