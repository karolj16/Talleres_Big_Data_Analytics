import sys
import json
from nltk.tokenize import word_tokenize
      
def main(args):
    stopwords = []    
    file_stopwords = open("stopwords.txt", "r", errors="replace")        
    stopwords = file_stopwords.read().split() 
    documents = {}    
    file_documents = open("noticias.txt", "r")        
    documents = json.JSONDecoder().decode(file_documents.read())     
    newDoc = {}
    listword = []
    for key,doc in documents.items():
        doc_listwords = []
        for word in word_tokenize(doc):
           if word not in stopwords:              
              doc_listwords.append(word)
              if word not in listword:
                  listword.append(word)                
        newDoc[key] = doc_listwords   
    file = open("words.txt","w")        
    file.write(json.JSONEncoder().encode(newDoc))
    file.close()        
    file = open("terminos_unicos.txt","w")        
    file.write(json.JSONEncoder().encode(listword))
    file.close() 
        
# metodo main
if __name__ == '__main__':
    main(sys.argv)
    
