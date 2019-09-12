# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:35:08 2019

@author: Souparna
"""
import heapq
from contextlib import ExitStack
import sys
from utilities import write_index_to_file
#from utilities import save_object

heap_list = []

inv_index = {}

def merge(dict1, dict2):
    key_set = set()
    for key in dict1.keys():
        key_set.add(key)
    for key in dict2.keys():
        key_set.add(key)
    for key in key_set:
        if key in dict1 and key in dict2:
            dict1[key] = {**dict1[key], **dict2[key]}
        elif key in dict2:
            dict1[key] = dict2[key]
    for key in dict1:
        dict1[key] = dict(sorted(dict1[key].items(), key=lambda kv:kv[1], reverse = True))
    return dict1




def merge_index_files(filenames, secondary_index_folder_path, size):
    word_dict = [None]*len(filenames)
    with ExitStack() as stack:
        files = [stack.enter_context(open(i, "r", errors = 'replace')) for i in filenames]
        count = len(filenames)
        for i, file in enumerate(files):
            d = eval(file.readline())
            key = list(d.keys())[0]
            word_dict[i] = d[key]
            heap_list.append((key, i))
            
        heapq.heapify(heap_list)
        last_key = ""
        while True:
            temp = heapq.heappop(heap_list)
            if temp[0] != last_key and sys.getsizeof(inv_index) > size: #1MB
                pathname = secondary_index_folder_path+last_key
#                save_object(inv_index, pathname)
                write_index_to_file(pathname, inv_index)
                inv_index.clear()
            last_key = temp[0]
            
            if temp[0] in inv_index:
                inv_index[temp[0]] = merge(word_dict[temp[1]], inv_index[temp[0]])
            else:
                inv_index[temp[0]] = word_dict[temp[1]]
                
            d = files[temp[1]].readline()
            if d != '':
                d = eval(d)
                key = list(d.keys())[0]
                word_dict[temp[1]] = d[key]
                heapq.heappush(heap_list, (key, temp[1]))
            else:
                files[temp[1]].close()
                count-=1
                if count == 0:
                    break
                
                
        pathname = secondary_index_folder_path+last_key
        write_index_to_file(pathname, inv_index)
            
            
            
    