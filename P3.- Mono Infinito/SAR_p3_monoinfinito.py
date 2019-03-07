#! -*- encoding: utf8 -*-

from operator import itemgetter
import re
import sys
import pickle

#Hecho por José Cantó Moscardó y Javier López Sanz
#Ej ampliación realizado

clean_re = re.compile('\W+')
def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        yield key, value

def separar_frase(texto):
    clean_texto = re.split('\?|\.|\!|\/|\;|\:|\n\n', texto)
    frases = filter(str.strip, clean_texto)
    frases = list(frases)
    return frases
    
def save_object(object, file_name):
    with open(file_name, 'wb') as fh:
        pickle.dump(object, fh)

if __name__ == "__main__":
    w=0
    d = {}
    f = {}
    input = open(sys.argv[1]).read()
    input = input.lower()
    frases = separar_frase(input)
    for i in range(len(frases)):    #recorremos las frases
        frases[i] = clean_text(frases[i])
        frases[i] = frases[i].strip()
        if not frases[i]=="":
            frases[i] = "$ "+frases[i]+" $"
            palabras = frases[i].split(" ")
            for j in range(len(palabras)-1):    #recorremos las palabras de la frase i
                palabra = palabras[j]
                palabra_sucesora = palabras[j+1]
                valor = d.get(palabra,[0,{}])
                dic_sucesor = valor[1]
                valor_sucesor = dic_sucesor.get(palabra+" "+palabra_sucesora,0)
                dic_sucesor[palabra+" "+palabra_sucesora] = valor_sucesor+1    #insertar apariciones j y j+1 en diccionario auxiliar 
                d[palabra] = [valor[0]+1,dic_sucesor]    #insertamos el valor de la palabra j (nºapariciones,diccionario auxiliar)
    for i in sorted(d.keys()):    #recorremos el diccionario d para insertarlo ordenado en el diccionario f
        dic_sucesor = d[i][1]
        freq = sort_dic(dic_sucesor)
        lista_sucesor = []
        for j in freq:    #cada par clave/valor ordenados por valor lo insertamos en la posting list de la clave i
            palabra_sucesora = (str(j[0]).split(" "))[1]
            lista_sucesor.append((palabra_sucesora, j[1]))
        f[i] = (d[i][0],lista_sucesor)    #el diccionario f contiene como valor de la clave i (nº de apariciones,posting list)
    save_object(f,sys.argv[2])