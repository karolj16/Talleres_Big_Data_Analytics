import sys
from json import JSONEncoder
from json import JSONDecoder
from math import log
from time import time
  
def main(args):
    vector_space = {}
    file_list_vs = open("vectorSpace.txt", "r")
    vector_space = JSONDecoder().decode(file_list_vs.read())
    file_list_vs.close()

    documents = {}
    file_list_documents = open("words.txt", "r")
    documents = JSONDecoder().decode(file_list_documents.read())
    file_list_documents.close()

    dic = []
    file_dic = open("terminos_unicos.txt", "r")
    dic = JSONDecoder().decode(file_dic.read())
    file_dic.close()

    tfidf = {}    
    inv_vector = []
    doc_lenght = len(vector_space)
    
    t0 = time()

    for word in dic:        
        count = 0
        for document in documents.values():
            if word in document:
                count +=1                
        inv_frec = log(doc_lenght/count)               
        inv_vector.append(inv_frec)    
    
    print("done in %0.3fs." % (time() - t0))

    t0 = time()

    for key, value in vector_space.items():
        newtable = []
        for id, ter_frec in enumerate(value):
            eq = 0
            if ter_frec > 0:
                eq = ter_frec*inv_vector[id]              
            newtable.append(eq)
        tfidf[key] = newtable        
    
    print("done in %0.3fs." % (time() - t0))

    file = open("tfidf.txt","w")
    file.write(JSONEncoder().encode(tfidf))
    file.close()

    file = open("vector.txt","w")
    file.write(JSONEncoder().encode(inv_vector))
    file.close()

# metodo main
if __name__ == '__main__':
    main(sys.argv)
