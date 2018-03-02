import sys
import json
from time import time

def td(docs):
    indiceInvertido = {}
    for key, text in docs.items():
        for word in text:            
            if indiceInvertido.get(word, False):
                if key not in indiceInvertido[word]:
                    indiceInvertido[word].append(key)
            else:
                indiceInvertido[word] = [key]
    return indiceInvertido


def main(args):

    vectorSpace = {}
    file_terminos = open("words.txt", "r")
    vectorSpace = json.JSONDecoder().decode(file_terminos.read())

    t0 = time()

    indiceInv = td(vectorSpace)

    print("done in %0.3fs." % (time() - t0))

    file = open("indice_invertido.txt", "w")
    file.write(json.JSONEncoder().encode(indiceInv))
    file.close()

# main
if __name__ == '__main__':
    main(sys.argv)
