# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:46:27 2019

@author: Souparna
"""
from merger import merge_index_files
import os
from time import time

p_index_path = "G:/index/"
s_index_path = "G:/secondary_index/"

primary_indexes = os.listdir(p_index_path)
#print(len(primary_indexes))
sindex_file_size = 10*1024576           # secondary index file sizes 10MB
start_time = time()
#print(os.path.normpath(p_index_path))
merge_index_files(primary_indexes,p_index_path, s_index_path, sindex_file_size)
print("time_taken:%.2f"%(time()-start_time))