import requests 
from lxml import etree 
  
# manually storing desired URL 
url="https://en.wikipedia.org/wiki/Narendra_Modi"
  
# fetching its url through requests module   
req = requests.get(url)  
  
store = etree.fromstring(req.text) 
print(store)
  
# this will give Motto portion of above  
# URL's info box of Wikipedia's page 
output = store.xpath('//table[@class="infobox vcard"]/tr[th/text()="Motto"]/td/i')  
  
# printing the text portion 
print(output)
#print (output[0].text)   