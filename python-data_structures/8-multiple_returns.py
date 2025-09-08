#!/usr/bin/python3
def multiple_returns(sentence):
    l_sentence = len(sentence)
    if l_sentence == 0:
        return 0, None
    return l_sentence, sentence[0]
