# Given an input string of a certain length, design an algorithm that compresses the string

#  consecutive duplicates of characters are replaced with whe character and followed by the number of consecutive duplicates

"""
    INPUTS/OUTPUTS
        "wwwwaaadexxxxxx" => "w4d3dex6"

    NOTES
        - we have to somehow keep count of how many times a letter appears
        - we should only keep count while the consecutive letters match
        - we can use an index pointer to help us loop through the string
        - if the counter is just equal to 1, then we can just add the letter to our new result
        - else, we add the letter plus the string version of our counter
"""


def stringCompression(string):
    index = 0
    res = ''

    while index < len(string):
        appeareance_counter = 0
        string_length = len(string)

        while ((index < string_length - 1) and string[index] == string[index + 1]):
            appeareance_counter += 1
            index += 1

        if appeareance_counter == 1:
            res += string[index]
        else:
            res += string[index] + str(appeareance_counter)

        index += 1

    return res
