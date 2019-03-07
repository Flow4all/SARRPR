#! -*- encoding: utf8 -*-

from operator import itemgetter
import re
import sys
import pickle
import random

#Hecho por José Cantó Moscardó y Javier López Sanz
#Ej ampliación realizado
    
def load_object(file_name):
    with open(file_name, 'rb') as fh:
        obj = pickle.load(fh)
    return obj

if __name__ == "__main__":
    for i in range(10):
        frase = ""
        d = load_object(sys.argv[1])
        for k in range(25):    #máximo 25 palabras por frase
        	   if k == 0:    #primera palabra se escogera partiendo de $ $
        	       anterior="$"
        	       posterior="$"
        	   start_list = d[anterior+" "+posterior][1]
        	   num = random.randint(1, d[anterior+" "+posterior][0])
        	   for j in start_list:    #seleccionamos siguiente palabra considerando la probabilidad de cada una
        	       valor = j[1]
        	       if num <= valor:
        	           anterior=posterior
        	           posterior = j[0]
        	           break
        	       else:
        	           num -= valor
        	   if posterior == "$":    #si palabra seleccionada=$ la frase termina
        	       break
        	   frase += posterior
        	   if k == 25:    #si ya hay 25 palabras la frase termina
        	       break
        	   frase += " "
        print(frase)