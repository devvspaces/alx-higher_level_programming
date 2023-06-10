#!/usr/bin/python3

def multiple_returns(sentence):
    length = 0
    first = None
    if sentence:
        length = len(sentence)
        first = sentence[0]
    return (length, first)
