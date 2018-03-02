from pymongo import MongoClient
from json import JSONDecoder

def opendDocuments():    
    file_inverIndex = open("indice_invertido.txt", "r")
    inverIndex = JSONDecoder().decode(file_inverIndex.read())
    file_inverIndex.close()
    
    file_stopwords = open("stopwords.txt", "r", errors="replace")
    stopwords = file_stopwords.read().split()
    file_stopwords.close()
    
    file_words = open("terminos_unicos.txt", "r")
    words = JSONDecoder().decode(file_words.read())
    file_words.close()
    
    file_words = open("tfidf.txt", "r")
    Tfidf = JSONDecoder().decode(file_words.read())
    file_words.close()

    file_Not = open("noticias.txt", "r")
    Not = JSONDecoder().decode(file_Not.read())
    file_Not.close()

    file_vector = open("vector.txt", "r")
    vector = JSONDecoder().decode(file_vector.read())
    file_vector.close()
    
    return inverIndex, stopwords, words, Tfidf, Not, vector

client = MongoClient('localhost',27017)
db = client.text

inverIndex, stopwords, words, Tfidf ,Not, vector = opendDocuments()

dbinverIndex = db.inverIndex
dbinverIndex.delete_many({})
i = 0
for key,value in inverIndex.items():
    dic = {}
    dic ['_id'] = i
    dic ['word'] = key
    dic ['docs'] = value
    i+=1
    dbinverIndex.insert_one(dic)

dbStopwords = db.stopwords
dbStopwords.delete_many({})
for id, stopword in enumerate(stopwords):
    dic = {}
    dic ['_id'] = id
    dic ['stopword'] = stopword    
    i+=1
    dbStopwords.insert_one(dic)

dbWords = db.words
dbWords.delete_many({})
for id, word in enumerate(words):   
    dic = {}
    dic ['_id'] = id
    dic ['words'] = word        
    dbWords.insert_one(dic)

dbTfidf = db.Tfidf
dbTfidf.delete_many({})
i = 0
for key,value in Tfidf.items():
    dic = {}
    dic ['_id'] = i
    dic ['doc'] = key
    dic ['words'] = value
    i+=1
    dbTfidf.insert_one(dic)

dbNot = db.Not
dbNot.delete_many({})
i = 0
for key,value in Not.items():
    dic = {}
    dic ['_id'] = key
    dic ['doc'] = value    
    i+=1
    dbNot.insert_one(dic)

dbvector= db.inv_frec_vector
dbvector.delete_many({})
for id,value in enumerate(vector):
    dic = {}
    dic ['_id'] = id
    dic ['value'] = value        
    dbvector.insert_one(dic)

print("finish")