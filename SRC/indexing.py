# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:03:39 2019

@author: Souparna
"""

        
def create_inverted_index(doc_list, id_title, tf_idf = False):
    inverted_index = dict()
    for doc in doc_list:
#        text = doc.title
#        text.extend(doc.text)
#        text.extend(doc.comment)
#        for w in text:
#            if w in inverted_index:
#                if int(doc.id) in inverted_index[w]:
#                    inverted_index[w][int(doc.id)]+=1
#                else:
#                    inverted_index[w][int(doc.id)] = 1
#            else:
#                inverted_index[w]={int(doc.id):1}
          
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
        
        
    return {**inverted_index, **id_title}
        

        

