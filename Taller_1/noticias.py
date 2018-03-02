from bs4 import BeautifulSoup
import glob
import os
import sys
import json
 
def replace(string):    
    string = string.replace("\n", " ")
    string = string.replace("\r", " ")
    string = string.replace("\t", " ")
    string = string.replace("\x03", " ")    
    string = string.replace("     ", " ")
    string = string.replace("    ", " ")
    string = string.replace("   ", " ")
    string = string.replace("  ", " ")    
    return  string
        
def main(args):
    paq_not = 'noticias/'
    noticias = []
    for filename in glob.glob(os.path.join(paq_not, '*.sgm')):
        file = open(filename, "r")        
        noticias.append(BeautifulSoup(file.read(), "html.parser"))             
    file = open("noticias.txt","w", encoding="utf8")     
    dit = {}    
    cont = 0
    for doc in noticias:     
        for reuters in doc.find_all('reuters'):       
            title = ""
            body = ""
            if reuters.title:                        
                title = reuters.title.get_text()
            if reuters.body:
                body = reuters.body.get_text()
            content = title + " " + body
            dit[cont] = replace(content).lower()
            cont = cont + 1       
    file.write(json.JSONEncoder().encode(dit))
    file.close()
    print(cont)
# main
if __name__ == '__main__':
    main(sys.argv)
