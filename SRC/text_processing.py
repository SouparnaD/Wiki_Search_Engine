# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 02:08:07 2019

@author: Souparna
"""
#import spacy
import string
#from nltk.stem.porter import PorterStemmer
#from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
#from multiprocessing import Pool

from stemming.porter import stem

#nlp = spacy.load('en', disable=["tagger", "ner", "parsing"])
new_stop_words = ['n', 'r']
stop_words = stopwords.words("english")
stop_words.extend(new_stop_words)




#import Stemmer
#stemmer = Stemmer.Stemmer('english')
    
#stemmer = PorterStemmer()
#wnl = WordNetLemmatizer()



translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
'''
def myfunc(w):
    print("addfsfsd")
    return stem(w)

def lemm(text, cores = 4):
    with Pool(processes = cores) as pool:
        result = pool.map(myfunc, text)
        return result
'''
def text_processing(texts):
    if isinstance(texts, list):
        clean = []
        for st in texts:
            clean.extend([stem(w) for w in st.casefold().translate(translator).split() if w not in stop_words])
        return clean
            
    clean = [stem(w) for w in texts.casefold().translate(translator).split() if w not in stop_words]

        
    return clean
