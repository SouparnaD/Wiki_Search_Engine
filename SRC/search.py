# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:13:05 2019

@author: Souparna
"""
from time import time
from utilities import get_saved_object
from text_processing import text_processing
from itertools import combinations
import re
#import sys
import os
from bisect import bisect_right
index_path = "G:/wikidata/index/secondary_index/"
doc_title_path = 'G:/wikidata/index/doc_title_map'

file_names = os.listdir(index_path)
file_names.sort()
doc_title_map = get_saved_object(doc_title_path)

def find_intersect(query, key):
    doc_id_list = []
    for word in query:
        inv_index_name = file_names[bisect_right(file_names, word)]
        
        with open(index_path+inv_index_name, "r", errors = 'replace') as f:
            while True:
                string = f.readline()
                if string == '':
                    break
                s = string
                w = s.split(":")[0][2:-1]

                if w == word:
                    inv_index = eval(string)
                    
                
                
                
    
 
                    doc_list = set()
                    if word in inv_index.keys():
                        if key == "all":
                            for k in inv_index[word].keys():
                                doc_list = doc_list | set(list(inv_index[word][k].keys())[0:50])
                            
                        else:
                            if key in inv_index[word].keys():
                                doc_list = doc_list | set(list(inv_index[word][key].keys())[0:50])
                        doc_id_list.append(doc_list)

    if (len(doc_id_list)) >=1:
        res = doc_id_list[0]
        for r in doc_id_list:
            res = res & r
        return res
    else:
        return set()


def query_processing(query):
    result = []
    result_field = set()
    for key in query.keys():
        if len(query[key]) > 0:
            result_field = find_intersect(query[key], key)
            n = len(query[key]) - 1
            while len(result_field) < 30:    
                if n > 0:
                    combs = combinations(query[key], n)
                    for comb in combs:
                        result_field = result_field | find_intersect(comb, key)
                        if len(result_field)>=30:
                            result.append(result_field)
                            break
                    n -= 1
                else:
                    break
            result.append(result_field)
    if len(result) >= 1:
        final_result = result[0]
    else:
        final_result = set()
    for sets in result:
        final_result = final_result & sets
    n = len(result) -1
    while(len(final_result) < 10):
        if n > 0:
            combs = combinations(result, n)
            for comb in combs:
                final_result = final_result | set.intersection(*comb)
                if len(final_result) >= 10:
                    return final_result
            n -= 1
        else:
            return final_result
    return final_result


def check_fields(query):
    d = dict()
    d["all"] = ""
    fields = ["title", "body", "infobox", "category", "ref","comment"]
    q = re.sub(':', ' ', query)
    q = q.split()
    for w in q:
        if w in fields:
            field = w
            d[field] = ""
        else:
            try:
                d[field] += w + ' '
            except:
                d["all"] += w + ' '
    return d
    




#queries = f.readlines()

while True:
    print("enter query")
    query = input()
    start_time = time()
    q = check_fields(query)
    for key in q.keys():
        q[key] = text_processing(q[key])
    doc_ids = list(query_processing(q))
    
    if (len(doc_ids)) == 0:

        print("No Results found")
    else:
        
        for i in doc_ids[0:10]:
            print(doc_title_map[i], end="\r")
        print()
    print("time taken: %.2f\n"%(time()-start_time))



    


        


                


