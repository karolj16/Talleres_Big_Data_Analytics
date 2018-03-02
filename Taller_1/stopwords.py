import glob
import os
import sys
 
def main(args):
    list_stopwords = 'list_stopwords/'
    stop_words = []
    for filename in glob.glob(os.path.join(list_stopwords, '*.txt')):
        file = open(filename)        
        stop_words = stop_words + (file.read().split())        

    file = open("stopwords.txt","w")    
    dit = {}
    for sw in stop_words:
        lCase = sw.lower()
        if lCase is not dit.keys():
            dit[lCase] = sw

    for out in dit:
        file.write(out + '\n')
    
    file.close() 

# main
if __name__ == '__main__':
    main(sys.argv)
