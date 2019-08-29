# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:03:39 2019

@author: Souparna
"""

        
def create_inverted_index(doc_list, id_title, tf_idf = False):
    inverted_index = dict()
    for doc in doc_list:
# =============================================================================
#         text = doc.title
#         for w in text:
#             if w in inverted_index:
#                 if "title" in inverted_index[w]:
#                     if int(doc.id) in inverted_index[w]["title"]:
#                         inverted_index[w]["title"][int(doc.id)]+=1
#                     else:
#                         inverted_index[w]["title"][int(doc.id)]=1
#                 else:
#                     inverted_index[w]["title"] = {int(doc.id):1}
#             else:
#                 inverted_index[w]={"title":{int(doc.id):1}}
#                 
#         text = doc.text
#         for w in text:
#             if w in inverted_index:
#                 if "text" in inverted_index[w]:
#                     if int(doc.id) in inverted_index[w]["text"]:
#                         inverted_index[w]["text"][int(doc.id)]+=1
#                     else:
#                         inverted_index[w]["text"][int(doc.id)]=1
#                 else:
#                     inverted_index[w]["text"] = {int(doc.id):1}
#             else:
#                 inverted_index[w]={"text":{int(doc.id):1}}
#         text = doc.comment
#         for w in text:
#             if w in inverted_index:
#                 if "comment" in inverted_index[w]:
#                     if int(doc.id) in inverted_index[w]["comment"]:
#                         inverted_index[w]["comment"][int(doc.id)]+=1
#                     else:
#                         inverted_index[w]["comment"][int(doc.id)]=1
#                 else:
#                     inverted_index[w]["comment"] = {int(doc.id):1}
#             else:
#                 inverted_index[w]={"comment":{int(doc.id):1}}
# =============================================================================
        
        
        
        
          
        title = doc.title
        for w in title:
            if "title" in inverted_index:
                if w in inverted_index["title"]:
                    if int(doc.id) in inverted_index["title"][w]:
                        inverted_index["title"][w][int(doc.id)]+=1
                    else:
                        inverted_index["title"][w][int(doc.id)] = 1
                else:
                    inverted_index["title"][w]={int(doc.id):1}
                    
            else:
                inverted_index["title"] = {w: {int(doc.id):1}}
        text = doc.text
        for w in text:
            if "text" in inverted_index:
                if w in inverted_index["text"]:
                    if int(doc.id) in inverted_index["text"][w]:
                        inverted_index["text"][w][int(doc.id)]+=1
                    else:
                        inverted_index["text"][w][int(doc.id)] = 1
                else:
                    inverted_index["text"][w]={int(doc.id):1}
                    
            else:
                inverted_index["text"] = {w: {int(doc.id):1}}
        comment = doc.comment
        for w in comment:
            if "comment" in inverted_index:
                if w in inverted_index["comment"]:
                    if int(doc.id) in inverted_index["comment"][w]:
                        inverted_index["comment"][w][int(doc.id)]+=1
                    else:
                        inverted_index["comment"][w][int(doc.id)] = 1
                else:
                    inverted_index["comment"][w]={int(doc.id):1}
                    
            else:
                inverted_index["comment"] = {w: {int(doc.id):1}}
        
        category = doc.category
        for w in category:
            if "category" in inverted_index:
                if w in inverted_index["category"]:
                    if int(doc.id) in inverted_index["category"][w]:
                        inverted_index["category"][w][int(doc.id)]+=1
                    else:
                        inverted_index["category"][w][int(doc.id)] = 1
                else:
                    inverted_index["category"][w]={int(doc.id):1}
                    
            else:
                inverted_index["category"] = {w: {int(doc.id):1}}
        ref = doc.ref
        for w in ref:
            if "ref" in inverted_index:
                if w in inverted_index["ref"]:
                    if int(doc.id) in inverted_index["ref"][w]:
                        inverted_index["ref"][w][int(doc.id)]+=1
                    else:
                        inverted_index["ref"][w][int(doc.id)] = 1
                else:
                    inverted_index["ref"][w]={int(doc.id):1}
                    
            else:
                inverted_index["ref"] = {w: {int(doc.id):1}}
        infobox = doc.infobox
        for w in infobox:
            if "infobox" in inverted_index:
                if w in inverted_index["infobox"]:
                    if int(doc.id) in inverted_index["infobox"][w]:
                        inverted_index["infobox"][w][int(doc.id)]+=1
                    else:
                        inverted_index["infobox"][w][int(doc.id)] = 1
                else:
                    inverted_index["infobox"][w]={int(doc.id):1}
                    
            else:
                inverted_index["infobox"] = {w: {int(doc.id):1}}
        
    return {**inverted_index, **id_title}
        

        

