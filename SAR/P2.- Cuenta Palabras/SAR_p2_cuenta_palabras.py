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

def text_statistics(filename, to_lower, remove_stopwords, extra):
    fichero=open(filename)
    texto=fichero.read()
    if to_lower:
        texto = texto.lower()
    texto_limpio=clean_text(texto)
    palabras=texto_limpio.split(" ")
    lineas=texto.split("\n")
    
    if remove_stopwords:
        stopwords = (open("stopwords_en.txt")).read().split("\n")
        aux=[]
        for palabra in palabras:
            if not palabra in stopwords:
                aux.append(palabra)
    
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
    if extra:
        lineas=texto_limpio.split("\n")
        for i in range(len(lineas)): 
            if i!=len(lineas)-1:
                lineas[i]="$ "+lineas[i]+"$"
            else:
                lineas[i]="$ "+lineas[i]+" $"
            clean_list=lineas[i].split(" ") 
            if remove_stopwords:
                aux=[]
                for j in range(len(clean_list)):
                    if not clean_list[j] in stopwords:
                        aux.append(clean_list[j])
                lineas[i]=" ".join(aux)
        d2={}
        s2={}
        for i in lineas:
            palabras=i.split(" ")
            for j in range(len(palabras)-1):
                d2[palabras[j]+" "+palabras[j+1]]=d2.get(palabras[j]+" "+palabras[j+1],0) + 1
                for k in range(len(palabras[j])-1):
                    if j!=0:
                        s2[palabras[j][k]+palabras[j][k+1]]=s2.get(palabras[j][k]+palabras[j][k+1],0) + 1
                
        print("Word pairs (alphabetical order):")
        for i in sorted(d2.keys()):
            print("    ("+str(i)+","+str(d2[i])+")")
        print("Word pairs(frequency order):")
        freq = sort_dic(d2)
        for i in freq:
            print("    "+str(i))
        print("Symbol pair(alphabetical order):")
        for i in sorted(s2.keys()):
            print("    ("+str(i)+","+str(s2[i])+")")
        print("Symbol pairs(frequency order):")
        freq = sort_dic(s2)
        for i in freq:
            print("    "+str(i))

def syntax():
    print ("\n%s filename.txt [to_lower?[remove_stopwords?]\n" % sys.argv[0])
    sys.exit()    

if __name__ == "__main__":
    name = sys.argv[1]
    lower = False
    stop = False
    extra = False
    if len(sys.argv) > 2:
        lower = (sys.argv[2] in ('1', 'True', 'yes'))
        if len(sys.argv) > 3:
            stop = (sys.argv[3] in ('1', 'True', 'yes'))
            if len(sys.argv) > 4 and sys.argv[4]=='extra':
                extra=True
    text_statistics(name, lower, stop, extra)
