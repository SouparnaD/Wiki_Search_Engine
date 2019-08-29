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

def find_intersect(query, key):
    doc_id_list = []
    for word in query:
        doc_list = set()
        if key == "all":
            for k in ["title", "text", "comment", "infobox", "category", "ref"]:
                i_index = inv_index[k]
                if word in i_index:
                    doc_list = doc_list | set(i_index[word].keys())
            doc_id_list.append(doc_list)
        else:
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
    for key in query.keys():
        if len(query[key]) > 0:
            result = find_intersect(query[key], key)
            n = len(query[key]) - 1
            while len(result) < 10:    
                if n > 0:
                    combs = combinations(query[key], n)
                    for comb in combs:
                        result = result | find_intersect(comb, key)
                        if len(result)>=10:
                            return result
                n -= 1
    return result
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
    

inv_index = get_saved_object("../index/index.pickle")

f = open("../sampleQueriesAndResults/queryfile", "r")
queries = f.readlines()
for query in queries:
#    start_time = time()
    q = check_fields(query)
    for key in q.keys():
        q[key] = text_processing(q[key])
    doc_ids = list(query_processing(q))
    for i in doc_ids[0:10]:
        print(inv_index[i], end = "\r")
#    print()
#    print("time taken: %.2f\n"%(time()-start_time))



    


        


                


