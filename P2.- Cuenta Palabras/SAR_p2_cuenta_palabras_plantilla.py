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

def text_statistics(filename, to_lower=True, remove_stopwords=True):
    f2=open(name,r)
    if to_lower:
        f2.lowercase()
    l=f2.readlines()
    lines = len(l)
    f=clean_text(f2)
    f=f.split(" ")
    words = len(f)
    if remove_stopwords:
        stopwords = (clean_text(open("nombre del fichero",r))).split(" ")
        for w in f:
            if not word in stopwords:
                aux = aux.append()
        f = aux        
    d={}
    for w in f:
        d[w] = d.get(w,0) + 1
    print ('COMPLETAR')


def syntax():
    print ("\n%s filename.txt [to_lower?[remove_stopwords?]\n" % sys.argv[0])
    sys.exit()    

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        syntax()
    name = sys.argv[1]
    lower = False
    stop = False
    if len(sys.argv) > 2:
        lower = (sys.argv[2] in ('1', 'True', 'yes'))
        if len(sys.argv) > 3:
            stop = (sys.argv[3] in ('1', 'True', 'yes'))
    text_statistics(name, to_lower=lower, remove_stopwords=stop)
