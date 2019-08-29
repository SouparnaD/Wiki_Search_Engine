# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:46:27 2019

@author: Souparna
"""
from time import time
from parse import XmlParser
import pickle
import sys
from text_processing import text_processing
from indexing import create_inverted_index
from utilities import get_saved_object, save_object
data_path = '../data/data_phase1.xml'

    
def main():
    start_time = time()
    
    doc_list = XmlParser(data_path)
    print("xml parsing time: %.2f"%(time()-start_time))
    save_object(doc_list, "../data/xml_parsed.pickle")
    
    '''
    doc_list = get_saved_object("../data/xml_parsed.pickle")
    '''
    print(len(doc_list))
    print("data size:", int(sys.getsizeof(pickle.dumps(doc_list)))/1024**2)
    
    c=0
    id_title = {}
    for doc in range(0,len(doc_list)):
        id_title[int(doc_list[doc].id)] = doc_list[doc].title
        text = text_processing(doc_list[doc].text)
        title = text_processing(doc_list[doc].title)
        comment = text_processing(doc_list[doc].comment)
        category = text_processing(doc_list[doc].category)
        infobox = text_processing(doc_list[doc].infobox)
        ref = text_processing(doc_list[doc].ref)
        doc_list[doc].category = category
        doc_list[doc].infobox = infobox
        doc_list[doc].ref = ref
        doc_list[doc].text = text
        doc_list[doc].title = title
        doc_list[doc].comment = comment
        c+=1
        if(c%10000 == 0):
            print("indexed_data:", c)
    
    i_index = create_inverted_index(doc_list, id_title)

    print("total time: %.2f"%(time()-start_time))
    
    save_object(i_index, "../index/index.pickle")
    print("i_index_size = ",int(sys.getsizeof(pickle.dumps(i_index)))/1024**2)
    
#    for i in range(0, 3):
#        print(doc_list[i].text,doc_list[i].title)
  
main()