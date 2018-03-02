import math
from collections import Counter
from time import time
from pymongo import MongoClient

def readDatabase(db):
    inverIndex = db.inverIndex
    stopwords = db.stopwords
    words = db.words
    Tfidf = db.Tfidf
    Not = db.Not
    vector = db.vector

    return inverIndex, stopwords, words, Tfidf, Not, vector


def findCoincidences(doc, find_term):
    coinc = 0
    for word in doc:
        if word == find_term:
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


def createHistogram(query):
    listQuery = []
    for word in query.lower().split():              
        if stopwords.find_one({'stopword':  word}) is None:                            
            listQuery.append(word)
    return Counter(listQuery)


def createVectorSpace(histogram):
    vectorSpace = []
    for word in words.find():        
        vectorSpace.append(findCoincidences(histogram, word.get('words')))
    return vectorSpace


def createTdiDf(vectorSpace):
    tfidf = []
    for id, ter_frec in enumerate(vectorSpace):
        eq = 0
        if ter_frec > 0:
            inv_frec = vector.find_one({'_id':  id})
            eq = ter_frec*inv_frec.get('value')
        tfidf.append(eq)
    return tfidf


def search(tfidf):
    cosSim = {}
    for palabra in histQuery:        
        inv_idx = inverIndex.find_one({'word':  palabra})
        if inv_idx != None:                
            for key in inv_idx.get('docs'):
                if key not in cosSim:
                    documents_tfidf = Tfidf.find_one({'doc': key})
                    calc = cosine_similarity(tfidf, documents_tfidf.get('words'))
                    cosSim[key] = calc
    return cosSim


client = MongoClient('localhost',27017)
db = client.text

inverIndex, stopwords, words, Tfidf, Not, vector = readDatabase(db)

query = input('Ingrese texto a buscar: ')

t0 = time()

histQuery = createHistogram(query)

vectorSpace = createVectorSpace(histQuery)

tfidf = createTdiDf(vectorSpace)

docs = search(tfidf)

totalTime = time()-t0

print("La consulta es: " + query)
print()
i = 0
for key in sorted(docs, key=docs.get, reverse=True):
    Notic = Not.find_one({'_id': key})    
    print("Noticia encontrada: #%s" % i)
    print('%s' % Notic.get('doc') + "...")
    print()
    i += 1

    if (i > 10):
        break