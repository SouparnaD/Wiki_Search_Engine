#!/usr/bin/python
from time import time
import xml.sax
#import nltk
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer 


# nltk.download('punkt')

doc_list = []
inverted_index = {}
#stop_words = stopwords.words('english')
#stemmer = PorterStemmer() 


class document():
   def __init__(self):
      self.title = ""
      self.ns = ""
      self.id = ""
      self.redirect = ""
      self.r_id = ""
      self.timestamp = ""
      self.con_user = ""
      self.con_id = ""
      self.comment  = ""
      self.model = ""
      self.format = ""
      self.text = ""

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.doc_running =  False
      self.Current_tag = ""
      self.revision  = False
      self.contributor = False
      self.doc =  ""

   # Call when an element starts
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


   # Call when an elements ends
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

         try :
            if self.doc.id : 
               self.doc.id = int(self.doc.id)
            if self.doc.r_id :
               self.doc.r_id = int(self.doc.r_id)
            if self.doc.con_id :
               self.doc.con_id = int(self.doc.con_id)
         except : 
            print(self.doc.id)
            print(self.doc.r_id)
            print(self.doc.con_id)

         doc_list.append(self.doc)
         self.doc = ""


   def characters(self, content):

      if self.doc_running == False :
         return 

      if self.Current_tag == "ns":
         self.doc.ns += content

      elif self.Current_tag == "title":
         self.doc.title += content

      elif self.Current_tag == "redirect" : 
         self.doc.redirect +=  content

      elif self.Current_tag == "id" :
         if self.revision == False :
            self.doc.id += content
         elif self.contributor == True :
            self.doc.con_id += content
         else :
            self.doc.r_id += content

      elif self.Current_tag == "comment" : 
         self.doc.comment += content

      elif self.Current_tag == "model" :
         self.doc.model += content

      elif self.Current_tag == "timestamp" :
         self.doc.timestamp += content

      elif self.Current_tag == "username":
         self.doc.con_user += content

      elif self.Current_tag == "format" :
         self.doc.format += content

      elif self.Current_tag == "text":
         self.doc.text += content



def search(query):
   query = query.lower()
   words = word_tokenize(query)
   words = [stemmer.stem(w) for w in words]
   result_found = True

   # result = dict()
   # for word in words :
   #    if word in inverted_index:
         
   #       if word not in result :
   #          result[word] =  []

   #       for docid in inverted_index[word]:         


   #    else:
   #       result_found = False
   #       break



if ( __name__ == "__main__"):
   
   # create an XMLReader
   t1 = time()
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("data/data_phase1.xml")
   print(len(doc_list))

# =============================================================================
#    print(time() - t1)
#    
#    for doc in doc_list:
#       tokens = word_tokenize(doc.text)
#       tokens = map(lambda x : x.lower(),  tokens)
#       tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
# 
#       print(doc.id)
#       
#       for token in tokens :
#          if token in inverted_index:
#             inverted_index[token].append(doc.id)
#          else:
#             inverted_index[token] = [doc.id]
# 
#    print(len(inverted_index))
# 
#    for key in inverted_index :
#       print("key : " + key + ", docs_id : " + str(inverted_index[key][0]))
# 
#    print("time taken : " + str(time() - t1))
# =============================================================================


