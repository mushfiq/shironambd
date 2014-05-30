#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import nltk


def do_tokenize(content):
    return nltk.word_tokenize(content)
    
def remove_punctuation(content):
    TRANS_TABLE = string.maketrans('|', '|')
    # TRANS_TABLE = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~|'
    content_is_unicode = isinstance(content, unicode)
    if content_is_unicode:
        content = content.encode('utf-8')
    stripped_input = content.translate(TRANS_TABLE, string.punctuation)

    if content_is_unicode:
        return stripped_input.decode('utf-8')
    return stripped_input


def do_it(si):
        s = nltk.stem.isri.ISRIStemmer()
        words = []
        for word in nltk.tokenize.wordpunct_tokenize(si):
            words.append(s.stem(word))
        return words

if __name__=='__main__':
    s1 = 'We are in Dhaka now, tmrw will move to somewhere else'
    s2 = 'আমি বাংলার    গান গাই, আমি বরিশালের চাল খাই। তুমি কোথায় থাক?'
    print do_it(s2)
    # print remove_punctuation(s2)
