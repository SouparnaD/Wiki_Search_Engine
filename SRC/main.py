# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 23:46:27 2019

@author: Souparna
"""
from time import time
from parse import XmlParser
#import pickle
#import sys
from merger import merge_index_files
#from text_processing import text_processing
#from indexing import create_inverted_index
#from utilities import get_saved_object, save_object
data_path = 'G:/wikidata/wiki_dump_50.xml'
index_path = 'G:/wikidata/index/'
secondary_index_folder_path = 'G:/wikidata/index/secondary_index/'
index_file_size = 1024576*4       # secondary index file sizes 3MB
    
def main():
    start_time = time()
    

    filenames = XmlParser(data_path, index_path)
    print("first level index time: %.2f"%(time()-start_time))
    
    merge_index_files(filenames, secondary_index_folder_path, index_file_size)

    print("total time: %.2f"%(time()-start_time))

  
main()