#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

stence = "At school, I learnt C!"
length, first = multiple_returns(stence)
print("Length: {:d} - First character: {}".format(length, first))