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
data_path = '../data/data_phase1.xml'
def save_object(doc_list, file_name):
    file = open(file_name, "wb")
    pickle.dump(doc_list, file)
    file.close()
def get_saved_object(file_name):
    pickle_in = open(file_name, "rb")
    return pickle.load(pickle_in)
    
def main():
    start_time = time()
    '''
    doc_list = XmlParser(data_path)
    print(len(doc_list))
    print("xml parsing time: %.2f"%(time()-start_time))
    save_object(doc_list, "../data/xml_parsed.pickle")
    '''
    
    doc_list = get_saved_object("../data/xml_parsed.pickle")
    print(len(doc_list))
    print("data size:", int(sys.getsizeof(pickle.dumps(doc_list)))/1024**2)
    
    c=0
    for doc in range(0,len(doc_list)):
        text = text_processing(doc_list[doc].text)
        title = text_processing(doc_list[doc].title)
        comment = text_processing(doc_list[doc].comment)
        doc_list[doc].text = text
        doc_list[doc].title = title
        doc_list[doc].comment = comment
        c+=1
        if(c%5000 == 0):
            print(c)
    
    i_index = create_inverted_index(doc_list)
#    for key in i_index.keys():
#        print(key, ":",i_index[key])
    print("total time: %.2f"%(time()-start_time))
    
    save_object(i_index, "../index/index.pickle")
    print("i_index_size = ",int(sys.getsizeof(pickle.dumps(i_index)))/1024**2)
    
#    for i in range(0, 3):
#        print(doc_list[i].text,doc_list[i].title)
  
main()