# Given an input string of a certain length, design an algorithm that compresses the string

#  consecutive duplicates of characters are replaced with whe character and followed by the number of consecutive duplicates

"""
    INPUTS/OUTPUTS
        "wwwwaaadexxxxxx" => "w4d3dex6"

    NOTES
        - we have to somehow keep count of how many times a letter appears
        - we should only keep count while the consecutive letters match
        - if the counter is just equal to 1, then we can just add the letter to our new result
        - else, we add the letter plus the string version of our counter
"""
