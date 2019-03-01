#! -*- encoding: utf8 -*-

from operator import itemgetter
import re
import sys

#Hecho por José Cantó Moscardó y Javier López Sanz
#Ej ampliación realizado

clean_re = re.compile('\W+')
def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        yield key, value

def separar_frase(texto):
    texto_limpio=""
    frases=[]
    for i in range(len(texto)):
        if not ([texto[i]] in [",",";","!","?",".","\n"]):
            print( not(texto[i] in [",",";","!","?",".","\n"]))
            texto_limpio=texto_limpio+texto[i]
        elif not (texto[i]=="\n" and texto[i+1]=="\n"):      
            frases.append("$ "+texto_limpio+" $")
            texto_limpio=""
    return frases

if __name__ == "__main__":
    print(separar_frase(",hola yo soy alguien, no soy nadie\n\nY yo tambien"))