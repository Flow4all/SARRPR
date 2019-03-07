#! -*- encoding: utf8 -*-

from operator import itemgetter
import re
import sys

clean_re = re.compile('\W+')
def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        yield key, value

def text_statistics(filename, to_lower, remove_stopwords):
    fichero=open(filename)
    texto=fichero.read()
    if to_lower:
        texto = texto.lower()
    texto_limpio=clean_text(texto)
    palabras=texto_limpio.split(" ")
    if remove_stopwords:
        stopwords = (open("stopwords_en.txt")).read().split("\n")
        aux=[]
        for palabra in palabras:
            if not palabra in stopwords:
                aux.append(palabra)
    lineas=texto.split("\n")
    lines = len(lineas)
    words = len(palabras)
           
    d={}
    s={}
    symbols=0
    if remove_stopwords:
        vocabulario=aux
    else:
        vocabulario=palabras
    for palabra in vocabulario:
        for i in range(len(palabra)):
    	      letra = palabra[i]
    	      s[letra] = s.get(letra,0) + 1
        d[palabra] = d.get(palabra,0) + 1
        symbols+=len(palabra)
        
    #print ('COMPLETAR')
    print("Lines: "+str(lines))
    if remove_stopwords:
        print("Number words (without stopwords): "+str(len(aux)))
    print("Number words (with stopwords): "+str(words))
    print("Vocabulary size: "+str(len(d)))
    print("Number of symbols: "+str(symbols))
    print("Number of different symbols: "+str(len(s)))
    print("Words (alphabetical order):")
    for i in sorted(d.keys()):
        print("    ("+str(i)+","+str(d[i])+")")
    print("Words(frequency order):")
    freq = sort_dic(d)
    for i in freq:
        print("    "+str(i))
    print("Symbols (alphabetical order):")
    for i in sorted(s.keys()):
        print("    ("+str(i)+","+str(s[i])+")")
    print("Symbols(frequency order):")
    freq = sort_dic(s)
    for i in freq:
        print("    "+str(i))

def syntax():
    print ("\n%s filename.txt [to_lower?[remove_stopwords?]\n" % sys.argv[0])
    sys.exit()    

if __name__ == "__main__":
    name = sys.argv[1]
    lower = False
    stop = False
    if len(sys.argv) > 2:
        lower = (sys.argv[2] in ('1', 'True', 'yes'))
        if len(sys.argv) > 3:
            stop = (sys.argv[3] in ('1', 'True', 'yes'))
    text_statistics(name, lower, stop)
