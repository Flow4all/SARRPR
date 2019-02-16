#!/usr/bin/env python
"""#! -*- encoding: utf8 -*- PYTHON2"""
"""PYTHON3"""
# coding=utf-8
"""
1.- Pig Latin

Javier López Sanz:

José Cantó Moscardó:
"""

import sys



def piglatin_word(word):
    if not word[0].isalpha():
        return word
    elif word[0].lower() in 'aeiou':
        if word.isupper():
            return word+"YAY"
        else:
            return word+"yay"
    else:
        aux=""
        if word.isupper():
            mayus = 2
        elif word[0].isupper():
            mayus = 1
        else:
            mayus = 0
        for i in range(0, len(word)):
            if word[i] in 'aeiouAEIOU':
                aux = word[i:]+aux          
                break
            else:
                aux+=word[i]
                   
        if mayus == 2:
            word = aux+"AY"
        elif mayus == 1:
            word = aux.lower()+"ay"
            aux = word[0]
            aux = aux.upper()
            word = aux+word[1:]
        else:
            word = aux+"ay"
                  
        return word


def piglatin_sentence(sentence):
    sentence = piglatin_word(sentence)
    return  sentence


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(piglatin_sentence(sys.argv[1]))
    else:
        inp = "cualquiercosa"
        while inp:
            print("Introduce una frase:")
            inp = input()
            if len(inp) > 0:
                r = piglatin_sentence(inp)
                print(r)
