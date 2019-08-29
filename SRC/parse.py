# -*- coding: utf-8 -*-
" created by @Souparna on 20-08-2019"

import re
import xml.sax
doc_list = []



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

count___ = 0

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

        

def XmlParser(path):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    
    Handler = WikiContentHandler()
    parser.setContentHandler(Handler)
    
    parser.parse(path)
    
    return doc_list

    


            
            