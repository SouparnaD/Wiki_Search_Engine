# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:03:39 2019

@author: Souparna
"""
from utilities import write_index_to_file
        
def create_inverted_index(doc_list,i_count,index_folder_path,  tf_idf = False):
    inverted_index = dict()
    for doc in doc_list:
        
        
        
        
          
        title = doc.title
        for w in title:
            if w in inverted_index:
                if "title" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["title"]:
                        inverted_index[w]["title"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["title"][int(doc.id)] = 1
                else:
                    inverted_index[w]["title"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"title" : {int(doc.id) : 1}}
        
        
        text = doc.text
        for w in text:
            if w in inverted_index:
                if "body" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["body"]:
                        inverted_index[w]["body"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["body"][int(doc.id)] = 1
                else:
                    inverted_index[w]["body"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"body" : {int(doc.id) : 1}}
        
        comment = doc.comment
        for w in comment:
            if w in inverted_index:
                if "comment" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["comment"]:
                        inverted_index[w]["comment"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["comment"][int(doc.id)] = 1
                else:
                    inverted_index[w]["comment"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"comment" : {int(doc.id) : 1}}
        
        category = doc.category

        for w in category:
            if w in inverted_index:
                if "category" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["category"]:
                        inverted_index[w]["category"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["category"][int(doc.id)] = 1
                else:
                    inverted_index[w]["category"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"category" : {int(doc.id) : 1}}
        
        ref = doc.ref

        for w in ref:
            if w in inverted_index:
                if "ref" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["ref"]:
                        inverted_index[w]["ref"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["ref"][int(doc.id)] = 1
                else:
                    inverted_index[w]["ref"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"ref" : {int(doc.id) : 1}}
                
                
        infobox = doc.infobox

        for w in infobox:
            if w in inverted_index:
                if "infobox" in inverted_index[w]:
                    if int(doc.id) in inverted_index[w]["infobox"]:
                        inverted_index[w]["infobox"][int(doc.id)] += 1
                    else:
                        inverted_index[w]["infobox"][int(doc.id)] = 1
                else:
                    inverted_index[w]["infobox"] = {int(doc.id) : 1}
            else:
                inverted_index[w] = {"infobox" : {int(doc.id) : 1}}
                
                
    
    for key in inverted_index.keys():
        for k in inverted_index[key].keys():
            inverted_index[key][k] = dict(sorted(inverted_index[key][k].items(), key=lambda kv: kv[1], reverse = True))
    inverted_index = dict(sorted(inverted_index.items(), key=lambda kv:kv[0]))

    path_to_save = index_folder_path + str(i_count)
    write_index_to_file(path_to_save, inverted_index)
    
    return path_to_save
        

        

