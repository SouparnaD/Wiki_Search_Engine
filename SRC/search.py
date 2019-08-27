# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:13:05 2019

@author: Souparna
"""
from time import time
from utilities import get_saved_object
from text_processing import text_processing
from itertools import combinations


def find_intersect(query):
    doc_id_list = []
    for word in query:
#        print("fuckoff")
        doc_list = set()
        for key in ["title", "text", "comment"]:
            i_index = inv_index[key]
            if word in i_index:
                doc_list = doc_list | set(i_index[word].keys())
        doc_id_list.append(doc_list)
    res = doc_id_list[0]
    for r in doc_id_list:
        res = res & r
    return res


def query_processing(query):
    result = set()
    if len(query) == 0:
        print("no relevant results")
    else:
        result = find_intersect(query)
        n = len(query) - 1
        while len(result) < 10:    
            if n > 0:
                combs = combinations(query, n)
                for comb in combs:
                    result = result | find_intersect(comb)
                    if len(result)>=10:
                        return result
            n -= 1
    return result

inv_index = get_saved_object("../index/index.pickle")

f = open("../sampleQueriesAndResults/queryfile", "r")
queries = f.readlines()
for query in queries:
    start_time = time()
    q = text_processing(query)
    doc_ids = list(query_processing(q))
    for i in doc_ids[0:10]:
        print(inv_index[i], end = "\r")
    print()
    print("time taken: %.2f\n"%(time()-start_time))



    


        


                


