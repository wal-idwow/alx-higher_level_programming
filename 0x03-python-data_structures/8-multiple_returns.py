#!/usr/bin/python3
#function that returns a tuple with the length of a string and its first character
def multiple_returns(sentence):
    # Check if sentence is empty
    if not sentence:
        return (0, None)
    
    # Return a tuple with the string length and the first character
    return (len(sentence), sentence[0])
