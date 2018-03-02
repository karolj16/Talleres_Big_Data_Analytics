import sys
import json

def find(doc, find_term):
    coinc = 0
    for term in doc:
        if term == find_term:
            coinc = coinc + 1
    return coinc

def main(args):
    terms = []
    fileWords = open("terminos_unicos.txt", "r")
    terms = json.JSONDecoder().decode(fileWords.read())
    documents = []
    file_documents = open("words.txt", "r")
    documents = json.JSONDecoder().decode(file_documents.read())
    listword = {}
    for key, doc in documents.items():
        hist = []
        for term in terms:
            hist.append(find(doc, term))
        listword[key] = hist
    file = open("vectorSpace.txt", "w")
    file.write(json.JSONEncoder().encode(listword))
    file.close()

# main
if __name__ == '__main__':
    main(sys.argv)