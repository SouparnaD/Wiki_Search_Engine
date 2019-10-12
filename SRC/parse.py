# -*- coding: utf-8 -*-
" created by @Souparna on 20-08-2019"

import re
import xml.sax
from text_processing import text_processing
from indexing import create_inverted_index
from utilities import write_index_to_file, save_object

doc_list = []
docid_title_map = {}
i_count = 0
doc_chunk_size = 50000
filenames = []
index_folder_path = ''

# Regular Expression for Categories
catRegExp = r'\[\[Category:(.*?)\]\]'
# Regular Expression for Infobox
infoRegExp = r'{{Infobox(.*?)}}'
# Regular Expression for References
refRegExp = r'== ?References ?==(.*?)=='
# Regular Expression to remove Infobox from text
regExp1 = re.compile(infoRegExp,re.DOTALL)
# Regular Expression to remove references
regExp2 = re.compile(refRegExp,re.DOTALL)

# Regular Expression to remove CSS
regExp3 = re.compile(r'{\|(.*?)\|}',re.DOTALL)
# Regular Expression to remove {{cite **}} or {{vcite **}}
regExp4 = re.compile(r'{{v?cite(.*?)}}',re.DOTALL)



def remove_extra(text):
    text = regExp1.sub('',text)
    text = regExp2.sub('',text)
    text = regExp3.sub('',text)
    text = regExp4.sub('',text)
    return text
class document():
   def __init__(self):
      self.title = ""
#      self.ns = ""
      self.id = ""
#      self.redirect = ""
#      self.r_id = ""
#      self.timestamp = ""
#      self.con_user = ""
#      self.con_id = ""
      self.comment  = ""
#      self.model = ""
#      self.format = ""
      self.text = ""
      self.infobox = ""
      self.category = ""
      self.ref = ""
      

class WikiContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.doc_running =  False
        self.Current_tag = ""
        self.revision  = False
        self.contributor = False
        self.doc =  ""
        
    def startElement(self, tag, attributes):

      self.Current_tag = tag

      if tag == "page":
         self.doc_running = True
         self.revision = False
         self.contributor  = False
         self.doc = document()

      elif self.doc_running == False :
         return
      
      elif  tag == "revision" :
         self.revision =  True 

      elif tag == "contributor":
         self.contributor = True


    def endElement(self, tag):
      # print(tag  + " ==== ends ")
      global i_count
      if self.doc_running == False :
         return

      if tag == "revision" : 
         self.revision = False

      elif tag == "contributor":
         self.contributor = False

      elif tag == "page" :
         self.doc_running  = False
         self.doc.category = ' '.join(re.findall(catRegExp,self.doc.text,flags=re.MULTILINE))
         self.doc.infobox = ' '.join(re.findall(infoRegExp,self.doc.text,re.DOTALL))
         self.doc.ref = ' '.join(re.findall(refRegExp,self.doc.text,flags=re.DOTALL))
         self.doc.text = remove_extra(self.doc.text)
         
         docid_title_map[int(self.doc.id)] = self.doc.title
         
         self.doc.text = text_processing(self.doc.text)
         self.doc.title = text_processing(self.doc.title)
         self.doc.comment = text_processing(self.doc.comment)
         self.doc.category = text_processing(self.doc.category)
         self.doc.infobox = text_processing(self.doc.infobox)
         self.doc.ref = text_processing(self.doc.ref)
         
         
         

# =============================================================================
#          try :
#             if self.doc.id : 
#                self.doc.id = int(self.doc.id)
#             if self.doc.r_id :
#                self.doc.r_id = int(self.doc.r_id)
#             if self.doc.con_id :
#                self.doc.con_id = int(self.doc.con_id)
#          except : 
#             print(self.doc.id)
#             print(self.doc.r_id)
#             print(self.doc.con_id)
# =============================================================================

         doc_list.append(self.doc)
         if len(doc_list) == doc_chunk_size:
             i_count += 1
             fname = create_inverted_index(doc_list, i_count, index_folder_path)
             filenames.append(fname)
#             i_count += 1
#             path_to_save = "../index/i_index" + str(i_count) + ".txt"
#             write_index_to_file(path_to_save, i_index)
             doc_list.clear()
             
             
             
         self.doc = ""
         
    def characters(self, content):
        
        if self.doc_running == False :
            return 
        
        if self.Current_tag == "title":
            self.doc.title += content
        
        elif self.Current_tag == "id" :
            if self.revision == False :
                self.doc.id += content
                
            #-----------contributor details--------------
#            elif self.contributor == True :
#                self.doc.con_id += content
#            else :
#                self.doc.r_id += content
                
        elif self.Current_tag == "text":
             self.doc.text += content
             
#             if self.doc.infobox != "":
#                 print(self.doc.infobox)
            
                 
            
                
                 
                
                        
                 
        elif self.Current_tag == "comment" : 
             self.doc.comment += content
# 
#         elif self.Current_tag == "ns":
#             self.doc.ns += content
# 
#         elif self.Current_tag == "redirect" : 
#             self.doc.redirect +=  content
# 
#         
# 
#         elif self.Current_tag == "model" :
#             self.doc.model += content
# 
#         elif self.Current_tag == "timestamp" :
#             self.doc.timestamp += content
# 
#         elif self.Current_tag == "username":
#             self.doc.con_user += content
# 
#         elif self.Current_tag == "format" :
#             self.doc.format += content
# =============================================================================

        

def XmlParser(path, index_path):
    global index_folder_path
    index_folder_path = index_path
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    Handler = WikiContentHandler()
    parser.setContentHandler(Handler)
    
    parser.parse(path)
    global i_count
#    return doc_list, docid_title_map
    if len(doc_list) >= 1:
        i_count += 1
#        path_to_save = "../index/i_index" + str(i_count) + ".txt"
        fname = create_inverted_index(doc_list, i_count, index_folder_path)
        filenames.append(fname)
#        write_index_to_file(path_to_save, i_index)
    
    save_object(docid_title_map, index_folder_path+"doc_title_map")
    return filenames

    


            
            