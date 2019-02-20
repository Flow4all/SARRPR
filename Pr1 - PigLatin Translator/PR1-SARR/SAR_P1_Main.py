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
    else:  # Ignorar palabras con acentos añadido 20-2-2019
        for string in word:
            if string.lower() in 'áàéèíìóòúùäëïöü':
                return word
        if word[0].lower() in 'aeiou':
            if word.isupper():
                return word + "YAY"
            else:
                return word + "yay"
        else:
            aux = ""
            if word.isupper():
                mayus = 2
            elif word[0].isupper():
                mayus = 1
            else:
                mayus = 0
            for i in range(0, len(word)):
                if word[i] in 'aeiouAEIOU':
                    aux = word[i:] + aux          
                    break
                else:
                    aux += word[i]
                       
            if mayus == 2:
                word = aux + "AY"
            elif mayus == 1:
                word = aux.lower() + "ay"
                aux = word[0]
                aux = aux.upper()
                word = aux + word[1:]
            else:
                word = aux + "ay"
                      
            return word


def piglatin_sentence(sentence): #Añadido separador de palabras 20-2-2019
    rawList = sentence.split(" ")
    cleanList = []
    auxvar = ""
    for word in rawList:
        if "," in word or ";" in word or "." in word or "?" in word or "!" in word:
            for i in range(0, len(word)): #Palabra con caracter especial
                if word[i] in ",;.?!":
                    if auxvar.__eq__(""): #Caracter especial al principio
                        cleanList.append(word[0])
                        cleanList.append(word[1:])
                else:        
                    auxvar + word[i]
                
                if (i == len(word)):
                    auxvar = ""
        else: #Palabra sin caracter especial
            cleanList.append(word)    
    #sentence = piglatin_word(sentence)
    print(cleanList)
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
