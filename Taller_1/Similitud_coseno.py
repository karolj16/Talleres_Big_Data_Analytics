import math
import json
from time import time
from collections import Counter
from nltk.tokenize import word_tokenize

def find(doc, find_term):
    coinc = 0
    for term in doc:
        if term == find_term:
            coinc = coinc + 1
    return coinc


def cosine_similarity(vectorSpace1, vectorSpace2):
    numerator = 0 
    sumxx, sumyy = 0, 0
    for i in range(len(vectorSpace1)):
        x = vectorSpace1[i]
        y = vectorSpace2[i]
        sumxx += x*x
        sumyy += y*y
        numerator += x*y
    return numerator/math.sqrt(sumxx*sumyy)


indice_invertido = {}
file_indice_invertido = open("indice_invertido.txt", "r")
inverdIndex = json.JSONDecoder().decode(file_indice_invertido.read())
file_indice_invertido.close()

stopwords = []
file_stopwords = open("stopwords.txt", "r", errors="replace")
stopwords = file_stopwords.read().split()
file_stopwords.close()

terminos = []
file_terminos = open("terminos_unicos.txt", "r")
terminos = json.JSONDecoder().decode(file_terminos.read())
file_terminos.close()

Tfidf = {}
file_tfidf = open("tfidf.txt", "r")
Tfidf = json.JSONDecoder().decode(file_tfidf.read())
file_tfidf.close()

documents = {}
file_documents = open("noticias.txt", "r")
documents = json.JSONDecoder().decode(file_documents.read())
file_documents.close()

inv_frec_vector = []
file_inv_frec_vector = open("vector.txt", "r")
inv_frec_vector = json.JSONDecoder().decode(file_inv_frec_vector.read())
file_inv_frec_vector.close()

query = "company"
t0 = time()

listQuery = []
for word in word_tokenize(query.lower()):
    if word not in stopwords:
        listQuery.append(word)
histQuery = Counter(listQuery)

vectorSpace = []
for word in terminos:
    vectorSpace.append(find(histQuery, word))

tfidf = []
for id, ter_frec in enumerate(vectorSpace):
    eq = 0
    if ter_frec > 0:
        eq = ter_frec*inv_frec_vector[id]
    tfidf.append(eq)

Simcos = {}
for consulta in histQuery:
    if consulta in inverdIndex:
        for key in inverdIndex.get(consulta):
            if key not in Simcos:
                calcular = cosine_similarity(tfidf, Tfidf[key])
                Simcos[key] = calcular
print()
print("La frase o palabra consultada es: " + query)
print()

i = 0
for key in sorted(Simcos, key=Simcos.get, reverse=True):
    print("Noticia encontrada: #%s, SimCos: %f" % (i,Simcos[key]))
    print('La consultaa se encuentra en la noticia %s: %s' % (key, documents[key]) + "...")
    print()
    i += 1

    if i>10:
        break