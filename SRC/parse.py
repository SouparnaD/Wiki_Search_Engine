# -*- coding: utf-8 -*-
" created by @Souparna on 20-08-2019"


import xml.sax
doc_list = []


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
#             texts.append(content)
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

    


            
            