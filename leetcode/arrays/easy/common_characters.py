# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

"""
    INPUT/OUTPUT
        words = ["bella","label","roller"] => ["e", "l", "l"]

    NOTES
        brute force solution is to loop through the array, then loop through the word
        use a dictionary to keep track of the appearance for each
        then loop through dictionary and append to a new array the key which should be the letter
"""


def commonChars(words):
    char_freq = {}

    for word in words:
        for char in word:
            if char_freq[word] == 0:
                pass

    pass


commonChars(["bella", "label", "roller"])
